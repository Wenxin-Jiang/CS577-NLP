---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
inference: false
---
Made with a custom merge, won't work with SD 2.x.

Yes it's another one of these negative prompt embeddings, inspired by all the previous ones (bad_prompt, bad-artist, etc.) It's a good idea tbh, if anything just as a meme experiment.

Cherrypicked examples, not enough of them

No embedding:
![01095-1838347573-highly detailed vfx portrait of emma watson as warrior girl, stephen bliss, unreal engine, chrome reflect, greg rutkowski, tom b.png](https://s3.amazonaws.com/moonup/production/uploads/1670907109298-63716cac15aafbe231371caa.png)
![01054-3906507010-a beautiful painting of imogen poots representative of the art style of artgerm and wlop and wes anderson and spike jonze.png](https://s3.amazonaws.com/moonup/production/uploads/1670907207789-63716cac15aafbe231371caa.png)
![01288-69696969-kurisu makise steins gate anime, atmospheric, elegant, smiling, laughing, super highly detailed, professional digital painting,-before-highres-fix.png](https://s3.amazonaws.com/moonup/production/uploads/1670908574598-63716cac15aafbe231371caa.png)

Embedding:
![01096-1838347573-highly detailed vfx portrait of emma watson as warrior girl, stephen bliss, unreal engine, chrome reflect, greg rutkowski, tom b.png](https://s3.amazonaws.com/moonup/production/uploads/1670907109348-63716cac15aafbe231371caa.png)
![01055-3906507010-a beautiful painting of imogen poots representative of the art style of artgerm and wlop and wes anderson and spike jonze.png](https://s3.amazonaws.com/moonup/production/uploads/1670907207778-63716cac15aafbe231371caa.png)
![01286-69696969-kurisu makise steins gate anime, atmospheric, elegant, smiling, laughing, super highly detailed, professional digital painting,-before-highres-fix.png](https://s3.amazonaws.com/moonup/production/uploads/1670908574564-63716cac15aafbe231371caa.png)

Made with my own schizo negs that would get me dingdongbannu just posting and main credit goes to the HD negs from: 
https://huggingface.co/Deltaadams/HentaiDiffusion/blob/main/Universal%20Negative%20Prompt%20Text.txt

What it's not: an actual guaranteed fix for anything

What it is: something that steers outputs towards a certain style and any fixes are just coincidence

Usage:

Put it in negatives with gigaschizonegs, either alone or in between <> (might not be needed anymore), or between parenthesis like (gigaschizonegs:0.8) with a custom value to increase or decrease strenght.

Put it in positives to see the monstruosities that were used to make it.

Trained at 15k steps with 1000+ horrors made with the prompt. Yes I have no idea what I'm doing. I'm only putting this here as an online backup tee bee eich.

I don't like making model cards.