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
- text: >-
    Painting of vincentcat cat flying around the moon in the style of Leonardo
    Da Vinci
datasets:
- juancopi81/jcp-vincent-cat
---

# DreamBooth model for the vincentcat concept trained by juancopi81 on the juancopi81/jcp-vincent-cat dataset.

This is a Stable Diffusion model fine-tuned on the [vincentcat](https://huggingface.co/datasets/juancopi81/jcp-vincent-cat) concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of vincentcat cat**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `cat` images for the animal theme.


## Examples

---
Prompt: A painting of vincentcat cat in the style of Van Gogh
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_VG_final.jpeg">

---
Prompt: 
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_Cartoon_1.png">
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_Cartoon_2.png">

---
Prompt: painting of vincentcat cat as an anime warrior, trending on artstation pixiv makoto shinkai
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_7.jpg">

---
Prompt: A painting of vincentcat cat, acrylic palette knife
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_3.jpg">

---
Prompt: 
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_VG_2.png">

---
Prompt: Painting of vincentcat cat flying around the moon in the style of Leonardo Da Vinci
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_7.jpg">

---
Prompt: A photo of the Acropolis, and a portrair of vincentcat cat walking near the tower
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_6.jpg">

---
Prompt: A photo of the Eiffel Tower, a vincentcat cat is walking near the tower
<img src="https://huggingface.co/juancopi81/vincentcat-cat/resolve/main/Vincent_5.jpg">

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('juancopi81/vincentcat-cat')
image = pipeline().images[0]
image
```