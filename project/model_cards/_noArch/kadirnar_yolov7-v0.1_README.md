---
license: gpl-3.0
tags:
  - object-detection
  - computer-vision
  - yolov7
  - pypi
datasets:
  - detection-datasets/coco
---

### Model Description
[YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/abs/2207.02696)

[YOLOv7-Pip: Packaged version of the Yolov7 repository](https://github.com/kadirnar/yolov7-pip)

[Paper Repo: Implementation of paper - YOLOv7](https://github.com/WongKinYiu/yolov7)

### Installation
```
pip install yolov7detect
```

### Yolov7 Inference
```python
import yolov7

# load pretrained or custom model
model = yolov7.load('kadirnar/yolov7-v0.1', hf_model=True)

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.classes = None  # (optional list) filter by class

# set image
imgs = 'inference/images'

# perform inference
results = model(imgs)

# inference with larger input size and test time augmentation
results = model(img, size=1280, augment=True)

# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, y1, x2, y2
scores = predictions[:, 4]
categories = predictions[:, 5]

# show detection bounding boxes on image
results.show()
```

### BibTeX Entry and Citation Info
 ```
@article{wang2022yolov7,
  title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2207.02696},
  year={2022}
}
```
