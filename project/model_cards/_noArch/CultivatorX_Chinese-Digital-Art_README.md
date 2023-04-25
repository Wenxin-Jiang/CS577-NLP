---
language:
- en

thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1670742434498-633a20a88f27255b6b56290b.png"

license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

# Chinese Digital Art Diffusion 
**Trigger Words: CNDigitalArt Style**

This is a fine-tuned Stable Diffusion model trained on some of the **Chinese Digital Arts** style that usually uses on Chinese Interactive Reading (Visual Novel) platforms such as **Orange Light** [66rpg.com](https://66rpg.com) or **NetEase Interactive Reading Platform** [avg.163.com](https://avg.163.com/). 
_if you don't know what that is, don't worry, it's just one of those really big thing in China that majority of Westerners had no clue about._
![Trained.png](https://s3.amazonaws.com/moonup/production/uploads/1670748193502-633a20a88f27255b6b56290b.png)


Use the tokens **_CNDigitalArt Style_** in your prompts to test and experiment it yourself.

**EXAMPLES:**
_These results were tested on the 2000 Steps model [ **CNDigitalArt_2000.ckpt**](https://huggingface.co/CultivatorX/Chinese-Digital-Art/blob/main/CNDigitalArt_2000.ckpt).
I just did 20 batches of -1 seeds in random for each of the prompt (most of which isn't that good) but it does have some really good ones.

Prompt: **a portrait of Megan Fox in CNDigitalArt Style**

Negative prompt: _lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, two faces, two heads_
Steps: 20, Sampler: Euler, CFG scale: 7, Seed: 593563256, Face restoration: GFPGAN, Size: 512x512, Model hash: 2258c119
![Scarlett Fox.png](https://s3.amazonaws.com/moonup/production/uploads/1670742434498-633a20a88f27255b6b56290b.png)
Prompt: **a portrait of Scarlett Johansson in CNDigitalArt Style**

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, two faces, two heads
Steps: 20, Sampler: Euler, CFG scale: 7, Seed: 4272335413, Face restoration: GFPGAN, Size: 512x512, Model hash: 2258c119
=====================================================================
=====================================================================

Prompt: **a portrait of Emma Watson in CNDigitalArt Style**

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, two faces, two heads
Steps: 20, Sampler: Euler, CFG scale: 7, Seed: 3813059825, Face restoration: GFPGAN, Size: 512x512, Model hash: 2258c119
![Emma Zendeya.png](https://s3.amazonaws.com/moonup/production/uploads/1670742782225-633a20a88f27255b6b56290b.png)
Prompt: **a portrait of Zendaya in CNDigitalArt Style**

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, two faces, two heads
Steps: 20, Sampler: Euler, CFG scale: 7, Seed: 962052606, Face restoration: GFPGAN, Size: 512x512, Model hash: 2258c119