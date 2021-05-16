import cv2


body_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_profileface.xml')
face_cascade = cv2.CascadeClassifier(
    './cascades/haarcascade_frontalcatface_extended.xml')
#eye_cascade = cv2.CascadeClassifier(
 #   './cascades/haarcascade_eye.xml')

camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            faces = face_cascade.detectMultiScale(
                roi_gray, 1.1, 5, minSize=(60, 60))
            for (ex, ey, ew, eh) in faces:
                cv2.rectangle(frame, (x+ex, y+ey),
                              (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        cv2.imshow('person Detection', frame)

