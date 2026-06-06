import streamlit as st
import pandas as pd
import json

st.set_page_config(
    page_title="SmartVision AI",
    layout="wide"
)

st.title("SmartVision AI")
st.subheader("Intelligent Multi-Class Object Recognition System")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Image Classification",
        "Object Detection",
        "Model Performance",
        "About"
    ]
)

if page == "Home":
    st.header("Project Overview")
    st.write("""
    SmartVision AI is a computer vision project that performs image classification
    and object detection using deep learning models.
    """)

    st.write("""
    The project uses 25 selected COCO object classes and includes transfer learning
    models such as MobileNetV2, VGG16, ResNet50, EfficientNetB0, and YOLOv8.
    """)

elif page == "Image Classification":

    import tensorflow as tf
    import numpy as np
    from PIL import Image

    st.header("Image Classification")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            width=300
        )

        
        model = tf.keras.models.load_model(
               "models/mobilenetv2.keras"
)
        

        class_names = [
            'airplane','bed','bench','bicycle','bird',
            'bottle','bowl','bus','cake','car',
            'cat','chair','couch','cow','cup',
            'dog','elephant','horse','motorcycle',
            'person','pizza','potted plant',
            'stop sign','traffic light','truck'
        ]

        img = image.resize((224,224))

        img_array = np.array(img)

        img_array = img_array / 255.0

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        prediction = model.predict(img_array)

        predicted_class = np.argmax(prediction)

        st.success(
            f"Predicted Class: {class_names[predicted_class]}"
        )

elif page == "Object Detection":

    from ultralytics import YOLO
    from PIL import Image
    import tempfile
    import matplotlib.pyplot as plt

    st.header("Object Detection")

    uploaded_file = st.file_uploader(
        "Upload Image for Object Detection",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            width=400
        )

        model = YOLO("yolov8n.pt")
        

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            image.save(temp_file.name)
            temp_path = temp_file.name

        results = model.predict(
            temp_path,
            conf=0.15,
            save=False
        )

        result_img = results[0].plot()

        st.image(
            result_img,
            caption="Detected Objects",
            use_container_width=True
        )
elif page == "Model Performance":
    st.header("Model Performance")

    st.subheader("Classification Results")

    classification_results = pd.DataFrame({
        "Model": ["MobileNetV2", "VGG16", "ResNet50", "EfficientNetB0"],
        "Validation Accuracy": [0.4027, 0.1573, 0.0880, 0.0400]
    })

    st.dataframe(classification_results, use_container_width=True)

    st.bar_chart(
        classification_results,
        x="Model",
        y="Validation Accuracy"
    )

    st.subheader("YOLOv8 Detection Results")

    yolo_results = pd.DataFrame({
        "Metric": ["Precision", "Recall", "mAP50", "mAP50-95"],
        "Value": [0.453, 0.429, 0.385, 0.162]
    })

    st.dataframe(yolo_results, use_container_width=True)

    st.bar_chart(
        yolo_results,
        x="Metric",
        y="Value"
    )

elif page == "About":
    st.header("About")
    st.write("""
    Developed as part of the SmartVision AI computer vision project.
    """)