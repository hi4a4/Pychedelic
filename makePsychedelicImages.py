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
from multiprocessing import Pool


def saveFrame(framenum, args):
    print(f'Processing frame: {framenum}')
    cap = cv2.VideoCapture(args['<mp3file>'])
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(1, framenum)
    check, frame = cap.read()
    if check:
        cv2.imwrite(args['<savepath>']+'/' +
                    args['<prefix>']+str(framenum)+".png", frame)
    else:
        print("Failed to read frame")
    cap.release()


if __name__ == "__main__":
    args = docopt(__doc__, version='Four.2.Zero')
    with Pool() as p:
        p.starmap(saveFrame,
                  [(framenum, args) for framenum in range(
                      int(args['--framestart']), int(args['--framestop']))])
