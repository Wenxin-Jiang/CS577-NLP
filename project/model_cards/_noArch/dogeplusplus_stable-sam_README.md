---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- sam-the-cat
widget:
- text: a photo of samruane cat
---

# sam

![](sam.png)

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dogeplusplus/stable-sam')
image = pipeline().images[0]
image
```
