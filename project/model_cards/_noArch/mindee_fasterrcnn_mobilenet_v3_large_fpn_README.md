---
license: apache-2.0
tags:
- object-detection
- pytorch
library_name: doctr
datasets:
- docartefacts
---


# Faster-RCNN model

Pretrained on [DocArtefacts](https://mindee.github.io/doctr/datasets.html#doctr.datasets.DocArtefacts). The Faster-RCNN architecture was introduced in [this paper](https://arxiv.org/pdf/1506.01497.pdf).


## Model description

The core idea of the author is to unify Region Proposal with the core detection module of Fast-RCNN.


## Installation

### Prerequisites

Python 3.6 (or higher) and [pip](https://pip.pypa.io/en/stable/) are required to install docTR.

### Latest stable release

You can install the last stable release of the package using [pypi](https://pypi.org/project/python-doctr/) as follows:

```shell
pip install python-doctr[torch]
```

### Developer mode

Alternatively, if you wish to use the latest features of the project that haven't made their way to a release yet, you can install the package from source *(install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) first)*:

```shell
git clone https://github.com/mindee/doctr.git
pip install -e doctr/.[torch]
```


## Usage instructions

```python
from PIL import Image
import torch
from torchvision.transforms import Compose, ConvertImageDtype, PILToTensor
from doctr.models.obj_detection.factory import from_hub

model = from_hub("mindee/fasterrcnn_mobilenet_v3_large_fpn").eval()

img = Image.open(path_to_an_image).convert("RGB")

# Preprocessing
transform = Compose([
    PILToTensor(),
    ConvertImageDtype(torch.float32),
])

input_tensor = transform(img).unsqueeze(0)

# Inference
with torch.inference_mode():
    output = model(input_tensor)
```


## Citation

Original paper

```bibtex
@article{DBLP:journals/corr/RenHG015,
  author    = {Shaoqing Ren and
               Kaiming He and
               Ross B. Girshick and
               Jian Sun},
  title     = {Faster {R-CNN:} Towards Real-Time Object Detection with Region Proposal
               Networks},
  journal   = {CoRR},
  volume    = {abs/1506.01497},
  year      = {2015},
  url       = {http://arxiv.org/abs/1506.01497},
  eprinttype = {arXiv},
  eprint    = {1506.01497},
  timestamp = {Mon, 13 Aug 2018 16:46:02 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/RenHG015.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

Source of this implementation

```bibtex
@misc{doctr2021,
    title={docTR: Document Text Recognition},
    author={Mindee},
    year={2021},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/mindee/doctr}}
}
```
