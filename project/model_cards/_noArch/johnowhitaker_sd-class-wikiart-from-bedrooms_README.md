---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Example Fine-Tuned Model for Unit 2 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

This model is a diffusion model initialized from https://huggingface.co/google/ddpm-bedroom-256 and trained for 5000 steps on https://huggingface.co/datasets/huggan/wikiart.
Script: https://github.com/huggingface/diffusion-models-class/blob/main/unit2/finetune_model.py
Training Logs (with example images): https://wandb.ai/johnowhitaker/dm_finetune/runs/2upaa341

## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('johnowhitaker/sd-class-wikiart-from-bedrooms')
image = pipeline().images[0]
image
```
