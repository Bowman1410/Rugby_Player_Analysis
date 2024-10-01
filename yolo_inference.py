from ultralytics import YOLO

model = YOLO('models/best (2).pt')

results = model.predict('input_videos\input_vid_1.avi', save=True)
print(results[0])
print('---------------------------------')
for box in results[0].boxes:
    print(box)
    