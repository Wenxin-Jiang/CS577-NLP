---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/andite/pastel-mix/resolve/main/example-images/01194-%20.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

Fantasy.ai is the official and exclusive hosted AI generation platform that holds a commercial use license for Pastel Mix, you can use their service at https://Fantasy.ai/

Please report any unauthorized commercial use.

---------------------

## **CivitAI! -> https://civitai.com/models/5414/pastel-mix-stylized-anime-model I'd appreciate the ratings, thank you!**


<center><h1><b>Pastel Mix</b></h1></center>
 <p align="center">Welcome to Pastel Mix - a stylized latent diffusion model. This model is intended to produce high-quality, highly detailed anime style with just a few prompts.</p>

   <p align="center">This model is made with the thought of imitating pastel-like art and the potential of mixing LORAs into a model altogether to create a fantastic mix. 
   Recipe for this mix could be found below. Like other anime-style Stable Diffusion models, it also supports danbooru tags to generate images. </p>

<p align="center">e.g. <b>masterpiece, best quality, upper body, 1girl, looking at viewer, red hair, medium hair, purple eyes, demon horns, black coat, indoors, dimly lit</b></p>

<p align="center"><img src="https://huggingface.co/andite/Pastel-Mix/resolve/main/example-images/grid-0020.png">
<img src="https://huggingface.co/andite/Pastel-Mix/resolve/main/example-images/grid-0018.png"></p>

-------

## How to download with Git

```
git lfs install
git clone https://huggingface.co/andite/pastel-mix
```

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "andite/pastel-mix"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "hatsune_miku"
image = pipe(prompt).images[0]

image.save("./hatsune_miku.png")
```

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run pastel-mix:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/pastel-mix)



## Examples

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/grid-0035.png)

```
masterpiece, best quality, ultra-detailed, illustration, portrait, 1girl
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Size: 448x640, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 960x1280, Hires steps: 20, Hires upscaler: Latent
```
![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/grid-reimu.png)

```
masterpiece, best quality, ultra-detailed, illustration, portrait, hakurei reimu, 1girl, throne room, dimly lit
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Size: 448x640, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 960x1280, Hires steps: 20, Hires upscaler: Latent
```

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/grid-0043.png)

```
masterpiece, best quality, ultra-detailed, illustration, 1girl, witch hat, purple eyes, blonde hair, wielding a purple staff blasting purple energy, purple beam, purple effects, dragons, chaos
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Size: 448x640, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 960x1280, Hires steps: 20, Hires upscaler: Latent
```

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/01166-%20.png)

```
masterpiece, best quality, ultra-detailed, illustration, close-up, straight on, 1girl, black hair, yellow eyes, red roses, chains
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2203084815, Size: 640x448, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 1280x960, Hires steps: 20, Hires upscaler: Latent
```

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/01177-%20.png)

```
masterpiece, best quality, ultra-detailed, illustration, close-up, straight on, face focus, 1girl, white hair, golden eyes, long hair, halo, angel wings, serene expression, looking at viewer
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 240742293, Size: 640x448, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 1280x960, Hires steps: 20, Hires upscaler: Latent
```

## So what the hell is the 'better-vae' version?

I merged the pastel-waifu-diffusion.vae.pt inside the model so you don't have to set up the vae anymore. 

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/xyz_grid-0004-%20.png)

life so much ez now since you don't have to download the vae and set it up right?

## What is pastelmix-lora.safetensors?

It's a lora version which is made from extracting the loras from pastel-mix using a script that is similar to add-difference method.

https://github.com/bmaltais/kohya_ss/blob/master/train_network_README.md

## Guide

For the settings or parameters, I recommend using these settings.

![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/settings.png)

```
Sampler: DPM++ 2M Karras

Steps: 20

CFG Scale: 7

Hires. Fix: On

Upscaler: Latent (MUST!)

Hires Steps: 20

Denoising Strength: 0.
```

I prefer using 0.6 since it's the sweet spot of this model. If you can find a better setting for this model, then good for you lol.

Latent upscaler is the best setting for me since it retains or enhances the pastel style. Other upscalers like Lanczos or Anime6B tends to smoothen them out, removing the pastel-like brushwork.

Please use the **VAE** that I uploaded in this repository. It is from the [Waifu Diffusion](https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae) team. Credits to [haru](https://huggingface.co/hakurei) for letting me rename and upload it.

## Tip (Optional)

Putting mksks style in the beginning of the prompt can further influence the pastel-like style and make the output better. It is optional though, so it's up to you. You don't really need it.
![](https://huggingface.co/andite/pastel-mix/resolve/main/example-images/xy_grid-0016-%20.png)

```
mksks style, masterpiece, best quality, upper body, 1girl, looking at viewer, red hair, medium hair, purple eyes, demon horns, black coat, indoors, dimly lit
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 580841049, Size: 448x640, Model hash: 7edc8e08, Model: pastelmix-fp32, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires resize: 960x1280, Hires steps: 20, Hires upscaler: Latent
```

## Recipe

Merging the models.

| Model: A | Model: B | Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| [dpepmkmp](https://huggingface.co/closertodeath/dpepmkmp)  | [Tea](https://huggingface.co/andite/desserts) | 1,0.9,0.7,0.5,0.3,0.1,1,1,1,1,1,1,0,1,1,1,1,1,1,0.1,0.3,0.5,0.7,0.9,1 | 0 | dpeptea |
| dpeptea | [basil-mix](https://huggingface.co/nuigurumi/basil_mix) | 1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 | 0 | dpeptea-basil |

Merging the loras into the model.

| Model | Lora | Weight | Merge Name |
| --- | --- | --- | --- |
| [dpeptea-basil](https://huggingface.co/closertodeath/dpepteahands3) | [Magic LORA](https://cdn.discordapp.com/attachments/1065289257243115540/1066346221876301845/MagicLORA.pt) | 0.3 | dpeptea-1 |
| dpeptea-1 | [Jordan_3](https://huggingface.co/SatyamSSJ10/ConceptArt) | 1 | dpeptea-2 |
| dpeptea-2 | [sttabi_v1.4-04](https://huggingface.co/dolphinz/stlora) | 0.5 | dpeptea-3 |
| dpeptea-3 | [xlimo768](https://huggingface.co/closertodeath/ctdlora) | 0.6 | dpeptea-4 |
| dpeptea-4 | [dpep 2 768](https://huggingface.co/closertodeath/ctdlora)| 0.35 | Pastel-Mix |

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

-------

## Big Thanks to

The 東方Project AI community for their wonderful LORAs.

- [Closertodeath](https://huggingface.co/closertodeath) for dpepmkmp model, and the loras: xlimo768, dpep 2 768
- [dolphinz/sometimes#9353](https://huggingface.co/dolphinz) for tabi artstyle Lora.
- [SatyamSSJ10](https://huggingface.co/SatyamSSJ10/ConceptArt) for Jordan_3 Lora.
- randomaccessmemories#4004 for Magic Lora