# SmartVision AI

## Intelligent Multi-Class Object Recognition System

SmartVision AI is a Deep Learning based computer vision application that performs both Image Classification and Object Detection using state-of-the-art models.

The project combines Transfer Learning models for image classification and YOLOv8 for object detection, deployed through an interactive Streamlit web application.

---

## Project Features

* Image Classification using:

  * MobileNetV2
  * VGG16
  * ResNet50
  * EfficientNetB0

* Object Detection using:

  * YOLOv8

* Interactive Streamlit Dashboard

* Model Performance Visualization

* Upload and Predict Images

* Bounding Box Visualization

---

## Dataset

The project uses images from the COCO Dataset.

Number of Classes: 25

Classes include:

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

---

## Project Structure

SmartVision_AI/

├── app/

│ └── app.py

├── notebooks/

│ ├── 01_dataset_preparation.ipynb

│ ├── 02_EDA.ipynb

│ ├── 03_Classification_Models.ipynb

│ ├── 04_YOLO_Training.ipynb

│ ├── 05_Model_Evaluation.ipynb

│ └── 06_Final_Demo.ipynb

├── models/

│ ├── mobilenetv2.keras

│ ├── vgg16.keras

│ ├── resnet50.keras

│ ├── efficientnetb0.keras

│ └── metrics.json

├── yolo/

│ └── best.pt

├── requirements.txt

├── README.md

└── SmartVision_AI_Report.pdf

---

## Classification Model Performance

| Model          | Validation Accuracy |
| -------------- | ------------------- |
| MobileNetV2    | 40.27%              |
| VGG16          | 15.73%              |
| ResNet50       | 8.80%               |
| EfficientNetB0 | 4.00%               |

MobileNetV2 achieved the best performance among the classification models and was selected for deployment.

---

## YOLOv8 Detection Performance

| Metric    | Value |
| --------- | ----- |
| Precision | 0.453 |
| Recall    | 0.429 |
| mAP50     | 0.385 |
| mAP50-95  | 0.162 |

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/SmartVision-AI.git

Move to project folder:

cd SmartVision-AI

Install dependencies:

pip install -r requirements.txt

Run Streamlit application:

streamlit run app.py

---

## Streamlit Application

The application contains:

1. Home Page
2. Image Classification
3. Object Detection
4. Model Performance Dashboard
5. About Page

---

## Technologies Used

* Python
* TensorFlow / Keras
* YOLOv8
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Streamlit

---

## Future Improvements

* Increase classification accuracy using larger datasets
* Hyperparameter tuning
* Ensemble learning approaches
* Real-time webcam detection
* Cloud deployment optimization

---

## Author

Swetha Dasari

Project developed as part of the AIML Capstone Project.
