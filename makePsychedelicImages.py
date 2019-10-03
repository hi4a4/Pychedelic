import cv2


def getVideoFrames(url):
    cap = cv2.VideoCapture(url)
    fps = cap.get(cv2.CAP_PROP_FPS)
    for i in range(3246):
        cap.set(1, i*fps)
        check, frame = cap.read()
        if check:
            cv2.imwrite(str(i)+".png", frame)
        else:
            print("Failed to read frame")
        break
    cap.release()

def main():
    getVideoFrames('./psyVideo.mp4')

if __name__ == "__main__":
    main()
