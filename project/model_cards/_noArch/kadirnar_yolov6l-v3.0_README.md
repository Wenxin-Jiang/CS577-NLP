---
license: gpl-3.0
tags:
  - object-detection
  - computer-vision
  - yolov6
  - yolo
datasets:
  - detection-datasets/coco
---

### Model Description
[YOLOv6:](https://arxiv.org/abs/2209.02976) A single-stage object detection framework dedicated to industrial applications.

[YOLOv6 v3.0](https://arxiv.org/abs/2301.05586): A Full-Scale Reloading

[YOLOv6-Pip: Packaged version of the Yolov6 repository](https://github.com/kadirnar/yolov6-pip/)

[Paper Repo: Implementation of paper - YOLOv6](https://github.com/meituan/YOLOv6/)

### Installation
```
pip install yolov6detect
```

### Yolov6 Inference
```python
from yolov6 import YOLOV6

model = YOLOV6(weights='kadirnar/yolov6l-v3.0', device='cuda:0', hf_model=True)

model.classes = None
model.conf = 0.25
model.iou = 0.45
model.show = False
model.save = True

pred = model.predict(source='data/images',yaml='data/coco.yaml', img_size=640)
```

### BibTeX Entry and Citation Info
 ```
@article{li2022yolov6,
  title={YOLOv6: A single-stage object detection framework for industrial applications},
  author={Li, Chuyi and Li, Lulu and Jiang, Hongliang and Weng, Kaiheng and Geng, Yifei and Li, Liang and Ke, Zaidan and Li, Qingyuan and Cheng, Meng and Nie, Weiqiang and others},
  journal={arXiv preprint arXiv:2209.02976},
  year={2022}
}
```