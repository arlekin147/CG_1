import numpy as np

class Figure(object):

    def __init__(self, x : list, y : list, z : list):
        self.deg = 0
        self.x = x
        self.y = y
        self.z = z

    def spin(self, axis : str):
        
        """x = x + 1
        y = y + 1
        z = z + 1
        add = np.ones(len(x))"""
        alpha = self.deg * np.pi / 180
        mx = np.array([self.x, self.y, self.z])
        axis = axis.upper()
        if axis == "X":
                 spinMX = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)],
                 [0, np.sin(alpha), np.cos(alpha)]])
                 """spinMX = np.array([[1, 0, 0, 0], [0, np.cos(alpha), -np.sin(alpha), 0],
                 [0, np.sin(alpha), np.cos(alpha), 0], [0, 0, 0, 1]])"""
        elif axis == "Y":
                spinMX = np.array([[np.cos(alpha), 0, np.sin(alpha)], [0, 1, 0],
                 [-np.sin(alpha), 0, np.cos(alpha)]])
                """spinMX = np.array([[np.cos(alpha), 0, np.sin(alpha), 0], [0, 1, 0, 0],
                 [-np.sin(alpha), 0, np.cos(alpha), 0], [0, 0, 0, 1]])"""
        elif axis == "Z":
                spinMX = np.array([[np.cos(alpha), -np.sin(alpha), 0], [np.sin(alpha), 
                np.cos(alpha), 0],[0, 0, 1]])
                """spinMX = np.array([[np.cos(alpha), -np.sin(alpha), 0, 0], [np.sin(alpha), 
                np.cos(alpha), 0, 0],[0, 0, 1, 0], [0, 0, 0, 1]])"""
        newMX = mx.T.dot(spinMX).T
        print("spinned")
        #newMX = np.array([mx[0][0:len(mx[0]-1)],mx[1][0:len(mx[1]-1)] ,mx[2][0:len(mx[2]-1)]])
        self.x = newMX[0]
        self.y = newMX[1]
        self.z = newMX[2]
