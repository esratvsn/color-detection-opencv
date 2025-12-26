import cv2
import numpy as np

cap = cv2.VideoCapture(0)

kernel = np.ones((5,5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red = (
        cv2.inRange(hsv, np.array([0,100,50]), np.array([10,255,255])) +
        cv2.inRange(hsv, np.array([160,100,50]), np.array([180,255,255]))
    )

    
    mask_green = cv2.inRange(
        hsv, np.array([35,50,50]), np.array([85,255,255])
    )

    
    mask_blue = cv2.inRange(
        hsv, np.array([90,50,50]), np.array([140,255,255])
    )

    
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)


    cv2.imshow("Mask Red", mask_red)
    cv2.imshow("Mask Green", mask_green)
    cv2.imshow("Mask Blue", mask_blue)

    for color_name, mask, box_color in [
        ("Red", mask_red, (0,0,255)),
        ("Green", mask_green, (0,255,0)),
        ("Blue", mask_blue, (255,0,0))
    ]:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 300:
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x,y), (x+w,y+h), box_color, 2)
                cv2.putText(frame, color_name, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

    cv2.imshow("Goruntu", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
