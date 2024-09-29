from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from models.predict import predict_video

app = FastAPI()

UPLOAD_FOLDER = "./videos_app/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    try:
        # Check for video MIME type (e.g., only allow mp4, avi, mkv)
        if file.content_type not in ["video/mp4", "video/avi", "video/mkv"]:
            return JSONResponse(content={"error": "Invalid video file format. Only mp4, avi, and mkv are supported."}, status_code=400)

        # Save the uploaded video temporarily
        video_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Call the prediction function
        predicted_genre = predict_video(video_path)

        # Return a JSON response with the predicted genre
        return JSONResponse(content={"predicted_genre": predicted_genre})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

    finally:
        # Clean up: remove the video after processing
        if os.path.exists(video_path):
            os.remove(video_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
