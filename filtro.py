import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('Turquia.jpg')

imgray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
forma = np.shape(imgray)
img2 = np.zeros(forma)

print("Selecciona el tipo de filtro que quieres aplicar a tu imagen")
print("1.-Blur")
print("2.- Bottom Solbel")
print("3.- Emboss")
print("4.- Left Sobel")
print("5.- Outline")
print("6.- Night Sobel")
print("7.- Sharpen")
print("8.- Top Sobel")
op=input()

if op=="1":
  kernel = np.array([[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]])
  n_filter="Imagen con filtro Blur"

elif op=="2":
  kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
  n_filter="Imagen con filtro Botton Solbel"

elif op=="3":
  kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
  n_filter="Imagen con filtro Emboss"
elif op=="4":
  kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
  n_filter="Imagen con filtro Left Sobel"

elif op=="5":
  kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
  n_filter="Imagen con filtro Outline"

elif op=="6":
  kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
  n_filter="Imagen con filtro Night Sobel"

elif op=="7":
  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
  n_filter="Imagen con filtro Sharpen"

elif op=="8":
  kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  
  n_filter="Imagen con filtro Top Sobel"

else:
  kernel = np.array([[0, 0, 0], [0, 1, -0], [0, 0, 0]])  


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
plt.title( n_filter )
plt.show()