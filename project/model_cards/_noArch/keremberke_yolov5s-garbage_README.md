 
---
tags:
- yolov5
- yolo
- vision
- object-detection
- pytorch
library_name: yolov5
library_version: 7.0.7
inference: false

datasets:
- keremberke/garbage-object-detection

model-index:
- name: keremberke/yolov5s-garbage
  results:
  - task:
      type: object-detection

    dataset:
      type: keremberke/garbage-object-detection
      name: keremberke/garbage-object-detection
      split: validation

    metrics:
      - type: precision  # since mAP@0.5 is not available on hf.co/metrics
        value: 0.38002559554830656  # min: 0.0 - max: 1.0
        name: mAP@0.5
---

<div align="center">
  <img width="640" alt="keremberke/yolov5s-garbage" src="https://huggingface.co/keremberke/yolov5s-garbage/resolve/main/sample_visuals.jpg">
</div>

### How to use

- Install [yolov5](https://github.com/fcakyon/yolov5-pip):

```bash
pip install -U yolov5
```

- Load model and perform prediction:

```python
import yolov5

# load model
model = yolov5.load('keremberke/yolov5s-garbage')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

# set image
img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
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
yolov5 train --data data.yaml --img 640 --batch 16 --weights keremberke/yolov5s-garbage --epochs 10
```

**More models available at: [awesome-yolov5-models](https://github.com/keremberke/awesome-yolov5-models)**
