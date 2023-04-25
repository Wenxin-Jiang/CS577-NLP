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
- text: a photo of a ðŁĴŁ jellyfish in the snow
- text: a photo of a ðŁĴŁ jellyfish next to a dog
- text: a photo of a ðŁĴŁ jellyfish on top of a mountain
---

# Iridescent Jellyfish

**Iridescent Jellyfish** is a Dreambooth model for the `iridescent` jellyfish concept (represented by the `ðŁĴŁ` identifier).
It applies to the *animal* theme.
It is fine-tuned from `runwayml/stable-diffusion-v1-5` checkpoint on a small dataset of jellyfish images.
It can be used by modifying the `instance_prompt`: **a photo of a ðŁĴŁ jellyfish in the snow**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

#### Fine-Tuning Details

- Number of training images: 17
- Learning rate: 2e-06
- Training steps: 800
- Guidance Scale: 7
- Inference Steps: 50

#### Output Examples

<table>
  <tr>
    <td>a oil painting of a <b>ðŁĴŁ</b> jellyfish</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish next to a dog</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish in the snow</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(4).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(5).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(6).png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish on top of a mountain</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish in the sky</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(7).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(8).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(9).png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish skydiving</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish sutfing on a surfboard</td>
    <td>a photo of a choclate <b>ðŁĴŁ</b> jellyfish</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(10).jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(11).jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(12).jpg" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish shooting fireworks in the sky</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish on rollerblades</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish in a beer bottle</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(13).jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(14).jpg" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(15).jpg" style="height:200px"> </td>
  </tr>
  <tr>
    <td>a colorful sketch of a <b>ðŁĴŁ</b> jellyfish</td>
    <td>a photo of a <b>ðŁĴŁ</b> jellyfish in the jungle</td>
    <td>a mystic <b>ðŁĴŁ</b> jellyfish, trending on artstation</td>
  </tr>
  <tr>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(1).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(2).png" style="height:200px"> </td>
    <td align="center"><img src="https://huggingface.co/simonschoe/iridescent-jellyfish/resolve/main/output/jelly%20(3).png" style="height:200px"> </td>
  </tr>
</table>

## Usage

```python
from diffusers import StableDiffusionPipeline
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
pipeline = StableDiffusionPipeline.from_pretrained('simonschoe/iridescent-jellyfish').to(device)

prompt = "a photo of a ðŁĴŁ jellyfish in the snow"

image = pipeline(
    prompt,
    num_inference_steps=50,
    guidance_scale=7,
    num_images_per_prompt=1
).images[0]

image
```
