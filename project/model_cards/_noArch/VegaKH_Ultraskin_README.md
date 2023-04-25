---
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- photographic
- skin
- diffusers
inference: true
license: creativeml-openrail-m
---

# Ultraskin 0.9 - SD 2.1 768 finetuned on images of ultra-detailed human skin

This model will add a LOT of skin detail compared to SD 2.1. Sometimes this makes images look more realistic, sometimes less realistic!

**Prompting for this model is the same as 2.1 and can be tricky compared to 1.5.**

Try these tags in your prompts:
"teen","twenties" or "twenty year old", "thirties" or "thirty year old", continued all the way to "eighties" or "eighty year old", "elderly", "moles", "freckles", "scar","skin detail"

For stronger results, use the activation word **ultraskin** in your prompt. I recommend using this token toward the end of your prompt as it can lead to exaggerated detail and plastic looking skin.

Recommended negative prompts (if you want photographic results):
*rendered, 3d, blender, octane, unreal engine, video game character, cat*

This model is based on the 768 model and was trained on 768px x 768px images, so you will have better results creating images at least this size.

# Sample outputs:
![Samples](https://huggingface.co/VegaKH/Ultraskin/resolve/main/preview1.jpg)
![Samples](https://huggingface.co/VegaKH/Ultraskin/resolve/main/preview2.jpg)
![Samples](https://huggingface.co/VegaKH/Ultraskin/resolve/main/preview3.jpg)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion 2.1 model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

If using this with a web UI that requires a YAML file, download the YAML file and place it next to the model.