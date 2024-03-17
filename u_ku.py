# #View settings with 'yolo settings' or at 'C:\Users\Fysisk\AppData\Roaming\Ultralytics\settings.yaml'
# #Update settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'
#
# from collections import defaultdict
#
# import cv2
# import numpy as np
#
#from ultralytics import YOLO

# ########检测跟踪
# # Load an official or custom model
# model = YOLO('yolov8n.pt')  # Load an official Detect model
#
# # # Perform tracking with the model
# # # results = model.track(source=0, show=True)  # Tracking with default tracker
# # results = model.track(source=0, conf=0.3, iou=0.5, show=True, tracker="bytetrack.yaml")  # Tracking with ByteTrack tracker
#
#
# ######视频轨迹跟踪
# video_path = 0 # "path/to/video.mp4"
# cap = cv2.VideoCapture(video_path)
#
# # Store the track history
# track_history = defaultdict(lambda: [])
#
# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()
#
#     if success:
#         # Run YOLOv8 tracking on the frame, persisting tracks between frames
#         results = model.track(frame, persist=True)
#         for fr, result in enumerate(results):
#             if (result.boxes.id != None):
#                 # Get the boxes and track IDs
#                 boxes = results[0].boxes.xywh.cpu()
#                 track_ids = results[0].boxes.id.int().cpu().tolist()
#
#                 # Visualize the results on the frame
#                 annotated_frame = results[0].plot()
#
#                 # Plot the tracks
#                 for box, track_id in zip(boxes, track_ids):
#                     x, y, w, h = box
#                     track = track_history[track_id]
#                     track.append((float(x), float(y)))  # x, y center point
#                     if len(track) > 30:  # retain 90 tracks for 90 frames
#                         track.pop(0)
#
#                     # Draw the tracking lines
#                     points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
#                     cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=1)
#
#                 # Display the annotated frame
#                 cv2.imshow("YOLOv8 Tracking", annotated_frame)
#
#                 # Break the loop if 'q' is pressed
#                 if cv2.waitKey(1) & 0xFF == ord("q"):
#                     break
#     else:
#         # Break the loop if the end of the video is reached
#         break
#
# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()
# ######

# ###### 测试模型在不同设备的推理速度及精度
# from ultralytics.utils.benchmarks import benchmark
#
# # Benchmark on GPU
# benchmark(model='yolov8n.pt', data='coco8.yaml', imgsz=640, half=False, device=0)
# ########

### 转出格式
# model = YOLO('yolov8n.pt') #或者换自己的路径
# results = model.export(format='engine',device=0)
###