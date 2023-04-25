---
tags:
- object-detection
---

## Dataset

The dataset was referenced in the Smartathon competition.It's consist of 7874 images annontated with 11 classes: 

* GARBAGE 8597
* CONSTRUCTION_ROAD 2730
* POTHOLES 2625
* CLUTTER_SIDEWALK 2253
* BAD_BILLBOARD 1555
* GRAFFITI 1124
* SAND_ON_ROAD 748
* UNKEPT_FACADE 127
* FADED_SIGNAGE 107
* BROKEN_SIGNAGE 83
* BAD_STREETLIGHT 1

The dataset highly imbalanced and contain some humman errors.

## Our SEE Team Solution

1. Convert from Pascal VOC to YOLO format
2. Model Hyperparamter tuning
3. Train the data on Yolov7
4. Evaluate the model
5. Expalin Different techniques to Automation of Data Annotation

For our solution detials: [notebook](https://colab.research.google.com/drive/1mo3HxJrg8wDGp_FhkB_0qAs41XvQ3hjR?usp=sharing)

### How to use

1. You can just download file weights from the files section
2. clone yolov7 repo `!git clone https://github.com/WongKinYiu/yolov7`
3. ensure your current working directory is yolov7 then run `! pip install -r requirements.txt`
4. then run the detector script `! python detect.py --weights " model.pt path" --img 736 --conf 0.27 --source "testing image path" --save-txt`