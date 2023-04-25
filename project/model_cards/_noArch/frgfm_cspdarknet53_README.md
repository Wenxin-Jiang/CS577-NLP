---
license: apache-2.0
tags:
- image-classification
- pytorch
datasets:
- frgfm/imagenette
---


# CSP-Darknet-53 model

Pretrained on [ImageNette](https://github.com/fastai/imagenette). The CSP-Darknet-53 architecture was introduced in [this paper](https://arxiv.org/pdf/1911.11929.pdf).


## Model description

The core idea of the author is to change the convolutional stage by adding cross stage partial blocks in the architecture.


## Installation

### Prerequisites

Python 3.6 (or higher) and [pip](https://pip.pypa.io/en/stable/)/[conda](https://docs.conda.io/en/latest/miniconda.html) are required to install Holocron.

### Latest stable release

You can install the last stable release of the package using [pypi](https://pypi.org/project/pylocron/) as follows:

```shell
pip install pylocron
```

or using [conda](https://anaconda.org/frgfm/pylocron):

```shell
conda install -c frgfm pylocron
```

### Developer mode

Alternatively, if you wish to use the latest features of the project that haven't made their way to a release yet, you can install the package from source *(install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) first)*:

```shell
git clone https://github.com/frgfm/Holocron.git
pip install -e Holocron/.
```


## Usage instructions

```python
from PIL import Image
from torchvision.transforms import Compose, ConvertImageDtype, Normalize, PILToTensor, Resize
from torchvision.transforms.functional import InterpolationMode
from holocron.models import model_from_hf_hub

model = model_from_hf_hub("frgfm/cspdarknet53").eval()

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
@article{DBLP:journals/corr/abs-1911-11929,
  author    = {Chien{-}Yao Wang and
               Hong{-}Yuan Mark Liao and
               I{-}Hau Yeh and
               Yueh{-}Hua Wu and
               Ping{-}Yang Chen and
               Jun{-}Wei Hsieh},
  title     = {CSPNet: {A} New Backbone that can Enhance Learning Capability of {CNN}},
  journal   = {CoRR},
  volume    = {abs/1911.11929},
  year      = {2019},
  url       = {http://arxiv.org/abs/1911.11929},
  eprinttype = {arXiv},
  eprint    = {1911.11929},
  timestamp = {Tue, 03 Dec 2019 20:41:07 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1911-11929.bib},
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
