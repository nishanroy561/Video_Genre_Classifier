# models/train.py

from model import build_model
from tensorflow import keras
from PIL import Image
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
import os

def train_model():
    dataset_path = 'data/frames'
    
    model = build_model()

    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='training'
    )
    
    validation_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='validation'
    )
    
    model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=10
    )

    model.save('models/model_weights.h5')

if __name__ == "__main__":
    train_model()
