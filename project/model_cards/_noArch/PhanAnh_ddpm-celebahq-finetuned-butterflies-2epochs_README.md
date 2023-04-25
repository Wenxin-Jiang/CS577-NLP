---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Example Fine-Tuned Model for Unit 2 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

fine-tune a pretrained model on face to butterfly 

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('PhanAnh/ddpm-celebahq-finetuned-butterflies-2epochs')
image = pipeline().images[0]
image
```
