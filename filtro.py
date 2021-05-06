import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('Turquia.jpg')

imgray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)