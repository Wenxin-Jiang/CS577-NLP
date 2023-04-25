---
license: gpl-3.0
inference: false
tags:
  - object-detection
  - computer-vision
  - vision
  - yolo
  - yolov5
datasets:
  - detection-datasets/coco
---

### How to use

- Install yolov5:

```bash
pip install -U yolov5
```

- Load model and perform prediction:

```python
import yolov5

# load model
model = yolov5.load('fcakyon/yolov5s-v7.0')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

# set image
img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model(img)

# inference with larger input size
results = model(img, size=640)

# inference with test time augmentation
results = model(img, augment=True)

# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, y1, x2, y2
scores = predictions[:, 4]
categories = predictions[:, 5]

# show detection bounding boxes on image
results.show()

# save results into "results/" folder
results.save(save_dir='results/')
```

- Finetune the model on your custom dataset:

```bash
yolov5 train --img 640 --batch 16 --weights fcakyon/yolov5s-v7.0 --epochs 10 --device cuda:0
```