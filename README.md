## 🎥 Demo

![Drowsiness Detection Preview](./live%20test/img.png)

# 📦 Requirements

## ⚠️ Important File Needed

Download the facial landmark predictor model:

### 🔗 shape_predictor_68_face_landmarks.dat.bz2

## Once downloaded:

bash

bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2

Place the extracted shape_predictor_68_face_landmarks.dat file in the project root directory.

## 🔧 Python Dependencies

Install the required libraries:

bash

pip install -r requirements.txt

## The main dependencies include:

numpy

dlib

pygame

imutils

opencv-python

scipy

# 🚀 Usage

## ✅ Detect Face and Eyes in a Single Image

Place your image inside the images folder as test.jpeg, or

Change the image path in face_and_eye_detector_single_image.py (Line 14) to match your image file.

Run the script:

bash

python face_and_eye_detector_single_image.py

## ✅ Detect Face and Eyes from Webcam Feed

### Run the script:

bash

python face_and_eye_detector_webcam_video.py

## ✅ Drowsiness Detection

### Run the script:

bash

python drowsiness_detect.py

ℹ️ The drowsiness detection system uses Eye Aspect Ratio (EAR) to determine eye closure over time.

📚 Credit

The Eye Aspect Ratio (EAR) technique is based on the blog post by Adrian Rosebrock from PyImageSearch.
