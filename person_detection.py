from ultralytics import YOLO

import cv2
import cvzone

import datetime

from utils.utils import inisialize_csv_file, fill_null_date
from utils.recognition import Recognition
from utils.attendance import Attendance
from utils.presence import Presence
from utils.correct_names import get_correct_name



def main(path):
    cap = cv2.VideoCapture(path)

    detection = YOLO('models/yolov8n-face.pt')

    inisialize_csv_file()

    while True:
        try:
            rt,image = cap.read()
            image = cv2.resize(image,(1020,720))
            faces = detection.predict(image,conf=0.43, iou=0.5)
        except:
            fill_null_date()
            break

        count_face = 0
        confidence = []
        names = []

        for face in faces:
            for box in face.boxes:
                count_face += 1

                x1, y1, x2, y2 =  box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                h,w = y2-y1,x2-x1

                face = image[y1:y2,x1:x2]

                title = 'test/face_'+str(count_face)+'.png'
                cv2.imwrite(title , face)

                name, conf = Recognition(title)

                if name in names:
                    name = get_correct_name(names,count_face)
                
                confidence.append(conf)
                names.append(name)

                cvzone.cornerRect(image,[x1,y1,w,h],l=9,rt=3)
                cv2.putText(image, name+' '+conf, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        
        date = datetime.datetime.now().strftime('%y-%m-%d')
        time = datetime.datetime.now().strftime('%H:%M:%S')
        
        Presence(names,count_face,time)
        Attendance(count_face,date,time)

        cv2.putText(image, f"faces:{count_face}", (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
        cv2.putText(image, f"Time:{time}", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)

        cv2.imshow('frame',image)
        cv2.waitKey(1)


if __name__ == "__main__":
    path = "video/Test2.mp4"
    main(path)
