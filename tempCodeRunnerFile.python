import cv2 as cv
import numpy as np

def scan_qr_code():
    cap = cv.VideoCapture(0)
    qr_scanner = cv.QRCodeDetector()
    data_result = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Couldn't get camera")
            break

        data, pointer, _ = qr_scanner.detectAndDecode(frame)
        if data:
            data_result = data  # Capture the data to send to the view
            break
        
        cv.imshow("QR Code Scanner", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    
    return data_result  # Return the data to be used in the view
