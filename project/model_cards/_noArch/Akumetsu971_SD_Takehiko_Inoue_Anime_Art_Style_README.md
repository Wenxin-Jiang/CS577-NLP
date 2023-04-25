---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---


# SD_Takehiko_Inoue_Anime_Art_Style is an open source Stable Diffusion Embedding on art style of the Mangaka Takehiko Inoue, by Akumetsu971 (https://www.tiktok.com/@akumetsu971)
---

### Model used to train: 

wd-v1-3-full-opt.ckpt (https://huggingface.co/hakurei/waifu-diffusion-v1-3)

### Files 
2 files available (trained at 4000steps):

-Vgbnd_style - 4000 steps (deterministic method, style is strong and hard to control)

-Vgbnd_style2 - 4000 steps (once method, recommended)


### Prompt 

You need to use DeepDanBooru Tags (https://gigazine.net/gsc_news/en/20221012-automatic1111-stable-diffusion-webui-deep-danbooru/)

And Elysium_Anime_V2.ckpt (https://huggingface.co/hesw23168/SD-Elysium-Model)

### Example 

Positive Prompt:

(Vgbnd_style2:1.0), (1boy:1.2), attractive, (solo:1.2), portrait, (best quality), (masterpiece:1.2), (ultra-detailed),(official art),(an extremely delicate and beautiful), (beautiful detailed eyes), (dynamic colours, vibrant colours), depth of field, god rays, dynamic lighting, (monochrome:1.2), greyscale

Negative Prompt:

(mediocre:1.2), (average:1.2), (bad:1.2), (wrong:1.2), (error:1.2), (fault:1.2),( badly_drawn:1.2), (poorly_drawn:1.2), ( low_quality:1.2), no_quality, bad_quality, no_resolution, low_resolution, (lowres:1.2), normal_resolution, (disfigured:1.6), (deformed:1.6), (distortion:1.2), bad_anatomy, (no_detail:1.2), low_detail, normal_detail, (scribble:1.2), (rushed:1.2), (unfinished:1.2), blur, (blurry:1.4), claws, (misplaced:1.2), (disconnected:1.2), nonsense, random, (noise:1.2), (deformation:1.3), 3d, dull, boring, uninteresting, screencap, (text:1.2), (frame:1.1), (out_of_frame:1.2), (title:1.2), (description:1.3), (sexual:1.2), text, error,(logo:1.3), (watermark:1.3), bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, (mutated_hand:1.2), (extra_finger:1.2), (missing_finger:1.2), broken_finger, (fused_fingers:1.3), extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, (extra_digit:1.3), (fewer_digits:1.3), elves_ears, (naked:1.3), (wet:1.2), uncensored, (long_neck:1.2), blurry_background, monochrome, (grainy:1.4), greyscale,

<img src="https://huggingface.co/Akumetsu971/SD_Takehiko_Inoue_Anime_Art_Style/resolve/main/06687-1426260890-(Vgbnd_style2_1.0)%2C%201boy%2C%20(breast_1.3)%2C%20(solo_1.2)%2C%20portrait%2C%20(light_dress_1.2)%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detai.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Takehiko_Inoue_Anime_Art_Style/resolve/main/06690-1426260890-(Vgbnd_style2_1.0)%2C%201boy%2C%20(solo_1.2)%2C%20portrait%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(official%20art)%2C(an%20extremely.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Takehiko_Inoue_Anime_Art_Style/resolve/main/06709-948062698-(Vgbnd_style2_1.0)%2C%20(1girl_1.2)%2C%20attractive%2C%20(solo_1.2)%2C%20portrait%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(official.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Takehiko_Inoue_Anime_Art_Style/resolve/main/06710-948062699-(Vgbnd_style2_1.0)%2C%20(1girl_1.2)%2C%20attractive%2C%20(solo_1.2)%2C%20portrait%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(official.png" width="50%"/>


### Other 

I trained the model with more male images than female images. Therefore, you can get result as bellow. The trick is to adjust Embedding weight: Vgbnd_style2(0.8)
Or to add in negative prompt (male_focus:1.5), (mustache:1.4)

<img src="https://huggingface.co/Akumetsu971/SD_Takehiko_Inoue_Anime_Art_Style/resolve/main/06697-3671910494-(Vgbnd_style2_1.0)%2C%201girl%2C%20attractive%2C%20(solo_1.2)%2C%20portrait%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(official%20art)%2C.png" width="50%"/>


```
