---
license: creativeml-openrail-m
language:
- en
thumbnail: "https://huggingface.co/Norod78/sd21-hearthstone-cards/resolve/main/sample_images/00005-166904889-Snoop%20Dogg%20music%20power%20Hearthstone%20card.png"
tags:
- text-to-image
- stable-diffusion
- stable-diffusion-diffusers
datasets:
- Norod78/hearthstone-cards-512
inference: true
widget:
- text: 3 Cute dog, Fluff. Hearthstone card
- text: Gal Gadot Super Wonderwoman power. Hearthstone card
- text: Cute Pikachu Pokemon Electricity buzzzz Hearthstone card
- text: 4 Snoop Dogg music power Hearthstone card
library_name: diffusers
pipeline_tag: text-to-image
---

# SDv2.1 sd21-hearthstone-cards model
### Stable-Diffusion v2.1 fine-tuned for 10k steps using [Huggingface Diffusers train_text_to_image script](https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image.py)  upon [Norod78/hearthstone-cards-512](https://huggingface.co/datasets/Norod78/hearthstone-cards-512)
# Stable-Diffusion Hearthstone card generator. First digit in prompt controls the Mana-cost (pretty well) then card name, then special ability and description, then "Hearthstone card".

![thumbnail](https://huggingface.co/Norod78/sd21-hearthstone-cards/resolve/main/sample_images/sd21-hearthstone-cards-animation-GalGadot.gif)

## A few sample pictures generated with this model are available [here](https://huggingface.co/Norod78/sd21-hearthstone-cards/tree/main/sample_images)

Please note that the entire training set contains actual Hearthstone card images which are copyrighted by Blizzard
So it is possible that the generated images contain copyrighted elements and should only be use for your private entertainment 

Trained by [@Norod78](https://twitter.com/Norod78)