---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/SouthParkStyle/resolve/main/showcase_southRick.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
---

# SouthPark Style

<p>
	<img alt="Showcase" src="https://huggingface.co/Guizmus/SouthParkStyle/resolve/main/showcase_southRick.jpg"/><br/>
	This model was based on <a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">RunwayML 1.5</a> model with updated VAE.<br/>
	The dataset is made mostly of South Park characters and scenary, with some regularisation around Rick Roll and Fullbody Shots photography.<br/>
	99 total pictures in the dataset, 800 repeats total each, over 16 Epoch on LR1e-6 (around 79k unitary steps).<br/>
	This was trained using EveryDream with a full caption of all training pictures.<br/>
	<br/>
	The style will be called by the use of the token <b>SouthPark Style</b>, and the tokens <b>Rick Roll</b> and <b>FullBody Shot</b> have also been refined.<br/>
	<br/>
	To access this model, you can download the CKPT file below.
</p>

## Downloads 

[2GB CKPT](https://huggingface.co/Guizmus/SouthParkStyle/resolve/main/SouthParkStyle_v1.ckpt)

[11GB CKPT with training optimizers](https://huggingface.co/Guizmus/SouthParkStyle/resolve/main/SouthParkStyle_v1_with_optimizers.ckpt)

[dataset for the first version](https://huggingface.co/Guizmus/SouthParkStyle/resolve/main/dataset.zip)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/SouthParkStyle"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Yoda SouthPark Style"
image = pipe(prompt).images[0]

image.save("./SouthParkStyle.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)