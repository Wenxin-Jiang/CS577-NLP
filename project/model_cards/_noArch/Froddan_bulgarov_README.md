---
license: cc0-1.0
inference: false
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
---

# Stable Diffusion fine tuned on art by [Vitaly Bulgarov](https://www.artstation.com/vbulgarov)

### Usage
Use by adding the keyword "bulgarovstyle" to the prompt. The model was trained with the "knight" classname, which can also be added to the prompt.

## Samples
For this model I made two checkpoints. The "bulgarovstyle knight x2" model is trained for twice as long as the regular checkpoint, meaning it should be more fine tuned on the style but also more rigid. The top 3 images are from the regular version, the rest are from the x2 version (I think). I hope it gives you an idea of what kind of styles can be created with this model.

<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/dog_v1_1.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/greg_v1.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/greg3.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/index4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/index_1600_2.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/index_1600_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/tmp1zir5pbb.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/tmp6lk0vp7p.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/tmpgabti6yx.png" width="256px"/>
<img src="https://huggingface.co/Froddan/bulgarov/resolve/main/tmpgvytng2n.png" width="256px"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).
