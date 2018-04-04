#!/usr/bin/env python

import cv2
import os
import sys
import numpy as np

from data_generator import DataGenerator

class ImageGenerator(DataGenerator):

  def __init__(self, video_file, name='image_gen'):
    super(ImageGenerator, self).__init__(name)

    if not os.path.exists(video_file):
      raise IOError('video file path does not exist' + str(video_file))

    self.vidcap = cv2.VideoCapture(video_file)
    self.length = int(self.vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    self.width  = int(self.vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    self.height = int(self.vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    self.fps    = self.vidcap.get(cv2.cv.CV_CAP_PROP_FPS)

    print('length', self.length)
    print('width', self.width)
    print('height', self.height)
    print('fps', self.fps)

  def get_video_size(self):
    return self.length

  def generate_large_size(self):
    return bytearray(self.vidcap.read()[1])

  def show_image_from_bytearray(self, image_bytearray):
    print(type(image_bytearray))
    print(len(image_bytearray[0]))
    nparr = np.asarray(image_bytearray[0], np.uint8).reshape(self.height, self.width, 3)
    img_np = cv2.cvtColor(nparr, cv2.cv.CV_BGR2RGB)
    cv2.imshow('image', img_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
