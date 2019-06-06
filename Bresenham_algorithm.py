import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math
import cv2


class Bresenham:

    def __init__(self, name):

        self.rays_detected = []
        self.name = str(name) + ".jpg"

    def create_image(self,x,y):
        self.size_x = x
        self.size_y = y
        self.img = np.zeros((self.size_x,self.size_y,3), dtype = np.uint8)
        self.img = self.img + 255
        # misc.imsave(str(self.name), self.img)
        cv2.imwrite(str(self.name), self.img)

    # fill pixels
    def draw(self, x1, y1, x2, y2):

        self.x1 = y1
        self.y1 = x1
        self.x2 = y2
        self.y2 = x2


        if self.x1 <= self.x2:
            kx = 1
        else:
            kx = -1
        if self.y1 <= self.y2:
            ky = 1
        else:
            ky = -1

        dx = int(math.fabs(self.x2 - self.x1))
        dy = int(math.fabs(self.y2 - self.y1))

        self.img[self.x1, self.y1, :] = 0

        if dx < dy:
            e = dy /2
            for i in range(dy):
                self.y1 = self.y1 + ky
                e = e - dx
                if e >= 0:
                    self.img[self.x1, self.y1, :] = 0
                else:
                    self.x1 = self.x1 + kx
                    e = e + dy
                    self.img[self.x1, self.y1, :] = 0
        else:
            e = dx / 2

            for i in range(dx):
                self.x1 = self.x1 + kx
                e = e - dy

                if e >= 0:
                    self.img[self.x1, self.y1,:] = 0

                else:
                    self.y1 = self.y1 + ky
                    e = e + dx
                    self.img[self.x1, self.y1,:] = 0

        # misc.imsave(str(self.name), self.img)
        cv2.imwrite(str(self.name), self.img)

    # read pixels
    def read(self, x1, y1, x2, y2):

        self.x1 = y1
        self.y1 = x1
        self.x2 = y2
        self.y2 = x2

        filename  = self.name
        # img = misc.imread(filename)
        img = cv2.imread(filename)

        index = 0
        if self.x1 <= self.x2:
            kx = 1
        else:
            kx = -1
        if self.y1 <= self.y2:
            ky = 1
        else:
            ky = -1

        dx = int(math.fabs(self.x2 - self.x1))
        dy = int(math.fabs(self.y2 - self.y1))

        if sum(img[self.x1][self.y1]) <= 50:
            index += 1

        if dx < dy:
            e = dy / 2
            for i in range(dy):
                self.y1 = self.y1 + ky
                e = e - dx
                if e >= 0:
                    if sum(img[self.x1][self.y1]) <= 50:
                        index += 1
                else:
                    self.x1 = self.x1 + kx
                    e = e + dy
                    if sum(img[self.x1][self.y1]) <= 50:
                        index += 1
        else:
            e = dx / 2

            for i in range(dx):
                self.x1 = self.x1 + kx
                e = e - dy

                if e >= 0:
                    if sum(img[self.x1][self.y1]) <= 50:
                        index += 1

                else:
                    self.y1 = self.y1 + ky
                    e = e + dx
                    if sum(img[self.x1][self.y1]) <= 50:
                        index += 1

        self.rays_detected.append(index)
        return self.rays_detected


# bresenham = Bresenham("ct_scan")
# bresenham.create_image(100,100)   # Bresenham(size_X, size_Y, name)
# bresenham.draw(0,50,99,50)                 # .draw(x1, y1, x2, y2)
# print(bresenham.read(0,50,99,50))
