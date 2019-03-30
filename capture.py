import cv2
def getcapture(filename):
    cap = cv2.VideoCapture(0)
    print("Type q to click photo")
    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out = cv2.imwrite(str(filename)+'.jpg', frame)
            break
    cap.release()
    cv2.destroyAllWindows()