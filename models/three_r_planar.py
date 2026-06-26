import numpy as np

# defining the parameters for a three-r-planar arm
def get_arm():
    S1 = np.array([0,0,1,0,0,0])
    S2 = np.array([0,0,1,0,-1,0])
    S3 = np.array([0,0,1,0,-1.8,0])
    L1 = 1.0
    L2 = 0.8
    L3 = 0.5
    screw_axis = {"S1":S1,"S2":S2,"S3":S3}
    lengths = {"L1":L1,"L2":L2,"L3":L3}
    return {"screw axes": screw_axis,"lengths":lengths}
