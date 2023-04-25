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
widget:
- text: a photo of miffy rabbit (insert your choice of action)
---

# DreamBooth model for miffy the rabbit concept.

This is a Stable Diffusion model fine-tuned on the miffy concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of miffy rabbit**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `miffy the rabbit` images for the wildcard theme.

## Examples and Data

<table>
  <tr>
    <td>Fine-tuned on<br>"a photo of miffy by the campfire"</td>
    <td>Another prompt would be a<br>"psychedelic miffy rabbit by van gogh"</td>
  </tr>
 <tr>
    <td>
 <img src="https://i.imgur.com/9DnLluf.jpeg" style="height:200px"> 
    </td>
       <td>
 <img src="https://i.imgur.com/sA153Z5.jpeg" style="height:200px"> 
    </td>
 </tr>
</table>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Verne/miffy-rabbit')
image = pipeline().images[0]
image
```
