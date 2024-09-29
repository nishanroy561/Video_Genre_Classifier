# extract_frames.py
import cv2
import os

# Paths
video_dir = 'data/raw_videos'
frame_output_dir = 'data/frames'
log_file = 'data/metadata/frame_extraction_log.txt'

# List of genres
genres = ['Entertainment', 'Gaming', 'Vlog', 'Tech Reviews']

# Ensure output directories exist
for genre in genres:
    os.makedirs(os.path.join(frame_output_dir, genre), exist_ok=True)

# Frame extraction function
def extract_frames(video_path, output_dir, frame_rate=1):
    cap = cv2.VideoCapture(video_path)
    count = 0
    success, image = cap.read()
    while success:
        if count % frame_rate == 0:
            frame_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}_frame_{count}.jpg"
            cv2.imwrite(os.path.join(output_dir, frame_filename), image)
        success, image = cap.read()
        count += 1
    cap.release()

# Process each genre
with open(log_file, 'w') as log:
    for genre in genres:
        genre_video_dir = os.path.join(video_dir, genre)
        genre_frame_output_dir = os.path.join(frame_output_dir, genre)
        
        # Process each video in the genre directory
        for video_file in os.listdir(genre_video_dir):
            if video_file.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                video_path = os.path.join(genre_video_dir, video_file)
                log.write(f"Extracting frames from {video_file}...\n")
                extract_frames(video_path, genre_frame_output_dir)
    log.write("Frame extraction completed.\n")

print("Frame extraction completed.")
