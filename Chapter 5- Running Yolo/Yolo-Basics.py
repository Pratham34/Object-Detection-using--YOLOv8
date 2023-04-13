from ultralytics import YOLO
import cv2

# There are different types of weights - the nano, the medium, the large . It's based on you which one you want to choose .
model = YOLO('../Yolo-Weights/yolov8l.pt')

results = model("Images/3.png", show=True)
cv2.waitKey(0)