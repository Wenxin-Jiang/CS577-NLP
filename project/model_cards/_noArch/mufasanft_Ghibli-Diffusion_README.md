---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/nitrosocke/Ghibli-Diffusion/resolve/main/images/ghibli-diffusion-thumbnail.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers

---
### Ghibli Diffusion

This is the fine-tuned Stable Diffusion model trained on images from modern anime feature films from Studio Ghibli.
Use the tokens **_ghibli style_** in your prompts for the effect.

**If you enjoy my work and want to test new models before release, please consider supporting me**
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

**Characters rendered with the model:**
![Characters Samples](https://huggingface.co/nitrosocke/Ghibli-Diffusion/resolve/main/images/ghibli-diffusion-samples-01s.jpg)
**Cars and Animals rendered with the model:**
![Misc. Samples](https://huggingface.co/nitrosocke/Ghibli-Diffusion/resolve/main/images/ghibli-diffusion-samples-02s.jpg)
**Landscapes rendered with the model:**
![Landscape 1](https://huggingface.co/nitrosocke/Ghibli-Diffusion/resolve/main/images/ghibli-diffusion-samples-03s.jpg)
_ghibli style beautiful Caribbean beach tropical (sunset) - Negative prompt: soft blurry_
![Landscape 2](https://huggingface.co/nitrosocke/Ghibli-Diffusion/resolve/main/images/ghibli-diffusion-samples-04s.jpg)
_ghibli style ice field white mountains ((northern lights)) starry sky low horizon - Negative prompt: soft blurry_

#### Prompt and settings for the Strom Trooper:
**ghibli style (storm trooper) Negative prompt: (bad anatomy)**
_Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3450349066, Size: 512x704_

#### Prompt and settings for the VW Beetle:
**ghibli style VW beetle Negative prompt: soft blurry**
_Steps: 30, Sampler: Euler a, CFG scale: 7, Seed: 1529856912, Size: 704x512_

This model was trained using the diffusers based dreambooth training by ShivamShrirao using prior-preservation loss and the _train-text-encoder_ flag in 15.000 steps.

<!-- ### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI run redshift-diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/nitrosocke/Ghibli-Diffusion-Demo)-->

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "nitrosocke/Ghibli-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "ghibli style magical princess with golden hair"
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