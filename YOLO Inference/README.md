## YOLO V3

This implementation is based on Zihao Zhang's [implementation](https://github.com/zzh8829/yolov3-tf2). Thanks to him!


### Installation

Convert the Darknet model using the following command:

    wget https://pjreddie.com/media/files/yolov3.weights -O weights/yolov3.weights
    python convert.py --weights weights/yolov3.weights --output weights/yolov3.tf


Tip. The notebook shared in this folder illustrates some notions from the book "Hands-on Computer Vision with TensorFlow 2" written by Eliot Andres and Benjamin Planche, published by Packt. If you enjoyed the insights shared here, please consider acquiring the book!  

The book provides further guidance for those eager to learn about computer vision and to harness the power of TensorFlow 2 and Keras to build efficient recognition systems for object detection, segmentation, video processing, smartphone applications, and more.  
