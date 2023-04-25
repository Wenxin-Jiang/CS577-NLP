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
- text: a photo of terrier dog swimming in the pool
---

# DreamBooth model for the terrier concept trained by bobber on the bobber/Terrier-images dataset.

This is a Stable Diffusion model fine-tuned on the terrier concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of terrier dog**

This model was created as part of the DreamBooth Hackathon 🔥. My daughter helped me selecting 18 images about Terriers from petfind. Hope you enjoy it. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Examples

<table>
  <tr>
    <td>Generated Image of "a photo of terrier dog <br>in space suit walking in the mars"</td>
    <td>Generated Image of "a photo of terrier dog <br>in the background of chinese new year"</td>
    <td>Generated Image of "a photo of terrier dog <br>swimming in the pool"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://i.imgur.com/YW483rm.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://i.imgur.com/4m5Fv86.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://i.imgur.com/ZCdapRU.jpg" style="height:200px"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a photo of terrier dog <br>walking in Paris by Van Gogh"</td>
    <td>Generated Image of "a photo of terrier dog <br>with The Great Wave by Katsushika Hokusai"</td>
    <td>Generated Image of "a photo of terrier dog <br>by Leonardo da Vinci"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://i.imgur.com/uzYLctu.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://i.imgur.com/9wxxyD4.jpg" style="height:200px"> </td>
    <td align="center"><img src="https://i.imgur.com/xufDxxD.jpg" style="height:200px"> </td>
  </tr>
</table>


## Description


This is a Stable Diffusion model fine-tuned on 18 Terrier `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('bobber/terrier-dog')
image = pipeline().images[0]
image
```
