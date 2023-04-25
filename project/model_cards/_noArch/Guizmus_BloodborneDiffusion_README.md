---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/BloodborneDiffusion/resolve/main/bloodbornestyle_showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: true
---

# Bloodborne Diffusion
<p>
	<img src="https://huggingface.co/Guizmus/BloodborneDiffusion/resolve/main/bloodbornestyle_showcase.jpg"/><br/>
	This is a Dreamboothed Stable Diffusion model trained on the Bloodborne series Style.<br/>
	The total dataset is made of 100 pictures, and the training has been done on runawayml 1.5 and the new VAE, with 12k steps (poly LR1e-6).<br/>
	The token "Bloodborne Style" will bring in the new concept.<br/>
	The recommended sampling is k_Euler_a or DPM++ 2M Karras on 20 steps, CFGS 7 .
	
</p>

[CKPT download link](https://huggingface.co/Guizmus/Bloodborne/resolve/main/BloodborneStyle-v1-1.ckpt)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/BloodborneDiffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a red moon, Bloodborne Style"
image = pipe(prompt).images[0]

image.save("./BloodborneStyle.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)