---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/DeathNote/raw/main/samples/showcase_dn_2.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: true
---
# DeathNote Diffusion
<p>
	<img src="https://huggingface.co/Guizmus/DeathNote/raw/main/samples/showcase_dn_2.jpg"/><br/>
	This is the fine-tuned Stable Diffusion model trained on images from the anime Death Note.<br/>
	The total dataset is made of 93 pictures, and the training has been done on naclbit/trinart_stable_diffusion_v2 for 12500 steps.
	The following tokens will add their corresponding concept :<br/>
	<ul>
		<li><b>DeathNote notebook</b> : the Deathnote itself</li>
		<li><b>Light Yagami man</b> : Light Yagami, main character</li>
		<li><b>Ryuk demon</b> : Ryuk, Shinigami</li>
		<li><b>LLawliet man</b> : L, "full" name</li>
		<li><b>Misa Amane girl</b> : Second Kira</li>
		<li><b>Soichiro Yagami man</b> : Soichiro, Father of Light, Policeman</li>
		<li><b>Sayou Yagami girl</b> : Sayou, sister of Light</li>
		<li><b>Raye Penber man</b> : Raye, FBI Agent</li>
		<li><b>Naomi Misora girl</b> : Naomi, fiance of Raye</li>
		<li><b>DNStyle style</b> : style of the anime (only in v1, it was too bad to be kept)</li>
	</ul>
</p>

[current version, CKPT download link](https://huggingface.co/Guizmus/DeathNote/resolve/main/DeathNote_v2.ckpt)

[older version, CKPT download link](https://huggingface.co/Guizmus/DeathNote/resolve/main/DeathNote_v1.ckpt)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/DeathNote"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Ryuk demon, intricate, headshot, highly detailed"
image = pipe(prompt).images[0]

image.save("./Ryuk_demon.png")
```

## Examples

<p>
	<u>Sampling :</u> 30 steps using k_Euler_a<br/>
	<u>CFGS :</u> 7 to 9<br/>
	<u>Denoising :</u> 0.5<br/>
</p>

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)