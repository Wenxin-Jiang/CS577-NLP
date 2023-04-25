---
license: openrail++
thumbnail: "https://huggingface.co/Verah/ai-protest-anime/resolve/main/s0.webp"
tags:
- stable-diffusion
- text-to-image
inference: false
---

# "AI Protest" Anime Model

![Sample Image](s0.webp)

This model has been trained to simulate what it may be like if the current (December 2022) artstation protest images against AI were actually used as training data inside a conventional anime stable diffusion model.

For version 2, I trained two dreambooth models on the AI Protest imagery at 576px and 704px for 6k steps each. These unique models were then 50/50 merged. The intent behind this is regularization. The key word is still **ai protest**


Version 1 was a quick and dirty DreamBooth model trained without regularization for 3023 steps. the key word is **ai protest**, simply use it in your prompt. **you may wish to increase the weight and/or duplicate it, as the influence is quite weak.**

The base model (of both versions) is an early preview of WD1.4 (colloquially "WD 1.3.5") [wd-1-4-float32-booru-110k](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/9fa4a42a9c4a0948472fa909e6c1a39be0dda699/models/wd-1-4-float32-booru-110k.ckpt) This means you should probably be using danbooru-style image tags in your prompts


## new samples (model version 2)
negative prompt (for all):
- traditional media, graphite medium, ugly, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, lowres, bad anatomy, bad hands, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, username, blurry, bad feet, sketch

if you add `flat color, flat shading` to the negative prompt you can get uncanny early CG-like images.

prompts for the header images: 
- (ai protest:1.3), [:1girl, finely detailed, beautiful, arknights, ruins, still life, text, (ai protest), solo, long hair, white hair, red eyes, headgear:0.24]
- (ai protest:1.3), [:1girl, finely detailed, (cowboy shot), beautiful, arknights, ruins, still life, text, (ai protest), solo, long hair, white hair, red eyes, headgear:0.1]
- (ai protest:1.3), [:1girl, (upper body:1.2), finely detailed, beautiful, arknights, ruins, still life, text, (ai protest:1.3), solo, long hair, white hair, red eyes, headgear:0.4]

*I regularly use the prompt editing feature of automatic's UI. the fundamental syntax is for example: `[A:B:0.1]` this would be interprited as prompt A for the first 10% of samples, then after which it would become prompt B. In the examples above I am omitting any prompt A. With this method it will first draw the AI Protest sign, then add the anime girl to it after*

![Sample Image](s1.webp)
- (ai protest:1.4), [:1girl, bangs, black hair, blazer, flower, grey jacket, hair flower, hair ornament, jacket, long hair, looking at viewer, portrait, purple eyes, school uniform, solo, swept bangs, twintails, upper body, white background, idolmaster, idolmaster shiny colors, fukumaru koito, ruins, text, (ai protest:1.2):0.15]
- (ai protest:1.2), [:1girl, bangs, black hair, blazer, flower, grey jacket, hair flower, hair ornament, jacket, long hair, looking at viewer, portrait, purple eyes, school uniform, solo, swept bangs, twintails, upper body, white background, idolmaster, idolmaster shiny colors, fukumaru koito, text, (ai protest:1.2):0.15]
- (ai protest:1.3), [:1girl, armband, bangs, bare shoulders, belt, black gloves, black hair, black shirt, blue eyes, breasts, coat, cropped legs, floating hair, gloves, hair between eyes, long hair, long sleeves, mask, medium breasts, midriff, mouth mask, no headwear, no navel, open clothes, open coat, shirt, sleeveless, sleeveless shirt, solo, stomach, upper body, white coat, blue archive, saori \(blue archive\), ai protest:0.1]
- (ai protest:1.3), [:1girl, bangs, black dress, closed mouth, cropped torso, dress, green eyes, green hair, long sleeves, looking at viewer, medium hair, simple background, solo, upper body, wavy hair, white background, one-punch man, tatsumaki, ai protest:0.1]

Other tips: You don't neccessarily need to use the prompt editing trick, I just like it. A second pass in img2img or via enabling highres fix can improve the fidelity of outputs.


## old samples (model version 1)

![Sample Image](01.webp)
(ai protest:1.3), 1girl, mecha musume, headgear, (ai protest:1.3), (masterpiece), (best quality), (ultra-detailed), best illustration, (extremely delicate and beautiful), (ai protest:1.3)

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad feet


![Sample Image](02.webp)
(ai protest:1.3), 1girl, upper body, mecha musume, headgear, (ai protest:1.3)


![Sample Image](04.webp)
(ai protest:1.2), 1girl, bangs, black dress, closed mouth, cropped torso, dress, green eyes, green hair, long sleeves, looking at viewer, medium hair, simple background, solo, upper body, wavy hair, white background, one-punch man, tatsumaki


![Sample Image](05.webp)
(ai protest:1.3), 1girl, mecha musume, headgear, (ai protest:1.3), (masterpiece), (best quality), (ultra-detailed), best illustration, (extremely delicate and beautiful), (ai protest:1.3)


![Sample Image](06.webp)
(ai protest:1.6), mordred \(fate\) wears armor fighting, sword,

Negative prompt: (missing digits:1.5), (extra digits:1.5), extra limb, bad art, incomplete, weird colors, blurry, poorly drawn, deformed, cartoon, b&w, missing limbs, inconsistent, multiple girls, 1boy, male, 2boys, short hair, hu tao, lumine, keqing, shenhe, mona, eula, yelan, beidou, contorted, signature, watermark, username, blurry, artist name, symmetrical, bad hands, jpeg artifacts, error, pixelated, multiple girls, 2girls, 3girls,


![Sample Image](08.webp)
(ai protest:1.3), 1girl, upper body, mecha musume, headgear, (ai protest:1.3), (masterpiece), (best quality), (ultra-detailed), best illustration, (extremely delicate and beautiful)

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad feet

![Sample Image](09.webp)
ai protest, 1girl, tattoo, masterpiece, best quality, ultra-detailed, illustration