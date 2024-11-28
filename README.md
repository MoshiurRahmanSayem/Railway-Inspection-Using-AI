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


```plaintext
Railway-Inspection-Using-AI/
│
├── 📁 datasets/                 # Annotated datasets in YOLO format
├── 📁 models/                   # Trained models and configurations
├── 📁 scripts/                  # Python scripts for preprocessing, training, and testing
├── 📁 results/                  # Outputs like graphs, metrics, and detected images
├── 📁 docs/                     # Documentation and tutorials
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project description
└── 📄 LICENSE                   # License information
```

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
- **TensorFlow/PyTorch**: Deep learning framework for training and inference.
- **Kaggle**: Platform for dataset management and experimentation.
- **OpenCV**: Image processing and analysis library.

---

## 📄 Future Scope

- Enhance the model's robustness by adding more diverse datasets.
- Real-time deployment using edge devices like Raspberry Pi.
- Expand detection to include other railway components (e.g., switches, signals).
- Integrate predictive maintenance algorithms.

---

## 🤝 Contribution

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Feature description"`.
4. Push the changes: `git push origin feature-branch-name`.
5. Open a Pull Request.

---

### 📸 Additional Images

![val_batch0_pred](https://github.com/user-attachments/assets/64943a3f-5748-477d-99c7-8e987f36820e)

![val_batch1_pred](https://github.com/user-attachments/assets/ae889856-784a-4e65-9239-40ce29333537)

![val_batch2_pred](https://github.com/user-attachments/assets/14ad918c-1040-4bd5-aaa3-dfb7bd8c7346)
