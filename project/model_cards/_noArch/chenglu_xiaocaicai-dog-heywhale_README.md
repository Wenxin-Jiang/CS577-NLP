---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: illustration of a xiaocaicai dog sitting on top of the deck of a battle ship
    traveling through the open sea with a lot of ships surrounding it
---

# DreamBooth model for the xiaocaicai concept trained by chenglu.

This is a Stable Diffusion model fine-tuned on the xiaocaicai concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of xiaocaicai dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, 
corporated with the HeyWhale.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('chenglu/xiaocaicai-dog-heywhale')
image = pipeline().images[0]
image
```

## Some examples

Prompt: oil painting of a xiaocaicai dog wearing sunglasses by van gogh and by andy warhol

![](https://s3.amazonaws.com/moonup/production/uploads/1673711394333-63765e6b2361581ceb232cc8.jpeg)


![](https://s3.amazonaws.com/moonup/production/uploads/1673711484399-63765e6b2361581ceb232cc8.png)

Prompt: a black and white photograph of xiaocaicai dog wearing sunglasses by annie lebovitz, highly-detailed

![](https://s3.amazonaws.com/moonup/production/uploads/1673711740929-63765e6b2361581ceb232cc8.png)
