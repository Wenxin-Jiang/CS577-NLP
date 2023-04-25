---
tags:
  - fastai
  - resnet
  - computer-vision
  - classification
  - image-classification
  - binary-classification
license:
  - cc0-1.0
---

# Resnet34 Pokemon Card Classifier

## Model Description

This is a resnet34 model fine-tuned with fastai to [classify real and fake Pokemon cards (dataset)](https://www.kaggle.com/datasets/ongshujian/real-and-fake-pokemon-cards).

Here is a colab notebook that shows how the model was trained and pushed to the hub: [link](https://github.com/mindwrapped/pokemon-card-checker/blob/main/pokemon_card_checker.ipynb).

## Intended uses & limitation

This model is trained to identify real vs fake cards based on the backs of the cards, not the front.

## How to use

```python
from huggingface_hub import from_pretrained_fastai

# Pull model from hub
learn = from_pretrained_fastai('hugginglearners/pokemon-card-checker')

# Get prediction for this image
pred_label, _, scores = learn.predict(img)
```

## Training data

Dataset located here: [link](https://www.kaggle.com/datasets/ongshujian/real-and-fake-pokemon-cards).
