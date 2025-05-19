# Drowsiness Detection System
##Overview
This project is a Drowsiness Detection System that uses a Convolutional Neural Network (CNN) to detect whether a person's eyes are open or closed. If the system detects that the person's eyes are closed for a prolonged period, it triggers an alarm to alert the person. This system can be used in various scenarios, such as driving, to prevent accidents caused by drowsiness.

## Features
Real-time Detection: The system captures video from a webcam and processes it in real-time to detect the state of the eyes.

CNN Model: A pre-trained CNN model is used to classify whether the eyes are open or closed.

Alarm System: An alarm sound is played when the system detects drowsiness.

Haar Cascades: Haar cascades are used for face and eye detection to improve the accuracy of the system.

## Requirements
To run this project, you need the following:

Python 3.x

OpenCV

Keras

TensorFlow

NumPy

Pygame

You can install the required packages using pip:

## bash
pip install opencv-python keras tensorflow numpy pygame

## Project Structure
model_CNN.py / model_ResNet50.py: Those scripts contains the code to build, train, and save the CNN and ResNet50 models for eye state classification.

drowsiness detection.py: This script captures video from the webcam, detects the eyes, and uses the trained model to classify the eye state. It also triggers an alarm if drowsiness is detected.

haar cascade files/: This directory contains the Haar cascade XML files for face and eye detection.

data/: This directory should contain the training and validation data for the CNN model.

models/: This directory contains the saved CNN model (cnnCat2.h5).

## How to Run
### Train the Model:

Ensure you have the training and validation data in the data/train and data/valid directories.

### Run the model.py script to train the CNN model:
python model_CNN.py or python model_ResNet.py
The trained models will be saved as cnnCat2.h5 and resnet50.h5 in the models/ directory.

### Run the Drowsiness Detection:

Run the drowsiness detection.py script to start the real-time drowsiness detection:
python drowsiness detection.py
The system will capture video from your webcam, detect your face and eyes, and classify whether your eyes are open or closed.

If drowsiness is detected (i.e., eyes are closed for a prolonged period), an alarm will sound.

## Customization
Model Training: You can modify the models architecture or use a different dataset to train the model.

Alarm Sound: You can replace the alarm.wav file with a different sound file if desired.

Thresholds: Adjust the score threshold in drowsiness.py to change the sensitivity of the drowsiness detection.

## Acknowledgments
This project uses Haar cascades from OpenCV for face and eye detection.

The CNN model is built using Keras and TensorFlow.
