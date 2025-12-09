import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Cannot open camera")

fgbg = cv.createBackgroundSubtractorMOG2(history=50, varThreshold=25, detectShadows=True)
MIN_AREA = 1200  # adjust to ignore small motion

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_small = cv.resize(frame, (640, 480))
    fgmask = fgbg.apply(frame_small)

    # For Intensity of the Ddetection
    # clean mask - Remove Noide
    fgmask = cv.medianBlur(fgmask, 5)
    _, fgmask = cv.threshold(fgmask, 250, 255, cv.THRESH_BINARY)
    fgmask = cv.dilate(fgmask, None, iterations=2)

    contours, _ = cv.findContours(fgmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # pick largest contour above MIN_AREA
    big_cnt = None
    max_area = 0
    for c in contours:
        a = cv.contourArea(c)
        if a > MIN_AREA and a > max_area:
            max_area = a
            big_cnt = c

    display = frame_small.copy()
    if big_cnt is not None:
        x, y, w, h = cv.boundingRect(big_cnt)
        # Optionally expand ROI by a margin
        margin = 10
        x = max(0, x - margin); y = max(0, y - margin)
        w = min(display.shape[1]-x, w + 2*margin)
        h = min(display.shape[0]-y, h + 2*margin)
        cv.rectangle(display, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi = display[y:y+h, x:x+w]
        # show ROI in corner
        roi_small = cv.resize(roi, (int(w*0.6), int(h*0.6)))
        display[10:10+roi_small.shape[0], 10:10+roi_small.shape[1]] = roi_small

    cv.imshow("Auto ROI - Motion", display)
    cv.imshow("Mask", fgmask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
e1 = cv.getTickCount()

# ---- code you want to measure ----
for i in range(1000000):
    pass
# -----------------------------------

e2 = cv.getTickCount()

time_taken = (e2 - e1) / cv.getTickFrequency()
print("Time:", time_taken, "seconds")

cap.release()
cv.destroyAllWindows()
