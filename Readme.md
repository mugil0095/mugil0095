# Video Classification Pipeline with Diffusion Model and CNN+LSTM

## Overview

This Assignment implements a machine learning pipeline for video classification using a diffusion model for reconstruction error detection and a CNN+LSTM architecture for binary classification. The pipeline is designed to handle video data, perform feature extraction using a diffusion model, and classify videos based on the extracted features.

## Features

- **Diffusion Model**: Utilized for detecting reconstruction errors and extracting features from video frames.
- **CNN+LSTM Model**: Processes features extracted by the diffusion model for binary classification tasks.
- **Evaluation Metrics**: Computes accuracy, precision, recall, and F1-score for evaluating the performance of the classification model.


## Requirements

- Python 3.x
- PyTorch
- OpenCV
- scikit-learn
- torchvision

You can install the necessary Python packages using:

```bash
pip install torch torchvision opencv-python scikit-learn
```

## Code Structure

1. DiffusionModel: Defines a diffusion model for feature extraction and reconstruction error detection.
2. CNNLSTMModel: Defines a CNN+LSTM model for video classification.
3. VideoDataset: Custom dataset class for loading and preprocessing video data.
4. main: Main function to execute the pipeline, including:
- Uploading and unzipping video files
- Initializing models
- Processing video frames
- Performing classification
- Computing evaluation metrics


