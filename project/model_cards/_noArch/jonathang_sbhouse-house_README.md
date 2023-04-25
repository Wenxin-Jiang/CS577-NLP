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
- text: a photo of sbhouse house in the style of Dr Seuss
---

# Examples

<table>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Lenoardo da Vinci"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/eaxs6By.png" style="width: 100%;"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Picasso"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/VdYaDxD.png" style="width: 100%"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Van Gogh"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/gsI79PI.png" style="width: 100%"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Disney"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/v4hS450.png" style="width: 100%"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Dr Seuss"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/9uGCOa6.png" style="width: 100%"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of sbhouse house in the style of "<br>"Salvador Dali"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/3X2DSox.png" style="width: 100%"> </td>
  </tr>
</table>

# DreamBooth model for the sbhouse concept trained by jonathang on the jonathang/dreambooth-hackathon-images-sbob-jpeg dataset.

This is a Stable Diffusion model fine-tuned on the sbhouse concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of sbhouse house**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `house` images for the landscape theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jonathang/sbhouse-house')
image = pipeline().images[0]
image
```
