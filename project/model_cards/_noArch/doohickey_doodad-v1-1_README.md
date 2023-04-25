---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: false

---

# Doodad

*<p style="color:green"> <b> This is the 1st part of a 2 (3?) part project meant to be used with <a href="https://huggingface.co/doohickey">Doohickey</a> </b> </p>*

The style was trained with [Dreambooth-Stable](https://www.reddit.com/r/StableDiffusion/comments/xphaiw/dreambooth_stable_diffusion_training_in_just_125/) and is used with "imv" (an uncommonly used token recommended by the author I think) and it mixes especially well with the <midj-strong> style included in Doohickey. It's a finetuned version of the Trinart-Waifu-diffusion-50-50 included in this organization's models.

| Parameter | Value      |
|----------------------|------------|
| resolution | 512 |
| train_batch_size | 1 |
| gradient_accumulation_steps | 2 |
| learning_rate | 5e-6 |
| num_class_images | 120 |
| max_train_steps | 1200 |

Example outputs:

"portal into another dimension"
![](https://cdn.discordapp.com/attachments/1024588665596411944/1024618996479311892/unknown.png)

"portrait of a dying god"
![](https://pbs.twimg.com/media/Fdu1c9XWQAA4v2g?format=png&name=900x900)

"photograph"
![](https://pbs.twimg.com/media/Fdu6hg4X0AI5aNI?format=png&name=900x900)

"The alchemist's laboratory by Greg Rutkowski and Claude Monet, oil on canvas"
![](https://pbs.twimg.com/media/FdvB2ZiWYAQHg-7?format=png&name=900x900)