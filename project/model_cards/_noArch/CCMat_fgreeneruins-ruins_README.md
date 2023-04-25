---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: high quality photo of Venice in fgreeneruins ruins
---

# DreamBooth model for the fgreeneruins concept trained on the CCMat/db-forest-ruins dataset.

This is a Stable Diffusion model fine-tuned on the fgreeneruins concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fgreeneruins ruins**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!


## Description

This is a Stable Diffusion model fine-tuned on `ruins` images for the landscape theme.<br>
Concept: **fgreeneruins** : forest ruins, greenery ruins<br>
Pretrained Model: [nitrosocke/elden-ring-diffusion](https://huggingface.co/nitrosocke/elden-ring-diffusion)<br>
Learning rate: 2e-6<br>


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fgreeneruins-ruins')
image = pipeline().images[0]
image
```

## Samples

Prompt: "high quality photo of Venice in fruins ruins"
![example images](images/9f06e8395facb2d518579af064601bd4.png)
<br>

Prompt: "high quality photo of Rome in fgreeneruins ruins with the Colosseum in the background"
![example images](images/2dc4a78a70200e3e2665a6908271322c.png)
<br>

Prompt: "fgreeneruins ruins in London near the Tower Bridge, professional photograph"
![example images](images/d53c0d463653d97f4927cdbf7a49df0e.png)
<br>

Prompt: "photo of Paris in fgreeneruins ruins, elden ring style"
![example images](images/68bb7c41163f286930f32df8c95a4a5a.png)

Prompt: "fgreeneruins ruins in Saint Petersburg, Sovietwave"
![example images](images/12125fc604869ef9e0166f3a8ecc130e.png)