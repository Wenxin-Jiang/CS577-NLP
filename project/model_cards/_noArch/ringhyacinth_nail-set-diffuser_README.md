---
license: openrail
tags:
- text-to-image
- dreambooth-hackathon
- wildcard
- diffusers
---

# 💅 Nail Set Diffusion

This is the fine-tuned Stable Diffusion model trained on images from Nail Sets. 

Use the tokens {Nail Set} in your prompts for the effect.

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Nail-set-Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/ringhyacinth/Nail-Diffuser)


__Stable Diffusion fine tuned on Nail Set by [Weekend](https://weibo.com/u/5982308498) and [Hyacinth](https://twitter.com/ring_hyacinth).__

Put in a text prompt and generate your own nail set!

![image.png](https://cdn.discordapp.com/attachments/973053077672325120/1043909385891610674/fe869dbd7be07b59f284370645d7143.png)

> Nail Set, Sunflower (/Irises/Starry Night/Self Portrait) by Van Gogh, Van Gogh color scheme 

![image.png](https://cdn.discordapp.com/attachments/973053077672325120/1043908810613473321/b1e3d1f76c530f6a23ee2116dc9f01a.png)

> Nail Set, hamilton nail, broadway musical theme nail.

![image.png](https://cdn.discordapp.com/attachments/973053077672325120/1043910797694349312/bcac02c6ff64419f2df503b367561be.png)

> Nail Set, chinese new year nail, super detailed

![image.png](https://cdn.discordapp.com/attachments/973053077672325120/1043911547703001128/0f8faaf6b91e82bb23dc5d1a5c85223.png)

> Nail Set, thanksgiving nail, super detailed

![image.png](https://cdn.discordapp.com/attachments/973053077672325120/1043914949887524894/a4f3c62d7d1e47ae118a4bb4772f4e5.png)

> Nail set, Disney castle nail, cute Japanese girly nail

## Model description

Trained on [CLIP Ineterrogator captioned dataset](https://huggingface.co/spaces/pharma/CLIP-Interrogator) 

Using [EveryDream Finetune Script](https://github.com/victorchall/EveryDream-trainer) for around 10,000 step.