# models/predict.py

from tensorflow import keras
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
import cv2


# Load the trained model
model = load_model('models/model_weights.h5')

# Mapping the model's output to genre labels
labels = ['Entertainment', 'Gaming', 'Vlog', 'Tech Reviews']

def extract_frames(video_path, target_dir, max_frames=10):
    """Extract frames from a video and save them to the target directory."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(1, frame_count // max_frames)
    
    frame_list = []
    for i in range(0, frame_count, step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            frame_path = os.path.join(target_dir, f"{os.path.basename(video_path)}_frame_{i}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_list.append(frame_path)
    
    cap.release()
    return frame_list

def predict_video(video_path):
    # Directory to save extracted frames
    temp_frames_dir = os.path.join('temp', 'frames')
    
    # Extract frames from the video
    frame_paths = extract_frames(video_path, temp_frames_dir)
    
    # Predict the genre based on the extracted frames
    predictions = []
    for frame_path in frame_paths:
        img = load_img(frame_path, target_size=(64, 64))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array)
        predictions.append(prediction)
    
    # Average the predictions to get a final genre
    avg_prediction = np.mean(predictions, axis=0)
    predicted_label = labels[np.argmax(avg_prediction)]
    return predicted_label

if __name__ == "__main__":
    # Directory containing the random videos
    videos_dir = 'videos_predict/'  # This is the folder for random videos

    # Iterate through all video files in the directory
    for video_file in os.listdir(videos_dir):
        if video_file.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(videos_dir, video_file)
            prediction = predict_video(video_path)
            print(f"Prediction for {video_file}: {prediction}\n")