import os
os.environ["OPENCV_VIDEOIO_PRIORITY_GSTREAMER"] = "0"  # 禁用GStreamer优先级
import cv2
import time

camID = 0  # 使用 /dev/video0
cap = cv2.VideoCapture(camID)  # 尝试直接使用默认后端
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
time.sleep(0.5)  # 等待摄像头初始化

ret, frame = cap.read()
if ret:
    cv2.imshow("Test Frame", frame)
    cv2.waitKey(0)
else:
    print("无法打开摄像头")
cap.release()
cv2.destroyAllWindows()
