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

The style was trained with [Dreambooth-Stable](https://www.reddit.com/r/StableDiffusion/comments/xphaiw/dreambooth_stable_diffusion_training_in_just_125/) and is used with "<doodad>". Tt mixes especially well with the <midj-strong> style included in Doohickey. It's a finetuned version of the Trinart-Waifu-diffusion-50-50 included in this organization's models and was trained on 48 images from the author's ([crumb](https://huggingface.co/crumb)'s) Pinterest feed.

| Parameter | Value      |
|----------------------|------------|
| resolution | 512 |
| train_batch_size | 1 |
| gradient_accumulation_steps | 2 |
| learning_rate | 5e-6 |
| num_class_images | 120 |
| max_train_steps | 1200 |

Example outputs:
