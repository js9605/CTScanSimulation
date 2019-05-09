import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math


class Bresenham_max45:

    def __init__(self):

        self.img = np.zeros((10,10,3), dtype = np.uint8)
        self.img = self.img + 255

        # assuming that x2 > x1 ; y2 > y1 ; x2 - x1 > y2 - y1
        print("---01---")
        self.x1 = 1
        self.y1 = 1
        self.x2 = 7
        self.y2 = 5
        print("x1: ", self.x1)
        print("y1: ", self.y2)

        if (self.x2 - self.x1) <= (self.y2 - self.y1):
            print("CONDITIONS ARE NOT SATISFIED")

    def draw(self):

        # self.img[1,1, :] = 0
        index = 0

        dx = self.x2 - self.x1  # 01
        dy = self.y2 - self.y1  # 02
        e = dx / 2              # 03
        print("dx: ", dx)
        print("dy: ", dy)
        print("e: ", e)

        print("---02---")
        print("zapalam wspolrzedne: ", self.x1, self.y1)
        self.img[self.x1, self.y1,:] = 0    # 05

        for i in range(dx):     # 04
            print("---W PETLI--- nr: ", i)
            self.x1 = self.x1 + 1       # 06
            print("x2: ", self.x1)
            e = e - dy                  # 07
            print("e: ", e)

            if e >= 0:                  # 08
                print("zapalam: ", self.x1, self.y1)
                self.img[self.x1, self.y1,:] = 0   # 11
            else:
                self.y1 = self.y1 + 1       # 09
                print("y1: ", self.y1)
                self.img[self.x1, self.y1, :] = 0
                e = e + dx                  # 10
                print("e:  ", e)

        misc.imsave("Bresenham_sheet.jpg", self.img)


class Bresenham:

    def __init__(self, x1, y1, x2, y2):

        self.img = np.zeros((10,10,3), dtype = np.uint8)
        self.img = self.img + 255
        self.rays_detected = []

        self.x1 = x1
        self.y1 = y1
        self.x2 = y2
        self.y2 = x2

    def draw(self):

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
            # self.img[self.x1, self.y1,:] = 0    # 05

            for i in range(dx):     # 04
                self.x1 = self.x1 + kx       # 06
                e = e - dy                  # 07

                if e >= 0:                  # 08
                    self.img[self.x1, self.y1,:] = 0   # 11

                else:
                    self.y1 = self.y1 + ky       # 09
                    e = e + dx                  # 10
                    self.img[self.x1, self.y1,:] = 0

        misc.imsave("Bresenham_sheet_all_angles.jpg", self.img)

    def read(self):

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

        self.img[self.x1, self.y1, :] = 0

        if dx < dy:
            e = dy / 2
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
            # self.img[self.x1, self.y1,:] = 0    # 05

            for i in range(dx):  # 04
                self.x1 = self.x1 + kx  # 06
                e = e - dy  # 07

                if e >= 0:  # 08
                    self.img[self.x1, self.y1, :] = 0  # 11

                else:
                    self.y1 = self.y1 + ky  # 09
                    e = e + dx  # 10
                    self.img[self.x1, self.y1, :] = 0

        self.rays_detected.append(index)





# bresenham = Bresenham_max45()
bresenham = Bresenham(1,1,9,6)
bresenham.draw()


