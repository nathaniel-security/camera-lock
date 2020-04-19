import cv2

def main_start():
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)


    import os
    filename = "exit"
    while True:
        temp = os.path.isfile(filename)
        if(temp == True):
            break

    webcam.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main_start()