import numpy as np
import cv2

img = np.ones( (500,500), dtype=np.uint8) *255
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imshow(None, img)