---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
datasets: taesiri/Chrystus
widget:
- text: a photo of ccChrystus statue riding a horse
---

# DreamBooth model for the ccChrystus concept trained by taesiri on the taesiri/Chrystus dataset.

This is a Stable Diffusion model fine-tuned on the ccChrystus concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ccChrystus statue**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `statue` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('taesiri/Chrystus_w_Ogrojcu-statue')
image = pipeline().images[0]
image
```

## Sample Results


![Image alt text](result.png)

