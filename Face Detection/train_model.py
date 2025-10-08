import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# 1. Prepare dataset
data_dir = "face_dataset"
image_size = 100
data = []
labels = []
label_map = {}
current_label = 0

for person in os.listdir(data_dir):
    person_path = os.path.join(data_dir, person)
    if os.path.isdir(person_path):
        label_map[current_label] = person
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (image_size, image_size))
            img = img / 255.0
            data.append(img)
            labels.append(current_label)
        current_label += 1

data = np.array(data).reshape(-1, image_size, image_size, 1)
labels = to_categorical(labels)

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# 3. Build CNN model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(image_size, image_size, 1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(label_map), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. Train
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# 5. Save model
model.save("final_model.keras")

print("Model trained and saved as final_model.h5")
print("Label map:", label_map)
