import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

capture = cv2.VideoCapture(0)

while True:
    _ , image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)

    for(x,y,w,h) in face:
        cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0), 2)
        face_gray = gray[y:y+h, x:x+w]
        face_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_gray)    
        for(a,b,c,d) in eyes:
            cv2.rectangle(face_color, (a,b), (a+c, b+d), (0,255,0), 2)

    cv2.imshow("image", image)
    key = cv2.waitKey(30) & 0xff
    if key == 113:
        break

capture.release()
cv2.destroyAllWindows()    





