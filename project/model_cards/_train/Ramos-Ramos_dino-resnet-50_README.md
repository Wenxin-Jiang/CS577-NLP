---
tags:
- dino
- vision

datasets:
- imagenet-1k
---

# DINO ResNet-50

ResNet-50 pretrained with DINO. DINO was introduced in [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294), while ResNet was introduced in [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). The official implementation of a DINO Resnet-50 can be found [here](https://github.com/facebookresearch/dino).

Weights converted from the official [DINO ResNet](https://github.com/facebookresearch/dino#pretrained-models-on-pytorch-hub) using [this script](https://colab.research.google.com/drive/1Ax3IDoFPOgRv4l7u6uS8vrPf4TX827BK?usp=sharing).

For up-to-date model card information, please see the [original repo](https://github.com/facebookresearch/dino).

### How to use

**Warning: The feature extractor in this repo is a copy of the one from [`microsoft/resnet-50`](https://huggingface.co/microsoft/resnet-50). We never verified if this image prerprocessing is the one used with DINO ResNet-50.**

```python
from transformers import AutoFeatureExtractor, ResNetModel
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = AutoFeatureExtractor.from_pretrained('Ramos-Ramos/dino-resnet-50')
model = ResNetModel.from_pretrained('Ramos-Ramos/dino-resnet-50')
inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-2104-14294,
  author    = {Mathilde Caron and
               Hugo Touvron and
               Ishan Misra and
               Herv{\'{e}} J{\'{e}}gou and
               Julien Mairal and
               Piotr Bojanowski and
               Armand Joulin},
  title     = {Emerging Properties in Self-Supervised Vision Transformers},
  journal   = {CoRR},
  volume    = {abs/2104.14294},
  year      = {2021},
  url       = {https://arxiv.org/abs/2104.14294},
  archivePrefix = {arXiv},
  eprint    = {2104.14294},
  timestamp = {Tue, 04 May 2021 15:12:43 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2104-14294.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@inproceedings{he2016deep,
  title={Deep residual learning for image recognition},
  author={He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={770--778},
  year={2016}
}
```