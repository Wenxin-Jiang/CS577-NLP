---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---
# Arcane Diffusion
This is the fine-tuned Stable Diffusion model trained on images from the TV Show Arcane.
Use the tokens **_arcane style_** in your prompts for the effect.

**If you enjoy my work, please consider supporting me** 
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://patreon.com/user?u=79196446)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch

model_id = "nitrosocke/Arcane-Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "arcane style, a magical princess with golden hair"
image = pipe(prompt).images[0]

image.save("./magical_princess.png")
```

# Gradio & Colab

We also support a [Gradio](https://github.com/gradio-app/gradio) Web UI and Colab with Diffusers to run fine-tuned Stable Diffusion models:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/anzorq/finetuned_diffusion)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1j5YvfMZoGdDGdj3O3xRU1m4ujKYsElZO?usp=sharing)

![img](https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/magical_princess.png)

### Sample images from v3:
![output Samples v3](https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/arcane-v3-samples-01.jpg)
![output Samples v3](https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/arcane-v3-samples-02.jpg)
### Sample images from the model:
![output Samples](https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/arcane-diffusion-output-images.jpg)
### Sample images used for training:
![Training Samples](https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/arcane-diffusion-training-images.jpg)

**Version 3** (arcane-diffusion-v3): This version uses the new _train-text-encoder_ setting and improves the quality and edibility of the model immensely. Trained on 95 images from the show in 8000 steps.

**Version 2** (arcane-diffusion-v2): This uses the diffusers based dreambooth training and prior-preservation loss is way more effective. The diffusers where then converted with a script to a ckpt file in order to work with automatics repo.
Training was done with 5k steps for a direct comparison to v1 and results show that it needs more steps for a more prominent result. Version 3 will be tested with 11k steps.

**Version 1** (arcane-diffusion-5k): This model was trained using _Unfrozen Model Textual Inversion_ utilizing the _Training with prior-preservation loss_ methods. There is still a slight shift towards the style, while not using the arcane token.
