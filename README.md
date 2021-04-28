Video Processing for dash cams videos

Prepare environment
```
# Run script
bash start.sh

# activate virtual environment
source dataPrep/bin/activate
```

1. Video extraction 
```  
python3 video2frame.py -v PATHOFVIDEO -i 5 -o GIVENID -c STARTINGIMAGENUMBER -f FRAMERATE
``` 

Flags:
- video     = video path
- output    = Name of output (based on assigned id from SC, to avoid conflicts)
- counter   = The image number after assigned id

Optional Flags:
- frames    = The frame rate of video. Default value is set to 30.
- interval  = Time (in seconds) to capture frame. Default value is set to 1 second

eg:
User want to extract image every 5 second from a 30 fps video on path ../data/dashcam.MP4, assign 'dummy' as id and 10 as starting count
```  
python3 video2frame.py -v ../data/dashcam.MP4 -i 5 -o dummy -c 10 -f 30 
``` 

2. Convert PNG to JPG or JPEG
```
python3 convert_png2jpg.py --image test.png 
```
