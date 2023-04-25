---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
---

# EVA-Fusion 2.22 - You are (Not) HD

for an art project of mine

| model | init model | lr | bs | acc | total steps | training samples | training resolution | models trained |
|--- |--- | --- | --- | --- | --- | --- | --- | --- |
| eva-fusion-v2 |compvis 1-4| 2.057e-06 | 1 | 1 | 8,000 | 1,143 (captioned just "picture in the style of evangelion") | 512x384 (4:3) | unet |
| eva-fusion-v2.1 | eva-fusion-v2 | 1.313e-06 | 1 | 1 | 10,000 | + 560 (hand captioned) | 512x384 (4:3) | unet |
| eva-fusion-v2.22 "you are (not) HD" | previous models + compvis1-4 + wd1.3 at various ratios | x | x | x | x | x | x | x |

for generating let me suggest [Whatchamacallit](https://colab.research.google.com/github/aicrumb/whatchamacallit/blob/main/Whatchamacallit.ipynb), suggested in the negative prompt: "blurry jpeg, multiple views, simple background, black and white reference sheet".

it wasn't trained on black and white character sheets, it was barely trained on any grayscale images, I do not know why it leans heavily towards them sometimes.

link to ckpt file: https://huggingface.co/crumb/eva-model-ckpt/blob/main/test%20model%205.ckpt

I also recommend "in the style of Evangelion" in the prompt