import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('Turquia.jpg')

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

maxs = np.max(img2)

img2 = img2 * 255 / maxs

img2 = img2.astype(np.uint8)

plt.imshow(img, cmap='gray')
plt.title("Vertical Edge")
plt.show()

plt.imshow(imgray, cmap='gray')
plt.title("Vertical Edge")
plt.show()

plt.imshow(img2, cmap='gray')
plt.title("Vertical Edge")
plt.show()
