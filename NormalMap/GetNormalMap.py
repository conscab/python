#Create a Python method that takes as an input a NumPy array with the shape width x height representing
#a depth image where each value represents the distance in meters from a sensor as floating-point numbers
#and outputs a grayscale image representing the normalized depth where a black pixel is the closest point and
#a white pixel is the farthest one. Please also include a test method that validates the logic on a randomly
#initialized NumPy array.

import numpy as np
from PIL import Image


inputFloatData = np.array([[11, 0.3, 0.5, 0.1, 0.3, 0.5, 1, 0.3, 0.5, 0.1, 0.3, 0.5, 1, 1, 0.4],
              [0.3, 0.3, 0.5, 3, 0, 0.5, 0.1, 0.3, 0.5, 6, 0.3, 0.5, 6, 0.3, 0.5],
             [1, 0.3, 0.5, 0.1, 0.3, 0.5, 0, 0.3, 0.5, 0.1, 0.3, 0.5, 6, 0.3, 0.8],
              [2, 0, 0.5, 0, 0.3, 0, 0.1, 0.3, 0.5, 0.1, 6, 0.5, 0.1, 6, 6],
              [0.1, 0.3, 0.5, 0.1, 0.3, 9, 1, 0.3, 0.5, 0.1, 0.3, 0.5, 1, 1, 0.4],
              [0.3, 0.3, 0.5, 3, 0, 0.5, 0.1, 4, 0.5, 6, 0.3, 0.5, 6, 0.3, 0.5],
             [1, 0.3, 0.5, 0.1, 0.3, 0.5, 0, 5, 0.5, 0.1, 0.3, 0.5, 6, 0.3, 0.8],
              [2, 0, 0.5, 0, 0.3, 0, 0.1, 0.3, 0.5, 0.1, 6, 0.5, 0.1, 6, 0.1]], np.float32)

x = np.linspace(0,1,12*12)

type(inputFloatData)

#print(inputFloatData.shape)

print(inputFloatData)
print(x)
image = Image.fromarray(inputFloatData)
print(type(image))
print(image.mode)
print(image.size)

outputImage = Image.fromarray(inputFloatData).save('greyscaleMap.tiff')
outputImage = Image.fromarray(x).save('greyscaleMap2.tiff')