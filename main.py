import cv2
import numpy as np
import os
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


def mediapipe_detection(med_image, model):
    med_image = cv2.cvtColor(med_image, cv2.COLOR_BGR2RGB)
    med_image.flags.writeable = False
    med_results = model.process(med_image)
    med_image.flags.writeable = True
    med_image = cv2.cvtColor(med_image, cv2.COLOR_RGB2BGR)
    return med_image, med_results


def draw_landmarks(draw_image, draw_results):
    mp_drawing.draw_landmarks(draw_image, draw_results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                              mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                              mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1))


def extract_keypoints(results_key):
    pose_key = np.array([[res_key.x, res_key.y, res_key.z, res_key.visibility] for res_key in results_key.pose_landmarks.landmark]).flatten() \
        if results_key.pose_landmarks else np.zeros(33*4)
    face_key = np.array([[res_key.x, res_key.y, res_key.z] for res_key in results_key.face_landmarks.landmark]).flatten() \
        if results_key.face_landmarks else np.zeros(468*3)
    return np.concatenate([pose_key, face_key])


# Path for exported data, numpy arrays
DATA_PATH = os.path.join('MP_Data')

# Actions that we try to detect
# possible to record different gestures separately if you want
# just make sure to label accordingly
actions = np.array(['neutral'])
#actions = np.array(['neutral', 'up', 'down', 'left', 'right', 'tilt left', 'tilt right', 'shake head'])

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 15

for action in actions:
    for sequence in range(no_sequences):
        try:
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass


cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    # Loop through actions
    for action in actions:
        # Loop through sequences aka videos
        for sequence in range(no_sequences):
            # Loop through video length aka sequence length
            for frame_num in range(sequence_length):

                # Read feed
                ret, frame = cap.read()

                # Make detections
                image, results = mediapipe_detection(frame, holistic)

                # Draw landmarks
                draw_landmarks(image, results)

                # Apply wait logic
                if frame_num == 0:
                    print('Collecting frames for {} Video Number {}'.format(action, sequence))
                    cv2.putText(image, 'STARTING COLLECTION', (120, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15, 12),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.waitKey(1000)
                else:
                    print('Collecting frames for {} Video Number {}'.format(action, sequence))
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15, 12),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

                # NEW Export keypoints
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                # Show on screen
                cv2.imshow('OpenCV Feed', image)

                # Break using q key
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

    cap.release()
    cv2.destroyAllWindows()
