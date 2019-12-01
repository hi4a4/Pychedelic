#!/bin/bash
if [ $# -eq 0 ]
    then
        echo 'Usage: ./layPipe.sh <video_file> <model_name> <intensity>'
        echo 'video_file: video to process with e.g. swan.mp4'
        echo 'model_name: e.g. e2dmx_circle_jerk'
        echo 'intensity: Number of epcohed the model has been trained for, in increments of 5 e.g. 25'
    else
        SAVE_DIR="results"
        workon cv
        # Need to generate the video frames
        mkdir $SAVE_DIR
        python downloadFrames.py $1 $SAVE_DIR
        deactivate cv
        # Need to change the .pth file to update weight file with the intensity/epoch trained
        rm -rf "pytorch-CycleGAN-and-pix2pix/checkpoints/${2}/latest_net_G.pth"
        cp "pytorch-CycleGAN-and-pix2pix/checkpoints/${2}/${3}_net_G_A.pth" "pytorch-CycleGAN-and-pix2pix/checkpoints/${2}/latest_net_G.pth"

        # Run model on generated images 
        python pytorch-CycleGAN-and-pix2pix/test.py --num_test 60000 --preprocess scale_width --load_size 1024 --dataroot $SAVE_DIR --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --name $2 --model test --no_dropout
        
        workon cv
        # save the video
        python makeVideo.py $1 $2
        deactivate cv
        # Remove old generated video frames
        rm -rf "./results/"
fi

no_dropout