#Create a Python method that takes as an input a NumPy array with the shape width x height representing
#a depth image where each value represents the distance in meters from a sensor as floating-point numbers
#and outputs a grayscale image representing the normalized depth where a black pixel is the closest point and
#a white pixel is the farthest one. Please also include a test method that validates the logic on a randomly
#initialized NumPy array.

import numpy as np
from PIL import Image


inputFloatData = np.array([[0.1, 0.3, 0.5],
              [0.7, 2, 3.2],
             [1, 2, 3],
              [2.3, 0.2, 0.5]], np.float32)
type(inputFloatData)

#print(inputFloatData.shape)


print(inputFloatData)


image = Image.fromarray(inputFloatData)
print(type(image))

# summarize image details
print(image.mode)
print(image.size)

gr_im= Image.fromarray(inputFloatData).save('normalMap.tiff')