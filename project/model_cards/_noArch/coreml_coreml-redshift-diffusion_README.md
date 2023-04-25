---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---

# Core ML Converted Model

This model was converted to Core ML for use on Apple Silicon devices by following Apple's instructions [here](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).<br>
Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>

`split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
`original` version is only compatible with CPU & GPU option.

### Redshift Diffusion

This is the fine-tuned Stable Diffusion model trained on high resolution 3D artworks.
Use the tokens **_redshift style_** in your prompts for the effect.

**The name:** I used Cinema4D for a very long time as my go-to modeling software and always liked the redshift render it came with. That is why I was very sad to see the bad results base SD has connected with its token. This is my attempt at fixing that and showing my passion for this render engine.

**If you enjoy my work and want to test new models before release, please consider supporting me**
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

**Characters rendered with the model:**
![Videogame Samples](https://huggingface.co/nitrosocke/redshift-diffusion/resolve/main/images/redshift-diffusion-samples-01s.jpg)
**Cars and Landscapes rendered with the model:**
![Misc. Samples](https://huggingface.co/nitrosocke/redshift-diffusion/resolve/main/images/redshift-diffusion-samples-02s.jpg)

#### Prompt and settings for Tony Stark:
**(redshift style) robert downey jr as ironman Negative prompt: glasses helmet**
_Steps: 40, Sampler: DPM2 Karras, CFG scale: 7, Seed: 908018284, Size: 512x704_

#### Prompt and settings for the Ford Mustang:
**redshift style Ford Mustang**
_Steps: 20, Sampler: DPM2 Karras, CFG scale: 7, Seed: 579593863, Size: 704x512_

This model was trained using the diffusers based dreambooth training by ShivamShrirao using prior-preservation loss and the _train-text-encoder_ flag in 11.000 steps.

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI run redshift-diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/nitrosocke/Redshift-Diffusion-Demo)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "nitrosocke/redshift-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "redshift style magical princess with golden hair"
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