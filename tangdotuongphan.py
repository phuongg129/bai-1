import cv2
import numpy as np

def linear_contrast_adjustment(img, alpha, beta):

    # Chuyển ảnh về kiểu float để thực hiện phép tính
    new_img = np.float32(img)

    # Áp dụng công thức điều chỉnh độ tương phản tuyến tính
    dst = cv2.convertScaleAbs(new_img, alpha=alpha, beta=beta)

    return dst

# Đọc ảnh
img = cv2.imread('images.jpg')

# Điều chỉnh độ tương phản (ví dụ: tăng độ tương phản)
alpha = 1.2  # Hệ số điều chỉnh độ tương phản (alpha > 1: tăng, alpha < 1: giảm)
beta = 0    # Giá trị dịch chuyển (beta > 0: làm sáng, beta < 0: làm tối)

# Áp dụng hàm điều chỉnh
new_img = linear_contrast_adjustment(img, alpha, beta)

# Hiển thị ảnh
cv2.imshow('Original Image', img)
cv2.imshow('Adjusted Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()