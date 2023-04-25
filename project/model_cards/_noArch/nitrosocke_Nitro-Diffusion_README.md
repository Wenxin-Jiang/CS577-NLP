---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/nitro-diff-samples-02.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers

---
### Nitro Diffusion

Welcome to Nitro Diffusion - the first Multi-Style Model trained from scratch! This is a fine-tuned Stable Diffusion model trained on three artstyles simultaniously while keeping each style separate from the others. This allows for high control of mixing, weighting and single style use.
Use the tokens **_archer style, arcane style or modern disney style_** in your prompts for the effect. You can also use more than one for a mixed style like in the examples down below:

**If you enjoy my work and want to test new models before release, please consider supporting me**
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

**Multi Style Characters from the model:**
![Multi Samples](https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/nitro-diff-samples-02.jpg)
**Single Style Characters from the model:**
![Single Samples](https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/nitro-diff-samples-01.jpg)
**Multi Style Scenes from the model:**
![Misc. Samples](https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/nitro-diff-samples-03.jpg)

**You can find animated GIFs of Batman and Lara Croft showing the weighting and prompt influence on the bottom of the page.**

#### Prompt and settings for Gal Gadot:
**arcane archer modern disney gal gadot**
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 598801516, Size: 512x768_

#### Prompt and settings for the Audi TT:
**(audi TT car) arcane modern disney style archer**
_Steps: 30, Sampler: Euler a, CFG scale: 7, Seed: 713702776, Size: 768x512_


## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Nitro-Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/nitrosocke/Nitro-Diffusion-Demo)


### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "nitrosocke/nitro-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "archer arcane style magical princess with golden hair"
image = pipe(prompt).images[0]

image.save("./magical_princess.png")
```


## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)


## Video Demos
# Batman
![Batman](https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/batman-demo-01.gif)
# Lara Croft
![Lara Croft](https://huggingface.co/nitrosocke/Nitro-Diffusion/resolve/main/laracroft-demo-01.gif)