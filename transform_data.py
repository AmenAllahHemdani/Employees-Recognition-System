import os
import cv2 
from ultralytics import YOLO

class_name = {
    'Alice': 0, 'Alison': 1, 'Lydia': 2, 'Scott': 3
}

face_detection = YOLO('yolov8n-face.pt')

image_folder = "Data/train/images"
label_folder = "Data/train/labels"

for name in os.listdir('Data/face'):
    if name.endswith(".DS_Store"):
        continue
    path = os.path.join('Data/face', name)
    n=0

    for img in os.listdir(path):
        if img.endswith(".jpg") or img.endswith(".png"):
            n+=1
            filename = name +'_'+str(n)+'.png'
            image_path = os.path.join(image_folder, filename)
            try:
                img = cv2.imread(os.path.join(path, img))
                if img is None:
                    print(f"Could not read image: {os.path.join(path, img)}")
                    continue  
                
                face = face_detection.predict(img,conf=0.40)
                if len(face)==0:
                    print(f"Could not find face in this image: {img_path}")
                    continue

                h_img, w_img = img.shape[:2]

                for info in face:
                    for box in info.boxes:
                        x1, y1, x2, y2 =  box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        h, w = y2-y1, x2-x1

                cvzone.cornerRect(img,[x1,y1,w,h],l=9,rt=2)
                cv2.putText(img, str(class_mapping[filename[:filename.find('_')]]), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)
                cv2.imwrite(image_path,img)

                with open(os.path.join(label_folder,filename.replace(".png", ".txt")), "w") as label_file:
                    label_file.write(f"{class_name[filename[:filename.find('_')]]} {x1} {y1} {w} {h}")

            except Exception as e:
                print(f"Error processing {img}: {e}")
print('Train data saved')