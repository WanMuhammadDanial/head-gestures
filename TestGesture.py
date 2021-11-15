from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import cv2
import mediapipe as mp
import numpy as np
from matplotlib import pyplot as plt
import time
from scipy import stats

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


def mediapipe_detection(med_image, model_pipe):
    med_image = cv2.cvtColor(med_image, cv2.COLOR_BGR2RGB)
    med_image.flags.writeable = False
    med_results = model_pipe.process(med_image)
    med_image.flags.writeable = True
    med_image = cv2.cvtColor(med_image, cv2.COLOR_RGB2BGR)
    return med_image, med_results


def draw_landmarks(draw_image, draw_results):
    mp_drawing.draw_landmarks(draw_image, draw_results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                              mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1))


def extract_keypoints(results_key):
    pose_key = np.array([[res_key.x, res_key.y, res_key.z, res_key.visibility] for res_key in results_key.pose_landmarks.landmark]).flatten() \
        if results_key.pose_landmarks else np.zeros(33*4)
    face_key = np.array([[res_key.x, res_key.y, res_key.z] for res_key in results_key.face_landmarks.landmark]).flatten() \
        if results_key.face_landmarks else np.zeros(468*3)
    return np.concatenate([pose_key, face_key])


# make sure to update this with another new dictionary(?) of color values every time you add a new gesture
# not really necessary but its amusing
# need to find a way to translate this into the UI thingy
colors = [(117, 245, 16), (117, 245, 16), (16, 117, 245), (12, 123, 234), (12, 123, 234)]


def prob_viz(res_viz, action_viz, input_frame, color_viz):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res_viz):
        cv2.rectangle(output_frame, (0, 60 + num * 40), (int(prob * 100), 90 + num * 40), color_viz[num], -1)
        cv2.putText(output_frame, action_viz[num], (0, 85 + num * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return output_frame


# make sure to have the same number + type of actions as during training
# order is important, gesture name doesn't matter here but will definitely help to avoid confusion
actions = np.array(['neutral', 'up', 'down', 'left', 'right'])
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 1536)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
model.built = True
model.load_weights('head_gesture.h5')
model.summary()

# 1. New detection variables
sequence = []
sentence = []
predictions = []
threshold = 0.8

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        # Draw landmarks
        draw_landmarks(image, results)

        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]

        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(actions[np.argmax(res)])

            # 3. Viz logic
            if res[np.argmax(res)] > threshold:
                if len(sentence) > 0:
                    if actions[np.argmax(res)] != sentence[-1]:
                        sentence.append(actions[np.argmax(res)])
                else:
                    sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5:
                sentence = sentence[-5:]

            # Viz probabilities
            image = prob_viz(res, actions, image, colors)

        cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Show on screen
        cv2.imshow('OpenCV Feed', image)

        # Break using q key
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
