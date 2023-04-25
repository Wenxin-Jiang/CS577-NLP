---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

# 『Date Mix & RDt Mix』

![a](Image/DateMix.png)
![a](Image/1.png)

- "Date Mix" is a model created by hierarchical merging based on "anything-v4.5"([andite/anything-v4.0 · Hugging Face](https://huggingface.co/andite/anything-v4.0)).

----

![a](Image/RDtMix.png)
![a](Image/2.png)

- "RDtMix" is a merged realistic model based on "Date Mix".

----

# ◆Discord
[Join Discord Server](https://discord.gg/eN6aSWRddT)

- The merged model community of Hemlok.

----

# ◆About

- This model was created to improve composition and color tone.

- If you like realistic illustrations, please use "RDtModel".

- Sampler: DDIM or DPM++ SDE Karras

- Steps: 50~

- Clipskip: 2

- CFG Scale: 5-12

- Denoise strength: 0.5-0.7(As you like)

- Negative prompts should be as few as possible.
- vae: As you wish. (Any etc. If not used, color may become lighter)

----

# ◆How to use

- Please download the file by yourself and use it with WebUI(AUTOMATIC1111) etc.

- Use the f16 version for Colab(T4) or a PC with low RAM.

----

# ◆Colab Note

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Bsm7p_Db5u3IiHr3YjTeKu4jOllfTyqZ?usp=sharing)
- (I have not checked the operation but it probably works.)

----

# ◆Comparison

<img src="https://i.imgur.com/fW2cPsY.jpg" width="1700" height="">

<img src="https://i.imgur.com/0k48okp.jpg" width="1700" height="">

```
kawaii, 1girl, looking at viewer, smile
```

----

<img src="https://i.imgur.com/d44iIvs.jpg" width="1700" height="">

```
(morning), (school), 1girl, solo, looking at viewer, cowboy shot, (school uniform), smile, black hair, stockings
```

----

# ◆Sampler & CFG Scale
<img src="https://i.imgur.com/vzUBzmw.jpg" width="1700" height="">

```
(morning), (school), 1girl, solo, looking at viewer, cowboy shot, (school uniform), smile, black hair, stockings
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