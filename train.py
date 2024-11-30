from ultralytics import YOLO

print("Hello World")

# Load a model
model = YOLO("yolov8m.pt")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=100, device= '0, 1')  # train the model
