import cv2

cap = cv2.VideoCapture(0)

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    
    if frame is not None:
        # 1. Object Detection
        mask = object_detector.apply(frame)
        mask = cv2.threshold(mask, 80, 100, cv2.THRESH_BINARY)[1]
        contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        detections = []
        for cnt in contours:
            # Calculate area and remove small elements
            area = cv2.contourArea(cnt)
            if area > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                detections.append((x, y, w, h))

        for i in detections:
            (startX, startY, endX, endY) = i
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(30)
        if key == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)