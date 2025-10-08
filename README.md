# Real-Time Face Recognition Using Keras & OpenCV

![Face Recognition](https://img.shields.io/badge/Status-Completed-brightgreen)


## Overview

This project implements a **real-time face detection and recognition system** using Python, Keras, TensorFlow, and OpenCV. It allows you to identify multiple users from a live video feed (e.g., IP webcam on your mobile device) with high accuracy, based on a custom-trained dataset.

The system combines traditional **computer vision techniques** for face detection and **deep learning models** for recognition, making it robust and efficient for small-scale deployment.

---

## Features

- ✅ Real-time face detection using OpenCV’s Haar Cascades  
- ✅ Face recognition for multiple users using a custom-trained Keras CNN model  
- ✅ Dataset collection automation via `collect_data.py`  
- ✅ Preprocessing and data normalization for accurate predictions  
- ✅ Lightweight, portable, and easy to extend for new users  

---

## Project Structure

```text
FaceDetection/
├─ images/                  # Raw images of users
├─ face_dataset/            # Organized images for training
├─ recognize.py             # Real-time recognition script
├─ train_model.py           # Train the recognition model
├─ collect_data.py          # Script to capture images from webcam/IP camera
├─ sort_images.py           # Organize raw images into labeled folders
├─ final_model.keras        # Trained Keras model (not uploaded due to size/privacy)
├─ keras.check.py           # Keras environment verification script
├─ .gitignore               # Files/folders to ignore from GitHub
├─ LICENSE                  # MIT License
└─ README.md                # This file
```

# Setup & Installation

1. **Clone the repository:**

    git clone https://github.com/ANIsha-Mahto/Face-Recognition.git
    cd Face-Recognition

2. **Install dependencies:**
    pip install opencv-python tensorflow keras numpy scikit-learn

3. **Run the model verification**
    python keras.check.py

Usage

1. Collect images of new users:

    python collect_data.py


2. Organize images into dataset folders:

    python sort_images.py


3. Train the recognition model:

    python train_model.py
    This will generate final_model.keras.

4. Run real-time recognition:
   
     Update the IP webcam URL in recognize.py, then run:
     python recognize.py

Press q to exit the live feed.

**Concepts & Technologies Used**

1.Computer Vision: OpenCV Haar Cascades for face detection

2.Deep Learning: Convolutional Neural Networks (CNN) for face recognition

3.Data Preprocessing: Grayscale conversion, resizing, histogram equalization, normalization

4.Model Training & Saving: Keras + TensorFlow

5.Real-Time Streaming: IP webcam via urllib and OpenCV


**License**
This project is licensed under the MIT License – see the LICENSE
 file for details.


**Author**  
Anisha Mahto  
GitHub: [ANIsha-Mahto](https://github.com/ANIsha-Mahto)  
Email: your-anisha040mahto@gmail.com  
LinkedIn: [https://www.linkedin.com/in/anisha-mahto-766a64346/](https://www.linkedin.com/in/anisha-mahto-766a64346/)


