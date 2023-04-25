---
language:
- en
tags:
- stable-diffusion
- text-to-image
---

# Padoru AI

This model was trained with the style padoru based in Anything V3. Like other anime-style Stable Diffusion models, it also supports danbooru tags to generate images.

## Examples


**Padoru Boy:**
![Padoru Boy](https://huggingface.co/herrius/padoru/resolve/main/images/boy%201.png)
![Padoru Boy](https://huggingface.co/herrius/padoru/resolve/main/images/boy%202.png)
```
padoru,1boy,guitar,music,skulls,clothing black
Negative prompt: deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra_limb, ugly, poorly drawn hands, no color, weird colors, censored, deformed glasses, lowres, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, big boobs
Steps: 40, Sampler: DDIM, CFG scale: 7,Seed: 2151952332
```
**Padoru Girl:**
![Padoru Girl](https://huggingface.co/herrius/padoru/resolve/main/images/girl%201.png)
![Padoru Girl](https://huggingface.co/herrius/padoru/resolve/main/images/girl%202.png)
```
1girl,blonde,masterpiece, bg Christmas,snowing
Negative prompt: deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra_limb, ugly, poorly drawn hands, no color, weird colors, censored, deformed glasses, lowres, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username,cropped
Steps: 40, Sampler: DDIM, CFG scale: 9,Seed: 392298786, Size: 640x512
```
## Model
- [padoru3000](https://huggingface.co/herrius/padoru/blob/main/padoru-model3000.ckpt)
- [padoru6000](https://huggingface.co/herrius/padoru/blob/main/padoru-model6000.ckpt)