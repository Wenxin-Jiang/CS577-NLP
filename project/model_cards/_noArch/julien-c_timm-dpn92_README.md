---
tags:
- image-classification
- timm
- dpn
license: apache-2.0
datasets:
- imagenet
---

# `dpn92` from `rwightman/pytorch-image-models`

From [`rwightman/pytorch-image-models`](https://github.com/rwightman/pytorch-image-models):

```
""" PyTorch implementation of DualPathNetworks
Based on original MXNet implementation https://github.com/cypw/DPNs with
many ideas from another PyTorch implementation https://github.com/oyam/pytorch-DPNs.

This implementation is compatible with the pretrained weights from cypw's MXNet implementation.

Hacked together by / Copyright 2020 Ross Wightman
"""
```

## Model description

[Dual Path Networks](https://arxiv.org/abs/1707.01629)

## Intended uses & limitations

You can use the raw model to classify images along the 1,000 ImageNet labels, but you can also change its head
to fine-tune it on a downstream task (another classification task with different labels, image segmentation or
object detection, to name a few).

### How to use

You can use this model with the usual factory method in `timm`:

```python
import PIL
import timm
import torch

model = timm.create_model("julien-c/timm-dpn92")
img = PIL.Image.open(path_to_an_image)
img = img.convert("RGB")

config = model.default_cfg

if isinstance(config["input_size"], tuple):
    img_size = config["input_size"][-2:]
else:
    img_size = config["input_size"]

transform = timm.data.transforms_factory.transforms_imagenet_eval(
    img_size=img_size,
    interpolation=config["interpolation"],
    mean=config["mean"],
    std=config["std"],
)

input_tensor = transform(cat_img)
input_tensor = input_tensor.unsqueeze(0)
# ^ batch size = 1
with torch.no_grad():
    output = model(input_tensor)

probs = output.squeeze(0).softmax(dim=0)
```

### Limitations and bias

The training images in the dataset are usually photos clearly representing one of the 1,000 labels. The model will
probably not generalize well on drawings or images containing multiple objects with different labels.

The training images in the dataset come mostly from the US (45.4%) and Great Britain (7.6%). As such the model or
models created by fine-tuning this model will work better on images picturing scenes from these countries (see 
[this paper](https://arxiv.org/abs/1906.02659) for examples).

More generally, [recent research](https://arxiv.org/abs/2010.15052) has shown that even models trained in an
unsupervised fashion on ImageNet (i.e. without using the labels) will pick up racial and gender bias represented in
the training images.

## Training data

This model was pretrained on [ImageNet](http://www.image-net.org/), a dataset consisting of 14 millions of
hand-annotated images with 1,000 categories.

## Training procedure

To be completed

### Preprocessing

To be completed

## Evaluation results

To be completed

### BibTeX entry and citation info

```bibtex
@misc{rw2019timm,
  author = {Ross Wightman},
  title = {PyTorch Image Models},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  doi = {10.5281/zenodo.4414861},
  howpublished = {\url{https://github.com/rwightman/pytorch-image-models}}
}
```

and

```bibtex
@misc{chen2017dual,
      title={Dual Path Networks}, 
      author={Yunpeng Chen and Jianan Li and Huaxin Xiao and Xiaojie Jin and Shuicheng Yan and Jiashi Feng},
      year={2017},
      eprint={1707.01629},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```