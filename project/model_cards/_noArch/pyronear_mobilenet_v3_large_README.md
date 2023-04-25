---
license: apache-2.0
tags:
- image-classification
- pytorch
- onnx
datasets:
- pyronear/openfire
---


# MobileNet V3 - Large model

Pretrained on a dataset for wildfire binary classification (soon to be shared). The MobileNet V3 architecture was introduced in [this paper](https://arxiv.org/pdf/1905.02244.pdf).


## Model description

The core idea of the author is to simplify the final stage, while using SiLU as activations and making Squeeze-and-Excite blocks larger.


## Installation

### Prerequisites

Python 3.6 (or higher) and [pip](https://pip.pypa.io/en/stable/)/[conda](https://docs.conda.io/en/latest/miniconda.html) are required to install PyroVision.

### Latest stable release

You can install the last stable release of the package using [pypi](https://pypi.org/project/pyrovision/) as follows:

```shell
pip install pyrovision
```

or using [conda](https://anaconda.org/pyronear/pyrovision):

```shell
conda install -c pyronear pyrovision
```

### Developer mode

Alternatively, if you wish to use the latest features of the project that haven't made their way to a release yet, you can install the package from source *(install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) first)*:

```shell
git clone https://github.com/pyronear/pyro-vision.git
pip install -e pyro-vision/.
```


## Usage instructions

```python
from PIL import Image
from torchvision.transforms import Compose, ConvertImageDtype, Normalize, PILToTensor, Resize
from torchvision.transforms.functional import InterpolationMode
from pyrovision.models import model_from_hf_hub

model = model_from_hf_hub("pyronear/mobilenet_v3_large").eval()

img = Image.open(path_to_an_image).convert("RGB")

# Preprocessing
config = model.default_cfg
transform = Compose([
    Resize(config['input_shape'][1:], interpolation=InterpolationMode.BILINEAR),
    PILToTensor(),
    ConvertImageDtype(torch.float32),
    Normalize(config['mean'], config['std'])
])

input_tensor = transform(img).unsqueeze(0)

# Inference
with torch.inference_mode():
    output = model(input_tensor)
probs = output.squeeze(0).softmax(dim=0)
```


## Citation

Original paper

```bibtex
@article{DBLP:journals/corr/abs-1905-02244,
  author    = {Andrew Howard and
               Mark Sandler and
               Grace Chu and
               Liang{-}Chieh Chen and
               Bo Chen and
               Mingxing Tan and
               Weijun Wang and
               Yukun Zhu and
               Ruoming Pang and
               Vijay Vasudevan and
               Quoc V. Le and
               Hartwig Adam},
  title     = {Searching for MobileNetV3},
  journal   = {CoRR},
  volume    = {abs/1905.02244},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.02244},
  eprinttype = {arXiv},
  eprint    = {1905.02244},
  timestamp = {Thu, 27 May 2021 16:20:51 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-02244.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

Source of this implementation

```bibtex
@software{chintala_torchvision_2017,
author = {Chintala, Soumith},
month = {4},
title = {{Torchvision}},
url = {https://github.com/pytorch/vision},
year = {2017}
}
```