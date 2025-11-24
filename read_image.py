import cv2 as cv
import numpy as np
from pathlib import Path

def read_image():
    # IMAGE_PATH = Path("./images/hobbit_page.jpg")
    # WINDOW_NAME = "IMAGE"

    # image = cv.imread(IMAGE_PATH)
    # height, width = image.shape[:2]
    # roi = image[height//2-250:height-600, width//2-100:width] # manual fit
    # dsize = (700, 700)
    # resized_image = cv.resize(roi, dsize)

    # # Save roi
    # cv.imwrite("./images/hobbit_page_roi.jpg", resized_image)

    IMAGE_PATH = Path("./images/hobbit_page_roi.jpg")
    WINDOW_NAME = "IMAGE"
    image = cv.imread(IMAGE_PATH)

    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # image = cv.filter2D(image, -1, kernel)
    threshold_kernel= 15
    dst = 5
    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ths = cv.adaptiveThreshold(grayscale_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, threshold_kernel, dst)

    kernel=np.ones((2,2), np.uint8)
    opening = cv.morphologyEx(ths, cv.MORPH_OPEN, kernel)

    cv.imshow(WINDOW_NAME, opening)
    if cv.waitKey(0) == ord("s"):
        cv.destroyAllWindows()

if __name__ == "__main__":
    read_image()