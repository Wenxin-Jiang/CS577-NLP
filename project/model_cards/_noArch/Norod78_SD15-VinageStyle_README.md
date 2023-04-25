---
license: creativeml-openrail-m
language: 
  - en
thumbnail: "https://huggingface.co/Norod78/SD15-VinageStyle/resolve/main/sample_images/SD15-VintageStyle-Thumbnail.jpg"
tags:
- text-to-image
- stable-diffusion
- stable-diffusion-diffusers
datasets:
- Norod78/vintage-blip-captions
inference: true
widget:
- text: A Pulp Cover featuring Gal Gadot, very detailed, clean, high quality, sharp image, Saturno Butto
- text: A photo of an astronaut riding a horse on mars, Vintage style, Pulp Cover, very detailed, clean, high quality, sharp image, Dave Dorman
- text: A beatiful person, Vintage face
- text: A Vintage style commercial for cat food

---

# SDv1.5 SD15-VinageStyle model, trained by Norod78 in two parts.
### First Stable-Diffusion v1.5 fine-tuned for 10k steps using [Huggingface Diffusers train_text_to_image script](https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image.py)  upon [Norod78/vintage-blip-captions](https://huggingface.co/datasets/Norod78/vintage-blip-captions) then it underwent further fine tuning with Dreambooth using the same images as the ones in the dataset  but rather then having it blip-captioned, it was split into "Vintage style", "Vintage face" and "Pulp cover" concepts. 
### Dreambooth model was trained with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook

## Because the model was first fined-tuned on the whole dataset and only then it was fine-tuned again to learn each individual concept, you can use prompts without Trigger-Words and still get a subtle "Vintage" touch

# Trigger-Words are: "Vintage", "Vintage style", "Vintage face", "Pulp cover"

![thumbnail](https://huggingface.co/Norod78/SD15-VinageStyle/resolve/main/sample_images/SD15-VintageStyle-Thumbnail.jpg)

## A few sample pictures generated with this mode (more available [here](https://huggingface.co/Norod78/SD15-VinageStyle/tree/main/sample_images)):

A photo of Gal Gadot as wonderwoman, Vintage style, very detailed, clean, high quality, sharp image.Negative prompt: grainy, blurry, text, watermark, inconsistent, smudged.Steps: 40, Sampler: DPM++ 2M Karras, CFG scale: 7.5, Seed: 3486356206, Face restoration: CodeFormer, Size: 512x512, Model hash: 33006be6, Model: VintageStyle, Batch size: 4, Batch pos: 2

![1](https://huggingface.co/Norod78/SD15-VinageStyle/resolve/main/sample_images/00186-3486356206-A%20photo%20of%20Gal%20Gadot%20as%20wonderwoman%2C%20Vintage%20style%2C%20very%20detailed%2C%20clean%2C%20high%20quality%2C%20sharp%20image.jpeg)

A photo of Gal Gadot as wonderwoman fighting against Cthulhu, Vintage, very detailed, clean, high quality, sharp image, ,Naoto Hattori.Negative prompt: grainy, blurry, text, watermark, inconsistent, smudged.Steps: 40, Sampler: DPM++ 2M Karras, CFG scale: 7.5, Seed: 3408435550, Face restoration: CodeFormer, Size: 512x512, Model hash: 33006be6, Model: VintageStyle, Batch size: 4, Batch pos: 3

![2](https://huggingface.co/Norod78/SD15-VinageStyle/resolve/main/sample_images/00199-3408435550-A%20photo%20of%20Gal%20Gadot%20as%20wonderwoman%20fighting%20against%20Cthulhu%2C%20Vintage%2C%20very%20detailed%2C%20clean%2C%20high%20quality%2C%20sharp%20image%2C%20%2CNaoto%20H.jpeg)