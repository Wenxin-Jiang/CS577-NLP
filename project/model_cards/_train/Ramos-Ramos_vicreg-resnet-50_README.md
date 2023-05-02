---
tags:
- vicreg
- vision

datasets:
- imagenet-1k
---

# VICReg ResNet-50

ResNet-50 pretrained with VICReg. VICReg was introduced in [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](https://arxiv.org/abs/2104.14294), while ResNet was introduced in [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). The official implementation of a VICReg Resnet-50 can be found [here](https://github.com/facebookresearch/dino).

Weights converted from the official [VICReg ResNet](https://github.com/facebookresearch/vicreg#pretrained-models-on-pytorch-hub) using [this script](https://colab.research.google.com/drive/1G2Y3JVWSzOh-kX8xKJUg5m4nc7dNkzNc?usp=sharing).

For up-to-date model card information, please see the [original repo](https://github.com/facebookresearch/vicreg).

### How to use

**Warning: The feature extractor in this repo is a copy of the one from [`microsoft/resnet-50`](https://huggingface.co/microsoft/resnet-50). We never verified if this image prerprocessing is the one used with VICReg ResNet-50.**

```python
from transformers import AutoFeatureExtractor, ResNetModel
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = AutoFeatureExtractor.from_pretrained('Ramos-Ramos/vicreg-resnet-50')
model = ResNetModel.from_pretrained('Ramos-Ramos/vicreg-resnet-50')
inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

### BibTeX entry and citation info

```bibtex
@article{bardes2021vicreg,
  title={Vicreg: Variance-invariance-covariance regularization for self-supervised learning},
  author={Bardes, Adrien and Ponce, Jean and LeCun, Yann},
  journal={arXiv preprint arXiv:2105.04906},
  year={2021}
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