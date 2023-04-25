---
license: apache-2.0
tags:
- image-classification
- pytorch
- onnx
datasets:
- pyronear/openfire
---


# ReXNet-1.0x model

Pretrained on a dataset for wildfire binary classification (soon to be shared). The ReXNet architecture was introduced in [this paper](https://arxiv.org/pdf/2007.00992.pdf).


## Model description

The core idea of the author is to add a customized Squeeze-Excitation layer in the residual blocks that will prevent channel redundancy.


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

model = model_from_hf_hub("pyronear/rexnet1_0x").eval()

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
@article{DBLP:journals/corr/abs-2007-00992,
  author    = {Dongyoon Han and
               Sangdoo Yun and
               Byeongho Heo and
               Young Joon Yoo},
  title     = {ReXNet: Diminishing Representational Bottleneck on Convolutional Neural
               Network},
  journal   = {CoRR},
  volume    = {abs/2007.00992},
  year      = {2020},
  url       = {https://arxiv.org/abs/2007.00992},
  eprinttype = {arXiv},
  eprint    = {2007.00992},
  timestamp = {Mon, 06 Jul 2020 15:26:01 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2007-00992.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

Source of this implementation

```bibtex
@software{Fernandez_Holocron_2020,
author = {Fernandez, François-Guillaume},
month = {5},
title = {{Holocron}},
url = {https://github.com/frgfm/Holocron},
year = {2020}
}
```
