"""
Usage:
   makeVideo.py <youtubeURL> <model_name> <frame_end>

Options:
    -h --help          Show this screen.
"""
import cv2
import pafy
import youtube_dl
from docopt import docopt


def main(args):
    vPafy = pafy.new(args['<youtubeURL>'])
    play = vPafy.getbestvideo()
    cap = cv2.VideoCapture(play.url)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Set the video to end
    cap.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    frameEnd = int(cap.get(1))
    frameEnd = int(args['frame_end'])  # Temp for testing
    cap.release()

    imagePath = './results/' + args['<model_name>'] + '/test_latest/images/'
    height, width, channels = cv2.imread(imagePath+'0_fake.png').shape
    outFile = 'fake_' + args['<youtubeURL>'].split('=')[-1] + '.mp4'
    print("Saving video: " + outFile)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outFile, fourcc, round(fps), (width, height))
    for i in range(int(frameEnd+1)):  # Loop through all the frames
        frame = cv2.imread(imagePath+str(i)+'_fake.png')
        out.write(frame)
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    args = docopt(__doc__, version='Four.2.Zero')
    main(args)
