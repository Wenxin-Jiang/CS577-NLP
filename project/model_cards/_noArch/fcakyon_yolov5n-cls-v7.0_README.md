---
license: gpl-3.0
inference: false
tags:
  - image-classification
  - computer-vision
  - vision
  - yolo
  - yolov5
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
model = yolov5.load('fcakyon/yolov5n-cls-v7.0')

# set image
img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model(img)
```

- Finetune the model on your custom dataset:

```bash
yolov5 classify train --img 128 --data mnist2560 --model fcakyon/yolov5n-cls-v7.0 --epochs 1 --device cpu
```