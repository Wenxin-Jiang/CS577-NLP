---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---
# Yuunon V0.4C
V0.4 use different kinds of approach so the models will not be overfit and easy to generate.

Yuunon is a diffusion model with Dreambooth training that trained on artstyle artwork of artist, [Nagayama Yuunon](https://www.pixiv.net/users/149587).

This model is based on [ACertainty](https://huggingface.co/JosephusCheung/ACertainty), trained with 213 images collected from danbooru, yande.re and gelbooru, combined with 2130 self generated class images. Then with a learning rate of 1.0e-6 for 10 epoches, trained total 4280 steps.

You can use prompts including danbooru tags, just like other anime-style diffusion models. Use token prompt "(Nagayama_Yuunon)" (or Class:"artstyle") for better results.

## 🧨 Diffusers
This model can be used just like any other Stable Diffusion model. For more information, please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or FLAX/JAX.

```
from diffusers import StableDiffusionPipeline
import torch

model_id = "ochakaiwch/yuunon"
branch_name= "main"

pipe = StableDiffusionPipeline.from_pretrained(model_id, revision=branch_name, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "pikachu"
image = pipe(prompt).images[0]

image.save("./pikachu.png")
```

## 📋 Demos
[Will Update Soon]


## ✍️ Future Plans / Todo for V1
* Self-collected and well-prepared class image instead of self generation, give oppotunities of training certain parts of images (eg: hands, feet, shoes).
* May use higher resolution dataset for training (eg. 768^2).
* Much proper epoches/learning speed/training steps of models.
* Can training with **rectangle** images.

## 💻 Hardwares
This model is produced using Runpod RTX A6000 (48GB), with 8 vCPU, 128GB RAM and 70GB storage.

## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) [Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)