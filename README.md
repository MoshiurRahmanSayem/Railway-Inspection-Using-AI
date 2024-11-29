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

## 🚀 Installation


1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MdMehedi-Hassan/Railway-Inspection-Using-AI.git
   cd Railway-Inspection-Using-AI
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Dataset:**
   - Use YOLO format to annotate images of railway tracks.
   - Place the annotated dataset in the `datasets/` directory.

4. **Train Model:**
   ```bash
   python scripts/train.py
   ```

5. **Test Model:**
   ```bash
   python scripts/test.py --input path/to/test/images
   ```

---

## 📊 Results

### Sample Detection Output  

![Sample Output](https://github.com/user-attachments/assets/e8881892-aad8-49b0-a38c-78142190fb2e)


- **Model Performance:**
  - Precision: 98%
  - Recall: 95%
  - F1-Score: 96.5%

- **Detected Issues:** Cracks, displacements, and wear on tracks were effectively identified during testing.

---

## 🛠️ Tools and Technologies


- **Python**: Core programming language for scripting and modeling.
- **YOLO**: Annotation and detection framework for images.
- **Google CoLab**: Deep learning framework for training and inference.
- **Kaggle**: Platform for dataset management and experimentation.
- **OpenCV**: Image processing and analysis library.

---

## **Technology Stack**  
- **Machine Learning (ML)**:  
  - Used for feature extraction and classification to detect track defects.  
  - Ensures robust and reliable detection using a supervised learning approach.  

- **Neural Networks (CNN)**:  
  - Core of the defect detection system, implemented using YOLO for object detection.  
  - Processes and analyzes images to identify and localize defects with bounding boxes and confidence scores.  

- **Data Annotation**:  
  - Images were annotated in the YOLO format to train the model effectively.  

---

## **Implementation Details**  

### **Machine Learning (ML)**  
- **Purpose**: Feature extraction and classification of defects.  
- **Process**:  
  1. Data Preprocessing: Applied resizing, augmentation, and normalization to the dataset.  
  2. Model Training: YOLO-based ML models were trained on the annotated dataset.  
  3. Evaluation: Accuracy metrics such as precision, recall, and F1 score were used to validate performance.  

### **Neural Networks (CNN)**  
- **Purpose**: High-accuracy image recognition for defect detection.  
- **Implementation**:  
  - The YOLO model was trained on annotated railway track images.  
  - Optimized using techniques like batch normalization and learning rate scheduling.  

### **Natural Language Processing (NLP)**  
While NLP is not directly implemented in the current version, it has potential applications, such as:  
- **Automated Reporting**: Generating textual descriptions of detected defects.  
- **User Interaction**: Enabling inspectors to query the system about defects or maintenance recommendations using natural language.  

---

## **Future Scope**  
1. **Integrating NLP**: Add features for generating inspection reports and interacting with users via natural language queries.  
2. **Real-Time Analysis**: Improve the system to analyze video streams for live defect detection.  
3. **Deployment**: Implement the solution in edge devices for on-site railway inspections.  

---

### 📸 Additional Images

![val_batch0_pred](https://github.com/user-attachments/assets/64943a3f-5748-477d-99c7-8e987f36820e)

![val_batch1_pred](https://github.com/user-attachments/assets/ae889856-784a-4e65-9239-40ce29333537)

![val_batch2_pred](https://github.com/user-attachments/assets/14ad918c-1040-4bd5-aaa3-dfb7bd8c7346)

---
## **Conclusion**  
This project successfully combines Machine Learning and Neural Networks to automate railway track inspections, providing a scalable and efficient solution. Future iterations will integrate NLP for enhanced user interaction and reporting capabilities, making it an all-in-one AI-powered inspection tool.
