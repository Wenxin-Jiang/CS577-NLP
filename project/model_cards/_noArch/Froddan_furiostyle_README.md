---
license: cc0-1.0
inference: false
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
---

# Stable Diffusion fine tuned on art by [Furio Tedeshi](https://www.furiotedeschi.com/)

### Usage
Use by adding the keyword "furiostyle" to the prompt. The model was trained with the "demon" classname, which can also be added to the prompt.

## Samples
For this model I made two checkpoints. The "furiostyle demon x2" model is trained for twice as long as the regular checkpoint, meaning it should be more fine tuned on the style but also more rigid. The top 4 images are from the regular version, the rest are from the x2 version. I hope it gives you an idea of what kind of styles can be created with this model. I think the x2 model got better results this time around, if you would compare the dog and the mushroom.

<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/1000_2.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/1000_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/dog_1000_2.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/mushroom_1000_2.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/2000_1.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/2000_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/mushroom_cave_4.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/mushroom_cave_ornate.png" width="256px"/>
<img src="https://huggingface.co/Froddan/furiostyle/resolve/main/dog_2.png" width="256px"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).
