import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('images.jpg', 0)  # Đọc ảnh xám

# Tạo ảnh âm tính
height, width = img.shape
img_negative = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        img_negative[i, j] = 255 - img[i, j]

# Hiển thị ảnh
cv2.imshow('Original Image', img)
cv2.imshow('Negative Image', img_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()