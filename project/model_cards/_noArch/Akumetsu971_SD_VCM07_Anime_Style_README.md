---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---


# SD_VCM07_Anime_Style is an open source Stable Diffusion Embedding on art style of VCM07, by Akumetsu971 (https://www.tiktok.com/@akumetsu971)
---

### Model used to train: 

wd-v1-3-full-opt.ckpt (https://huggingface.co/hakurei/waifu-diffusion-v1-3)

### Files 
3 files available (Best version is V2):

-VCM07_style - 4000 steps (more focused on girl)

-VCM07_style2 - 4000 steps (allowed to create animals)

-Prompt_Blending Script (optional, used for prompt)

### Prompt 

You need to use DeepDanBooru Tags (https://gigazine.net/gsc_news/en/20221012-automatic1111-stable-diffusion-webui-deep-danbooru/) 

Elysium_Anime_V2.ckpt (https://huggingface.co/hesw23168/SD-Elysium-Model)

Prompt_blending script (https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/tree/main)

Embedding was trained with images of girls only. Therefore, getting a boy can be difficult. Adjust weight, negative prompt, etc...

### Human Example 

Positive Prompt:

(VCM07_style2:1.0), (1girl:1.2), looking_at_viewer, (best quality), (masterpiece:1.2), (ultra-detailed),(official art),(an extremely delicate and beautiful), (attractive:1.2), (beautiful detailed eyes), (dynamic colours, vibrant colours), depth of field, god rays, dynamic lighting
Negative Prompt:

(mediocre:1.2), (average:1.2), (bad:1.2), (wrong:1.2), (error:1.2), (fault:1.2),( badly_drawn:1.2), (poorly_drawn:1.2), ( low_quality:1.2), no_quality, bad_quality, no_resolution, low_resolution, (lowres:1.2), normal_resolution, (disfigured:1.6), (deformed:1.4), (distortion:1.2), bad_anatomy, (no_detail:1.2), low_detail, normal_detail, (scribble:1.2), (rushed:1.2), (unfinished:1.2), blur, blurry, claws, (misplaced:1.2), (disconnected:1.2), nonsense, random, (noise:1.2), (deformation:1.2), 3d, dull, boring, uninteresting, screencap, (text:1.2), (frame:1.1), (out_of_frame:1.2), (title:1.2), (description:1.3), (sexual:1.2), text, error,(logo:1.3), (watermark:1.3), bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, (mutated_hand:1.2), (extra_finger:1.2), (missing_finger:1.2), broken_finger, (fused_fingers:1.2), extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, (extra_digit:1.2), (fewer_digits:1.2), elves_ears, (naked:1.3), (wet:1.2), uncensored, (long_neck:1.2), (weapon:1.5)

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/06756-3422664593-(VCM07_style_1.2)%2C%20close-up%2C%20portrait%2C%201girl%2C%20(solo_1.2)%2C%20single%2C%20black_hair%2C%20blue_eyes%2C%20%20long_hair%2C%20looking_at_viewer%2C(best%20qua.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/07023-1420035308-(VCM07_style2_1.0)%2C%20(1girl_1.2)%2C%20looking_at_viewer%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(official%20art)%2C(an%20extre.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/07045-3879379165-(VCM07_style2_1.0)%2C%201girl%2C%20(pink_hair_1.8)%2C%20(solo_1.2)%2C%20looking_at_viewer%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/06785-1732689013-(VCM07_style_1.2)%2C%20close-up%2C%20portrait%2C%20(solo_1.4)%2C%20(1girl%2C)%2C%20(fox_1.6)%2C%20single%2C%20(pink_hair_1.6)%2C%20blue_eyes%2C%20%20long_hair%2C%20looking_.png" width="50%"/>

### Animals Example 

For V2, embedding was trained with dogs, cats, foxes. Therefore, it is easier to get these animals. However, it is possible to get frogs, elephants, tigers, lions, etc... I used a method with blend prompt script then I described the anatomy of the animal: eyes, ears, nose, fur, etc...

Positive Prompt:

(VCM07_style2:1.0), (cat:1.4|dog:0.5|fox:0.5), (cat_nose:1.2), (cat_eyes:1.2), (cat_ears:1.2), (solo:1.2), looking_at_viewer, (best quality), (masterpiece:1.2), (ultra-detailed),(official art),(an extremely delicate and beautiful), (attractive:1.2), (beautiful detailed eyes), (dynamic colours, vibrant colours), depth of field, god rays, dynamic lighting
Negative Prompt:

(mediocre:1.2), (average:1.2), (bad:1.2), (wrong:1.2), (error:1.2), (fault:1.2),( badly_drawn:1.2), (poorly_drawn:1.2), ( low_quality:1.2), no_quality, bad_quality, no_resolution, low_resolution, (lowres:1.2), normal_resolution, (disfigured:1.6), (deformed:1.5), (distortion:1.2), bad_anatomy, (no_detail:1.2), low_detail, normal_detail, (scribble:1.2), (rushed:1.2), (unfinished:1.2), blur, blurry, claws, (misplaced:1.2), (disconnected:1.2), nonsense, random, (noise:1.2), (deformation:1.2), 3d, dull, boring, uninteresting, screencap, (text:1.2), (frame:1.1), (out_of_frame:1.2), (title:1.2), (description:1.3), (sexual:1.2), text, error,(logo:1.3), (watermark:1.3), bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, (mutated_hand:1.2), (extra_finger:1.2), (missing_finger:1.2), broken_finger, (fused_fingers:1.2), extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, (extra_digit:1.2), (fewer_digits:1.2), elves_ears, (naked:1.3), (wet:1.2), uncensored, (long_neck:1.2)

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/07031-4095215986-(VCM07_style2_1.0)%2C%20(cat_1.4_dog_0.5_fox_0.5)%2C%20(cat_nose_1.2)%2C%20(cat_eyes_1.2)%2C%20(cat_ears_1.2)%2C%20(solo_1.2)%2C%20looking_at_viewer%2C%20(b.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/06915-1261422051-(VCM07_style2_1.0)%2C%20(cat_0.5_lion_0.5_dog_0.5_fox_1.2)%2C%20looking_at_viewer%2C%20(best%20quality)%2C%20(masterpiece_1.2)%2C%20(ultra-detailed)%2C(.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/06994-2098824635-(VCM07_style2_1.0)%2C%20(cat_0.5_lion_0.5_dog_0.5_fox_0.5_tiger_1.4)%2C%20(tiger_ears_1.4)%2C%20(tiger_nose_1.4)%2C%20(white_tiger_1.4)%2C%20(white_.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_VCM07_Anime_Style/resolve/main/06961-2420141730-(VCM07_style2_1.1)%2C%20(cat_0.5_lion_0.5_dog_0.5_fox_0.5_monkey_1.4)%2C%20(monkey_ears_1.4)%2C%20(monkey_nose_1.4)%2C%20looking_at_viewer%2C%20(bes.png" width="50%"/>


```
