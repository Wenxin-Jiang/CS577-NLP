---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Example Fine-Tuned Model for Unit 2 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

celebhq fine-tuned on nelorth/oxford-flowers

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('nrsmac/ddpm-celebahq-finetuned-flowers-2epochs')
image = pipeline().images[0]
image
```
