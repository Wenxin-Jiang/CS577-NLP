---
thumbnail: "https://huggingface.co/ID56/FF-Vision-CIFAR/resolve/main/assets/cover_image.png"
license: cc-by-sa-4.0
tags:
- image-classification
datasets:
- cifar10
metrics:
- accuracy
inference: false
---

# CIFAR-10 Upside Down Classifier

For the Fatima Fellowship 2022 Coding Challenge, DL for Vision track.

<a href="https://wandb.ai/dealer56/cifar-updown-classifier/reports/CIFAR-10-Upside-Down-Classifier-Fatima-Fellowship-2022-Coding-Challenge-Vision---VmlldzoxODA2MDE4" target="_parent"><img src="https://img.shields.io/badge/weights-%26biases-ffcf40" alt="W&B Report"/></a> 

<img src="https://huggingface.co/ID56/FF-Vision-CIFAR/resolve/main/assets/cover_image.png" alt="Cover Image" width="800"/>

## Usage

### Model Definition

```python
from torch import nn
import timm
from huggingface_hub import PyTorchModelHubMixin


class UpDownEfficientNetB0(nn.Module, PyTorchModelHubMixin):
    """A simple Hub Mixin wrapper for timm EfficientNet-B0. Used to classify whether an image is upright or flipped down, on CIFAR-10."""

    def __init__(self, **kwargs):
        super().__init__()
        self.base_model = timm.create_model('efficientnet_b0', num_classes=1, drop_rate=0.2, drop_path_rate=0.2)
        self.config = kwargs.pop("config", None)

    def forward(self, input):
        return self.base_model(input)
```
### Loading the Model from Hub

```python
net = UpDownEfficientNetB0.from_pretrained("ID56/FF-Vision-CIFAR")
```

### Running Inference

```python
from torchvision import transforms

CIFAR_MEAN = (0.4914, 0.4822, 0.4465)
CIFAR_STD = (0.247, 0.243, 0.261)

transform = transforms.Compose([
    transforms.Resize(40, 40),
    transforms.ToTensor(),
    transforms.Normalize(CIFAR_MEAN, CIFAR_STD)
])

image = load_some_image()  # Load some PIL Image or uint8 HWC image array
image = transform(image)   # Convert to CHW image tensor
image = image.unsqueeze(0) # Add batch dimension

net.eval()

pred = net(image)
```