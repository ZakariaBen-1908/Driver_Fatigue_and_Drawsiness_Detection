import os
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from keras.utils.np_utils import to_categorical
import random, shutil
from keras.models import Sequential
from keras.layers import Dropout, Conv2D, Flatten, Dense, MaxPooling2D, BatchNormalization
from keras.models import load_model
from keras.applications import ResNet50
from keras.optimizers import Adam
from keras.layers import GlobalAveragePooling2D

# Data Generator
def generator(dir, gen=image.ImageDataGenerator(rescale=1./255), shuffle=True, batch_size=1, target_size=(224, 224), class_mode='categorical'):
    return gen.flow_from_directory(
        dir,
        batch_size=batch_size,
        shuffle=shuffle,
        color_mode='rgb',  # Use RGB for ResNet50
        class_mode=class_mode,
        target_size=target_size
    )

# Parameters
BS = 32
TS = (224, 224)  # ResNet50 expects 224x224 RGB images
train_batch = generator('data/train', shuffle=True, batch_size=BS, target_size=TS)
valid_batch = generator('data/valid', shuffle=True, batch_size=BS, target_size=TS)
SPE = len(train_batch.classes) // BS
VS = len(valid_batch.classes) // BS
print(SPE, VS)

# Load ResNet50 model
base_model = ResNet50(
    weights='imagenet',  # Use pre-trained weights
    include_top=False,   # Exclude the final classification layer
    input_shape=(224, 224, 3)  # Input shape for ResNet50
)

# Freeze the base model (optional)
base_model.trainable = False

# Build the model
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),  # Add a global average pooling layer
    Dense(256, activation='relu'),  # Add a fully connected layer
    Dropout(0.5),  # Add dropout for regularization
    Dense(4, activation='softmax')  # Output layer for 4 classes
])

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.001),  # Use Adam optimizer
    loss='categorical_crossentropy',  # Categorical cross-entropy for multi-class classification
    metrics=['accuracy']
)

# Train the model
model.fit_generator(
    train_batch,
    validation_data=valid_batch,
    epochs=150,
    steps_per_epoch=SPE,
    validation_steps=VS
)

# Save the model
model.save('models/resnet50.h5', overwrite=True)