---
license: other
tags:
- vision
- image-segmentation
datasets:
- pascal-voc
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
---

# MobileViT + DeepLabV3 (small-sized model)

MobileViT model pre-trained on PASCAL VOC at resolution 512x512. It was introduced in [MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer](https://arxiv.org/abs/2110.02178) by Sachin Mehta and Mohammad Rastegari, and first released in [this repository](https://github.com/apple/ml-cvnets). The license used is [Apple sample code license](https://github.com/apple/ml-cvnets/blob/main/LICENSE).

Disclaimer: The team releasing MobileViT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

MobileViT is a light-weight, low latency convolutional neural network that combines MobileNetV2-style layers with a new block that replaces local processing in convolutions with global processing using transformers. As with ViT (Vision Transformer), the image data is converted into flattened patches before it is processed by the transformer layers. Afterwards, however, the patches are "unflattened" back into feature maps. This allows the MobileViT-block to be placed anywhere inside a CNN. MobileViT does not require any positional embeddings.

The model in this repo adds a [DeepLabV3](https://arxiv.org/abs/1706.05587) head to the MobileViT backbone for semantic segmentation.

## Intended uses & limitations

You can use the raw model for semantic segmentation. See the [model hub](https://huggingface.co/models?search=mobilevit) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model:

```python
from transformers import MobileViTFeatureExtractor, MobileViTForSemanticSegmentation
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = MobileViTFeatureExtractor.from_pretrained('Matthijs/deeplabv3-mobilevit-small')
model = MobileViTForSemanticSegmentation.from_pretrained('Matthijs/deeplabv3-mobilevit-small')

inputs = feature_extractor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits
predicted_mask = logits.argmax(1).squeeze(0)
```

Currently, both the feature extractor and model support PyTorch.

## Training data

The MobileViT + DeepLabV3 model was pretrained on [ImageNet-1k](https://huggingface.co/datasets/imagenet-1k), a dataset consisting of 1 million images and 1,000 classes, and then fine-tuned on the [PASCAL VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/) dataset.

## Training procedure

### Preprocessing

At inference time, images are center-cropped at 512x512. Pixels are normalized to the range [0, 1]. Images are expected to be in BGR pixel order, not RGB.

### Pretraining

The MobileViT networks are trained from scratch for 300 epochs on ImageNet-1k on 8 NVIDIA GPUs with an effective batch size of 1024 and learning rate warmup for 3k steps, followed by cosine annealing. Also used were label smoothing cross-entropy loss and L2 weight decay. Training resolution varies from 160x160 to 320x320, using multi-scale sampling.

To obtain the DeepLabV3 model, MobileViT was fine-tuned on the PASCAL VOC dataset using 4 NVIDIA A100 GPUs.

## Evaluation results

| Model            | PASCAL VOC mIOU | # params  | URL                                                          |
|------------------|-----------------|-----------|--------------------------------------------------------------|
| MobileViT-XXS    | 73.6            | 1.9 M     | https://huggingface.co/Matthijs/deeplabv3-mobilevit-xx-small |
| MobileViT-XS     | 77.1            | 2.9 M     | https://huggingface.co/Matthijs/deeplabv3-mobilevit-x-small  |
| **MobileViT-S**  | **79.1**        | **6.4 M** | https://huggingface.co/Matthijs/deeplabv3-mobilevit-small    |

### BibTeX entry and citation info

```bibtex
@inproceedings{vision-transformer,
title = {MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer},
author = {Sachin Mehta and Mohammad Rastegari},
year = {2022},
URL = {https://arxiv.org/abs/2110.02178}
}
```
