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


class Computer_tomography:

    def __init__(self):
        self.filename  = "flat.jpg"
        self.img = misc.imread(self.filename)

    def read_(self):
        rays_detected = []
        for row in range(len(self.img)):       #
            index = 0
            for col in range(len(self.img[row])):  #
                if sum(self.img[row][col]) == 0:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]

    # square matrix only
    def read_45angle(self):
        rays_detected = []
        for col in range(len(self.img) - 1, -1, -1):
            row = 0
            index = 0
            # print("---------------------")
            for row in range((len(self.img) - 1) - col):
                col += 1
                if sum(self.img[row][col]) == 0:
                    index += 1
                rays_detected.append(index)
                # print(row,col)
        return rays_detected[:]


ct = Computer_tomography()
pamiec = ct.read_45angle()
print(pamiec)
