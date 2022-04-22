import cv2
import numpy as np

# Import the face models and properties

try:
    face_model = cv2.dnn.readNetFromCaffe('faces_data\\detection\\deploy.prototxt',
                                          'faces_data\\detection\\res10_300x300_ssd_iter_140000.caffemodel')
except:
    face_model = cv2.dnn.readNetFromCaffe('Age_and_Gender\\faces_data\\detection\\deploy.prototxt',
                                          'Age_and_Gender\\faces_data\\detection\\res10_300x300_ssd_iter_140000.caffemodel')
face_blob_height = 300
face_average_color = (104, 177, 123)
# 99.5% confidence score is required to generate blobs and frames
face_confidence_threshold = 0.995

# No labels defined for DNN because of no classification

# Load age classifiers and define sample labels

try:
    age_model = cv2.dnn.readNetFromCaffe('faces_data\\age_gender_classification\\age_net_deploy.prototxt',
                                         'faces_data\\age_gender_classification\\age_net.caffemodel')
except:
    age_model = cv2.dnn.readNetFromCaffe('Age_and_Gender\\faces_data\\age_gender_classification\\age_net_deploy.prototxt',
                                         'Age_and_Gender\\faces_data\\age_gender_classification\\age_net.caffemodel')

age_labels = ['0-2', '4-6', '8-12', '15-20', '25-32', '38-43', '48-53', '60+']

# Labels are described to be discrete instead of continuous to make the classes separable

# Load the gender model and values
try:
    gender_model = cv2.dnn.readNetFromCaffe('faces_data\\age_gender_classification\\gender_net_deploy.prototxt',
                                            'faces_data\\age_gender_classification\\gender_net.caffemodel')
except:
    gender_model = cv2.dnn.readNetFromCaffe('Age_and_Gender\\faces_data\\age_gender_classification\\gender_net_deploy.prototxt',
                                            'Age_and_Gender\\faces_data\\age_gender_classification\\gender_net.caffemodel')
gender_labels = ['Male', 'Female']

# Average facial image is used for age and gender classification

age_gender_blob_size = (256, 256)
try:
    age_gender_average_image = np.load(
        'faces_data\\age_gender_classification\\average_face.npy')
except:
    age_gender_average_image = np.load(
        'Age_and_Gender\\faces_data\\age_gender_classification\\average_face.npy')

# Average image has been loaded as a numpy array

### MODELS AND PARAMETERS SETUP COMPLETED ###

# We can implement 2-3 variations of the feature with input from
# standard images or video clips or Cameras.
# For this time we are using the live camera. Videocapture(0)

Capture = cv2.VideoCapture(0)  # Reading stream from the cameras
success, frame = Capture.read()
while success:
    height, width = frame.shape[:2]
    aspect_ratio = width / height

    # Face detection framing

    face_blob_width = int(face_blob_height * aspect_ratio)
    face_blob_size = (face_blob_width, face_blob_height)

    face_blob = cv2.dnn.blobFromImage(
        frame, size=face_blob_size, mean=face_average_color)

    # Generate the model and result

    face_model.setInput(face_blob)
    face_results = face_model.forward()

    # Check the confidence score and generate rectangle frame by obtaining co-ordinates

    for face in face_results[0, 0]:
        face_confidence = face[2]

        # Verify confidence score for threshold

        if face_confidence > face_confidence_threshold:
            x0, y0, x1, y1 = (face[3:7] * [width, height,
                                           width, height]).astype(int)

            # Faces have been detected
            # Proceed to Age and Gender classification

            # Frame sizes need to be altered

            # Factor computed after several times
            y1_roi = y0 + int(1.2*(y1-y0))
            x_margin = ((y1_roi - y0) - (x1-x0)) // 2  # Average coordinate
            x0_roi = x0 - x_margin
            x1_roi = x1 + x_margin

            # Skip the face detected if the ROI is outside the frame

            if x0_roi < 0 or x1_roi > width or y0 < 0 or y1_roi > height:
                continue

            # Focus out the Face's ROI and obtain the normal face

            age_gender_roi = frame[y0:y1_roi, x0_roi:x1_roi]
            scaled_age_gender_roi = cv2.resize(
                age_gender_roi, age_gender_blob_size, interpolation=cv2.INTER_LINEAR).astype(np.float32)

            scaled_age_gender_roi[:] -= age_gender_average_image

            age_gender_blob = cv2.dnn.blobFromImage(
                scaled_age_gender_roi, size=age_gender_blob_size)

            # Feed blob to the age classifier and pick ID with highest confidence score
            # Then note the label and confidence score

            age_model.setInput(age_gender_blob)
            age_results = age_model.forward()
            age_id = np.argmax(age_results)
            age_label = age_labels[age_id]
            age_confidence = age_results[0, age_id]

            # Age classification completed

            # Similarly classify the Gender model

            gender_model.setInput(age_gender_blob)
            gender_results = gender_model.forward()
            gender_id = np.argmax(gender_results)
            gender_label = gender_labels[gender_id]
            gender_confidence = gender_results[0, gender_id]

            # Gender Classification completed

            # Draw a rectangle around the face

            cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)

            # Draw a square around the region of interest

            cv2.rectangle(frame, (x0_roi, y0),
                          (x1_roi, y1_roi), (0, 215, 255), 2)

            # Draw labels for the result labels and scores

            res = "%s years (%.1f%%), %s (%.1f%%)" % (
                age_label, age_confidence*100.0, gender_label, gender_confidence*100.0)

            # Position the text in the window
            cv2.putText(frame, res, (x0_roi, y0-20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 4)
            cv2.putText(frame, res, (x0_roi, y0-20),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

    cv2.imshow('Age and Gender Classifier', frame)

    key = cv2.waitKey(1)
    if key == 27:  # Escape button
        break

    success, frame = Capture.read()