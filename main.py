import cv2
import sys
import math

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
iwidth=video_capture.get(3)
iheight=video_capture.get(4)

print("width: "+str(iwidth)+" height: "+str(iheight))

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.CV_HAAR_SCALE_IMAGE
    )
    # Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        if(w*h >= 15000 and w*h <= 65000):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.circle(frame, (math.floor(x+(w/2)),math.floor(y+(h/2))),5,255)
        cv2.circle(frame,(math.floor(iwidth/2),math.floor(iheight/2)),5,100)
        cv2.line(frame,(math.floor(x+(w/2)),math.floor(y+(h/2))),(math.floor(iwidth/2),math.floor(iheight/2)),(255,255,0),2)
        cv2.putText(frame,"X: " + str(math.floor((iwidth/2)-(x+(w/2))))+" Y: " + str(math.floor((iheight/2)-(y+(h/2)))),(math.floor((x+(w/4))-50),math.floor((y+(h/4))-35)), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,255,255),2,cv2.LINE_AA)
        #calculate the distance using pythagorean thm
        cv2.putText(frame,
        str(math.floor(math.sqrt(math.pow(((iwidth/2)-(x+(w/2))),2) + math.pow(((iheight/2)-(y+(h/2))),2)))), 
        (math.floor(x+(w/4)),math.floor(y+(h/4))), 
        cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,100),2,cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()