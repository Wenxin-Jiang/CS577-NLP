---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
---

# DreamBooth model of Kratos from God of War

<img src="https://huggingface.co/matteopilotto/kratos-sd-v1-4-dreambooth/resolve/main/grid_hub_512px.png">

This is a Stable Diffusion model fine-tuned on the person concept with DreamBooth. It can be used by adding the string `krts person` to any prompt.

Check out the exampls below ☟ to see a few practical examples on how to use it.

If you are curious to learn more about the training script, then I suggest you to visit the [report](https://wandb.ai/matt24/dreambooth-kratos/reports/Kratos-Dreambooth--VmlldzozMzQyMjQ4)📝 I created with Weights & Biases 🐝. 

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on [`matteopilotto/kratos`](https://huggingface.co/datasets/matteopilotto/kratos) dataset containing 10 images of **Kratos** 🪓 from **God of War** for the wildcard theme using [`CompVis/stable-diffusion-v1-4`](https://huggingface.co/CompVis/stable-diffusion-v1-4) pre-trained model.


## Example Output

<img src="https://huggingface.co/matteopilotto/kratos-sd-v1-4-dreambooth/resolve/main/sample_outputs/245581956f83dc275e5d.png">

**Prompt:** "An illustration of **krts** **person** punk playing electric guitar, tristan eaton, victo ngai, artgerm, rhads, ross draws"\
**Negative prompt:** "low contrast, blurry, low resolution, warped"\
**Resolution:** 512 x 512\
**Guidance Scale:** 7\
**Inference steps:** 50\
**Seeds:** [556850, 459286, 768745, 594109]

---

<img src="https://huggingface.co/matteopilotto/kratos-sd-v1-4-dreambooth/resolve/main/sample_outputs/4c4a87edbc0d5f03469a.png">

**Prompt:** "a drawing of **krts** **person** wearing a Spider-man costume in the style of Marvel comics"\
**Negative prompt:** "low contrast, blurry, low resolution, warped"\
**Resolution:** 512 x 512\
**Guidance Scale:** 7\
**Inference steps:** 50\
**Seeds:** [553766, 537908, 147395, 343240]

---

<img src="https://huggingface.co/matteopilotto/kratos-sd-v1-4-dreambooth/resolve/main/sample_outputs/4dae428d30bddcc70967.png">

**Prompt:** "an illustration of **krts** **person** sitting in a movie theater eating popcorn watching a movie, unreal engine, cozy indoor lighting, artstation, detailed, digital painting, cinematic, character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render"\
**Negative prompt:** "low contrast, blurry, low resolution, warped"\
**Resolution:** 512 x 512\
**Guidance Scale:** 7\
**Inference steps:** 50\
**Seeds:** [737986, 488711, 799063, 121111]

## Usage

```python
import torch
from diffusers import StableDiffusionPipeline

# set device-agnostic code
device = (
    'mps' if torch.backends.mps.is_available()
    else 'cuda' if torch.cuda.is_available()
    else 'cpu'
)

# load pre-trained model
pretrained_ckpt = 'matteopilotto/kratos-sd-v1-4-dreambooth'
pipeline = StableDiffusionPipeline.from_pretrained(pretrained_ckpt).to(device)

# stable diffusion hyperparameters
unique_token = 'krts'
class_type = 'person'
prompt = f'An illustration of {unique_token} {class_type} punk playing electric guitar, tristan eaton, victo ngai, artgerm, rhads, ross draws'
negative_prompt = 'low contrast, blurry, low resolution, warped'
guidance_scale = 7
h = 512
w = 512
inference_steps = 50
seed = 594109

# set generator for reproducibility
generator = torch.Generator(device=device).manual_seed(seed)

# generate image
image = pipeline(
    prompt,
    negative_prompt=negative_prompt,
    guidance_scale=guidance_scale,
    height=h,
    width=w,
    num_inference_steps=inference_steps,
    generator=generator
).images[0]
```
