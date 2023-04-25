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
widget:
- text: "masterpiece, best quality, 1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden"
  example_title: "example 1girl"
- text: "masterpiece, best quality, 1boy, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden"
  example_title: "example 1boy"
---

# ACertainty

ACertainty is a carefully designed model that is well-suited for further fine-tuning and training for use in dreambooth. It is easier to train than other anime-style Stable Diffusion models, and is less biased and more balanced for further development. This model is less likely to be biased by laion-aesthetic preferences, brought by Stable-Diffusion-v1-4+.

This is not the base of ACertainModel, but you can use this model as your new base to train your new dreambooth model about a couple themes or charactors or styles.

e.g. **_masterpiece, best quality, 1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden_** 

## About online preview with Hosted inference API, also generation with this model

Parameters are not allowed to be modified, as it seems that it is generated with *Clip skip: 1*, for better performance, it is strongly recommended to use *Clip skip: 2* instead.

Here is an example of inference settings, if it is applicable with you on your own server: *Steps: 28, Sampler: Euler a, CFG scale: 11, Clip skip: 2*.

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or FLAX/JAX.

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "JosephusCheung/ACertainty"
branch_name= "main"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision=branch_name, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pikachu"
image = pipe(prompt).images[0]

image.save("./pikachu.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Is it a NovelAI based model? What is the relationship with SD1.2 and SD1.4?

See [ASimilarityCalculatior](https://huggingface.co/JosephusCheung/ASimilarityCalculatior)