"""
Usage:
   pipeline.py [options] <mp3file>

Options:
    -h --help          Show this screen.
    --framestart NUM   First frame to save.
    --framestop NUM    Last frame to save.
"""
import cv2
from docopt import docopt


def saveVideo(frameList, args, fps):
    height, width, channels = frameList[0].shape
    outFile = 'lsd_' + args['<mp3file>'].split('.')[0] + '.mp4'
    print("Saving video" + outFile)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outFile, fourcc, round(fps), (width, height))
    for frame in frameList:
        out.write(frame)
    out.release()


def runModel(frame):
    print("Type A -> Type B")
    return frame


def processFrames(args):
    frameList = []
    cap = cv2.VideoCapture(args['<mp3file>'])
    fps = cap.get(cv2.CAP_PROP_FPS)
    for i in range(int(args['--framestart']), int(args['--framestop'])):
        cap.set(1, i)
        check, frame = cap.read()
        if check:
            frameList.append(runModel(frame))
        else:
            print("Failed to read frame")
    cap.release()
    saveVideo(frameList, args, fps)
    cv2.destroyAllWindows()


def main(args):
    processFrames(args)


if __name__ == "__main__":
    args = docopt(__doc__, version='Four.2.Zero')
    main(args)
