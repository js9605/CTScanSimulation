import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math

class Bresenham:

    def __init__(self):

        self.img = np.zeros((10,10,3), dtype = np.uint8)
        self.img = self.img + 255

        # assuming that x2 > x1 ; y2 > y1 ; x2 - x1 > y2 - y1
        self.x1 = 0
        self.y1 = 0
        self.x2 = 9
        self.y2 = 9

        if (self.x2 - self.x1) > (self.y2 - self.y1):
            print("CONDITIONS ARE NOT SATISFIED")

    def read(self):

        # self.img[1,1, :] = 0

        index = 0

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        e = dx / 2

        self.img[self.x1, self.y1,:] = 0

        for i in range(dx):
            print("x: ", self.x1,"    ","y: ", self.y1)
            print("e: ", e)
            self.x1 = self.x1 + 1
            e = e - dy
            if e >= 0:
                self.img[self.x1, self.y1,:] = 0
            self.y1 = self.y1 + 1
            e = e + dx

        misc.imsave("Bresenham_sheet.jpg", self.img)

class Test:

    def __init__(self):

        self.img = np.zeros((7,7,3), dtype = np.uint8)
        self.img = self.img + 255

        # assuming that x2 > x1 ; y2 > y1 ; x2 - x1 > y2 - y1
        self.x1 = 0
        self.y1 = 0
        self.x2 = 9
        self.y2 = 9

        if (self.x2 - self.x1) > (self.y2 - self.y1):
            print("CONDITIONS ARE NOT SATISFIED")

    def read(self):

        index = 0

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        e = dx / 2

        self.img[self.x1, self.y1] = 0

        for i in range(dx):
            print(i)
            self.x1 = self.x1 + 1
            e = e - dy
            if e >= 0:
                self.img[self.x1, self.y1] = 0
            self.y1 = self.y1 + 1
            e = e + dx

        misc.imsave("Bresenham_sheet.jpg", self.img)


bresenham = Bresenham()
bresenham.read()

# filename  = "Bresenham_sheet.jpg"
# img = misc.imread(filename)
# print(img[0,2,0])




