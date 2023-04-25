---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---


# FloralMarble-WOKE_EDITION-SD2.x is an open source Stable Diffusion Model and embedding to create colorful and creative bust, by Akumetsu971 (https://www.tiktok.com/@akumetsu971)
---

### What for ?: 

Bust, statue with any type of skin color. Mainly trained for humans but may generate cats, lions, panther if you push it.

Dreambooth Model will give you only black women. To lighten it a little, I add another version mixed with custom model.

Embedding can give you any kind of skin color.

### Training: 

DreamBooth model was based on v2-1_512-ema-pruned.ckpt trained on 60 images at 1e-5 lr

Embedding was trained for around 500 epochs/steps. 38 images, 4 vectors. Batch size of 1, 5 grad acc steps, learning rate of 0.0020 for 3500steps.

### Files 

Files available :

-Black_MarbleV2_step_2000-001.ckpt + Black_MarbleV2_step_2000-001.yaml (recommanded)

-Black_MarbleV2_step_2000-001_0.5-SaimaSD2.1_0.5-Weighted_sum-merged.ckpt + Black_MarbleV2_step_2000-001_0.5-SaimaSD2.1_0.5-Weighted_sum-merged.yaml

-Black_MarbleV2_step_2500.ckpt + Black_MarbleV2_step_2500.yaml

-Black_MarbleV2_step_2500_0.5-SaimaSD2.1_0.5-Weighted_sum-merged.ckpt + Black_MarbleV2_step_2500_0.5-SaimaSD2.1_0.5-Weighted_sum-merged.yaml

-FloralMarble-WOKE_EDITION_embeddings.7z (embedding from step 100 to 3500, steps from 1500 to 2500 seem to give the best result but dont ask me why, all step from 100 to 3500 give good results)

-Upscalers(4x_fatal_Anime_500000_G, 4x-AnimeSharp, 4x_NMKD-Siax_200k)

-Embedding_dataset.7z and Dreambooth_dataset.zip - If you want to train your own model and embedding with my images


### Prompt tips 

You may use DeepDanBooru Tags (https://gigazine.net/gsc_news/en/20221012-automatic1111-stable-diffusion-webui-deep-danbooru/) 

You may use FloralMarble for SD 2.x embedding (https://huggingface.co/spaablauw/FloralMarble)

If the image is blurry, use an upscaler like: 4x_fatal_Anime_500000_G, 4x-AnimeSharp, 4x_NMKD-Siax_200k (they are all in Files and Version)

Keyword for the dreambooth model is "Blck_Mrbl". Use it if you need to strengthen the style.

You may change the weight of embedding, mix it with the dreambooth model or another embedding.


### Examples for Dreambooth model

Positive Prompt:

Bust of black woman in black_marble, black_marble_sculpture, (flower petals:1.2), water flow hyperfluid, gold powder, gold earrings, gold lips, (bubbles floating:1.2), looking at the camera, beautiful and aesthetic, close up, pretty, dramatic pose, intricate, highly detailed, detailed face, smooth, sharp focus, specular light, occlusion shadow, rim light

Negative Prompt:

mediocre, average, bad, wrong, error, fault, badly_drawn, poorly_drawn, low_quality, no_quality, bad_quality, no_resolution, low_resolution, lowres, normal_resolution, disfigured, deformed, distortion, bad_anatomy, no_detail, low_detail, normal_detail, scribble, rushed, unfinished, blur, blurry, claws, misplaced, disconnected, nonsense, random, noise, deformation, 3d, dull, boring, uninteresting, screencap, text, frame, out_of_frame, title, description, sexual, text, error, logo, watermark, bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, mutated_hand, extra_finger, missing_finger, broken_finger, fused_fingers, extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, extra_digit, fewer_digits, elves_ears, naked, wet, uncensored, long_neck, beads 

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/6_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/5_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/4_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/3_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/2_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/1_Image_Example.png" width="50%"/>

### Examples for Embedding

Positive Prompt:

EMB_Black_Marble_Style_V5-3000, (Bust:1.2), (1blackgirl:1.2), black_marble, (dark_skin:1.2), (floating_bubles:1.1), (water_splash:1.3), (milk_splash:1.2), (splash_art:1.3), looking at the camera, beautiful and aesthetic, close up, pretty, dramatic pose, intricate, highly detailed, detailed face, smooth, sharp focus, specular_light, occlusion_shadow, rim_light, (ULTRA-HD:1.2), 8K, unreal_engine_5, (translucent_white_smoke_cloud on background:1.3), (neon_light:1.1)

Negative Prompt:

mediocre, average, bad, wrong, error, fault, badly_drawn, poorly_drawn, low_quality, no_quality, bad_quality, no_resolution, low_resolution, lowres, normal_resolution, disfigured, deformed, distortion, bad_anatomy, no_detail, low_detail, normal_detail, scribble, rushed, unfinished, blur, blurry, claws, misplaced, disconnected, nonsense, random, noise, deformation, 3d, dull, boring, uninteresting, screencap, text, frame, out_of_frame, title, description, sexual, text, error, logo, watermark, bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, mutated_hand, extra_finger, missing_finger, broken_finger, fused_fingers, extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, extra_digit, fewer_digits, elves_ears, naked, wet, uncensored, long_neck, beads 

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/7_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/13_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/9_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/10_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/11_Image_Example.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/FloralMarble-WOKE_EDITION-SD2.x/resolve/main/12_Image_Example.png" width="50%"/>
