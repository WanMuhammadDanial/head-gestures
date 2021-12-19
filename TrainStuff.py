from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard

DATA_PATH = os.path.join('MP_Data')

# plug in all the gestures you want in actions
actions = np.array(['neutral', 'up', 'down', 'left', 'right', 'tilt left', 'tilt right', 'shake head'])
no_sequences = 30
sequence_length = 30
label_map = {label: num for num, label in enumerate(actions)}

sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

x = np.array(sequences)
y = to_categorical(labels).astype(int)
print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 1536)))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
opt = SGD(lr=0.01, momentum=0.9)
model.compile(loss='mean_absolute_error', optimizer=opt, metrics=['mse'])
#https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/

# not sure if this matters but I usually delete head_gesture.h5 every time before re-training
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(x_train, y_train, epochs=250)
model.summary()
model.save('head_gesture.h5')
