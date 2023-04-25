---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

# BG-VisualNovel-v03

A prototype project of generating Visual Novel backgrounds for game developers/artists. This model is intended to produce visual novel backgrounds with just a few prompts. Version 3 is based on Anything-V3.

* [Simple GUI Google Colab Demo here](https://colab.research.google.com/drive/1tR5e_EN9REJh0yr0T-dIyAIwiTMfNSxE?usp=sharing)

![](https://i.imgur.com/LF5UVuN.png)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "vinesmsuic/bg-visualnovel-v03"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a classroom"
image = pipe(prompt, height=512, width=512).images[0]
# ^ alternatively you can use for height=1920, width=1080 if you have enough CUDA memory
# make sure both height and width are divisible by 8
image.save("./classroom.png")

prompt = "a hospital building, two trees"
image = pipe(prompt, height=512, width=512).images[0]

image.save("./hospital.png")

prompt = "a street at night with nobody around"
image = pipe(prompt, height=512, width=512).images[0]

image.save("./nightstreet.png")
```

## Examples

a classroom
![](https://huggingface.co/vinesmsuic/bg-visualnovel-v03/resolve/main/_examples/classroom.png)

a hospital building, two trees
![](https://huggingface.co/vinesmsuic/bg-visualnovel-v03/resolve/main/_examples/hospital.png)

a street at night with nobody around
![](https://huggingface.co/vinesmsuic/bg-visualnovel-v03/resolve/main/_examples/nightstreet.png)


## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)