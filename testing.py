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

    def read(self):

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
        if sum(self.img[self.x1][self.y1]) <= 50:
            index += 1

        for i in range(dx):     # 04
            print("---W PETLI--- nr: ", i)
            self.x1 = self.x1 + 1       # 06
            print("x2: ", self.x1)
            e = e - dy                  # 07
            print("e: ", e)

            if e >= 0:                  # 08
                print("zapalam: ", self.x1, self.y1)
                if sum(self.img[self.x1][self.y1]) <= 50:
                    index += 1
            else:
                self.y1 = self.y1 + 1       # 09
                print("y1: ", self.y1)
                if sum(self.img[self.x1][self.y1]) <= 50:
                    index += 1
                e = e + dx                  # 10
                print("e:  ", e)

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




