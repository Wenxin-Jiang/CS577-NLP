---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

This model is a diffusion model for unconditional image generation of [Bored Apes](https://opensea.io/collection/boredapeyachtclub).

## Example
![example.png](https://s3.amazonaws.com/moonup/production/uploads/1670089095011-630283a6b002e9a4a216f3e4.png)

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('daspartho/bored-ape-diffusion')
image = pipeline().images[0]
image
```

## Training
The model is trained on [this dataset](https://huggingface.co/datasets/daspartho/bored-ape) of 10000 Bored Ape images.

[Notebook](https://github.com/daspartho/bored-ape-diffusion/blob/main/main.ipynb) for training the model is available on GitHub repo.