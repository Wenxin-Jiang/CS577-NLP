---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---
### Archer Diffusion

This is the fine-tuned Stable Diffusion model trained on screenshots from the TV-show Archer.
Use the tokens **_archer style_** in your prompts for the effect.

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

model_id = "nitrosocke/archer-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a magical princess with golden hair, archer style"
image = pipe(prompt).images[0]

image.save("./magical_princess.png")
```

**Portraits rendered with the model:**
![Portrait Samples](https://huggingface.co/nitrosocke/archer-diffusion/resolve/main/archer-diffusion-samples.png)
**Celebrities rendered with the model:**
![Celebrities Samples](https://huggingface.co/nitrosocke/archer-diffusion/resolve/main/archer-diffusion-samples4s.png)
**Landscapes rendered with the model:**
![Landscape Samples](https://huggingface.co/nitrosocke/archer-diffusion/resolve/main/archer-diffusion-samples3.png)
**Animals rendered with the model:**
![Animal Samples](https://huggingface.co/nitrosocke/archer-diffusion/resolve/main/archer-diffusion-samples2.png)
**Sample images used for training:**
![Training Samples](https://huggingface.co/nitrosocke/archer-diffusion/resolve/main/archer-diffusion-dataset.png)

#### Prompt and settings for portraits:
**archer style beautiful portrait of ariana grande**
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 946707299, Size: 512x704_
#### Prompt and settings for landscapes:
**archer style suburban street night blue indoor lighting Negative prompt: grey cars**
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2915669764, Size: 1024x576_

This model was trained using the diffusers based dreambooth training and prior-preservation loss in 4.000 steps and using the _train-text-encoder_ feature.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)