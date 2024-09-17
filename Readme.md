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

You can install the necessary Python packages using (Incase of running in vscode, cmd or any other):

```bash
pip install torch torchvision opencv-python scikit-learn
```

(Incase of Jupyter Notebook or google colab):
```bash
!pip install torch torchvision opencv-python scikit-learn
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


## Usage
### 1. Upload and Prepare Video Files:
Ensure that your video files are in a zip archive. The code will prompt you to upload this zip file, which will be extracted for processing.

### 2. Set Parameters:
Adjust the parameters in the main function, such as num_steps, frame_rate, and target_size, to fit your dataset and requirements.

### 3. The Pipeline:
Execute the main function to start the pipeline. The pipeline will process the video data, perform feature extraction, and classify each video. 

(Incase of running in vscode, cmd or any other):

```bash
python pipeline.py
```

## Note: 
Replace `/path/to/video/directory` in pipeline.py


## Troubleshooting

If you encounter issues while running the code, here are some common troubleshooting tips:

1. **Dependencies**: Ensure all required Python packages are installed. If you encounter import errors, verify that the packages are correctly installed using `pip install`.

2. **Device Compatibility**: If the script fails to detect a GPU, make sure you have the appropriate CUDA drivers and libraries installed. The code will fall back to CPU if a GPU is not available.

3. **Video File Formats**: The dataset loader assumes that video files are in formats such as `.mp4`, `.avi`, or `.3gp`. If your files are in different formats, you might need to update the `load_videos` method in the `VideoDataset` class.

4. **Memory Usage**: Processing large video files or a large number of videos may require significant memory. Ensure your environment has sufficient resources or adjust the batch size and frame extraction settings to manage memory usage.

## Future Improvements

- **Model Training**: Currently, the code is set up for evaluation only. To train the models, you would need to implement a training loop, handle loss functions, and optimize the models using backpropagation.

- **Advanced Metrics**: Implement additional evaluation metrics such as ROC-AUC or confusion matrices to gain deeper insights into model performance.

- **Optimization**: Explore model optimization techniques, such as fine-tuning hyperparameters or using more advanced architectures, to improve performance.

- **Deployment**: Add deployment instructions to serve the models in a production environment, either locally or in the cloud. This might involve setting up REST APIs or integrating with web applications.


## Acknowledgements

- **Research Papers**: This project builds on methodologies and techniques from relevant research papers in the field of machine learning and computer vision.
- **Open Source Libraries**: Special thanks to PyTorch, OpenCV, and scikit-learn for providing essential tools and libraries used in this project.

---

Thank you 
