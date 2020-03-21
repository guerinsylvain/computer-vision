### Convert pre-trained Darknet weights

Convert the Darknet model using the following command:

wget https://pjreddie.com/media/files/yolov3.weights -O data/yolov3.weights
python convert.py

Type  
```
python detect_video.py --video 0
```
to analyze webcam