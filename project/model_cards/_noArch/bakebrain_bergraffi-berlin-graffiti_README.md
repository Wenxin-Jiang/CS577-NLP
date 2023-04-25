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
- text: photo of bergraffi futuristic cyberpunk portrait painted by van gogh
---

# DreamBooth model for the bergraffi concept trained by bakebrain. 

This is a Stable Diffusion model fine-tuned on the bergraffi concept with DreamBooth. It can be used by modifying the `instance_prompt`: **photo of bergraffi futuristic cyberpunk portrait painted by van gogh**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on Berlin `graffiti` images.

#### Sample Images

150+ generated images can be found here: https://imgur.com/a/0Q00Rq7

<table>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_1.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_2.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_3.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_4.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_5.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_6.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_7.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_8.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_9.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_10.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_11.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_12.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_13.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_14.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_15.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_16.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_17.png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/bakebrain/bergraffi-berlin-graffiti/resolve/main/sample_images/bergraffi_sample_18.png" style="height:200px"> </td>
  </tr>
</table>


## Usage

Experiment with the guidance scale! Enjoy!

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('bakebrain/bergraffi-berlin-graffiti')
prompt = "photo of bergraffi futuristic cyberpunk portrait painted by van gogh"
guidance_scale = 12
image = pipeline(prompt, guidance_scale=guidance_scale).images[0]
image


```
