# Tools for data preparations

<p align="left">
    <a href="https://github.com/CertifaiAI/dataset-preparation/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/CertifaiAI/dataset-preparation">
    </a>
    <a href="https://sonarcloud.io/dashboard?id=CertifaiAI_dataset-preparation">
        <img alt="Quality Gate" src="https://sonarcloud.io/api/project_badges/measure?project=CertifaiAI_dataset-preparation&metric=alert_status">
    </a>
    <a href="https://sonarcloud.io/dashboard?id=CertifaiAI_dataset-preparation">
        <img alt="Bugs Count" src="https://sonarcloud.io/api/project_badges/measure?project=CertifaiAI_dataset-preparation&metric=bugs">
    </a>
    <a href="https://sonarcloud.io/dashboard?id=CertifaiAI_dataset-preparation">
        <img alt="Code Smell" src="https://sonarcloud.io/api/project_badges/measure?project=CertifaiAI_dataset-preparation&metric=code_smells">
    </a>
 </p>

Prepare environment (linux)
```
# Run script
bash start.sh

# activate virtual environment
source dataPrep/bin/activate
```
Prepare environment (windows)


## Video to images extraction 
```  
python3 video2frame.py -v PATHOFVIDEO -i 5 -c STARTINGIMAGENUMBER -f FRAMERATE
``` 

Must have Flags:
- video     = video path

Optional Flags:
- frames    = frame rate of video. Default value is set to 30.
- interval  = Time (in seconds) to capture frame. Default value is set to 1 second
- counter   = image number after unique id, default is set to 1.

eg:
User want to extract image every 5 second from a 30 fps video on path ../data/dashcam.MP4
```  
python3 video2frame.py -v ../data/dashcam.MP4 -i 5 -f 30 
``` 
Video to images extraction using Yolov4-tiny pretrained model 

You can use colab notebook [here](https://colab.research.google.com/drive/1auYpS0jC4KJuV7rdnrpkJApJm0vDk7mb?usp=sharing).
Please make a copy before you run the codes on colab.


## Convert PNG to JPG or JPEG
```
python3 convert_png2jpg.py --image test.png 
```

## Rename images with random ID
```
python3 rename.py --dir images
```
dir = path of directory for captured photos

## Data Augmentation
```
 python3 imgAug.py --dir trial --dest result -R -B --bright 2.0 -F
```
dir = path of data directory to perform augmentation

dest = path of directory to store result

bright = value of brightness

noise = value of noise 

degree = degree of rotation

N = use noise augmentation

R = use rotation augmentation

B = use brighness or darkness augmentation

F = use flip augmentation

Please refer to the code for further explaination 

## Remove '_jpg', '_JPG', '_jpeg' from filenames
```
python3 remove_jpg.py --dir PATH_TO_DIRECTORY
```
dir = path to folder

## Train, Test, Split scripts for object detections
```
python train_test_valid.py --dir experiments --train_out train --test_out test --valid_out valid
```
dir         = directory of database

train_out   = path of train dataset output

test_out    = path of ts
