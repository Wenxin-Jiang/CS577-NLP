---
license: apache-2.0
tags:
  - object-detection
  - computer-vision
  - yolox
  - yolov3
  - yolov5
datasets:
  - detection-datasets/coco
---

### Model Description
[YOLOX](https://arxiv.org/abs/2107.08430) is a high-performance anchor-free YOLO, exceeding yolov3~v5 with MegEngine, ONNX, TensorRT, ncnn, and OpenVINO supported.

[YOLOXDetect-Pip](https://github.com/kadirnar/yolox-pip/): This repo is a packaged version of the [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) for easy installation and use.

[Paper Repo]: Implementation of paper - [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)

### Installation
```
pip install yoloxdetect
```

### Yolox Inference
```python
from yoloxdetect import YoloxDetector
from yolox.data.datasets import COCO_CLASSES
model = YoloxDetector(
    model_path = "kadirnar/yolox_nano-v0.1.1",
    config_path = "configs.yolox_s",
    device = "cuda:0",
    hf_model=True
)
model.classes = COCO_CLASSES
model.conf = 0.25
model.iou = 0.45
model.show = False
model.save = True
pred = model.predict(image='data/images', img_size=640)
```

### BibTeX Entry and Citation Info
 ```
 @article{yolox2021,
  title={YOLOX: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```