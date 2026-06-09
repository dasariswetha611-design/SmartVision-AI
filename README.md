# SmartVision AI

## Intelligent Multi-Class Object Recognition System

SmartVision AI is a Deep Learning-based Computer Vision application that performs both **Image Classification** and **Object Detection** using state-of-the-art Deep Learning models.

The project combines Transfer Learning models for image classification and YOLOv8 for object detection, deployed through an interactive Streamlit web application.

---

## Live Demo

### Hugging Face Deployment

Paste your Hugging Face URL here:

```text
https://huggingface.co/spaces/Dasari12345/smartvision-ai
```

### GitHub Repository

Paste your GitHub repository URL here:

```text
https://github.com/dasariswetha611-design/SmartVision-AI
```

---

## Project Deliverables

* Dataset Preparation Pipeline
* Exploratory Data Analysis (EDA)
* Image Classification Models

  * MobileNetV2
  * VGG16
  * ResNet50
  * EfficientNetB0
* YOLOv8 Object Detection
* Model Evaluation Dashboard
* Streamlit Web Application
* Hugging Face Deployment
* Technical Report

---

## Project Features

### Image Classification

* MobileNetV2
* VGG16
* ResNet50
* EfficientNetB0

### Object Detection

* YOLOv8

### Dashboard Features

* Image Upload
* Classification Prediction
* Object Detection
* Performance Metrics Visualization
* Interactive Streamlit Interface

---

## Dataset

The project uses a subset of the COCO Dataset containing 25 object categories.

### Selected Classes

* airplane
* bed
* bench
* bicycle
* bird
* bottle
* bowl
* bus
* cake
* car
* cat
* chair
* couch
* cow
* cup
* dog
* elephant
* horse
* motorcycle
* person
* pizza
* potted plant
* stop sign
* traffic light
* truck

### Dataset Statistics

| Dataset Type      | Count |
| ----------------- | ----- |
| Training Images   | 1750  |
| Validation Images | 375   |
| Test Images       | 375   |
| Total Images      | 2500  |

---

## Project Architecture

Dataset Preparation

↓

Exploratory Data Analysis

↓

Transfer Learning Models

↓

YOLOv8 Object Detection

↓

Model Evaluation

↓

Streamlit Deployment

↓

Hugging Face Space

---

## Project Structure

```text
SmartVision_AI/

├── app.py
├── README.md
├── requirements.txt

├── notebooks/
│
├── models/
│   ├── mobilenetv2.keras
│   ├── vgg16.keras
│   ├── resnet50.keras
│   ├── efficientnetb0.keras
│   └── metrics.json
│
├── weights/
│   └── best.pt
│
├── screenshots/
│
└── SmartVision_AI_Report.pdf
```

---

## Classification Model Performance

| Model          | Validation Accuracy |
| -------------- | ------------------- |
| MobileNetV2    | 40.27%              |
| VGG16          | 15.73%              |
| ResNet50       | 8.80%               |
| EfficientNetB0 | 4.00%               |

### Best Classification Model

**MobileNetV2**

Validation Accuracy: **40.27%**

---

## YOLOv8 Detection Performance

| Metric    | Value |
| --------- | ----- |
| Precision | 0.453 |
| Recall    | 0.429 |
| mAP50     | 0.385 |
| mAP50-95  | 0.162 |

---

## Technologies Used

### Programming Language

* Python

### Deep Learning Frameworks

* TensorFlow
* Keras
* YOLOv8

### Libraries

* NumPy
* Pandas
* Matplotlib
* OpenCV
* Pillow
* Streamlit

### Development Environment

* Jupyter Notebook
* Anaconda
* Hugging Face Spaces

---

## Installation

### Clone Repository

```bash
git clone https://github.com/dasariswetha611-design/SmartVision-AI.git
```

### Move to Project Folder

```bash
cd SmartVision-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## Future Improvements

* Improve Classification Accuracy
* Larger Training Dataset
* Advanced Data Augmentation
* Hyperparameter Optimization
* Real-Time Webcam Detection
* Video Object Detection
* Cloud-Based GPU Deployment

---

## Project Status

Completed

* Dataset Preparation
* EDA
* Classification Models
* YOLOv8 Detection
* Streamlit Application
* Hugging Face Deployment
* Technical Documentation

---

## Author

### Swetha Dasari

AIML Capstone Project

SmartVision AI – Intelligent Multi-Class Object Recognition System
