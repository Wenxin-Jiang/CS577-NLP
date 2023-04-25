---
license: gpl-3.0
tags:
- object-detection
- computer-vision
- yolor
- yolov4
datasets:
- detection-datasets/coco
language:
- en
pipeline_tag: object-detection
library_name: yolor
library_version: 0.0.3
---

### Model Description
[YOLOR:](https://arxiv.org/abs/2105.04206)  You Only Learn One Representation: Unified Network for Multiple Tasks.

[YOLOR-Pip:](https://github.com/kadirnar/yolor-pip/) Packaged version of the YOLOR repository

[Paper Repo:](https://github.com/WongKinYiu/yolor/) Implementation of paper - YOLOR

### Installation
```
pip install yolor
```

### Yolov6 Inference
```python
from yolor.helpers import Yolor

model = Yolor(
  cfg='yolor/cfg/yolor_p6.cfg',
  weights='kadirnar/yolor-p6',
  imgsz=640,
  device='cuda:0',
  hf_model=True
)

model.classes = None
model.conf = 0.25
model.iou_ = 0.45
model.show = False
model.save = True

model.predict('yolor/data/highway.jpg')
```

### BibTeX Entry and Citation Info
 ```
@article{wang2021you,
  title={You Only Learn One Representation: Unified Network for Multiple Tasks},
  author={Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2105.04206},
  year={2021}
}
```