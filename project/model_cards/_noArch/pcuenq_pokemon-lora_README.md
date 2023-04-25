
---
license: creativeml-openrail-m
base_model: runwayml/stable-diffusion-v1-5
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---
    
# LoRA text2image fine-tuning - https://huggingface.co/pcuenq/pokemon-lora
These are LoRA adaption weights trained on base model https://huggingface.co/runwayml/stable-diffusion-v1-5. The weights were fine-tuned on the lambdalabs/pokemon-blip-captions dataset.

## How to Use

The script below loads the base model, then applies the LoRA weights and performs inference:

```Python
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from huggingface_hub import model_info

# LoRA weights ~3 MB
model_path = "pcuenq/pokemon-lora"

info = model_info(model_path)
model_base = info.cardData["base_model"]
pipe = StableDiffusionPipeline.from_pretrained(model_base, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

pipe.unet.load_attn_procs(model_path)
pipe.to("cuda")

image = pipe("Green pokemon with menacing face", num_inference_steps=25).images[0]
image.save("green_pokemon.png")
```

Please, check [our blog post](https://huggingface.co/blog/lora) or [documentation](https://huggingface.co/docs/diffusers/v0.15.0/en/training/lora#text-to-image-inference) for more details.

## Example Images

![img_0](./image_0.png)
![img_1](./image_1.png)
![img_2](./image_2.png)
![img_3](./image_3.png)
