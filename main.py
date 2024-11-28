import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd

# Load YOLOv8 model
model = YOLO("./runs/weights/best.pt")

# Streamlit App Configuration
st.set_page_config(
    page_title="Railway Track Defect Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Settings")
st.sidebar.write("Customize your detection experience.")
folder_path = st.sidebar.text_input("📂 Enter Folder Path:")

# App Header
st.title("🚂 Railway Track Defect Detection")
st.write(
    "Analyze railway track images for potential defects using the YOLOv8 model. "
    "This app organizes results in an easy-to-read format."
)

# Validation and Processing
if folder_path:
    if os.path.isdir(folder_path):
        st.success(f"📁 Found folder: `{folder_path}`")
        image_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(("jpg", "jpeg", "png"))
        ]

        if image_files:
            st.info(f"🔍 Found {len(image_files)} image(s). Processing...")

            # Summary Data
            summary_data = []

            # Tabs for each image
            tabs = st.tabs(image_files)

            for idx, image_file in enumerate(image_files):
                # Read Image
                image_path = os.path.join(folder_path, image_file)
                image = Image.open(image_path)

                # Convert PIL Image to OpenCV format
                image_np = np.array(image)
                image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

                # Perform inference
                results = model(image_bgr)

                # Annotate Image
                annotated_image = results[0].plot()

                # Detection Details
                detections = []
                for detection in results[0].boxes:
                    label = int(detection.cls)
                    confidence = float(detection.conf)
                    detections.append((label, confidence))
                detection_status = "Defects Detected" if detections else "No Defects"

                # Add to summary
                summary_data.append({
                    "Image Name": image_file,
                    "Status": detection_status,
                    "Detections": ", ".join(
                        [f"Label: {d[0]}, Confidence: {d[1]:.2f}" for d in detections]
                    )
                })

                # Display in tab
                with tabs[idx]:
                    st.subheader(f"Image: {image_file}")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(image, caption="Original Image", use_column_width=True)
                    with col2:
                        st.image(annotated_image, caption="Detected Image", use_column_width=True)
                    if detections:
                        st.markdown("### Detection Details")
                        for label, confidence in detections:
                            st.write(f"- **Label**: {label}, **Confidence**: {confidence:.2f}")

            # Display Summary Table
            st.markdown("## Detection Summary")
            summary_df = pd.DataFrame(summary_data)
            st.dataframe(summary_df, use_container_width=True)
        else:
            st.warning("⚠️ No valid images found in the folder.")
    else:
        st.error("🚫 The specified folder does not exist.")
else:
    st.info("📝 Please enter a folder path to get started.")