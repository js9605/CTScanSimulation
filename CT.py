import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

def load_image(filename):
    img = plt.imread(filename)
    print img.shape
    return img

def rotate_image(img, angle):
    r_img = ndimage.rotate(img, angle, reshape=False)
    return r_img

def get_profile(img):
    dim = len(img.shape)
    if dim == 3:
        rows, cols, colors = img.shape
    else:
        rows, cols = img.shape
    data = np.zeros(rows)
    for r in range(rows):
        if dim == 3:
            data[r] = img[r,:,0].sum()
        else:
            data[r] = img[r,:].sum()
    return data

def create_sinogram(img, step):
    angle = 180. / step
    if len(img.shape) == 3:
        rows, cols, colors = img.shape
    else:
        rows, cols = img.shape

    sinogram = np.zeros((rows, step))
    for i in range(step):
        alpha = i * angle
        r_img = rotate_image(img, alpha)
        sinogram[:,i] = get_profile(r_img)
    return sinogram

def filtered_sinogram(sinogram):
    # high-pass filter
    h = np.zeros((3,3))
    h[0] = [0.17, 0.67, 0.17]
    h[1] = [0.67, -3.33, 0.67]
    h[2] = [0.17, 0.67, 0.17]
    rows, cols = sinogram.shape
    
    # brzegi zostana niezmienione, wiec je kopiuje
    new_s = np.zeros(sinogram.shape)
    new_s[0] = sinogram[0]
    new_s[:,0] = sinogram[:,0]
    new_s[rows-1] = sinogram[rows-1]
    new_s[:,cols-1] = sinogram[:,cols-1]

    # teraz filtrujemy
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            val = h * sinogram[r-1:r+2,c-1: c+2]
            val = val.sum()
            new_s[r,c] = val
    return new_s
    
    
def reconstruction(sinogram):
    rows, steps = sinogram.shape
    img = np.zeros((rows, rows), dtype=np.float64)
    alpha = 180. / steps

    for i in range(steps):
        img = ndimage.rotate(img, alpha, reshape=False)
        for r in range(rows):
            val = sinogram[r,i]
            img[r] = img[r] + val
            
    return img

filename = 'test2.jpg'
img = load_image(filename)
sinogram = create_sinogram(img, 180)
fig, a = plt.subplots(1,2)
a[0].imshow(sinogram, cmap="binary")
f_s = filtered_sinogram(sinogram)
a[1].imshow(f_s, cmap="binary")
plt.show()

r_img = reconstruction(f_s)
plt.imshow(r_img, cmap="binary")
plt.show()




    
