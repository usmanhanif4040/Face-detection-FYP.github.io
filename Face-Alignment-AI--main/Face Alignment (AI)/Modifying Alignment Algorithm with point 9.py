class Face_Align_Mouth(Face_Align):    
    def get_perspective_points(self, l_eye, r_eye, nose, mouth_l, mouth_r):
        (xl, yl) = l_eye
        (xr, yr) = r_eye
        (xml, yml) = mouth_l
        (xmr, ymr) = mouth_r
        
        (xn, yn) = ( 0.5*(xl+xr), 0.5*(yl+yr) )
        (xm, ym) = ( 0.5*(xml+xmr), 0.5*(yml+ymr) )
        (dx, dy) = (xm-xn, ym-yn)
        (xl2, yl2) = (xl+1.1*dx, yl+1.1*dy)
        (xr2, yr2) = (xr+1.1*dx, yr+1.1*dy)
        
        s = self.size
        pts1 = np.float32([[xl, yl], [xr, yr], [xr2, yr2], [xl2, yl2]])
        pts2 = np.float32([[s*0.3, s*0.3], [s*0.7, s*0.3], [s*0.7, s*0.75], [s*0.3, s*0.75]])
        
        return (pts1, pts2)