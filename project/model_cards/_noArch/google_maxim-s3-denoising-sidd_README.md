---
license: apache-2.0
library_name: keras
language: en
tags:
- vision
- maxim
- image-to-image
datasets:
- sidd
---

# MAXIM pre-trained on SIDD for image denoising 

MAXIM model pre-trained for image denoising. It was introduced in the paper [MAXIM: Multi-Axis MLP for Image Processing](https://arxiv.org/abs/2201.02973) by Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan Bovik, Yinxiao Li and first released in [this repository](https://github.com/google-research/maxim). 

Disclaimer: The team releasing MAXIM did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

MAXIM introduces a shared MLP-based backbone for different image processing tasks such as image deblurring, deraining, denoising, dehazing, low-light image enhancement, and retouching. The following figure depicts the main components of MAXIM:

![](https://github.com/google-research/maxim/raw/main/maxim/images/overview.png)

## Training procedure and results

The authors didn't release the training code. For more details on how the model was trained, refer to the [original paper](https://arxiv.org/abs/2201.02973). 

As per the [table](https://github.com/google-research/maxim#results-and-pre-trained-models), the model achieves a PSNR of 39.96 and an SSIM of 0.96. 

## Intended uses & limitations

You can use the raw model for image denoising tasks. 

The model is [officially released in JAX](https://github.com/google-research/maxim). It was ported to TensorFlow in [this repository](https://github.com/sayakpaul/maxim-tf). 

### How to use

Here is how to use this model:

```python
from huggingface_hub import from_pretrained_keras
from PIL import Image

import tensorflow as tf
import numpy as np
import requests

url = "https://github.com/sayakpaul/maxim-tf/raw/main/images/Denoising/input/0011_23.png"
image = Image.open(requests.get(url, stream=True).raw)
image = np.array(image)
image = tf.convert_to_tensor(image)
image = tf.image.resize(image, (256, 256))

model = from_pretrained_keras("google/maxim-s3-denoising-sidd")
predictions = model.predict(tf.expand_dims(image, 0))
```

For a more elaborate prediction pipeline, refer to [this Colab Notebook](https://colab.research.google.com/github/sayakpaul/maxim-tf/blob/main/notebooks/inference-dynamic-resize.ipynb). 

### Citation

```bibtex
@article{tu2022maxim,
  title={MAXIM: Multi-Axis MLP for Image Processing},
  author={Tu, Zhengzhong and Talebi, Hossein and Zhang, Han and Yang, Feng and Milanfar, Peyman and Bovik, Alan and Li, Yinxiao},
  journal={CVPR},
  year={2022},
}
```