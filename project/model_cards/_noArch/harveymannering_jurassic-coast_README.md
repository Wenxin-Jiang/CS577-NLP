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
- text: a photo of ioprt cliff with a dog
---

# DreamBooth Hackathon model for the Isle of Portland concept trained by harveymannering on the [jurassic-coast](https://huggingface.co/datasets/harveymannering/jurassic-coast) dataset.

The model was fine-tuned on the `cliff` prior for the landscape theme.  I used the [jurassic-coast](https://huggingface.co/datasets/harveymannering/jurassic-coast) dataset which contains 14 images of a particular cliff on the Isle of Portland on the south coast of England.

This is a Stable Diffusion model fine-tuned on the Isle of Portland (shortened to the rare token `ioprt`) concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of ioprt cliff**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!


## Examples

<table>
  <tr>
      <td><b>In the style of different artists</b>
<br>"a photo of ioprt cliff in the style of monet"</td>
        <td><br>"a photo of ioprt cliff in the style of raphael"</td>
  </tr>
  <tr>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52595583182/in/dateposted-public/" title="monet"><img src="https://live.staticflickr.com/65535/52595583182_2f3e1597a3.jpg" width="300" height="300" alt="monet"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
    </td>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52596072366/in/dateposted-public/" title="raphael"><img src="https://live.staticflickr.com/65535/52596072366_b3142a805d.jpg" width="300" height="300" alt="raphael"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>    </td>
  </tr>
  <tr>
    <td><b>Adding things to the environment</b><br>"a photo of ioprt cliff with a dog"</td>
      <td><br>"a photo of ioprt cliff with a boat"</td>
  </tr>
  <tr>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52596072406/in/dateposted-public/" title="dog"><img src="https://live.staticflickr.com/65535/52596072406_f90bdeae1b.jpg" width="300" height="300" alt="dog"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>    </td>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52595583222/in/dateposted-public/" title="boat"><img src="https://live.staticflickr.com/65535/52595583222_ed4159e458.jpg" width="300" height="300" alt="boat"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  </tr>
  <tr>
    <td><b>Making changes to the environment</b><br>"a photo of a sunset at ioprt cliff"</td>
      <td><br>"a photo of ioprt cliff in the desert"</td>
  </tr>
  <tr>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52596072351/in/dateposted-public/" title="sunset"><img src="https://live.staticflickr.com/65535/52596072351_2af35dfef9.jpg" width="300" height="300" alt="sunset"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>    </td>
    <td>
      <a data-flickr-embed="true" href="https://www.flickr.com/photos/197317911@N06/52596334474/in/dateposted-public/" title="desert"><img src="https://live.staticflickr.com/65535/52596334474_de30ac48fd.jpg" width="300" height="300" alt="desert"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  </tr>
</table>

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('harveymannering/jurassic-coast')
image = pipeline().images[0]
image
```
