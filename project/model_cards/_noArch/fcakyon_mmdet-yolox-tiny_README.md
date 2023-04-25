---
license: apache-2.0
inference: false
tags:
- object-detection
- computer-vision
- vision
- mmdet
- sahi

datasets:
- detection-datasets/coco
---

### Model Description
[YOLOX: Exceeding YOLO Series in 2021](https://arxiv.org/abs/2107.08430)

[SAHI: Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection](https://arxiv.org/abs/2202.06934)

Improved anchor-free YOLO architecture for object detection task.


### Documents
- [GitHub Repo](https://github.com/open-mmlab/mmdetection/blob/master/configs/yolox/README.md)
- [Paper - YOLOX: Exceeding YOLO Series in 2021](https://arxiv.org/abs/2107.08430)
  
### Datasets
The YOLOX model was pre-trained on [ImageNet-1k](https://huggingface.co/datasets/imagenet2012) and fine-tuned on [COCO 2017 object detection](https://cocodataset.org/#download), a dataset consisting of 118k/5k annotated images for training/validation respectively. 


### How to use

- Install [sahi](https://github.com/obss/sahi) and `mmdet`:

```bash
pip install -U sahi
pip install mmcv-full==1.7.0 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html
pip install mmdet==2.26.0
```

- Load model and perform prediction:

```python
from sahi import AutoDetectionModel
from sahi.utils.file import download_from_url
from sahi.predict import get_prediction
from sahi.cv import read_image_as_pil

MMDET_YOLOX_TINY_MODEL_URL = "https://huggingface.co/fcakyon/mmdet-yolox-tiny/resolve/main/yolox_tiny_8x8_300e_coco_20211124_171234-b4047906.pth"
MMDET_YOLOX_TINY_MODEL_PATH = "yolox.pt"
MMDET_YOLOX_TINY_CONFIG_URL = "https://huggingface.co/fcakyon/mmdet-yolox-tiny/raw/main/yolox_tiny_8x8_300e_coco.py"
MMDET_YOLOX_TINY_CONFIG_PATH = "config.py"
IMAGE_URL = "https://user-images.githubusercontent.com/34196005/142730935-2ace3999-a47b-49bb-83e0-2bdd509f1c90.jpg"

# download weight and config
download_from_url(
  MMDET_YOLOX_TINY_MODEL_URL,
  MMDET_YOLOX_TINY_MODEL_PATH,
)
download_from_url(
  MMDET_YOLOX_TINY_CONFIG_URL,
  MMDET_YOLOX_TINY_CONFIG_PATH,
)

# create model
detection_model = AutoDetectionModel.from_pretrained(
    model_type='mmdet',
    model_path=MMDET_YOLOX_TINY_MODEL_PATH,
    config_path=MMDET_YOLOX_TINY_CONFIG_PATH,
    confidence_threshold=0.5,
    device="cuda:0", # or 'cpu'
)

# prepare input image
image = read_image_as_pil(IMAGE_URL)

# perform prediction
prediction_result = get_prediction(
  image=image,
  detection_model=detection_model
)

# visualize predictions
prediction_result.export_predictions(export_dir='results/')

# get predictions
prediction_result.object_prediction_list
```

More info at [demo notebook](https://github.com/obss/sahi/blob/main/demo/inference_for_mmdetection.ipynb).

### BibTeX Entry and Citation Info
```
@article{akyon2022sahi,
  title={Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection},
  author={Akyon, Fatih Cagatay and Altinuc, Sinan Onur and Temizel, Alptekin},
  journal={2022 IEEE International Conference on Image Processing (ICIP)},
  doi={10.1109/ICIP46576.2022.9897990},
  pages={966-970},
  year={2022}
}
```
```
@article{yolox2021,
  title={{YOLOX}: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```