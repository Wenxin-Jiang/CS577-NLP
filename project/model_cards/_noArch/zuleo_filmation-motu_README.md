---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- image-to-image
- art
- artistic
- diffusers
- filmation
---

# Filmation MOTU Diffusion


Fine-tuned Stable Diffusion model, based of ```SD 1.5```, trained with art from Masters of the Universe.

![Detailed Samples](https://huggingface.co/zuleo/filmation-motu/resolve/main/booth1.png)

## Model Usage

Use the token ```filmation motu style```


---

☕ If you enjoy this model, buy us a coffee [![Buy a coffee](https://badgen.net/badge/icon/kofi?icon=kofi&amp;label=buy%20us%20a%20coffee)](https://ko-fi.com/3eegames)

---


## 🧾 Prompt example:

**The MOTU styled woman**

```award winning masterpiece illustration of a woman, filmation motu style, trending on artstation, highly detailed, rendered with Unreal Engine, 8k```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 40, Sampler: DPM++ 2S a Karras, CFG scale: 7, Seed: 311713104, Size: 512x512, Model hash: c0302f10_

---

**Refined He-Man**

```award winning masterpiece illustration of a man, filmation motu style, trending on artstation, highly detailed```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 40, Sampler: DPM++ 2S a Karras, CFG scale: 7, Seed: 195692676, Size: 512x512, Model hash: c0302f10_

---


## ❎ Negative Prompt Template

All images were rendered with the negative prompt below:

```lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name```

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

Export the model:
- [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx)
- [MPS](https://huggingface.co/docs/diffusers/optimization/mps)
- [FLAX/JAX](https://huggingface.co/blog/stable_diffusion_jax)

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "zuleo/filmation-motu"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "award winning masterpiece illustration of a man, filmation motu style"
image = pipe(prompt).images[0]

image.save("./filmation_man.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

-  You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
-  The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
-  You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)