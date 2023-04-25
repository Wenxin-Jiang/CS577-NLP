---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Example Fine-Tuned Model for Unit 2 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

Unit 2 Diffusion Models Class Fine-tuning

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('davidaponte/ddpm-finetuned-butterflies-2epochs')
image = pipeline().images[0]
image
```
