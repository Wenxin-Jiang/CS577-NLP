---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---
# 『Plum Mix & Pear Mix』

<img src="https://i.imgur.com/uHMJpbH.png" width="1024" height="">

<img src="https://i.imgur.com/x5Aa0ly.jpg" width="1024" height="">

- "Plum Mix" is a model based on "AbyssOrangeMix2"(https://huggingface.co/WarriorMama777/OrangeMixs#abyssorangemix2) with hierarchical merging.
- "Pear Mix" is a realistic model based on "Plum Mix" adjusted by hierarchical merging.

----

# ◆Discord
[Join Discord Server](https://discord.gg/eN6aSWRddT)

- The merged model community of Hemlok.

----

# ◆About

- It is adjusted to produce a dark and lovely illustration.
- If you prefer a more realistic look, use the "Pear mix" model.
- Sampler: DDIM or DPM++ SDE Karras
- Steps: 50~
- Clipskip: 2
- CFG Scale: 5-8
- Denoise strength: 0.4-0.7(As you like)
- Negative prompts should be as few as possible.
- vae: As you wish. (Any etc. If not used, color may become lighter)

----

# ◆How to use

- Please download the file by yourself and use it with WebUI(AUTOMATIC1111) etc.
- Use the f16 version for Colab(T4) or a PC with low RAM.

----

# ◆Colab Note

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ajz2sZdClKTyNt145UTlKG3Vh6cq_7QS?usp=sharing)
- (I have not checked the operation but it probably works.)

----

# ◆Comparison

<img src="https://i.imgur.com/VMvsiIH.png" width="1700" height="">
<img src="https://i.imgur.com/2fQkoJU.png" width="1700" height="">

```
(masterpiece:1.2), (best quality:1.2), winter, (morning), (school), 1girl, solo, looking at viewer, cowboy shot, cardigan, (school uniform), smile, blonde hair, (knee socks), bag,
``` 

----

<img src="https://i.imgur.com/XvKhDVr.png" width="1700" height="">
<img src="https://i.imgur.com/jSZqx7X.png" width="1700" height="">

```
(masterpiece_1.2), (best quality_1.2), (1girl), (cowboy shot), (solo), (twintail), long hair, (school uniform), looking at viewe
```

----

# ◆Sampler & CFG Scale

## 『Plum Mix』
<img src="https://i.imgur.com/aU0jngA.jpg" width="1700" height="">
<img src="https://i.imgur.com/2CLd0Zw.jpg" width="1700" height="">

```
(masterpiece:1.2), (best quality:1.2), kawaii, winter, ((street)), ((building)), (noon), 1girl, solo, looking at viewer, ((maid uniform)), (twintails), long hair, blonde hair, smile, [small breast], shiny skin,
```
----

## 『Pear Mix』

<img src="https://i.imgur.com/njWmOqs.jpg" width="1700" height="">
<img src="https://i.imgur.com/DFGiAFm.jpg" width="1700" height="">

```
(masterpiece:1.2), (best quality:1.2), kawaii, winter, ((street)), ((building)), (noon), 1girl, solo, looking at viewer, ((maid uniform)), (twintails), long hair, blonde hair, smile, [small breast], shiny skin,
```


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
