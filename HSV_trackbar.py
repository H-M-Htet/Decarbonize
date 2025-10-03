import cv2 as cv
import numpy as np

def nothing(x):
    pass

# Load your image
img_bgr = cv.imread("img/redball.jpg")
if img_bgr is None:
    raise FileNotFoundError("⚠️ Image not found, check path.")

# Convert to HSV
img_hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)

# Create ONE window
cv.namedWindow("Color Detector", cv.WINDOW_NORMAL)

# Add trackbars to the same window
cv.createTrackbar("H Min", "Color Detector", 0, 179, nothing)
cv.createTrackbar("H Max", "Color Detector", 179, 179, nothing)
cv.createTrackbar("S Min", "Color Detector", 0, 255, nothing)
cv.createTrackbar("S Max", "Color Detector", 255, 255, nothing)
cv.createTrackbar("V Min", "Color Detector", 0, 255, nothing)
cv.createTrackbar("V Max", "Color Detector", 255, 255, nothing)

while True:
    # Read current slider positions
    h_min = cv.getTrackbarPos("H Min", "Color Detector")
    h_max = cv.getTrackbarPos("H Max", "Color Detector")
    s_min = cv.getTrackbarPos("S Min", "Color Detector")
    s_max = cv.getTrackbarPos("S Max", "Color Detector")
    v_min = cv.getTrackbarPos("V Min", "Color Detector")
    v_max = cv.getTrackbarPos("V Max", "Color Detector")

    # Build HSV lower and upper ranges
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create mask and apply
    mask = cv.inRange(img_hsv, lower, upper)
    result = cv.bitwise_and(img_bgr, img_bgr, mask=mask)

    # Stack original + result side by side
    combined = np.hstack((img_bgr, result))

    # Show in the SAME window
    cv.imshow("Color Detector", combined)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cv.waitKey(1)  # macOS cleanup
