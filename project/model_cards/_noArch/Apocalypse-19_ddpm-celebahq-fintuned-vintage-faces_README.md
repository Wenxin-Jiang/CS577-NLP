---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---


The celebhq model finetuned on vintage faces for face generation

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('Apocalypse-19/ddpm-celebahq-fintuned-vintage-faces')
image = pipeline().images[0]
image
```
