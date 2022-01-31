class VideoFD:    
    def __init__(self, detector):
        self.detector = detector
    
    def detect(self, video, save_path = None, align = False, draw_points = False):
        detection_num = 0;
        capture = cv2.VideoCapture(video)
        img = None

        dname = 'AI face detection'
        cv2.namedWindow(dname, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(dname, 960, 720)
        
        frame_count = 0
        dt = 0
        face_num = 0
        
        if align:
            fa = Face_Align_Nose(160)
        
        # Capture all frames
        while(True):    
            (ret, frame) = capture.read()
            if frame is None:
                break
            frame_count = frame_count+1
            
            t1 = time.time()
            faces = self.detector.detect(frame)
            t2 = time.time()
            p_count = len(faces)
            detection_num += p_count
            dt = dt + (t2-t1)
            
            if (not (save_path is None)) and (len(faces)>0) :
                f_base = os.path.basename(video)
                for (i, face) in enumerate(faces):
                    if align:
                        (f_cropped, f_img) = fa.align(frame, face)
                    else:
                        (f_cropped, f_img) = self.detector.extract(frame, face)
                    if (not (f_img is None)) and (not f_img.size==0):
                        if draw_points:
                            Utils.draw_faces([f_cropped], (255, 0, 0), f_img, draw_points, False)
                        face_num = face_num+1
                        dfname = os.path.join(save_path, f_base + ("_%06d" % face_num) + ".png") 
                        cv2.imwrite(dfname, f_img)
            
            if len(faces)>0:
                Utils.draw_faces(faces, (0, 0, 255), frame)
                if not (save_path is None):
                    dfname = os.path.join(save_path, f_base + ("_%06d" % face_num) + "_frame.png")
                    cv2.imwrite(dfname, frame)

            # Display the resulting frame
            cv2.imshow(dname,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        capture.release()
        cv2.destroyAllWindows()    
        
        fps = frame_count/dt
        
        return (detection_num, fps)