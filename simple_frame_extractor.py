import cv2
import os

# Load the video file
video_path = "input_video.avi"  # Change this to your video file
output_folder = "frames_output"  # Folder to save frames
frame_format = "png"  # Change to "jpg" if needed

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)
frame_count = 0

# Detect frame rate (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Detected frame rate: {fps:.2f} FPS")

while cap.isOpened():
    ret, frame = cap.read()

        
    if not ret:
        print(f"❌ No more frames to read. Processed {frame_count} frames.")
        break  # Exit loop when video ends

    print(f"🔹 Processing Frame {frame_count}")  # Debug print

    if not ret:
        break  # Stop when video ends
    
    # Save each frame as an image file
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.{frame_format}")
    cv2.imwrite(frame_filename, frame)  # Save as PNG or JPG
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames and saved in '{output_folder}'")
