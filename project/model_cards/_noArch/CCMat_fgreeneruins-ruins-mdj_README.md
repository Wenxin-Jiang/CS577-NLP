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
- text: a photo of fgreeneruins ruins in Paris in front of the Arc de triomphe, mdjrny-v4
    style
---

# DreamBooth model for the fgreeneruins concept trained on the CCMat/db-forest-ruins dataset.

This is a Stable Diffusion model fine-tuned on the fgreeneruins concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fgreeneruins ruins**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `ruins` images for the landscape theme.<br>
Concept: **fgreeneruins** : forest ruins, greenery ruins<br>
Pretrained Model: [prompthero/openjourney](https://huggingface.co/prompthero/openjourney)<br>
Learning rate: 2e-6<br>


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fgreeneruins-ruins-mdj')
image = pipeline().images[0]
image
```

## Samples

Prompt: "high quality photo of Venice in fgreeneruins ruins, HDR, UHD, 64K"
![example images](images/416f43963ab43a43541c737a4fe7210c.png)
<br>

Prompt: "Fallout concept of fgreeneruins ruins in underwater city, unreal engine 5"
![example images](images/11c0880ae973031f5d6180519e14b5a0.png)
<br>

Prompt: "New York City in fgreeneruins ruins with the Empire State Building in the background by Alejandro Bursido"
![example images](images/adad061f7c53713c1811d902bb22497e.png)
<br>

Prompt: "Manhattan in fgreeneruins ruins by Makoto Shinkai"
![example images](images/f83246cd3df6221dbf4ef29e73cecbf7.png)
<br>

Prompt: "The Taj Mahal in fgreeneruins ruins, professional photograph"
![example images](images/172f9a41e691aeec772d8f03be2c64ce.png)
