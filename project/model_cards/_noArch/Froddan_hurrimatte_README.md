---
license: cc0-1.0
inference: false
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
---

# Stable Diffusion fine tuned on art by [Björn Hurri](https://www.artstation.com/bjornhurri)
This model is fine tuned on some of his matte-style paintings. I also have a version for his "shinier" works.

### Usage
Use by adding the keyword "hurrimatte" to the prompt. The model was trained with the "monster" classname, which can also be added to the prompt.

## Samples
For this model I made two checkpoints. The "hurrimatte monster x2" model is trained for twice as long as the regular checkpoint, meaning it should be more fine tuned on the style but also more rigid. The top 3 images are from the regular version, the rest are from the x2 version. I hope it gives you an idea of what kind of styles can be created with this model.

<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index_1200_3.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index_1200_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/1200_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index2.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index3.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index_2400_5.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index_2400_6.png" width="256px"/>
<img src="https://huggingface.co/Froddan/hurrimatte/resolve/main/index_2400_7.png" width="256px"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).
