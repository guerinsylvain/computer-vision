# To run this notebook, download the YOLO V3 weights and convert them using the command: 
#
# wget https://pjreddie.com/media/files/yolov3.weights -O weights/yolov3.weights
#
# python convert.py --weights weights/yolov3.weights --output weights/yolov3.tf

import time
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2cd..
import numpy as np
import tensorflow as tf
from models import YoloV3
from utils import draw_outputs, transform_images
import matplotlib.pyplot as plt
import os 

scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)
f = os.path.basename(scriptpath)
print(f)
path = scriptpath[:-(len(f))-1]
print(path)

CLASSES_PATH = path + '/coco.names'
print(CLASSES_PATH)
WEIGHTS_PATH = path + '/weights/yolov3.tf'
print(WEIGHTS_PATH)
IMAGE_SIZE = 416

# Load the model, the classes and the example image
yolo = YoloV3()
yolo.load_weights(WEIGHTS_PATH)
class_names = [c.strip() for c in open(CLASSES_PATH).readlines()]

img = tf.image.decode_image(open(path + '/dog_example.jpg', 'rb').read(), channels=3)
plt.imshow(img)
plt.show()

input_img = tf.expand_dims(img, 0)
input_img = transform_images(input_img, IMAGE_SIZE)

# Run inference and display result
boxes, scores, classes, nums = yolo(input_img)


logging.info('detections:')
for i in range(nums[0]):
    print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
                                       np.array(scores[0][i]),
                                       np.array(boxes[0][i])))

prediction_img = draw_outputs(img.numpy(), (boxes, scores, classes, nums), class_names)
plt.figure(figsize=(10, 20))
plt.imshow(prediction_img)
plt.show()