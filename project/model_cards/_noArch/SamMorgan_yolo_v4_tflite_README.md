---
language: en
tags: 
- object detection
- computer vision
- darknet
- yolo

datasets:
- coco
- imagenette

license: mit

thumbnail: https://github.com/hunglc007/tensorflow-yolov4-tflite

pipeline_tag: object-detection 
---

# YOLOv4

YOLO, for "You Only Look Once", is an object detection system in real-time, introduced in [this paper](https://arxiv.org/abs/2004.10934), that recognizes various objects in a single enclosure. It identifies objects more rapidly and more precisely than other recognition systems. Three authors Alexey Bochkovskiy, the Russian developer who built the YOLO Windows version, Chien-Yao Wang, and Hong-Yuan Mark Liao, are accounted for in this work and the entire code is available on [Github](https://github.com/AlexeyAB/darknet).

This YOLOv4 library, inspired by previous YOLOv3 implementations here:
  * [Yolov3 tensorflow](https://github.com/YunYang1994/tensorflow-yolov3)
  * [Yolov3 tf2](https://github.com/zzh8829/yolov3-tf2)uses Tensorflow 2.0 and is available on this [Github](https://github.com/hunglc007/tensorflow-yolov4-tflite). 
  
  
 ### Limitations and biases
Object-recognition technology has improved drastically in the past few years across the industry, and it is now part of a huge variety of products and services that millions of people worldwide use. However, errors in object-recognition algorithms can stem from the training data used to create the system is geographically constrained and/or that it fails to recognize cultural differences.

The COCO dataset used to train yolov4-tflite has been found to have annotation errors on more than 20% of images. Such errors include captions describing people differently based on skin tone and gender expression. This serves as a reminder to be cognizant that these biases already exist and a warning to be careful about the increasing bias that is likely to come with advancements in image captioning technology.



### How to use YOLOv4tflite
You can use this model to detect objects in an image of choice. Follow the following scripts to implement on your own!

```bash
# install git lfs
git lfs install

# if presented with the error "git: 'lfs' is not a git command. See 'git --help'", try running these linux commands:
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash

# change directory to base
cd ..

# install git-lfs
sudo apt-get install git-lfs

# for message "Git LFS initialized"
git lfs install

# change directory to yolo_v4_tflite
cd ./yolo_v4_tflite

# clone this repo into your notebook
git clone https://huggingface.co/SamMorgan/yolo_v4_tflite

# Run demo tensor flow for an example of how this model works
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --image ./data/kite.jpg --output ./test.jpg

# Try with your own image
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --image <insert path to image of choice> --output <insert path to output location of choice>


```

### Evaluate on COCO 2017 Dataset
```bash
# run script in /script/get_coco_dataset_2017.sh to download COCO 2017 Dataset
# preprocess coco dataset
cd data
mkdir dataset
cd ..
cd scripts
python coco_convert.py --input ./coco/annotations/instances_val2017.json --output val2017.pkl
python coco_annotation.py --coco_path ./coco 
cd ..

# evaluate yolov4 model
python evaluate.py --weights ./data/yolov4.weights
cd mAP/extra
python remove_space.py
cd ..
python main.py --output results_yolov4_tf
```
#### mAP50 on COCO 2017 Dataset

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3      | 55.43   | 52.32   |         |
| YoloV4      | 61.96   | 57.33   |         |

### Benchmark
```bash
python benchmarks.py --size 416 --model yolov4 --weights ./data/yolov4.weights
```
#### TensorRT performance
 
| YoloV4 416 images/s |   FP32   |   FP16   |   INT8   |
|---------------------|----------|----------|----------|
| Batch size 1        | 55       | 116      |          |
| Batch size 8        | 70       | 152      |          |

#### Tesla P100

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3 FPS  | 40.6    | 49.4    | 61.3    |
| YoloV4 FPS  | 33.4    | 41.7    | 50.0    |

#### Tesla K80

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3 FPS  | 10.8    | 12.9    | 17.6    |
| YoloV4 FPS  | 9.6     | 11.7    | 16.0    |

#### Tesla T4

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3 FPS  | 27.6    | 32.3    | 45.1    |
| YoloV4 FPS  | 24.0    | 30.3    | 40.1    |

#### Tesla P4

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3 FPS  | 20.2    | 24.2    | 31.2    |
| YoloV4 FPS  | 16.2    | 20.2    | 26.5    |

#### Macbook Pro 15 (2.3GHz i7)

| Detection   | 512x512 | 416x416 | 320x320 |
|-------------|---------|---------|---------|
| YoloV3 FPS  |         |         |         |
| YoloV4 FPS  |         |         |         |


### Traning your own model
```bash
# Prepare your dataset
# If you want to train from scratch:
In config.py set FISRT_STAGE_EPOCHS=0 
# Run script:
python train.py
# Transfer learning: 
python train.py --weights ./data/yolov4.weights
```
The training performance is not fully reproduced yet, so I recommended to use Alex's [Darknet](https://github.com/AlexeyAB/darknet) to train your own data, then convert the .weights to tensorflow or tflite.


### References

  * YOLOv4: Optimal Speed and Accuracy of Object Detection [YOLOv4](https://arxiv.org/abs/2004.10934).
  * [darknet](https://github.com/AlexeyAB/darknet)
