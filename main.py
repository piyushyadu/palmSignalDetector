import cv2
import mediapipe as mp
import time
import module as htm
import conditionProviders as cnd

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.9)

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    ans = ""
    if len(lmList) != 0:
        res = cnd.listCal(lmList)
        n = cnd.valueCal(res)
        ans = cnd.alphaCal(n)
    cv2.putText(img, ans, (640, 360), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 255), 5)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

