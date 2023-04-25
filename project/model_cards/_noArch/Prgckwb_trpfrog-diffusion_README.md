
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
datasets:
- TrpFrog/trpfrog-icons
widget:
- text: a photo of trpfrog 
---

# DreamBooth model for the trpfrog concept trained by Prgckwb on the TrpFrog/trpfrog-icons dataset.

This is a Stable Diffusion model fine-tuned on the trpfrog concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of trpfrog**
![](output3.png)

## Description
TrpFrog ([@Trpfrog](https://twitter.com/trpfrog?s=21&t=GcDGy74adYhOBYxX9HloOg)) is a famous Japanese Twitter comedian.

Below is a screenshot of the site he is creating.
![](trpfrog.png)

This is a fine-tuned model of Stable Diffusion with the powerful help of Dreambooth. 
The model is made specifically for TrpFrog and faithfully reproduces its appearance.



## Usage
First install the necessary packages.

```bash
pip install diffusers transformers accelerate scipy safetensors
```

The image can then be generated with the following script.

```python
import torch
from diffusers import StableDiffusionPipeline

keyword = "trpfrog"
prompt = f"a photo of {keyword}"

model_id = "Prgckwb/trpfrog-diffusion"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16
).to("cuda")

image = pipe(prompt).images[0]
image.save("trpfrog.jpg")
```

## Generated Images
**a photo of trpfrog in spring**
![](spring.png)

**a photo of trpfrog in summer**
![](summer.png)

**a photo of trpfrog in autumn**
![](autumn.png)

**a photo of trpfrog in winter**
![](winter.png)

**a photo of trpfrog on fire**
![](output.png)

**a photo of trpfrog growing shiitake mushrooms**
![](output2.png)