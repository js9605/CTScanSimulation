import rotate as r
import Bresenham_algorithm as ba
import cv2
from statistics import mean
import matplotlib.pyplot as plt


# reading
im_name = "ct_scan"
r.white_background(im_name)
# r.rotate(str(im_name))

bresenham = ba.Bresenham(im_name)
image_len0 = len(cv2.imread(str(im_name) + ".jpg"))
rotated_images = []

# UWAGA --------------------------------------------------------------------
# Dlaczego jak zmieniam i w linii 21 to program dziala, a gdy staram sie zmienic i w for i in range to nie dziala?

for i in range(len(r.rotate(str(im_name)))):            # to przeskakuje pomiedzy obrazkami
# for i in range(5):  # to przeskakuje pomiedzy obrazkami
    # i = 5

    rays_detected = []
    image = r.rotate(str(im_name))[i]                   # zamienia image na kolejny obrocony obrazek
    margins = (len(image) / 4)                          # marginesy = 5 dla obrazka 20
    image_len = (image_len0 + 2 * margins)

    for i in range(image_len):
        index = 0
        for j in range(image_len):
            if (i > margins and i < image_len - margins + 1) and (j > margins and j < image_len - margins + 1):
                # print mean(image[i][j])
                # [ruch pomiedzy wierszami][ pomiedzy kolumnami]
                if mean(image[i][j]) <= 82:
                    # print i,j
                    index += 1
        rays_detected.append(index)

    # cv2.imshow("Rotated", image)
    # cv2.waitKey(0)
    cv2.imwrite('rotated_sample' + str(i) + '.png',image)

    rotated_images.append(rays_detected)

print("rotated images: ", rotated_images)

for i in range(len(rotated_images)):
    # plt.clf()       # cleares plots
    x = []
    for j in range(len(rotated_images[i])):
        x.append(j)
    plt.plot(x,rotated_images[i])
    plt.savefig("sinogram" + str(i) + ".jpg")



# image = r.rotate(str(im_name))[0]
# image_len = len(cv2.imread(str(im_name) + ".jpg"))
#
# # print image[0]
#
# for i in range(image_len):
#     print "next row"
#     for j in range(image_len):
#         print image[i][j]
