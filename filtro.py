import numpy as np
import cv2
import matplotlib.pyplot as plt

def outline(nombre):
    img=cv2.imread(nombre)

    imgray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    forma = np.shape(imgray)
    img2 = np.zeros(forma)

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    for x in list(range(1, forma[0] - 1)):
        for y in list(range(1, forma[1] - 1)):
            suma = 0

            for i in list(range(-1, 2)):
                for j in list(range(-1, 2)):
                    suma = imgray[x - i, y - j] * kernel[i + 1, j + 1] + suma

            img2[x, y] = suma

    imgfilt = np.stack(img2)
    imgfilt[imgfilt > 255] = 255
    imgfilt[imgfilt < 0] = 0
    imgfilt = imgfilt.astype("uint8")

    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")
    plt.show()

    plt.imshow(imgray, cmap='gray')
    plt.title("Imagen blanco y negro")
    plt.show()

    plt.imshow(imgfilt, cmap='gray')
    plt.title("Imagen con filtro 2")
    plt.show()

