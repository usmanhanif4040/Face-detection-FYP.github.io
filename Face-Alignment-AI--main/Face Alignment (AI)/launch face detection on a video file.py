d = MTCNN_Detector(50, 0.95)
vd = VideoFD(d)
v_file = r"C:\PI_FR\video\5_2.mp4"

save_path = r"C:\PI_FR\detect"
(f_count, fps) = vd.detect(v_file, save_path, True, False)

print("Face detections: "+str(f_count))
print("FPS: "+str(fps))