---
language:
- en
tags:
- zero-shot-image-classification
license: mit
datasets:
- coco2017
---

# Tiny CLIP
## Introduction
This is a smaller version of CLIP trained for EN only. The training script can be found [here](https://www.kaggle.com/code/sachin/tiny-en-clip/). This model is roughly 8 times smaller than CLIP. This was achieved by using a small text model (`microsoft/xtremedistil-l6-h256-uncased`) and a small vision model (`edgenext_small`). For a in-depth guide of training CLIP see [this blog](https://sachinruk.github.io/blog/pytorch/pytorch%20lightning/loss%20function/gpu/2021/03/07/CLIP.html).

## Usage
For now this is the recommended way to use this model
```
git lfs install 
git clone https://huggingface.co/sachin/tiny_clip
cd tiny_clip
```
Once you are in the folder you could do the following:
```python
import models
text_encoder, tokenizer, vision_encoder, transform = models.get_model()
```