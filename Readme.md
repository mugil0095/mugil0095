# Transformer-Based Text Classification Pipeline

## Overview
This project implements a continuous training and deployment pipeline for a transformer-based text classification model. The pipeline supports both **live** and **batch** inference, and retrains the model upon detecting staleness or performance degradation using monitoring tools like **MLflow**.

## Prerequisites

1. **Python**: Ensure Python 3.8+ is installed on your system.
2. **Dependencies**: Install required Python libraries. Run the following command to install all dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   textclassification
 ├── data
 │    ├── IMDB Dataset.csv         # Dataset for training and validation
 │    ├── batch_input.csv          # Input for batch inference
 │    └── batch_output.csv         # Output generated after batch inference
 ├── model
 │    ├── config.json              # Generated automatically during training
 │    └── model.safetensor         # Model weights generated automatically
 ├── scripts
 │    ├── __init__.py              # Initialization script
 │    ├── preprocess.py            # Data preprocessing script
 │    ├── train.py                 # Model training script
 │    ├── inference.py             # Batch inference script
 │    ├── live_inference.py        # FastAPI for live inference
 │    └── monitoring.py            # Monitoring script for performance degradation
 ├── pipeline.py                   # Master pipeline to orchestrate the execution of steps
 └── requirements.txt              # List of required Python packages
