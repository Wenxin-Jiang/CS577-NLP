---
license: openrail++
tags:
  - text-to-image
  - stable-diffusion
widget:
  - text: "pbr brick wall"
    example_title: "Brick Wall"
  - text: "pbr cobblestone path"
    example_title: "Cobblestone Path"
---

# Texture Diffusion
This DreamBooth model is fine-tuned for diffuse textures. It produces flat textures with very little visible lighting/shadows.

## Samples
Here are a few example images (generated with 50 steps).

| pbr uneven stone wall | pbr dirt with weeds | pbr bright white marble |
| --- | --- | --- |
| ![](samples/pbr%20uneven%20stone%20wall.png) | ![](samples/pbr%20dirt%20with%20weeds.png) | ![](samples/pbr%20bright%20white%20marble.png) |

## Usage
Use the token `pbr` in your prompts to invoke the style.

This model was made for use in [Dream Textures](https://github.com/carson-katri/dream-textures), a Stable Diffusion add-on for Blender.

You can also use it with [🧨 diffusers](https://github.com/huggingface/diffusers):

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "dream-textures/texture-diffusion"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pbr brick wall"
image = pipe(prompt).images[0]  
    
image.save("bricks.png")
```

## Training Details

* Base Model: [stabilityai/stable-diffusion-2-base](https://huggingface.co/stabilityai/stable-diffusion-2-base)
* Resolution: `512`
* Prior Loss Weight: `1.0`
* Class Prompt: `texture`
* Batch Size: `1`
* Learning Rate: `1e-6`
* Precision: `fp16`
* Steps: `4000`
* GPU: Tesla T4

### Dataset
This model was trained on 278 CC0 textures from [PolyHaven](https://polyhaven.com/).