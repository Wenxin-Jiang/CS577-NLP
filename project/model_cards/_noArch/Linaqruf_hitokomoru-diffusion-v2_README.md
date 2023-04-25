---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/example_image/thumbnail.png"
language:
- en
pipeline_tag: text-to-image
tags:
- stable-diffusion
- stable-diffusion-diffusers
- diffusers
- waifu-diffusion
inference: true
widget:
- text: >-
    masterpiece, best quality, 1girl, brown hair, green eyes, colorful, autumn,
    cumulonimbus clouds, lighting, blue sky, falling leaves, garden
  example_title: example 1girl
- text: >-
    masterpiece, best quality, 1boy, medium hair, blonde hair, blue eyes,
    bishounen, colorful, autumn, cumulonimbus clouds, lighting, blue sky,
    falling leaves, garden
  example_title: example 1boy
---

# Hitokomoru Diffusion V2

![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/example_image/thumbnail.png)

A latent diffusion model that has been trained on Japanese Artist artwork, [ヒトこもる/Hitokomoru](https://www.pixiv.net/en/users/30837811). The current model is fine-tuned from [waifu-diffusion-1-4](https://huggingface.co/hakurei/waifu-diffusion-v1-4) (`wd-1-4-anime_e2.ckpt`) with a learning rate of `2.0e-6`, 15000 training steps and 4 batch sizes on the `257 artworks` collected from Danbooru. This model supposed to be a continuation of [hitokomoru-diffusion](https://huggingface.co/Linaqruf/hitokomoru-diffusion/) fine-tuned from Anything V3.0. Dataset has been preprocessed using [Aspect Ratio Bucketing Tool](https://github.com/NovelAI/novelai-aspect-ratio-bucketing) so that it can be converted to latents and trained at non-square resolutions. Like other anime-style Stable Diffusion models, it also supports Danbooru tags to generate images.

e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

- Use it with the [`Automatic1111's Stable Diffusion Webui`](https://github.com/AUTOMATIC1111/stable-diffusion-webui) see: [how-to-use](#howtouse)
- Use it with 🧨 [`diffusers`](##🧨Diffusers)


# Model Details

- **Developed by:** Linaqruf
- **Model type:** Diffusion-based text-to-image generation model
- **Model type:** This is a model that can be used to generate and modify images based on text prompts. 
- **License:** [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
- **Finetuned from model:** [waifu-diffusion-v1-4-epoch-2](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/wd-1-4-anime_e2.ckpt)

## How to Use
- Download the `hitokomoru-v2.ckpt` [here](https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/hitokomoru-v2.ckpt), or download the safetensors version [here](https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/hitokomoru-v2.safetensors).
- This model is fine-tuned from [waifu-diffusion-v1-4-epoch-2](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/wd-1-4-anime_e2.ckpt), which is also fine-tuned from [stable-diffusion-2-1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base). So in order to run this model in [`Automatic1111's Stable Diffusion Webui`](https://github.com/AUTOMATIC1111/stable-diffusion-webui), you need to put inference config .YAML file next to the model, you can find it [here](https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/hitokomoru-v2.yaml)
- You need to adjust your prompt using aesthetic tags, Based [Official Waifu Diffusion 1.4 release notes](https://gist.github.com/harubaru/8581e780a1cf61352a739f2ec2eef09b#prompting), an ideal negative prompt to guide the model towards high aesthetic generations would look like:
```
worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
```
- And, the following should also be prepended to prompts to get high aesthetic results:
```
masterpiece, best quality, high quality, absurdres
```
## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information, please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion). You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

You should install dependencies below in order to running the pipeline

```bash
pip install diffusers transformers accelerate scipy safetensors
```
Running the pipeline (if you don't swap the scheduler it will run with the default DDIM, in this example we are swapping it to DPMSolverMultistepScheduler):

```python
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "Linaqruf/hitokomoru-diffusion-v2"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "masterpiece, best quality, high quality, 1girl, solo, sitting, confident expression, long blonde hair, blue eyes, formal dress"
negative_prompt = "worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry"

with autocast("cuda"):
    image = pipe(prompt, 
                 negative_prompt=negative_prompt, 
                 width=512,
                 height=728,
                 guidance_scale=12,
                 num_inference_steps=50).images[0]
    
image.save("anime_girl.png")
```



## Example

Here is some cherrypicked samples:

![Anime Girl](https://huggingface.co/Linaqruf/hitokomoru-diffusion-v2/resolve/main/example_image/cherry-picked-sample.png)

### Prompt and settings for Example Images

```
masterpiece, best quality, high quality, 1girl, solo, sitting, confident expression, long blonde hair, blue eyes, formal dress, jewelry, make-up, luxury, close-up, face, upper body.

Negative prompt: worst quality, low quality, medium quality, deleted, lowres, comic, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry

Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 994051800, Size: 512x768, Model hash: ea61e913a0, Model: hitokomoru-v2, Batch size: 2, Batch pos: 0, Denoising strength: 0.6, Clip skip: 2, ENSD: 31337, Hires upscale: 1.5, Hires steps: 20, Hires upscaler: Latent (nearest-exact)
``````
## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Credit
- [ヒトこもる/Hitokomoru](https://www.pixiv.net/en/users/30837811) for Datasets
