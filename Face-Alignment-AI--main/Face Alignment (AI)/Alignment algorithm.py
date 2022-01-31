class Face_Align:    
    def __init__(self, size):
        self.size = size
    
    def align_point(self, point, M):
        (x, y) = point
        p = np.float32([[[x, y]]])
        p = cv2.perspectiveTransform(p, M)
        
        return (int(p[0][0][0]), int(p[0][0][1]))

    def align(self, frame, face):
        (x1, y1, w, h) =  face['box']
        (l_eye, r_eye, nose, mouth_l, mouth_r) = Utils.get_keypoints(face)
        
        (pts1, pts2) = self.get_perspective_points(l_eye, r_eye, nose, mouth_l, mouth_r)
        
        s = self.size
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(frame, M, (s, s))
        
        f_aligned = copy.deepcopy(face)
        f_aligned['box'] = (0, 0, s, s)
        f_img = dst
        
        l_eye = self.align_point(l_eye, M)
        r_eye = self.align_point(r_eye, M)
        nose = self.align_point(nose, M)
        mouth_l = self.align_point(mouth_l, M)
        mouth_r = self.align_point(mouth_r, M)
        
        f_aligned = Utils.set_keypoints(f_aligned, (l_eye, r_eye, nose, mouth_l, mouth_r))
        
        return (f_aligned, f_img)

class Face_Align_Nose(Face_Align):    
    def get_perspective_points(self, l_eye, r_eye, nose, mouth_l, mouth_r):
        (xl, yl) = l_eye
        (xr, yr) = r_eye
        (xn, yn) = nose
        (xm, ym) = ( 0.5*(xl+xr), 0.5*(yl+yr) )
        (dx, dy) = (xn-xm, yn-ym)
        (xl2, yl2) = (xl+2.0*dx, yl+2.0*dy)
        (xr2, yr2) = (xr+2.0*dx, yr+2.0*dy)
        
        s = self.size
        pts1 = np.float32([[xl, yl], [xr, yr], [xr2, yr2], [xl2, yl2]])
        pts2 = np.float32([[s*0.25, s*0.25], [s*0.75, s*0.25], [s*0.75, s*0.75], [s*0.25,s*0.75]])
        
        return (pts1, pts2)