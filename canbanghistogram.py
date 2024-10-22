import cv2
import numpy as np

def increase_contrast(img, gamma=1.5):
    
    # Histogram equalization
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img_out = cdf[img]

    return img_out

# Example usage
img = cv2.imread('images.jpg')
img_out = increase_contrast(img)  # Or "log", "gamma"

cv2.imshow('Original Image', img)
cv2.imshow('Increased Contrast Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()