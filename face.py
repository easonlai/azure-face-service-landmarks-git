# Import necessary libraries
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import os
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import cv2

# Define Azure Face Service key and endpoint
KEY = "PLEASE_ENTER_YOUR_OWN_AZURE_FACE_SERVICE_KEY"
ENDPOINT = "https://PLEASE_ENTER_YOUR_OWN_AZURE_FACE_SERVICE_ENDPOINT_NAME.cognitiveservices.azure.com/"

# Define the Face Service client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Initialize camera by CV2
cam = cv2.VideoCapture(0)
cv2.namedWindow("face")
img_counter = 0

# While loop to continuously process the video frames 
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("face", frame)
    # Post video frames to Azure Face Service to obtain face landmarks
    image = cv2.imencode('.jpg', frame)[1].tostring()
    subscription_key = KEY
    face_api_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/detect"
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'returnFaceId': 'true', 'returnFaceLandmarks': 'true'}
    response = requests.post(face_api_url, params=params, headers=headers, data=image)
    response.raise_for_status()
    faces = response.json()
    print(faces)

    # Parse collected face landmarks into variables
    for face in faces:
        flm = face['faceLandmarks']
        pupilLeft = flm['pupilLeft']
        pupilRight = flm['pupilRight']
        noseTip = flm['noseTip']
        mouthLeft = flm['mouthLeft']
        mouthRight = flm['mouthRight']
        eyebrowLeftOuter = flm['eyebrowLeftOuter']
        eyebrowLeftInner = flm['eyebrowLeftInner']
        eyeLeftInner = flm['eyeLeftInner']
        eyeLeftTop = flm['eyeLeftTop']
        eyeLeftBottom = flm['eyeLeftBottom']
        eyeLeftOuter = flm['eyeLeftOuter']
        eyebrowRightOuter = flm['eyebrowRightOuter']
        eyebrowRightInner = flm['eyebrowRightInner']
        eyeRightInner = flm['eyeRightInner']
        eyeRightTop = flm['eyeRightTop']
        eyeRightBottom = flm['eyeRightBottom']
        eyeRightOuter = flm['eyeRightOuter']
        noseRootLeft = flm['noseRootLeft']
        noseRootRight = flm['noseRootRight']
        noseLeftAlarTop = flm['noseLeftAlarTop']
        noseRightAlarTop = flm['noseRightAlarTop']
        noseLeftAlarOutTip = flm['noseLeftAlarOutTip']
        noseRightAlarOutTip = flm['noseRightAlarOutTip']
        upperLipTop = flm['upperLipTop']
        upperLipBottom = flm['upperLipBottom']
        underLipTop = flm['underLipTop']
        underLipBottom = flm['underLipBottom']
    
        # Measure value between Left eye bottom and top position
        eyeLeftvalue =  int(eyeLeftBottom['y']) - int(eyeLeftTop['y'])
        # Define distance value for left eye blinking
        eyeLeftcloseValue = 20
        # Show Left Eye Blinking message if distance between top and bottom is lower than defined value
        if eyeLeftvalue < eyeLeftcloseValue:
            eyeLeftvalueMsg = cv2.putText(frame, "Left Eye Blinking", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('face_landmarks', eyeLeftvalueMsg)

        # Measure value between Right eye bottom and top position
        eyeRightvalue =  int(eyeRightBottom['y']) - int(eyeRightTop['y'])
        # Define distance value for right eye blinking
        eyeRightcloseValue = 20
        # Show Right Eye Blinking message if distance between top and bottom is lower than defined value
        if eyeRightvalue < eyeRightcloseValue:
            eyeRightvalueMsg = cv2.putText(frame, "Right Eye Blinking", (50, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('face_landmarks', eyeRightvalueMsg)

        # Define CV2 circle points by face landmarks x y position
        pupilLeft = cv2.circle(frame,(int(pupilLeft['x']), int(pupilLeft['y'])), 8, (0, 0, 255), -1)
        pupilRight = cv2.circle(frame,(int(pupilRight['x']), int(pupilRight['y'])), 8, (0, 0, 255), -1)
        noseTip = cv2.circle(frame,(int(noseTip['x']), int(noseTip['y'])), 8, (0, 0, 255), -1)
        mouthLeft = cv2.circle(frame,(int(mouthLeft['x']), int(mouthLeft['y'])), 8, (0, 0, 255), -1)
        mouthRight = cv2.circle(frame,(int(mouthRight['x']), int(mouthRight['y'])), 8, (0, 0, 255), -1)
        eyebrowLeftOuter = cv2.circle(frame,(int(eyebrowLeftOuter['x']), int(eyebrowLeftOuter['y'])), 8, (0, 0, 255), -1)
        eyebrowLeftInner = cv2.circle(frame,(int(eyebrowLeftInner['x']), int(eyebrowLeftInner['y'])), 8, (0, 0, 255), -1)
        eyeLeftInner = cv2.circle(frame,(int(eyeLeftInner['x']), int(eyeLeftInner['y'])), 8, (0, 0, 255), -1)
        eyeLeftTop = cv2.circle(frame,(int(eyeLeftTop['x']), int(eyeLeftTop['y'])), 8, (0, 0, 255), -1)
        eyeLeftBottom = cv2.circle(frame,(int(eyeLeftBottom['x']), int(eyeLeftBottom['y'])), 8, (0, 0, 255), -1)
        eyeLeftOuter = cv2.circle(frame,(int(eyeLeftOuter['x']), int(eyeLeftOuter['y'])), 8, (0, 0, 255), -1)
        eyebrowRightInner = cv2.circle(frame,(int(eyebrowRightInner['x']), int(eyebrowRightInner['y'])), 8, (0, 0, 255), -1)
        eyebrowRightOuter = cv2.circle(frame,(int(eyebrowRightOuter['x']), int(eyebrowRightOuter['y'])), 8, (0, 0, 255), -1)
        eyeRightInner = cv2.circle(frame,(int(eyeRightInner['x']), int(eyeRightInner['y'])), 8, (0, 0, 255), -1)
        eyeRightTop = cv2.circle(frame,(int(eyeRightTop['x']), int(eyeRightTop['y'])), 8, (0, 0, 255), -1)
        eyeRightBottom = cv2.circle(frame,(int(eyeRightBottom['x']), int(eyeRightBottom['y'])), 8, (0, 0, 255), -1)
        eyeRightOuter = cv2.circle(frame,(int(eyeRightOuter['x']), int(eyeRightOuter['y'])), 8, (0, 0, 255), -1)
        noseRootLeft = cv2.circle(frame,(int(noseRootLeft['x']), int(noseRootLeft['y'])), 8, (0, 0, 255), -1)
        noseRootRight = cv2.circle(frame,(int(noseRootRight['x']), int(noseRootRight['y'])), 8, (0, 0, 255), -1)
        noseLeftAlarTop = cv2.circle(frame,(int(noseLeftAlarTop['x']), int(noseLeftAlarTop['y'])), 8, (0, 0, 255), -1)
        noseRightAlarTop = cv2.circle(frame,(int(noseRightAlarTop['x']), int(noseRightAlarTop['y'])), 8, (0, 0, 255), -1)
        noseLeftAlarOutTip = cv2.circle(frame,(int(noseLeftAlarOutTip['x']), int(noseLeftAlarOutTip['y'])), 8, (0, 0, 255), -1)
        noseRightAlarOutTip = cv2.circle(frame,(int(noseRightAlarOutTip['x']), int(noseRightAlarOutTip['y'])), 8, (0, 0, 255), -1)
        upperLipTop = cv2.circle(frame,(int(upperLipTop['x']), int(upperLipTop['y'])), 8, (0, 0, 255), -1)
        upperLipBottom = cv2.circle(frame,(int(upperLipBottom['x']), int(upperLipBottom['y'])), 8, (0, 0, 255), -1)
        underLipTop = cv2.circle(frame,(int(underLipTop['x']), int(underLipTop['y'])), 8, (0, 0, 255), -1)
        underLipBottom = cv2.circle(frame,(int(underLipBottom['x']), int(underLipBottom['y'])), 8, (0, 0, 255), -1)

        # Show CV2 circle points overlay on camera stream
        cv2.imshow('face_landmarks', pupilLeft)
        cv2.imshow('face_landmarks', pupilRight)
        cv2.imshow('face_landmarks', noseTip)
        cv2.imshow('face_landmarks', mouthLeft)
        cv2.imshow('face_landmarks', mouthRight)
        cv2.imshow('face_landmarks', eyebrowLeftOuter)
        cv2.imshow('face_landmarks', eyebrowLeftInner)
        cv2.imshow('face_landmarks', eyeLeftInner)
        cv2.imshow('face_landmarks', eyeLeftTop)
        cv2.imshow('face_landmarks', eyeLeftBottom)
        cv2.imshow('face_landmarks', eyeLeftOuter)
        cv2.imshow('face_landmarks', eyebrowRightOuter)
        cv2.imshow('face_landmarks', eyebrowRightInner)
        cv2.imshow('face_landmarks', eyeRightInner)
        cv2.imshow('face_landmarks', eyeRightTop)
        cv2.imshow('face_landmarks', eyeRightBottom)
        cv2.imshow('face_landmarks', eyeRightOuter)
        cv2.imshow('face_landmarks', noseRootLeft)
        cv2.imshow('face_landmarks', noseRootRight)
        cv2.imshow('face_landmarks', noseLeftAlarTop)
        cv2.imshow('face_landmarks', noseRightAlarTop)
        cv2.imshow('face_landmarks', noseLeftAlarOutTip)
        cv2.imshow('face_landmarks', noseRightAlarOutTip)
        cv2.imshow('face_landmarks', upperLipTop)
        cv2.imshow('face_landmarks', upperLipBottom)
        cv2.imshow('face_landmarks', underLipTop)
        cv2.imshow('face_landmarks', underLipBottom)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

# Release camera
cam.release()

# Close all camera windows
cv2.destroyAllWindows()