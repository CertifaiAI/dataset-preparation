import cv2
import time
import os
import argparse
from os import path
import imutils
import uuid

# arguements
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
ap.add_argument("-i", "--interval", default=1, 
	help="interval (in seconds) between captured frames")
ap.add_argument("-c", "--counter", default=1,
	help="starting count number")
ap.add_argument("-f", "--frames", default=30,
	help="frame rates of video file")
args = vars(ap.parse_args())

def video_to_frames():
    # Initialize variables and constants
    interval = int(args['interval'])
    counter = int(args['counter'])
    vid_path = args['video']
    frame_rate = int(args['frames'])
    # Get random id
    id = uuid.uuid4()
    # Target frame
    '''
    Target frame = frame rate * interval(in seconds)
    for example, given the video is 30 per seconds, so each second will have more or less 30 frames. If interval (seconds) is 1. The script
    will save the frame every 30 frames (30*1). if interval is 5s. The script will save frame every 150 frame.
    '''
    target_frame= frame_rate * interval
    
    # Make directory if not exist
    cwd = os.getcwd()
    if not path.exists(cwd+'/images'):
        os.mkdir(cwd+'/images')

    # Log start time
    time_start = time.time()

    # Start capturing the feed
    cap = cv2.VideoCapture(vid_path)

    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    frame_count = frame_rate
    print ("Converting video..\n")

    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # if frame count reach 30 again -> take frame
        if frame_count == target_frame:
            # Resize image to 800
            frame = imutils.resize(frame, width=800)
            cv2.imwrite("images/{}_{}.jpg".format(id, counter), frame)
            # Set frame count to 0 
            frame_count = 0
            counter+= 1
        # Counting total number of frames
        count += 1
        frame_count += 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break

if __name__=="__main__":
    video_to_frames()