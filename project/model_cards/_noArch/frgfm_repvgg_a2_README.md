---
license: apache-2.0
tags:
- image-classification
- pytorch
- onnx
datasets:
- frgfm/imagenette
---


# RepVGG-A2 model

Pretrained on [ImageNette](https://github.com/fastai/imagenette). The RepVGG architecture was introduced in [this paper](https://arxiv.org/pdf/2101.03697.pdf).


## Model description

The core idea of the author is to distinguish the training architecture (with shortcut connections), from the inference one (a pure highway network). By designing the residual block, the training architecture can be reparametrized into a simple sequence of convolutions and non-linear activations.


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

model = model_from_hf_hub("frgfm/repvgg_a2").eval()

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
@article{DBLP:journals/corr/abs-2101-03697,
  author    = {Xiaohan Ding and
               Xiangyu Zhang and
               Ningning Ma and
               Jungong Han and
               Guiguang Ding and
               Jian Sun},
  title     = {RepVGG: Making VGG-style ConvNets Great Again},
  journal   = {CoRR},
  volume    = {abs/2101.03697},
  year      = {2021},
  url       = {https://arxiv.org/abs/2101.03697},
  eprinttype = {arXiv},
  eprint    = {2101.03697},
  timestamp = {Tue, 09 Feb 2021 15:29:34 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2101-03697.bib},
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
