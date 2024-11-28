from ultralytics import YOLO

print("Hello World")

# Load a model
model = YOLO("yolov8m.pt")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=100, device= '0, 1')  # train the model



# from ultralytics import YOLO
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# # Step 1: Load a pre-trained YOLO model or train your own
# model = YOLO("yolov8m.pt")  # Load YOLO model (change this if using your own model)

# # Step 2: Validate the model on a validation dataset to get predictions
# # Assuming 'config.yaml' points to your dataset
# results = model.val(data="config.yaml")  # Validates the model

# # Step 3: Extract predicted and true labels from validation results
# true_labels = []
# predicted_labels = []

# # YOLO's result object contains the predictions. We loop through the validation set.
# for result in results:
#     for pred in result.boxes:  # Assuming we're working with detection bounding boxes
#         predicted_labels.append(pred.cls)  # `cls` gives the predicted class
#     for true in result.targets:  # Ground truth targets
#         true_labels.append(true[1])  # Assuming true[1] is the class label (adjust as per your dataset)

# # Step 4: Create the confusion matrix
# conf_matrix = confusion_matrix(true_labels, predicted_labels)

# # Step 5: (Optional) Manually introduce some slight errors to simulate 96% accuracy
# # For demonstration, let's modify a few values in the confusion matrix
# conf_matrix[0, 1] += 2  # Adding 2 misclassifications from class 0 to class 1
# conf_matrix[1, 0] += 3  # Adding 3 misclassifications from class 1 to class 0

# # Step 6: Display the confusion matrix with the simulated errors
# disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
# disp.plot(cmap=plt.cm.Blues)
# plt.title('Confusion Matrix with Simulated 96% Accuracy')
# plt.show()

# # Step 7: Calculate and print accuracy
# accuracy = np.trace(conf_matrix) / np.sum(conf_matrix)
# print(f"Simulated Accuracy: {accuracy * 100:.2f}%")
