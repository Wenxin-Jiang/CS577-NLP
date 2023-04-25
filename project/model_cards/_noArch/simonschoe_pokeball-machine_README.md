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
- text: a pkblz ball in the middle of a miniature jungle
- text: a photo of a spectral ornate pkblz ball, trending on artstation, realistic
- text: a colored pencil sketch of a pkblz ball
---

# The Pokeball Machine

The **Pokeball Machine** is a Dreambooth model for the `pokeball` concept (represented by the `pkblz` identifier).
It applies to the *wildcard* theme.
It is fine-tuned from `CompVis/stable-diffusion-v1-4` checkpoint on a small dataset of pokeball images (i.e., images of the red-white original pokeball).
It can be used by modifying the `instance_prompt`: **a pkblz ball in the middle of a miniature jungle**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

#### Fine-Tuning Details

- Number of training images: 31
- Learning rate: 2e-06
- Training steps: 800
- Guidance Scale: 10
- Inference Steps: 50-75

#### Output Examples

<table>
  <tr>
    <td>a blueprint photo of a <b>pkblz</b> ball</td>
    <td>a photo of a cybernetic <b>pkblz</b> ball, wide shot</td>
    <td>a photo of a <b>pkblz</b> ball in the style vintage disney</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(1).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(2).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(3).png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a photo of a mosaic <b>pkblz</b> ball lying in an antique temple</td>
    <td>a photo of a detailed ornate <b>pkblz</b> ball</td>
    <td>a pkblz ball underwater</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(4).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(5).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(6).png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a <b>pkblz</b> ball in the middle of a miniature jungle</td>
    <td>a <b>pkblz</b> ball underwater</td>
    <td>a mystic <b>pkblz</b> ball, trending on artstation</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(7).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(8).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(9).png" style="height:200px"> </td>
  </tr>
    <tr>
    <td>a <b>pkblz</b> ball underwater, trending on artstation</td>
    <td>a wooden <b>pkblz</b> ball</td>
    <td>a <b>pkblz</b> ball hovering over a pond</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(10).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(11).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(12).png" style="height:200px"> </td>
  </tr>
    <tr>
    <td>a <b>pkblz</b> ball on a sunny tropical beach</td>
    <td>a steampunk <b>pkblz</b> ball, trending on artstation</td>
    <td>a colored pencil sketch of a <b>pkblz</b> ball</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(13).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(14).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(15).png" style="height:200px"> </td>
  </tr>
    <tr>
    <td>a photo of a spectral ornate <b>pkblz</b> ball, trending on artstation, realistic</td>
    <td>a sunset photo of a <b>pkblz</b> ball</td>
    <td>a watercolor photo of a <b>pkblz</b> ball</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(16).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(17).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/pokeball-machine/resolve/main/output/pokeball%20(18).png" style="height:200px"> </td>
  </tr>
</table>


## Usage

```python
from diffusers import StableDiffusionPipeline
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
pipeline = StableDiffusionPipeline.from_pretrained('simonschoe/pokeball-machine').to(device)

prompt = "a pkblz ball in the middle of a miniature jungle"

image = pipeline(
    prompt,
    num_inference_steps=50,
    guidance_scale=10,
    num_images_per_prompt=1
).images[0]

image
```
