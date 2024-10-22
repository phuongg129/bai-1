import cv2
import numpy as np

def log_transform(c, img):
  # Chuyển ảnh về float để thực hiện phép tính logarit
  img_float = img.astype(np.float64)

  # Thực hiện biến đổi log
  img_log = c * np.log(1 + img_float)

  # Chuyển về dạng uint8 để hiển thị
  img_log = np.uint8(img_log)

  return img_log

# Đọc ảnh
img = cv2.imread('images.jpg', 0)  # Đọc ảnh xám

# Chọn hằng số c (bạn có thể điều chỉnh giá trị này)
c = 255 / np.log(1 + np.max(img))

# Thực hiện biến đổi log
img_log = log_transform(c, img)

# Hiển thị ảnh
cv2.imshow('Original Image', img)
cv2.imshow('Log Transformed Image', img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()