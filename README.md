## 🎥 Demo

![Drowsiness Detection Preview](./live%20test/img.png)

# Requirements
## IMPORTANT

Download shape_predictor_68_face_landmarks.dat.bz2 from Shape Predictor 68 features Extract the file in the project folder using bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2

numpy
dlib
pygame
imutils
opencv_python
scipy
Use pip install -r requirements.txtto install the given requirements.

# Usage
Detect Face and Eyes in a Single Image
Put your file to be detected in images folder with name test.jpeg or change the file path in Line : 14 face_and_eye_detector_single_image.py to your image file.

# Run script using:

python face_and_eye_detector_single_image.py
Detect Face and Eyes in a Webcam Feed

# Run script using:

python face_and_eye_detector_webcam_video.py
Drowsiness Detection

#Run script using:

python drowsiness_detect.py
The algorithm for Eye Aspect Ratio was taken from pyimagesearch.com blog, by Adrian RoseBrock.
