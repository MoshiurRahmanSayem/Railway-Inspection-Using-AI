# Railway Inspection Using AI 🚆🤖

This project leverages artificial intelligence to automate the inspection of railway tracks, ensuring safety, efficiency, and reduced human intervention. Using cutting-edge computer vision techniques and deep learning, this system detects and analyzes railway track conditions from images captured during inspection.

---

## 📌 Features

- **Railway Track Inspection:** Detect cracks, misalignments, and other irregularities on tracks.
- **YOLO-based Annotation:** Utilize YOLO (You Only Look Once) for object detection and annotation of railway images.
- **Dataset Management:** Process and annotate images into a structured dataset for training and testing models.
- **Integration with Kaggle:** Dataset uploaded and trained in Kaggle for collaborative research and model development.
- **Mobile Image Collection:** Easily capture railway images using a smartphone for field deployment.

---

## 📂 Project Structure

![Project Structure](https://github.com/user-attachments/assets/a727ca9f-6a29-4b1c-854f-8cc891facadd)

---

## 📊 Results

### Sample Detection Output  

![Sample Output](https://github.com/user-attachments/assets/e8881892-aad8-49b0-a38c-78142190fb2e)

- **Model Performance:**
  - Precision: 100%
  - Recall: 100%
  - F1-Score: 99.5%

![F1 Curve]![image](https://github.com/user-attachments/assets/eefa5dba-b1da-4c4d-abca-7c0fe33caa53)

- **Detected Issues:** Cracks, displacements, and wear on tracks were effectively identified during testing.

---

## 🛠️ Tools and Technologies

- **Python**: Core programming language for scripting and modeling.
- **YOLO**: Annotation and detection framework for images.
- **Google CoLab**: Deep learning framework for training and inference.
- **Kaggle**: Platform for dataset management and experimentation.
- **OpenCV**: Image processing and analysis library.

---

## 🧠 Technology Stack

- **Machine Learning (ML)**:  
  - Used for feature extraction and classification to detect track defects.  
  - Ensures robust and reliable detection using a supervised learning approach.  

- **Neural Networks (CNN)**:  
  - Core of the defect detection system, implemented using YOLO for object detection.  
  - Processes and analyzes images to identify and localize defects with bounding boxes and confidence scores.  

- **Data Annotation**:  
  - Images were annotated in the YOLO format to train the model effectively.  

---

## 💻 Implementation Details  

### **Machine Learning (ML)**  
- **Purpose**: Feature extraction and classification of defects.  
- **Process**:  
  1. Data Preprocessing: Applied resizing, augmentation, and normalization to the dataset.  
  2. Model Training: YOLO-based ML models were trained on the annotated dataset.  
  3. Evaluation: Accuracy metrics such as precision, recall, and F1 score were used to validate performance.  

### **Neural Networks (CNN)**  
- **Purpose**: High-accuracy image recognition for defect detection.  
- **Implementation**:  
  1. The YOLO model was trained on annotated railway track images.  
  2. Optimized using techniques like batch normalization and learning rate scheduling.  

### **Natural Language Processing (NLP)**  
While NLP is not directly implemented in the current version, it has potential applications, such as:  
- **Automated Reporting**: Generating textual descriptions of detected defects.  
- **User Interaction**: Enabling inspectors to query the system about defects or maintenance recommendations using natural language.  

---

## 📈 Future Scope

1. **Real-Time Video Integration**  
   The system now supports real-time video feed analysis, enabling continuous monitoring of railway tracks for potential defects.

2. **Fully Software-Based Solution**  
   Developed a platform-independent software application compatible with both laptops and mobile devices. The application utilizes laptop or mobile cameras to process live or recorded videos efficiently.

3. **Live GPS-Based Defect Localization**  
   Integrated GPS-based tagging to accurately locate defects. Maintenance teams can now identify exact locations using railway track pillar numbers or GPS coordinates.

4. **Google Maps Integration**  
   Seamlessly integrated Google Maps to allocate defect locations in real time, providing precise directions for maintenance teams to address issues swiftly.  

This robust solution ensures enhanced railway track safety by combining real-time monitoring, precise defect localization, and seamless accessibility across devices.
 
---

### 📸 Additional Images

![val_batch0_pred](https://github.com/user-attachments/assets/64943a3f-5748-477d-99c7-8e987f36820e)

![val_batch1_pred](https://github.com/user-attachments/assets/ae889856-784a-4e65-9239-40ce29333537)

![val_batch2_pred](https://github.com/user-attachments/assets/14ad918c-1040-4bd5-aaa3-dfb7bd8c7346)

---

## 🌟 Conclusion

This project demonstrates the power of combining Machine Learning, Neural Networks, and advanced Computer Vision techniques to tackle real-world challenges in railway safety. By automating the inspection of railway tracks, it offers a scalable, efficient, and accurate solution that reduces reliance on manual labor and minimizes human error.
The success of this system in detecting defects like cracks and misalignments underscores its potential as a critical tool for maintaining railway infrastructure. Looking ahead, the integration of Natural Language Processing for interactive reporting and real-time analysis capabilities will elevate the project into a comprehensive AI-powered inspection platform.
Through continuous development and real-world deployment, this project paves the way for smarter, safer, and more sustainable railway operations worldwide. 
