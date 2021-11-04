import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('vtest.avi')

fgbgBayesianSegmentation = cv2.bgsegm.createBackgroundSubtractorGMG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
ret = True
while ret:
    ret, frame = cap.read()
    if ret:
        fgbgBayesianSegmentationmask = fgbgBayesianSegmentation.apply(frame)
        fgbgBayesianSegmentationmask = cv2.morphologyEx(fgbgBayesianSegmentationmask, cv2.MORPH_OPEN, kernel)

        k = cv2.waitKey(40) & 0xff
        # blur = cv2.GaussianBlur(fgbgBayesianSegmentationmask , (5,5), 0)
        # _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(fgbgBayesianSegmentationmask, None, iterations=1)
        contours_fgbgBayesianSegmentationmask, _ = cv2.findContours(fgbgBayesianSegmentationmask, cv2.RETR_TREE,
                                                                    cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow("dilated", fgbgBayesianSegmentationmask)

        for contour in contours_fgbgBayesianSegmentationmask:
            (x, y, w, h) = cv2.boundingRect(contour)

            if cv2.contourArea(contour) > 150 and w < 1.5 * h:
                if w > 40:

                    cv2.rectangle(frame, (x, y), (x + w/2, y + h), (0, 255, 0), 2)

                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("frame_contours_fgbgBayesianSegmentationmask", frame)

        if k == ord('q'):
            break
cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
print('Program Closed')
