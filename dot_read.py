import numpy as np
from scipy import misc
from matplotlib import pyplot as plt

# print(img.__class__)                  # wyswietli numpy.ndarray
# print(img.shape)                      # rozmiar tablicy numpyego (512,512)
# print(img.dtype)                      # dane w tablicy (uint8)

# print(img[:,0][:])                        # otworz obrazek w postaci macierzy
# print(img[:,0][20])                      # pierwszy wiersz
# print(img[:,0][0][0])                   # pierwszy wyraz w tym wierszu




class Ct:

    def __init__(self):
        self.filename  = "dot_square.png"
        self.img = misc.imread(self.filename)

    def read_row(self):
        rays_detected = []
        for i in range(len(self.img[:, 0])):
            index = 0
            for j in range(len(self.img[:, 0][i])):
                if self.img[:, 0][i][j] == 0:
                    index += 1
            rays_detected.append(index)

        return rays_detected[:]

    #  only for square pictures
    def read_angle45(self):
        # sum_first_diagonal = sum(a[i][i] for i in range(n))

        rays_detected = []
        matrix_size = len(self.img)
        for i in range(matrix_size):
            for j in range(matrix_size,0,-1):
                print(i)



        return rays_detected[:]


ct = Ct()
pamiec = ct.read_angle45()
print(pamiec)
