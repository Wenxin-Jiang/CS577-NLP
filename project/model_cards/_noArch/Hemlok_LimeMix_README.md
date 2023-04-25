---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

# 『LimeMix V1 & V2』

<img src="https://i.imgur.com/RGcmq84.jpg" width="1024" height="">
<img src="https://i.imgur.com/14goJA5.png" width="1024" height="">

- "LimeMix" is a model created by hierarchical merging based on "anything-v4.5"([andite/anything-v4.0 · Hugging Face](https://huggingface.co/andite/anything-v4.0)).

----

# ◆Discord
[Join Discord Server](https://discord.gg/eN6aSWRddT)

- The merged model community of Hemlok.

----

# ◆About

- "LimeMix" is a model with more emphasis on composition and illustration than "DateMix".

- Sampler: DDIM or DPM++ SDE Karras

- Steps: 20~

- Clipskip: 2

- CFG Scale: 5-8

- Denoise strength: 0.5-0.7(As you like)

- Negative prompts should be as few as possible.

- vae: As you wish. (Any etc. If not used, color may become lighter)

- V1: Main model.
- V2: A model that is even more composition-oriented than V1. It excels at illustrations that show the whole body.

----

# ◆How to use

- Please download the file by yourself and use it with WebUI(AUTOMATIC1111) etc.

- Use the fp16 version for Colab(T4) or a PC with low RAM.

----

# ◆Colab Note

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10-FYdd2xl4f9ugybZrKM3B3DWUx5twQo?usp=sharing)
- (I have not checked the operation but it probably works.)

----

# ◆Comparison

<img src="https://i.imgur.com/astFr0y.jpg" width="1700" height="">

```
(morning), (school), 1girl, solo, looking at viewer, cowboy shot, (school uniform), smile, stockings
```

----

<img src="https://i.imgur.com/LVFWSal.jpg" width="1700" height="">

```
kawaii, winter, ((street)), ((building)), (noon), 1girl, solo, looking at viewer, ((maid uniform)), (twintails), long hair, blonde hair, smile, [small breast], shiny skin,
```

----

# ◆Sampler & CFG Scale
## V1
<img src="https://i.imgur.com/tm10msn.jpg" width="1700" height="">

## V2
<img src="https://i.imgur.com/xscqBWn.jpg" width="1700" height="">

----

# Disclaimer

- The creation of SFW and NSFW images is at the discretion of the individual creator.

- This model is not a model created to publish NSFW content in public places, etc.

----

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.

The CreativeML OpenRAIL License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content

2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license

3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)

(Full text of the license: https://huggingface.co/spaces/CompVis/stable-diffusion-license)