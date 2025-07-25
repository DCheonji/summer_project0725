from ultralytics import YOLO
import cv2
model = YOLO("yolo11s.pt")
image_path = "image1.jpg"
results = model(image_path)
results[0].save("result1.jpg")
