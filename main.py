import cv2
import time
from ultralytics import solutions
import numpy as np

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

cap = cv2.VideoCapture("C:/Users/Administrateur/Desktop/apprentissage/comptage/input_video.mp4") 
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

processing_times = []  # List to store processing times for each frame

# Define region points
region_points = [(156, 206), (161, 240), (387, 245), (395, 216)]  # For rectangle region counting

# Video writer
video_writer = cv2.VideoWriter("C:/Users/Administrateur/Desktop/apprentissage/comptage/output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init ObjectCounter
counter = solutions.ObjectCounter(
    show=True,  # Display the output
    region=region_points,  # Pass region points
    model="C:/Users/Administrateur/Desktop/apprentissage/comptage/yolo11n.pt",  # Model path
    classes=[0],  # Person class in COCO pretrained model
    show_in=True,  # Display in counts
    show_out=True,  # Display out counts
)

# Variables to track in/out counts
people_in = 0
people_out = 0

# Process video
while cap.isOpened():

    start_frame_time = time.time()  # Start time for the frame

    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    # Count objects and update the in/out counts
    im0 = counter.count(im0)

    # Update in/out counters from the ObjectCounter object
    people_in = counter.in_count  # Get the number of people entering
    people_out = counter.out_count  # Get the number of people exiting

    # Calculate the number of people inside
    people_inside = people_in - people_out

    # Add the count text to the frame (top-left corner)
    text = f"People Inside: {people_inside}"# (In: {people_in}, Out: {people_out})"
    cv2.putText(im0, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Frame processing time
    end_frame_time = time.time()     # End time for the frame
    frame_processing_time = end_frame_time - start_frame_time
    processing_times.append(frame_processing_time)  # Save the time for this frame

    # Write the processed frame to video
    video_writer.write(im0)


# Calculate the average processing time after the loop
avg_processing_time = np.mean(processing_times)
print(f"Average processing time per frame: {avg_processing_time:.4f} seconds")

print("Program Stopped")

# Release video resources
cap.release()
video_writer.release()
cv2.destroyAllWindows()
