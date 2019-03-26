import numpy as np
from scipy import misc
from matplotlib import pyplot as plt

# img = misc.imread("kropka.jpg")
# print(img.__class__)                  # wyswietli numpy.ndarray
# print(img.shape)                      # rozmiar tablicy numpyego (512,512)
# print(img.dtype)                      # dane w tablicy (uint8)

# print(img[:,0][:])                        # otworz obrazek w postaci macierzy
# print(img[:,0][20])                      # pierwszy wiersz
# print(img[:,0][0][0])                   # pierwszy wyraz w tym wierszu


def wyswietl_obraz_w_macierzy():

    # nazwa_pliku = input("Podaj nazwe pliku z rozszerzeniam: ")
    nazwa_pliku = "kropka.jpg"
    img = misc.imread(nazwa_pliku)
    pamiec = []
    for i in range(len(img[:,0][:])):       # leci po wierszach
        pamiec.append([])                   # tworzy miejsce na zapisanie danych do kolorowania
        # print(img[0:,i][i])                # Wyswietli cala macierz

        for j in range(len(img[:,0][i])):   # leci po poszczegolnych elementach wiersza
            print(img[:,0][i][j])           # wyswiettla kazdy element macierzy

            if img[:,0][i][j] == 0:         # wyswietla tylko elementy rowne 0
                # print(img[:, 0][i][j])
                pass

class Ct:


    def read_row(self):                  # zczytuje ile jest zer w wierszu

        nazwa_pliku = "kropka.jpg"
        img = misc.imread(nazwa_pliku)
        pamiec = []
        for i in range(len(img[:, 0])):    # len 31
            indeks = 0
            for j in range(len(img[:, 0][i])):  # len 4
                if img[:, 0][i][j] == 0:
                    indeks += 1
            pamiec.append(indeks)

        return pamiec[:]


    def draw_ct(self):

        img = 0
        misc.imsave("3.jpg", img)  # ZApisuje obrazek


# zczytaj_macierz()
ct = Ct()
pamiec = ct.read_row()
print(pamiec)


# misc.imsave("3.jpg", img) # ZApisuje obrazek
