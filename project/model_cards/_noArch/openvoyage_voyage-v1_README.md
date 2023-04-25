---
license: creativeml-openrail-m
tags:
- text-to-image
---
# Voyage: Let's explore unexplored sea of AI Art

## What is Voyage?

[Voyage](https://huggingface.co/openvoyage/voyage-v1) is basically a _text to image_ model developed by [Muhammadreza Haghiri](https://haghiri75.com/en) and it is based on weights from Stable Diffusion version 2.0 and Midjourney version 4. This model helps creative people turn their ideas to artwork for free (in any sense of the word _free_). 

## How to use voyage with `diffusers` lib

### Installing needed libraries

```
!pip install --upgrade git+https://github.com/huggingface/diffusers.git transformers scipy ftfy accelerate
```

### Importing required libraries, functions and classes

These following libraries, functions and classes used by me in order to test the model. Feel free to add more of your need or remove unnecessary ones!

```python
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler, DiffusionPipeline, DPMSolverMultistepScheduler
import torch
```

### Setting up the model and scheduler

In order to get results like what I got, you have to set `euler` scheduler up. This is how you can get it:

```python
model_id = "openvoyage/voyage-v1"

scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
```

but if you need DPMS scheduler, you can use this line as well:

```python
scheduler = DPMSolverMultistepScheduler.from_pretrained(model_id, subfolder="scheduler")
```

### Inference

```python
prompt = "ultra realistic illustration of a young beautiful woman, intricate, elegant, sharp focus, smooth edges"
negative_prompt = ""
prompt = f'<voyage> style {prompt}'
image = pipe(prompt=prompt, negative_prompt=negative_prompt, num_inference_steps=25, width=512, height=512, guidance_scale=10).images[0]
```

and in order to save your images, you can use `image.save()` method and have it in PNG format.

## Colab notebook

[This github repository](https://github.com/prp-e/voyage-colab) belongs to the responsible colab notebook of the model. 

## Samples

![figure 1](voyage-cyberpunk-2_out.png)
![figure 2](voyage-cyberpunk-3_out.png)
![figure 3](voyage-face-2_out.png)
![figure 4](voyage-face-4_out.png)