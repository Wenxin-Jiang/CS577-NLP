---
tags:
- computer-vision
- video-classification
library_name: keras
---
# 🎬 Video Classification with a CNN-RNN Architecture

**Author:** Sayak Paul   
**Date created:** 2021/05/28    
**Last modified:** 2021/06/05     
**Description:** Training a video classifier with transfer learning and a recurrent model on the UCF101 dataset.     
**Keras documentation [link](https://keras.io/examples/vision/video_classification/)**  

This example demonstrates video classification, an important use-case with applications in recommendations, security, and so on. We will be using the UCF101 dataset to build our video classifier. The dataset consists of videos categorized into different actions, like cricket shot, punching, biking, etc. This dataset is commonly used to build action recognizers, which are an application of video classification.

A video consists of an ordered sequence of frames. Each frame contains spatial information, and the sequence of those frames contains temporal information. To model both of these aspects, we use a hybrid architecture that consists of convolutions (for spatial processing) as well as recurrent layers (for temporal processing). Specifically, we'll use a Convolutional Neural Network (CNN) and a Recurrent Neural Network (RNN) consisting of GRU layers. This kind of hybrid architecture is popularly known as a CNN-RNN.

```bash
Test video path: v_Punch_g03_c02.avi
  Punch: 56.50%
  TennisSwing: 29.97%
  PlayingCello:  6.47%
  ShavingBeard:  3.69%
  CricketShot:  3.38%
 ```   
![Example video from dataset](./animation.gif)
