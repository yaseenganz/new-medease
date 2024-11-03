import cv2 as cv
import numpy as np

def scan_qr_code():
    cap = cv.VideoCapture(0)
    qr_scanner = cv.QRCodeDetector()

    def getdata(data, pointer, frame):
        if data:
            print("QR code detected", data)
            if pointer is not None:
                pointer = pointer[0].astype(int)
                for i in range(len(pointer)):
                    ptr1 = tuple(pointer[i])
                    ptr2 = tuple(pointer[(i + 1) % len(pointer)])
                    cv.line(frame, ptr1, ptr2, (0, 255, 0), thickness=2)
            return data

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Could't get cammer")
            break
        
        data, pointer, _ = qr_scanner.detectAndDecode(frame)
        
        getout = getdata(data, pointer, frame)

        if getout:
            print("Link is: ", getout)
            break
            
        
        cv.imshow("video File", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

scan_qr_code()