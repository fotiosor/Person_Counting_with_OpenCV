# Person_Counting_with_OpenCV

This project uses a pre-trained YOLO (You Only Look Once) object detection model and the OpenCV library to count people in a video based on a defined region.

## Description

The goal of this project is to detect and count people entering and exiting a defined region in a video. The project uses the YOLOv5 (version 11n) model from the `ultralytics` library for object detection (in this case, people). The counting results are displayed in real-time on each frame of the video.

### Features

- Detection of people in a video.
- Counting people entering and exiting a defined region.
- Real-time display of the number of people inside the region on each frame of the video.
- Exporting the processed video with annotations.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy
- `ultralytics` (to use YOLOv5)

You can install the necessary dependencies via `pip`:

```bash
pip install opencv-python numpy ultralytics
