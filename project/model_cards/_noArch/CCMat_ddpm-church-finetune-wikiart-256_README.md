---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

This model is a diffusion model for unconditional image generation of churches ⛪️ finetuned on wikiart 🎨.<br>

Pretrained model : google/ddpm-church-256<br>
Dataset : huggan/wikiart<br>

## Usage

```python
from diffusers import DDPMPipeline

model_id = 'CCMat/ddpm-church-finetune-wikiart'

# load model and scheduler
pipeline = DDPMPipeline.from_pretrained(model_id)

# run pipeline in inference (sample random noise and denoise)
image = pipeline().images[0]

# save image
image.save("ddpm_church_wikiart.png")
```

## Samples
![example images](images/ddpm_church_wikiart_hf_0.png)
![example images](images/ddpm_church_wikiart_hf_3.png)
![example images](images/ddpm_church_wikiart_hf_7.png)
![example images](images/ddpm_church_wikiart_hf_8.png)
![example images](images/ddpm_church_wikiart_hf_9.png)
![example images](images/ddpm_church_wikiart_hf_10.png)
