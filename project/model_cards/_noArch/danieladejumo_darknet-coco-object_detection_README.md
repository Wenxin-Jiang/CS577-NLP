---
tags:
- object-detection
- COCO
- YOLO
- Darknet
model-index:
- name: darknet-coco-object_detection
  results:
  - metrics:
    - type: None
      value: '1'
      name: None
    task:
      type: object-detection
      name: object-detection
    dataset:
      name: COCO
      type: COCO
---

## Darknet Object Detection on the COCO dataset

This model uses a pretrained YOLO Darknet model to perform object detection on an input image. The model is able to identify 80 classes from the COCO dataset. The classes are listed here `config/coco.names`.

### Usage
Clone the repository using
```python
repo = Repository("/local_repo_name", clone_from="danieladejumo/darknet-coco-object_detection")
```

Run a detection by using the function `detect(path_to_image)` in the notebook `darknet-coco-object_detection.ipynb`. The output image with the detection rectangle and classes will be saved to `images/image_file_name-det.jpg`
