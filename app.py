import streamlit as st
from google.cloud import vision
from PIL import Image
import io

uploaded_file = st.file_uploader("Upload a Bird Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    image = Image.open(io.BytesIO(bytes_data))

    def detect_labels(path):
        """Detects labels in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        st.write('Labels:')
        for label in labels:
            st.write(label.description)
    
    detect_labels(image)