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
- text: 3d diagram of the solar system in the style of pprotein
---

# DreamBooth model for the pprotein concept trained by jonathang on the jonathang/dreambooth-hackathon-images-protein3 dataset.

This is a Stable Diffusion model fine-tuned on the pprotein concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a 3d model of pprotein**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Examples

<table>
  <tr>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Kandinsky"</td>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Van Gogh"</td>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Warhol"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/lhDA041.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/iug4k7D.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/eIMiTVG.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Leonardo da Vinci"</td>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Frida Kahlo"</td>
    <td>Generated Image of "a 3d diagram of pprotein in the style of "<br>"Salvador Dahli"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/hzKGWC2.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/loc8rLa.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/8nK81TA.png" style="height:200px"> </td>
  </tr>
  <tr>
    <td>Generated Image of "Tree in the style of"<br>"3d diagram of pprotein"</td>
    <td>Generated Image of "Soda Can in the style of"<br>"3d diagram of pprotein"</td>
    <td>Generated Image of "Vase in the style of"<br>"3d diagram of pprotein"</td>
  </tr>
  <tr>
    <td align="center"><img src="https://imgur.com/czOlY11.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/uhwueGs.png" style="height:200px"> </td>
    <td align="center"><img src="https://imgur.com/gSIrHAh.png" style="height:200px"> </td>
  </tr>
</table>

    
## Description


This is a Stable Diffusion model fine-tuned on `thing` images for the science theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jonathang/pprotein-thing')
image = pipeline().images[0]
image
```
