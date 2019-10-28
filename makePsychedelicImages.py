"""
Usage:
    makePsychedelicImages.py [options] <mp3file> <savepath> <prefix>

Options:
    -h --help          Show this screen.
    --framestart NUM   First frame to save.
    --framestop NUM    Last frame to save.
"""
import cv2
from docopt import docopt

def getVideoFrames(args):
    cap = cv2.VideoCapture(args['<mp3file>'])
    fps = cap.get(cv2.CAP_PROP_FPS)
    for i in range(int(args['--framestart']), int(args['--framestop'])):
        cap.set(1, i)
        check, frame = cap.read()
        if check:
            cv2.imwrite(args['<savepath>']+'/'+args['<prefix>']+str(i)+".png", frame)
        else:
            print("Failed to read frame")
    cap.release()

def main(args):
    getVideoFrames(args)

if __name__ == "__main__":
    args = docopt(__doc__, version='Four.2.Zero')
    main(args)

