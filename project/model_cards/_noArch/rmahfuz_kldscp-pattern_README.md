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
- text: a photo of kldscp pattern as a fruit salad
datasets:
- rmahfuz/kaleidoscope
---

# DreamBooth model for the kldscp concept trained by rmahfuz on the rmahfuz/kaleidoscope dataset.

This is a Stable Diffusion model fine-tuned on the kldscp concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of kldscp pattern**

Here are examples of some images generated with this fine-tuned model, along with the text prompts:

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/fruit_salad.png">
<p>kldscp pattern as a fruit salad, guidance: 11</p>

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/fruit_salad_30.png">
<p>kldscp pattern as a fruit salad, guidance: 30</p>

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/vegetable_salad_30.png">
<p>kldscp pattern as a vegetable salad, guidance: 30</p>

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/bouquet_20.png">
<p>kldscp pattern as a bouquet, guidance: 20</p>

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/starfish_shape_30.png">
<p>kldscp pattern in starfish shape, guidance: 30</p>

<img src="https://huggingface.co/rmahfuz/kldscp-pattern/resolve/main/black_night_sky_w_sparse_sparkling_white_stars_40.png">
<p>kldscp pattern as black night sky with sparse sparkling white stars, guidance: 40</p>


This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on kaleidoscope `pattern` images for the science theme.



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('rmahfuz/kldscp-pattern')
image = pipeline().images[0]
image
```