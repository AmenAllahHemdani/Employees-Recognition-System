from ultralytics import YOLO

class_name = ""
model = YOLO("models/best.pt")

def Recognition(title):

    global class_name
    confidence = 0.22

    results = model(title, conf=0.22, iou=0.5)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls) 

            if confidence < float(box.conf):  
                confidence = float(box.conf)
                class_name = model.names[class_id]

    return ('Unknoun',str(round(confidence,2))) if type(class_name) is not str else (class_name,str(round(confidence,2)))
