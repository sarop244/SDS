import numpy as np


def ucle(a,b):
    
    dist = np.linalg.norm([a] - b, axis=1)#유클리디안 거리계산
        

    print(dist)


