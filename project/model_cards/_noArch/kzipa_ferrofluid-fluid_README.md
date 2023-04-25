---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: ferrofluid fluid greets magnet, photorealistic, hd
---

# DreamBooth model for the ferrofluid concept trained by kzipa on the kzipa/ferrofluid dataset.

This is a Stable Diffusion model fine-tuned on the ferrofluid concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ferrofluid fluid**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `fluid` images for the science theme.


<img src="https://huggingface.co/kzipa/ferrofluid-fluid/resolve/main/prompt0_example1.png">
<p>ferrofluid fluid greets magnet, photorealistic, hd</p>
<img src="https://huggingface.co/kzipa/ferrofluid-fluid/resolve/main/prompt1_example0.png">
<p>ferrofluid fluid river, oil painting</p>
<img src="https://huggingface.co/kzipa/ferrofluid-fluid/resolve/main/prompt2_example0.png">
<p>a photo of a mouse covered by ferrofluid fluid</p>
<img src="https://huggingface.co/kzipa/ferrofluid-fluid/resolve/main/prompt3_example1.png">
<p>a photo of ferrofluid fluid on a top of Christmas tree</p>
<img src="https://huggingface.co/kzipa/ferrofluid-fluid/resolve/main/prompt4_example1.png">
<p>ferrofluid fluid and a cute magnet are kissing in the sunset, romantic</p>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('kzipa/ferrofluid-fluid')
image = pipeline().images[0]
image
```
