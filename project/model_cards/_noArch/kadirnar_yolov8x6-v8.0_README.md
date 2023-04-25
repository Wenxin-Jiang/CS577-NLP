---
license: gpl-3.0
tags:
  - object-detection
  - computer-vision
  - yolov8
  - yolov5
datasets:
  - detection-datasets/coco
---

### Model Description
[Ultralytics:](https://github.com/ultralytics/ultralytics/) YOLOv8 in PyTorch > ONNX > CoreML > TFLite]


### Installation
```
pip install ultralytics
```

### Yolov8 Inference
```python
from ultralytics import YOLO

model = YOLO('kadirnar/yolov8x6-v8.0')
model.conf = conf_threshold
model.iou = iou_threshold
prediction = model.predict(image, imgsz=image_size, show=False, save=False)
```

### BibTeX Entry and Citation Info
 ```

```