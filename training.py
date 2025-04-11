from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

model.train(
    data="Data/Dataset/data2/dataset.yaml", 
    epochs=100,  
    imgsz=640, 
    val=False
)
