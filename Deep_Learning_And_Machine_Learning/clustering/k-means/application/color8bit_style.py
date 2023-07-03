import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from mpl_toolkits.mplot3d import Axes3D


# Create a Tkinter root window
root = Tk()
root.withdraw()

# Open a file explorer dialog to select an image file
file_path = filedialog.askopenfilename()

# Read the selected image using cv2
image = cv2.imread(file_path)

# Convert the image to RGB color space
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get the dimensions of the image
height, width, _ = image_rgb.shape

# Reshape the image to a 2D array of pixels
pixels = image_rgb.reshape((height * width, 3))

# Create an empty dataset
dataset = []

# Iterate over each pixel and store the RGB values as a vector in the dataset
for pixel in pixels:
    dataset.append(pixel)

# Convert the dataset to a NumPy array
dataset = np.array(dataset)

# Get the RGB values from the dataset
red = dataset[:, 0]
green = dataset[:, 1]
blue = dataset[:, 2]

# Plot the histograms
plt.figure(figsize=(10, 6))
plt.hist(red, bins=256, color='red', alpha=0.5, label='Red')
plt.hist(green, bins=256, color='green', alpha=0.5, label='Green')
plt.hist(blue, bins=256, color='blue', alpha=0.5, label='Blue')
plt.title('RGB Value Histogram')
plt.xlabel('RGB Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# Plot the 3D scatter graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(red, green, blue, c='#000000', s=1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
ax.set_title('RGB Scatter Plot')
plt.show()


