# Video Classifier

**Video Classifier** is an AI-based tool designed to classify videos into the following genres:
- **Entertainment**
- **Gaming**
- **Vlog**
- **Tech Reviews**

## Features
- Extracts frames from videos for analysis.
- Uses a deep learning model to predict the genre of videos.
- Two ways to run the classification:
  1. Via a standalone script (`predict.py`).
  2. Via a FastAPI app (`app.py`).

## Project Structure

```
Video_Classifier/
├── data/
│   ├── raw_videos/
│   │   ├── Entertainment/
│   │   ├── Gaming/
│   │   ├── Vlog/
│   │   └── Tech Reviews/
│   ├── frames/
│   └── metadata/
│       └── frame_extraction_log.txt
├── models/
│   ├── extract_frames.py
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   └── model_weights.h5
├── videos_predict/
│   └── (folder for storing predicted videos)
├── videos_app/
│   └── (folder for storing uploaded videos)
├── app.py
├── requirements.txt
├── README.md
└── .venv/
```

## How to Run

### 1. Frame Extraction (`extract_frames.py`)

Before training or predicting, you need to extract frames from your raw videos stored in the `data/raw_videos/` folder.

#### Steps:
1. Place your training videos in their respective genre folders under `data/raw_videos/` (e.g., `Entertainment/`, `Gaming/`).
2. Run the following command to extract frames:
   ```bash
   python models/extract_frames.py
   ```
   This will extract frames from each video and store them in the `data/frames/` folder.

### 2. Model Training (`train.py`)

Once frames are extracted, you can train your model using the extracted frames.

#### Steps:
1. Ensure that frames are extracted and stored in `data/frames/`.
2. Run the following command to train the model:
   ```bash
   python models/train.py
   ```
   This will train the model and save the trained weights in `models/model_weights.h5`.

### 3. Running Video Classification using `predict.py`

After training, you can classify videos by placing them into the `videos_predict/` folder and running the standalone prediction script.

#### Steps:
1. Place your video files (`.mp4`, `.avi`, `.mkv`, etc.) into the `videos_predict/` folder.
2. Run the following command to classify videos:
   ```bash
   python models/predict.py
   ```
   The script will extract frames from each video, run predictions on each frame, and return the predicted genre for the video.

### 4. Running Video Classification through FastAPI (`app.py`)

You can also classify videos by uploading them via an HTTP POST request to the FastAPI app.

#### Steps:
1. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the FastAPI app:
   ```bash
   uvicorn app:app --reload
   ```
3. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.
4. Use the `/upload/` endpoint to upload a video and receive its predicted genre. Alternatively, you can use a tool like **Postman** or `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@path_to_your_video"
   ```
## Testing with Example Videos
For testing the classifier, you can use the training videos provided in the data/raw_videos/ folder. These example videos are good for basic testing, but you can add more videos to improve the accuracy of the model.

## Requirements

Ensure the following packages are installed:

```
tensorflow
keras
numpy
opencv-python
fastapi
uvicorn
shutil
```

## License
This project is licensed under the MIT License.