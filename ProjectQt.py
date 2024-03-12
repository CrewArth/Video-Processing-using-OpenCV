import cv2

PREVIEW = 0  # Preview Mode
BLUR = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY = 3  # Canny Edge Detector


win_name = "Edge & Blur Detection"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

image_filter = PREVIEW

cap = cv2.VideoCapture(1)

alive = True
while alive:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 80, 150)
    elif image_filter == BLUR:
        result = cv2.blur(frame, (13, 13))


    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR

cap.release()
cv2.destroyAllWindows()