import cv2
import cvzone

thres = 0.5
nmsThres = 0.2
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = 'neuralCoco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')

configPath = 'neuralSsd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "neuralFrozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cvzone.cornerRect(img, box)
        cv2.putText(img, f'{classNames[classId - 1].upper()} {round(confidence * 100, 2)}',
                    (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1, (0, 255, 0), 2)
        detectedObject = (classNames[classId-1])

    def neuralDetect(target:str, centralizeTarget:bool):
        if target == detectedObject:
            if centralizeTarget == True:
                if box[0] < 0 and box[1] < 0:
                    #print("turn right")
                    return
                elif box[0] > 0 and box[1] > 0:
                    #print("turn left")
                    return
                else:
                    #print("Everything is fine")
                    return
                    
            elif centralizeTarget == False:
                return None
            else:
                return None

    cv2.imshow("Image", img)
    #first two values of box is the x and y values respectively in matplotlib method
    print(box)
    cv2.waitKey(1)
    neuralDetect("person", True)