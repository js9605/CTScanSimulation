import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import math


filename  = "flat.jpg"
img = misc.imread(filename)
# print(img.__class__)                  # wyswietli numpy.ndarray
# print(img.shape)                      # rozmiar tablicy numpyego (512,512)
# print(img.dtype)                      # dane w tablicy (uint8)

# print(img[0])                        # otworz obrazek w postaci macierzy
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
                if sum(self.img[row][col]) == 0:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]

    # square matrix only
    def read_45angle_fromTopRight(self):
        rays_detected = []

        # rays_detected - from top right corner
        for col in range(len(self.img) - 1, -1, -1):
            print("NOWE COL----------------------")
            row = 0
            index = 0
            for row in range((len(self.img)-1) - col):    # 10 - 1 - [9,8,7]
                col += 1
                print("for row: ", row, col)
                if sum(self.img[row][col]) == 0:
                    print("if: ", row,col)
                    index += 1

            rays_detected.append(index)

        del rays_detected[0]

        # rays_detected - diagonal (left to right)
        # index = 0
        # for i in range(len(img)):
        #     if sum(self.img[i][i]) == 0:
        #         index += 1
        # rays_detected.append(index)

        # rays_detected - from diagonal to the bottom left
        # for i in range(len(img)):
        #     pass



        return rays_detected[:]


ct = Computer_tomography()
pamiec = ct.read_45angle_fromTopRight()
print(pamiec)
