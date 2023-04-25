---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---
**Elden Ring Diffusion**

This is the fine-tuned Stable Diffusion model trained on the game art from Elden Ring.
Use the tokens **_elden ring style_** in your prompts for the effect.

You can download the latest version here: [eldenRing-v3-pruned.ckpt](https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/main/eldenRing-v3-pruned.ckpt)

**If you enjoy my work, please consider supporting me** 
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch

model_id = "nitrosocke/elden-ring-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a magical princess with golden hair, elden ring style"
image = pipe(prompt).images[0]

image.save("./magical_princess.png")
```

**Portraits rendered with the model:**
![Portrait Samples](https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/main/eldenring-portraits-small.jpg)
**Landscape Shots rendered with the model:**
![Landscape Samples](https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/main/eldenring-landscapes-small.jpg)
**Sample images used for training:**
![Training Samples](https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/main/eldenring-samples-small.jpg)

This model was trained using the diffusers based dreambooth training and prior-preservation loss in 3.000 steps.
#### Prompt and settings for portraits:
**elden ring style portrait of a beautiful woman highly detailed 8k elden ring style**
_Steps: 35, Sampler: DDIM, CFG scale: 7, Seed: 3289503259, Size: 512x704_
#### Prompt and settings for landscapes:
**elden ring style dark blue night (castle) on a cliff dark night (giant birds) elden ring style Negative prompt: bright day**
_Steps: 30, Sampler: DDIM, CFG scale: 7, Seed: 350813576, Size: 1024x576_

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)