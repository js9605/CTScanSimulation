import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math


filename  = "top_right_square.jpg"
img = misc.imread(filename)
# print(img.__class__)                  # wyswietli numpy.ndarray
# print(img.shape)                      # rozmiar tablicy numpyego (512,512)
# print(img.dtype)                      # dane w tablicy (uint8)

# print(img[:])                        # otworz obrazek w postaci macierzy
# print(img[:,0][20])                      # pierwszy wiersz
# print(img[:,0][0][0])                   # pierwszy wyraz w tym wierszu

# len(img)     ile wierszy
# len(img[0])    ile kolumn

# print(img[9][0])

class Computer_tomography:

    def __init__(self):
        self.filename  = "top_right_square.jpg"
        self.img = misc.imread(self.filename)

    # left to right
    def read_row_leftToRight(self):
        rays_detected = []
        for row in range(len(self.img)):       #
            index = 0
            for col in range(len(self.img[row])):  #
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]

    # square matrix only
    def read_45angle_fromTopRight(self):
        rays_detected = []

        # rays_detected - from top right corner
        for col in range(len(self.img) - 1, -1, -1):

            index = 0
            for row in range((len(self.img)-1) - col):    # 10 - 1 - [9,8,7]
                col += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1

            rays_detected.append(index)

        #diagonal from bot right
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
            print("NEW ROW ----------------------------", row)
            index = 0
            for col in range((len(self.img)-1) - row):
                print(row, col)
                row += 1
                if sum(self.img[row][col]) <= 50:
                    index += 1
            rays_detected.append(index)

        del rays_detected[0]
        del rays_detected[-1]
        return rays_detected[:]


ct = Computer_tomography()
# pamiec = ct.read_row_leftToRight()
pamiec = ct.read_45angle_fromTopRight()
print(pamiec)
