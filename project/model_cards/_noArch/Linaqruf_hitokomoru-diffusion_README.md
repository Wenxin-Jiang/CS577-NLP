---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Linaqruf/hitokomoru/resolve/main/thumbnail.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

# Hitokomoru Diffusion

**Welcome to Hitokomoru Diffusion** - a latent diffusion model that has been trained on Japanese Artist artwork, [ヒトこもる/Hitokomoru](https://www.pixiv.net/en/users/30837811). The current model has been fine-tuned with a learning rate of `2.0e-6` for `20000 training steps`/`80 Epochs` on `255 images` collected from Danbooru. The model is trained using [NovelAI Aspect Ratio Bucketing Tool](https://github.com/NovelAI/novelai-aspect-ratio-bucketing) so that it can be trained at non-square resolutions. Like other anime-style Stable Diffusion models, it also supports Danbooru tags to generate images.

e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

There is 4 variations of this model available so far:
- `hitokomoru-5000.ckpt for the checkpoint trained on 5,000 steps.`
- `hitokomoru-10000.ckpt for the checkpoint trained on 10,000 steps.`
- `hitokomoru-15000.ckpt for the checkpoint trained on 15,000 steps.`
- `hitokomoru-20000.ckpt for the checkpoint trained on 20,000 steps.`

# Dataset

You can find `datasets` used to train this model and the `last-state` folder for resume training [here](https://huggingface.co/datasets/Linaqruf/hitokomoru-tag)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Linaqruf/hitokomoru-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "hatsune_miku"
image = pipe(prompt).images[0]

image.save("./hatsune_miku.png")
```

## Examples

Below are some examples of images generated using this model:

#### Using Hitokomoru-5000-pruned.ckpt
**Anime Girl:**
![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/girl-5000.png)

**Anime Boy:**
![Anime Boy](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/boy-5000.png)

#### Using Hitokomoru-10000-pruned.ckpt

**Anime Girl:**
![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/girl-10000.png)

**Anime Boy:**
![Anime Boy](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/boy-10000.png)

#### Using Hitokomoru-15000-pruned.ckpt

**Anime Girl:**
![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/girl-15000.png)

**Anime Boy:**
![Anime Boy](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/boy-15000.png)

#### Using Hitokomoru-20000-pruned.ckpt

**Anime Girl:**
![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/girl-20000.png)

**Anime Boy:**
![Anime Boy](https://huggingface.co/Linaqruf/hitokomoru/resolve/main/example_images/boy-20000.png)

### Prompt and settings for Example Images

**Anime Girl:**
```
(masterpiece:1.05),illustration,beautiful detailed,colourful,finely detailed,dramatic light,intricate details,1 girl, 1990, 1980, hatsune miku

Negative prompt:
nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,missing fingers,bad hands,missing arms, long neck, Humpbacked,shadow,long body, Abnormal fingers,

Steps: 32, Sampler: Euler, CFG scale: 10, Seed: 2319346364, Size: 512x768, Model hash: 2700c435, Batch size: 2, Batch pos: 0, Clip skip: 2
```

**Anime Boy:**
```
Authentic and detailed face(man:1.2763)(boymasterpiece:1.1025), (best quality:1.1025), (ultra-detailed:1.1025), (illustration:1.1025), (tousled hair:1.1025), (frill:0.907) , white cutter shirt, (one boy:1.05), (solo:1.05) chest, detailed wet clothes, empty stare, pants, (flowers:1.05), beautifully detailed sky, beautifully detailed water, leaves, detailed and beautiful sea

Negative prompt: 
(big breasts:1.2763)(breast:1.1025)}(woman:1.2155)} little girl,(3d:1.1576)(girl:1.629), nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,missing fingers,bad hands,missing arms, long neck, Humpbacked

Steps: 40, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1870332858, Size: 512x768, Model hash: 2700c435, Batch size: 2, Batch pos: 0, Clip skip: 2
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## What's next?
- Hitokomoru Diffusion V2 soon, will added scenery datasets from MidJourney I hope it's working, because I'm getting bored the result is always simple background
## Credit
- [ヒトこもる/Hitokomoru](https://www.pixiv.net/en/users/30837811) for Datasets
- Just for my part

## Big Thanks to
- [Kohya](https://twitter.com/kohya_ss) with their [Kohya Trainer](https://note.com/kohya_ss/n/ne17e34dd51bf)
- Peeps on SD Training Labs Discord Server
- [ptsearch.info](https://www.ptsearch.info/) for prompt references