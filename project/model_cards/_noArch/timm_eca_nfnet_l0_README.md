---
tags:
- image-classification
- timm
- normalization-free
- efficient-channel-attention
license: apache-2.0
datasets:
- imagenet
library_tag: timm
---

# ECA-NFNet-L0

Pretrained model on [ImageNet](http://www.image-net.org/), this is a variant of the [NFNet (Normalization Free)](https://arxiv.org/abs/2102.06171) model family.

## Model description

This model variant was slimmed down from the original F0 variant in the paper for improved runtime characteristics (throughput, memory use) in PyTorch, on a GPU accelerator. It utilizes [Efficient Channel Attention (ECA)](https://arxiv.org/abs/1910.03151) instead of Squeeze-Excitation. It also features SiLU activations instead of the usual GELU.

Like other models in the NF family, this model contains no normalization layers (batch, group, etc). The models make use of [Weight Standardized](https://arxiv.org/abs/1903.10520) convolutions with additional scaling values in lieu of normalization layers. 

## Intended uses & limitations
You can use the raw model to classify images along the 1,000 ImageNet labels, but you can also change its head
to fine-tune it on a downstream task (another classification task with different labels, image segmentation or
object detection, to name a few).

### How to use
You can use this model with the usual factory method in [`timm`](https://github.com/rwightman/pytorch-image-models):
```python
import PIL
import timm
import torch

model = timm.create_model("hf_hub:timm/eca_nfnet_l0")

config = model.default_cfg
img_size = config["test_input_size"][-1] if "test_input_size" in config else config["input_size"][-1]
transform = timm.data.transforms_factory.transforms_imagenet_eval(
    img_size=img_size,
    interpolation=config["interpolation"],
    mean=config["mean"],
    std=config["std"],
    crop_pct=config["crop_pct"],
)

img = PIL.Image.open(path_to_an_image)
img = img.convert("RGB")
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
For stability during training it is highly recommended to train all NFNet variants with gradient clipping enabled. This model was trained with an Adaptive Gradient Clipping (AGC) factor of 0.015 as described in [the paper](https://arxiv.org/abs/2102.06171). Similar to the paper, a cosine learning rate decay was employed using SGD w/ nesterov. Moderate to heavy augmentation ([RandAugment](https://arxiv.org/abs/1909.13719)) and regularization (dropout, stochastic depth) is recommended for training.

### Preprocessing
The images are resized using bicubic interpolation to 288x288 and normalized with the usual ImageNet statistics.

## Evaluation results
This model has a top1-accuracy of 82.6% and a top-5 accuracy of 96.5% on the ImageNet evaluation set.

### BibTeX entry and citation info

NFNet model architecture:
```bibtex
@article{brock2021high,
  author={Andrew Brock and Soham De and Samuel L. Smith and Karen Simonyan},
  title={High-Performance Large-Scale Image Recognition Without Normalization},
  journal={arXiv preprint arXiv:2102.06171},
  year={2021}
}
```

L0 model variant & pretraining:
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
