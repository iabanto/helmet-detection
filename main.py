import cv2
import matplotlib.pyplot as plt

# Load an image using OpenCV
image = cv2.imread('construction.jpeg')

# Perform Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the edges
plt.imshow(edges, cmap='gray')
plt.axis('off')
plt.show()
