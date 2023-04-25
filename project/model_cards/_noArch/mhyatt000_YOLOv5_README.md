---
license: gpl-2.0
datasets:
- coco
library_name: stable-baselines3
tags:
- seals/CartPole-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
- object-detection
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
      verified: True
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/CartPole-v0
      type: seals/CartPole-v0
---


# YOLOv5

Ultralytics YOLOv5 model in Pytorch.  

Proof of concept for (TypoSquatting, Niche Squatting) security flaw on Hugging Face.


## Model Description



## How to use

```python
from transformers import YolosFeatureExtractor, YolosForObjectDetection
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = YolosFeatureExtractor.from_pretrained('mhyatt000/yolov5')
model = YolosForObjectDetection.from_pretrained('mhyatt000/yolov5')

inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
# model predicts bounding boxes and corresponding COCO classes

logits = outputs.logits
bboxes = outputs.pred_boxes
```

## Training Data

### Training

## Evaluation

Model was evaluated on [COCO2017](https://cocodataset.org/#home) dataset.

|   Model	|	size (pixels)	|	mAPval  |   Speed   |   params  |   FLOPS   |
|---------------|-------------------|-----------|-----------|-----------|-----------|
| YOLOv5s6	|	    1280       	|	43.3	|	4.3 	| 	12.7	|	17.4    |
| YOLOv5m6	|	    1280    	|	50.5	|	8.4	    | 	35.9	|	52.4    |
| YOLOv5l6	|	    1280	    |	53.4	|	12.3	| 	77.2	|	117.7   |
| YOLOv5x6	|	    1280	    |	54.4	|	22.4	| 	141.8	|	222.9   |

### Bibtex and citation info

```bibtex
@software{glenn_jocher_2022_6222936,
  author       = {Glenn Jocher and
                  Ayush Chaurasia and
                  Alex Stoken and
                  Jirka Borovec and
                  NanoCode012 and
                  Yonghye Kwon and
                  TaoXie and
                  Jiacong Fang and
                  imyhxy and
                  Kalen Michael and
                  Lorna and
                  Abhiram V and
                  Diego Montes and
                  Jebastin Nadar and
                  Laughing and
                  tkianai and
                  yxNONG and
                  Piotr Skalski and
                  Zhiqiang Wang and
                  Adam Hogan and
                  Cristi Fati and
                  Lorenzo Mammana and
                  AlexWang1900 and
                  Deep Patel and
                  Ding Yiwei and
                  Felix You and
                  Jan Hajek and
                  Laurentiu Diaconu and
                  Mai Thanh Minh},
  title        = {{ultralytics/yolov5: v6.1 - TensorRT, TensorFlow 
                   Edge TPU and OpenVINO Export and Inference}},
  month        = feb,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v6.1},
  doi          = {10.5281/zenodo.6222936},
  url          = {https://doi.org/10.5281/zenodo.6222936}
}
```
