---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
---

Example result:
===============
# Using whitemanedb_step_3500.ckpt
![whitemanedb_step_3500 1](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/tmpez9ubybz.png)
# Using dbwhitemane.ckpt
![image1 1](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/tmp45mql4vt.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/01019-2983591336-dbwhitemane%20standing%20at%20a%20rooftop%20looking%20over%20the%20city%2C%20night%2C%20cowboy%20shot%2C%20foggy%2C%20city%20lights%2Cdramatic%20lighting%2C%208k%2C%204k%2C%20(high.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/01068-2365801682-sbwhitemane%20taking%20a%20bath%2C%208k%2C%204k%2C%20(highres_1.1)%2C%20best%20quality%2C%20(masterpiece_1.3)%2C%20(red%20eyes_1.2)%2C%20blush%2C%20embarrassed.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/01095-1501953711-sbwhitemane%20leaning%20forward%2C%20princess%2C%201girl%2C%20solo%2Celf%20in%20forest%20%2C%20leather%20armor%2C%20large%20eyes%2C%20(ice%20green%20eyes_1.1)%2C%20lush%2C%20%20blond.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/01099-3504900055-leaning%20forward%2C%20princess%2C%201girl%2C%20solo%2C%20sbwhitemane%20%20in%20forest%20%2C%20leather%20armor%2C%20large%20eyes%2C%20lush.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/01103-1390776440-leaning%20forward%2C%20princess%2C%201girl%2C%20solo%2C%20sbwhitemane%20%20in%20forest%20%2C%20leather%20armor%2C%20large%20eyes%2C%20lush.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/05248-2547952708-whitemanedb%20in%20a%20forestns_l89cu.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/05253-2547952705-whitemanedb_in_a_forest28dbdxct.png)
![image2 2](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/05260-2547952708-whitemanedb_in_a_forest4ud2iio1.png)


Clip skip comparsion

![clip 1](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/resolve/main/concept_images/xy_grid-0005-3724517679.png)

I uploaded for now 3 models (more incoming for whitemane):
-[whitemanedb_step_2500.ckpt](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/blob/main/whitemanedb_step_2500.ckpt)
-[whitemanedb_step_3500.ckpt](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/blob/main/whitemanedb_step_3500.ckpt)
Are trained with 21 images and the trigger is "whitemanedb", this is my first attempts and I didn't get the final file because I ran out of space on drive :\ but model seems to work just fine.

The second model is [dbwhitemane.ckpt](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/blob/main/dbwhitemane.ckpt)
This one has a total of 39 images used for training that you can find [here](https://huggingface.co/sd-dreambooth-library/sally-whitemanev/tree/main/dataset)

**Model is based on AnythingV3 FP16 [38c1ebe3]
And so I would recommend to use a VAE from NAI, Anything or WaifuDiffusion**
**Also set clip skip to 2 will help because its based on NAI model**

# Promt examples

This one is for the comparsion on top
> whitemanedb , 8k, 4k, (highres:1.1), best quality, (masterpiece:1.3), (red eyes:1.2), blush, embarrassed
> Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, deformed face, (poorly drawn face)),((buckteeth)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), 1boy,
> Steps: 45, Sampler: Euler a, CFG scale: 7, Seed: 772493513, Size: 512x512, Model hash: 313ad056, Eta: 0.07, Clip skip: 2

> whitemanedb taking a bath, 8k, 4k, (highres:1.1), best quality, (masterpiece:1.3), (red eyes:1.2), nsfw, nude, blush, nipples,
> Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, deformed face, (poorly drawn face)),((buckteeth)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), 1boy,
> Steps: 45, Sampler: Euler a, CFG scale: 7, Seed: 3450621385, Size: 512x512, Model hash: 313ad056, Eta: 0.07, Clip skip: 2

> whitemanedb in a forest
> Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, deformed face
> Steps: 35, Sampler: Euler a, CFG scale: 10.0, Seed: 2547952708, Size: 512x512, Model hash: 313ad056, Eta: 0.07, Clip skip: 2

> lying in the ground , princess, 1girl, solo, sbwhitemane in forest , leather armor, red eyes, lush
> Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, deformed face, (poorly drawn face)),((buckteeth)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), 1boy,
> Steps: 58, Sampler: Euler a, CFG scale: 7, Seed: 1390776440, Size: 512x512, Model hash: 8b1a4378, Clip skip: 2

> sbwhitemane leaning forward, princess, 1girl, solo,elf in forest , leather armor, large eyes, (ice green eyes:1.1), lush, blonde hair, realistic photo
> Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, deformed face, (poorly drawn face)),((buckteeth)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), 1boy,
> Steps: 45, Sampler: Euler a, CFG scale: 7, Seed: 1501953711, Size: 512x512, Model hash: 8b1a4378, Clip skip: 2

Enjoy, any recommendation or help is welcome, this is my first model and probably a lot of things can be improved! 