---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/Tardisfusion/resolve/main/showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: true
---

# TARDISfusion
<p>
	<img src="https://huggingface.co/Guizmus/Tardisfusion/raw/main/showcase.jpg"/><br/>
	This is a Dreamboothed Stable Diffusion model trained on 3 Style concepts.<br/>
	The total dataset is made of 209 pictures, and the training has been done on runawayml 1.5 with 2500 steps and the new VAE.
	The following tokens will add their corresponding concept :<br/>
	<ul>
		<li><b>Classic Tardis style</b> : Architectural and furniture style seen inside the TARDIS in the series before the reboot.</li>
		<li><b>Modern Tardis style</b>: Architectural and furniture style seen inside the TARDIS in the series after the reboot</li>
		<li><b>Tardis Box style</b>: A style made from the TARDIS seen from the outside. Summons a TARDIS anywhere.</li>
	</ul>
</p>

[CKPT download link](https://huggingface.co/Guizmus/Tardisfusion/resolve/main/Tardisfusion-v2.ckpt)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/Tardisfusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a bedroom, Classic Tardis style"
image = pipe(prompt).images[0]

image.save("./TARDIS Style.png")
```