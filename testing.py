import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math

# FOR EXPERIMENTING
# filename  = "top_right_square.jpg"
# img = misc.imread(filename)
# print(img.__class__)                  # wyswietli numpy.ndarray
# print(img.shape)                      # rozmiar tablicy numpyego (512,512)
# print(img.dtype)                      # dane w tablicy (uint8)
# print(img[:])                        # otworz obrazek w postaci macierzy
# print(img[:,0][20])                      # pierwszy wiersz
# print(img[:,0][0][0])                   # pierwszy wyraz w tym wierszu
# len(img)     ile wierszy
# len(img[0])    ile kolumn
# print(img[0][1])

# COMMENTS
# Try to make "TopLeft" part as simple as "TopRight"


# ------------------------------------------------------------------------------------------

class Bresenham:

    def __init__(self):
        self.filename  = "graphic_for_testing.jpg"
        self.img = misc.imread(self.filename)
        self.rays_detected = []
        self.x = []
        self.y = []
        # end point
        self.x2 = len(self.img[0]) - 1
        self.y2 = len(self.img) - 1

        for i in range(len(self.img)):
            self.x.append(0)
        for i in range(1,len(self.img)):
            self.x.append(i)
        for i in range(len(self.img) - 1 ,0,-1):
            self.y.append(i)
        for i in range(len(self.img)):
            self.y.append(0)


    def read(self):

        # for angle < 45
        for i in range(len(self.img)):
            index = 0

            # starting points in Bresenham algorithm
            self.x1 = self.x[i]
            self.y1 = self.y[i]

            if self.x1 <= self.x2:                          # K01
                self.kx = 1     # step x
            else:
                self.kx = -1
            if self.y1 <= self.y2:                          # K02
                self.ky = 1
            else:
                self.ky = -1

            self.dx = int(math.fabs(self.x2 - self.x1))  # absolute value  #K03
            self.dy = int(math.fabs(self.y2 - self.y1))  # absolute value  # K04

            if sum(self.img[self.x1][self.y1]) <= 50:       # K05
                index += 1

            if self.dx < self.dy:                           # K06
                # for angle > 45
                self.e = self.dy / 2                        # k16
                for _ in range(self.dy):                    # K17
                    self.y1 = self.y1 + self.ky             # k18
                    self.e = self.e - self.dx               # k19
                    if self.e >= 0:                         # k20
                        if sum(self.img[self.x1][self.y1]) <= 50:  # k23
                            index += 1
                    else:
                        self.x1 = self.x1 + self.kx         # k21
                        self.e = self.e + self.dy           # k22
            else:
                self.e = self.dx / 2      # error expression # k07
                for _ in range(self.dx):                      # k08
                    self.x1 = self.x1 + self.kx
                    self.e = self.e - self.dy               # k10
                    if self.e >= 0:                         # K11
                        if sum(self.img[self.x1][self.y1]) <= 50:  # k14
                            index += 1
                    else:
                        self.y1 = self.y1 + self.ky         # K12
                        self.e = self.e + self.dx           # K13


        self.rays_detected.append(index)
        print(self.rays_detected)


# square matrix only
class Computer_tomography:

    def __init__(self):
        self.filename  = "graphic_for_testing.jpg"
        self.img = misc.imread(self.filename)

    def up(self):
        rays_detected = []
        for col in range(len(self.img[0])):
            index = 0
            for row in range(len(self.img)):
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)
        return rays_detected[:]

    def left(self):
        rays_detected = []
        for row in range(len(self.img)):
            index = 0
            for col in range(len(self.img[row])):
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]


    # ray goes from top left corner
    def topLeft(self):
        rays_detected = []

        # rays_detected - from top right corner
        for col in range(len(self.img) - 1, -1, -1):
            index = 0
            for row in range((len(self.img)-1) - col):    # 10 - 1 - [9,8,7]
                col += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        #diagonal
        index = 0
        for row in range(len(self.img)):
            if sum(self.img[row][row]) <= 50:
                index += 1
        rays_detected.append(index)

        # rays_detected - from top right corner
        for row in range(len(self.img) - 1, -1, -1):  # [9 8 7 ]
            index = 0
            for col in range((len(self.img)-1) - row):    # 10 - 1 - [9,8,7]     [0,1,2]
                row += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1

        for row in range(len(self.img)):
            index = 0
            for col in range((len(self.img)-1) - row):
                row += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        del rays_detected[0]
        del rays_detected[-1]
        return rays_detected[:]

    def topRight(self):
        list = []
        tsil = []

        for i in range(len(self.img)):
            list.append(i)

        for i in range(len(self.img) - 1,-1,-1):
            tsil.append(i)

        rays_detected = []
        row = 0
        for col in list:
            index = 0
            for j in range(col + 1):
                # print(row + j,col - j)
                if sum(self.img[row + j][col - j]) <= 50:
                    index += 1
            rays_detected.append(index)

        # after diagonal
        col = len(list) - 1
        for row in range(1,len(list)):
            # print("NEXT ROW")
            index = 0
            for j in range(len(list)):
                if row + j == len(list):
                    break
                # print(row + j,col - j)
                if sum(self.img[row + j][col - j]) <= 50:
                    index += 1
            rays_detected.append(index)

        return rays_detected


# ct = Computer_tomography()
# memory = ct.topRight()

bresenham = Bresenham()
bresenham.read()




