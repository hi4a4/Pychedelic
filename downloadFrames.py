"""
Usage:
    downloadFrames.py <youTubeURL> <savepath> <end_frame>

Options:
    -h --help          Show this screen.
"""
import cv2
import pafy
import youtube_dl
from docopt import docopt
from multiprocessing import Pool


def saveFrames(args):
    framenum = 0
    print(args['<youTubeURL>'])
    vPafy = pafy.new(args['<youTubeURL>'])
    print(vPafy)
    play = vPafy.getbestvideo()
    print(play)
    cap = cv2.VideoCapture(play.url)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(1, framenum)
    check, frame = cap.read()
    while check:
        cv2.imwrite(args['<savepath>'] + '/' + str(framenum) + ".png", frame)
        framenum += 1
        cap.set(1, framenum)
        if framenum > int(args['<end_frame>']):
            break
        check, frame = cap.read()
    cap.release()


if __name__ == "__main__":
    args = docopt(__doc__, version='Four.2.Zero')
    saveFrames(args)
