import numpy as np
from scipy import misc
import imutils
import cv2
from PIL import Image


def white_background(im_name):
    image = Image.open(str(im_name) + ".jpg")
    image_len = len(cv2.imread(str(im_name) + ".jpg"))
    margins = image_len * (2)
    background = Image.new('RGB', (image_len + margins / 2, image_len + margins / 2), color='white')
    background_copy = background.copy()
    position = ((margins / 4), (margins / 4))
    background_copy.paste(image, position)
    background_copy.save(str(im_name) + "white_bcgr" + ".jpg")
    return background_copy

def rotate(im_name):
    # image = Image.open(str(im_name) + ".jpg")
    # image = cv2.imread(str(im_name) + ".jpg")

    rotated_list = []
    image = white_background(im_name)
    for angle in np.arange(0, 360, 15):
        rotated = misc.imrotate(image, angle)

        # print rotated
        # cv2.imshow("Rotated", rotated)
        # cv2.waitKey(0)

        rotated_list.append(rotated)
    return rotated_list





