---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---
**Spider-Verse Diffusion**

This is the fine-tuned Stable Diffusion model trained on movie stills from Sony's Into the Spider-Verse.
Use the tokens **_spiderverse style_** in your prompts for the effect.

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

model_id = "nitrosocke/spider-verse-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a magical princess with golden hair, spiderverse style"
image = pipe(prompt).images[0]

image.save("./magical_princess.png")
```

**Portraits rendered with the model:**
![Portrait Samples](https://huggingface.co/nitrosocke/spider-verse-diffusion/resolve/main/spiderverse-portraits-small.jpg)
**Sample images used for training:**
![Training Samples](https://huggingface.co/nitrosocke/spider-verse-diffusion/resolve/main/spiderverse-training-small.jpg)

This model was trained using the diffusers based dreambooth training and prior-preservation loss in 3.000 steps.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)