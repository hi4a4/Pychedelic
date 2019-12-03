# Pychedelic
Since the existence of humans, people have attempted to depict the world as a physical representation of their perceptions--known as art. The purpose of our project is to explore and test whether a computer program can understand art. This requires two parts: to teach the program what the world looks like in its perspective, and to teach the program how to convert its style to an image of the world. If we achieve this, the program will be able to take in an image, and add its unique style to it, or take in a style and convert it to a photorealistic image. We plan that this project can be used by anyone for their personal entertainment. Specifically, our group is interested in designing a model that simulates a psychedelic trip. This will require two sets of images: environment and psychedelic images. Once our model has been trained, it will be able to take in an image, replicate the visual effects of hallucinogens onto the image, and output the image as it may be seen with those visuals. In addition, by running our model on each frame of a video, our team will generate a processed video.
# Results
<div>
  <img src="https://i.imgur.com/SO4PcmP.png"
    alt="Kurfess"
    width="32%"
    height="auto"
    style="display:inline-block;"
  />
  <img src="https://i.imgur.com/VGRT8uC.png"
    alt="Kurfess1"
    width="32%"
    height="auto"
    style="display:inline-block;" 
  />
  <img src="https://i.imgur.com/XH0WZJJ.png"
     alt="Kurfess2"
     width="32%"
     height="auto"
     style="display:inline-block;"
  />
  <caption>
    Fig 1-3: Show's a picture of our teacher, Dr. Kurfess, transformed by our CycleGAN at various levels of intensity (training time). From left to right (Original, 25 epoches, 65 epoches) 
  </caption>
</div>

# Usage

### To transform a youtube video:
<pre>
./layPipe.sh <video_file> <model_name> <intensity> <end_frame_num>
</pre>
- <b>video_file</b>: the url of a youtube to be modified
- <b>model_name</b>: the name of the trained CycleGAN model
- <b>intensity</b>: the epoch number for the wieghts file to use
- <b>end_frame_num</b>: the frame of the youtube video, which our script stops generating

Output:
fake_[youtube video code].mp4

A mp4 file with each frame in the video processed by our CycleGAN

### Example:
<pre>
./layPipe.sh https://www.youtube.com/watch?v=fiaaHpGOXBE trained_model 25 400
</pre>
Output: fake_fiaaHpGOXBE.mp4

# Task list
- [X] Make [video](https://www.youtube.com/watch?v=4X4HjIE1PSs) representation of redwood forest
- [X] Make [jupyter notebook](https://colab.research.google.com/drive/1bGVLS0-g3ns4aOUkfe2gLyJ4Hz5J4yJ5) of cycle gan for non-computer scientists

### Link to useful content for what we are doing
- [Backgroud Understanding](https://machinelearningmastery.com/what-is-cyclegan/)
- [CycleGAN implementation](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
