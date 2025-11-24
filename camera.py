import cv2 as cv
import numpy as np

def main():
    camera_id = 0
    cap = cv.VideoCapture(camera_id)

    # Getting camera resolution
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

    # Setting resolution
    cap.set(cv.CAP_PROP_FRAME_WIDTH, w * 1.2)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, h * 1.2)

    while True:
        if not cap.isOpened():
            print(f"Cannot open camera {camera_id}")
            exit()

        else:
            ret, frame = cap.read()

            if not ret:
                print("Cant recieve frame")
                break
            
            # Adjusts the contrast by scaling the pixel values by 2.3
            contrast = 2.3  
            frame = cv.addWeighted(frame, contrast, np.zeros(frame.shape, frame.dtype), 0, 1)
            cv.imshow("camera", frame)

            if cv.waitKey(1) == ord("s"):
                print("Camera stopped")
                break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

        
