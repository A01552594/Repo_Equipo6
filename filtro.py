#Importacion de librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt


def filters(nombre, opc):#Funcion para la lectura de imagenes y aplicacion de filtros
    img = cv2.imread(nombre)

    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    forma = np.shape(imgray)
    img2 = np.zeros(forma)


    #Eleccion y definicion de filtros
    if opc == 1:
        kernel = np.array([[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125],
                           [0.0625, 0.125, 0.0625]])
        n_filter = "Imagen con filtro Blur"

    elif opc == 2:
        kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        n_filter = "Imagen con filtro Botton Solbel"

    elif opc == 3:
        kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
        n_filter = "Imagen con filtro Emboss"

    elif opc == 4:
        kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        n_filter = "Imagen con filtro Left Sobel"

    elif opc == 5:
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        n_filter = "Imagen con filtro Outline"

    elif opc == 6:
        kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        n_filter = "Imagen con filtro Night Sobel"

    elif opc == 7:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        n_filter = "Imagen con filtro Sharpen"

    elif opc == 8:
        kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        n_filter = "Imagen con filtro Top Sobel"

    else:
        kernel = np.array([[0, 0, 0], [0, 1, -0], [0, 0, 0]])

    #Procedimiento para la convolucion
    for x in list(range(1, forma[0] - 1)):
        for y in list(range(1, forma[1] - 1)):
            suma = 0

            for i in list(range(-1, 2)):
                for j in list(range(-1, 2)):
                    suma = imgray[x - i, y - j] * kernel[i + 1, j + 1] + suma

            img2[x, y] = suma

    #Ajustes del filtro
    imgfilt = np.stack(img2)
    imgfilt[imgfilt > 255] = 255
    imgfilt[imgfilt < 0] = 0
    imgfilt = imgfilt.astype("uint8")

    #Impresion de imagesnes/graficas
    plt.imshow(img, cmap='gray')
    plt.title("Imagen original")
    plt.show()

    plt.imshow(imgray, cmap='gray')
    plt.title("Imagen blanco y negro")
    plt.show()

    plt.imshow(imgfilt, cmap='gray')
    plt.title(n_filter)
    plt.show()
