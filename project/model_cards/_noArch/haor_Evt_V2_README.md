---
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- anime
- diffusers
license: creativeml-openrail-m
---
# Evt_V2
Based on animefull-latest, fine-tuned using a training set of 15000 images (7700 flipped). Most of the training set uses [pixiv_AI_crawler](https://github.com/7eu7d7/pixiv_AI_crawler) to filter the pixiv daily ranking, and then mixes some nsfw animation images.

### Examples
![Image](https://0.00000.link/1121/1669040927.jpg)
![Image](https://0.00000.link/1122/1669088826.png)
![Image](https://0.00000.link/1121/1669041182.jpg)
![Image](https://0.00000.link/1121/1668968933.png)
![Image](https://0.00000.link/1121/1668969239.png)
```
best quality, illustration,highly detailed,1girl,upper body,beautiful detailed eyes, medium_breasts, long hair,grey hair, grey eyes, curly hair, bangs,empty eyes,expressionless, ((masterpiece)),twintails,beautiful detailed sky, beautiful detailed water, cinematic lighting, dramatic angle,((back to the viewer)),(an extremely delicate and beautiful),school uniform,black ribbon,light smile,
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,artist name,bad feet
Steps: 40, Sampler: Euler a, CFG scale: 7, Clip skip: 2
*evt_bs6_ema is the first version of evt
```
![Image](https://0.00000.link/1121/1669040982.jpg)
![Image](https://0.00000.link/1121/1669040981.jpg)
![Image](https://0.00000.link/1121/1668982508.png)
![Image](https://0.00000.link/1121/1668969770.png)
```
{Masterpiece, Kaname_Madoka, tall and long double tails, well rooted hair, (pink hair), pink eyes, crossed bangs, ojousama, jk, thigh bandages, wrist cuffs, (pink bow: 1.2)}, plain color, sketch, masterpiece, high detail, masterpiece portrait, best quality, ray tracing, {:<, look at the edge}
Negative prompt: ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)),extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((bad proportions))), ((extra limbs)), (((deformed))), (((disfigured))), cloned face, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), too many fingers, (((long neck))), (((low quality))), normal quality, blurry, bad feet, text font ui, ((((worst quality)))), anatomical nonsense, (((bad shadow))), unnatural body, liquid body, 3D, 3D game, 3D game scene, 3D character, bad hairs, poorly drawn hairs, fused hairs, big muscles, bad face, extra eyes, furry, pony, mosaic, disappearing calf, disappearing legs, extra digit, fewer digit, fused digit, missing digit, fused feet, poorly drawn eyes, big face, long face, bad eyes, thick lips, obesity, strong girl, beard，Excess legs
Steps: 40, Sampler: Euler a, CFG scale: 6,Clip skip: 2
```