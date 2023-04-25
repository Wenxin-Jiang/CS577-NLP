---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- text-to-image
- dreambooth-hackathon
- animal
widget:
- text: A photo of vishu cat
---

# Dreambooth Model for Animals trained on a custom dataset.
This is a Stable Diffusion model fine-tuned on the animal concept with DreamBooth. It can be used by modifying the `instance_prompt`: **A photo of vishu cat**

This model was created as part of the DreamBooth Hackathon 🔥.

## Description


Model finetuned on the pictures of our cat named Vishu, made for the Dreambooth Hackathon,
finetuned on Stable diffusion 2.1 Base


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Apocalypse-19/Vishu-the-Cat')
image = pipeline().images[0]
image
```


## Examples

Some examples of images generated with their prompts are (Guidance scale = 7.5 and Number of Inference steps = 50 for all):

Prompt = A photo of vishu cat as a genshin impact character
![a photo of vishu cat as a genshin impact character, high res, infstep=50, gs=7.5.png](https://s3.amazonaws.com/moonup/production/uploads/1673376172445-6366451164bcbbd03e2fcd19.png)

Prompt = A photo of vishu cat shaking hands with Donald Trump
![a photo of vishu cat shaking hands with Donald Trump, infstep=50, gs=7.5, no neg prompts.png](https://s3.amazonaws.com/moonup/production/uploads/1673376265681-6366451164bcbbd03e2fcd19.png)

Prompt = A photo of vishu cat as a Disney Princess
![vishu cat as a disney princess, infstep=50, gs=7.5, seed=1024.png](https://s3.amazonaws.com/moonup/production/uploads/1673376287080-6366451164bcbbd03e2fcd19.png)

Prompt = A photo of vishu cat cocking a gun
![a photo of vishu cat cocking a gun, infstep=50, gs=7.5, seed=1024.png](https://s3.amazonaws.com/moonup/production/uploads/1673376294767-6366451164bcbbd03e2fcd19.png)