---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: the cat called loulou, with snow in the background
language:
- zh
- en
---

# DreamBooth model for loulou cat

This is the model for a cat called "Lou Lou" (楼楼). The model is based on Stable Diffusion model, fine-tuned the cat taught to Stable Diffusion with DreamBooth. It trained by the member of tilake AIGC group on the dataset from internet, for entertainment only.
It can be used by modifying the `instance_prompt`: **the cat called loulou**

这是一个生成 “楼楼” 猫的模型。该模型基于 Stable Diffusion 模型，通过 DreamBooth 方法进行微调。该模型由 tilake AIGC 小组成员训练并开放给社区，仅供娱乐。  
你可以通过扩充以下 “instance_prompt” 来生成关于楼楼的不同场景、姿态：**the cat called loulou**


## Description

"Lou Lou" (楼楼) is a very popular cat online. At 0:25 on October 14, 2017, he left us forever because of illness and returned to his cat planet. As a loyal fan of "Lou Lou" (楼楼) and his expression pack, I trained a model specially used to generate the building as a memorial.

If you like this model, click the \[❤ like\]  button!

楼楼是一只人气超高的网红猫。2017年10月14日0时25分，它因病永远离开了我们回到喵星。作为楼楼及其表情包的忠实粉丝，我训练了一个专门用于生成楼楼的模型，将其用另一种方式永生，以作为纪念。如果喜欢该模型，欢迎点亮上方【like】按钮~

## Examples
- Prompt: ```the cat called loulou; wearing a christmas hat, christmas lights and snow in the background``` （圣诞楼楼）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/1.png">
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/2.png">
- Prompt: ```the cat called loulou; swimming in the river```（游泳楼楼）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/3.png">
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/4.png">
- Prompt: ```the cat called loulou curled up in a cardboard box```（纸箱楼楼）
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/5.png">
  <img width="200px" height="200px" src="https://huggingface.co/tilake/loulou-cat-diffusion/resolve/main/example/6.png">
  
## Usage

```python
from diffusers import StableDiffusionPipeline
pipeline = StableDiffusionPipeline.from_pretrained('tilake/loulou-cat-diffusion')
image = pipeline("the cat called loulou, with snow in the background").images[0]
image
```