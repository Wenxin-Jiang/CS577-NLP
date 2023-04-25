---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---


# SD_Anime_Futuristic_Armor_Model is an open source Stable Diffusion Model on art style of futuristic armor, by Akumetsu971 (https://www.tiktok.com/@akumetsu971)
---

### What for ?: 

Robot, Android, Mecha, futuristic armor, wepons, etc...

### Model used to train: 

DreamBooth based on Elysium_Anime_V2.ckpt (https://gigazine.net/gsc_news/en/20221012-automatic1111-stable-diffusion-webui-deep-danbooru/)

### Files 
4 files available :

-JhnsT3_step_4000.ckpt - 4000 steps (recommanded, last version I trained on Dreambooth)

-JhnsT3_step_4000_0.8-arcane-diffusion-v3_0.2-Weighted_sum-merged.ckpt - 4000 steps (mixed with an Arcane Diffusion model)

-JhsnT_Style4_step_5000.ckpt - 5000 steps(really good also, train with different images)

-JhsnT_Style4_step_5000_0.8-arcane-diffusion-v3_0.2-Weighted_sum-merged (mixed with an Arcane Diffusion model)

### Prompt 

You need to use DeepDanBooru Tags (https://gigazine.net/gsc_news/en/20221012-automatic1111-stable-diffusion-webui-deep-danbooru/) 

I also used Nixeu_style embedding (not necessary): https://huggingface.co/sd-concepts-library/nixeu)

If the image is blurry, use an upscaller like: 4x_fatal_Anime_500000_G, 4x-AnimeSharp, 4x_NMKD-Siax_200k (they are all in my files)


### Example for JhnsT3_step_4000_0.8-arcane-diffusion-v3_0.2-Weighted_sum-merged.ckpt

Positive Prompt:

(Nixeu_style:1.2), (millipen_(medium):1.3), (crosshatching:1.3), portrait, 1boy, solo, military, science fiction, (full_armor:1.1), male_focus, solo, glowing, (golden_helmet:1.1), detailed_helmet, (art by Agnes Cecile:1.3), high quality, high details, 8k, detailed_background

Negative Prompt:

 (mediocre:1.2), (average:1.2), (bad:1.2), (wrong:1.2), (error:1.2), (fault:1.2),( badly_drawn:1.2), (poorly_drawn:1.2), ( low_quality:1.2), no_quality, bad_quality, no_resolution, low_resolution, (lowres:1.2), normal_resolution, (disfigured:1.6), (deformed:1.6), (distortion:1.2), (bad_anatomy:1.4), (no_detail:1.2), low_detail, normal_detail, (scribble:1.2), (rushed:1.2), (unfinished:1.2), blur, blurry, claws, (misplaced:1.2), (disconnected:1.2), nonsense, random, (noise:1.2), (deformation:1.2), dull, boring, uninteresting, screencap, (text:1.2), (frame:1.1), (out_of_frame:1.2), (title:1.2), (description:1.3), (sexual:1.2), text, error,(logo:1.3), (watermark:1.3), bad_perspective, bad_proportions, cinematic, jpg_artifacts, jpeg_artifacts, extra_leg, missing_leg, extra_arm, missing_arm, long_hand, bad_hands, (mutated_hand:1.2), (extra_finger:1.2), (missing_finger:1.2), broken_finger, (fused_fingers:1.2), extra_feet, missing_feet, fused_feet, long_feet, missing_limbs, extra_limbs, fused_limbs, claw, (extra_digit:1.2), (fewer_digits:1.2), (fused:1.4), (artifacts:1.2), (frame:1.2), (pencil:1.1), (pen:1.1)
 
<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01106-3248021610-(Nixeu_style_1.2)%2C%20(millipen_(medium)_1.4)%2C%20(crosshatching_1.4)%2C%20(sketch_1.1)%2C%201boy%2C%20solo%2C%20military%2C%20science%20fiction%2C%20black_armo.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01107-3191274567-(Nixeu_style_1.2)%2C%20(millipen_(medium)_1.4)%2C%20(crosshatching_1.4)%2C%20(sketch_1.1)%2C%201boy%2C%20solo%2C%20military%2C%20science%20fiction%2C%20black_armo.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01108-293415920-(portrait%20of%20a%20robot%20wolf%20from%20horizon%20zero%20dawn_1.2)%2C%20machine%20face%2C%20upper%20body%2C%20decorated%20with%20chinese%20opera%20motifs%2C%20asian%2C%20tra.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01112-3191254788-.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01113-1742083899-classical_oil_painting%2C%20concept_art%2C%20(realistic_mecha_1.2)%2C%20anime%20key%20visual%20environment%2C%20trending%20on%20artstation%2C%20brush_strokes%2C.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01114-1432628887-classical_oil_painting%2C%20concept_art%2C%20(realistic_mecha_1.2)%2C%20anime%20key%20visual%20environment%2C%20trending%20on%20artstation%2C%20brush_strokes%2C.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01115-1757270431-classical_oil_painting%2C%20concept_art%2C%20(realistic_mecha_1.2)%2C%20anime%20key%20visual%20environment%2C%20trending%20on%20artstation%2C%20brush_strokes%2C.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/13010-4179249413-(Nixeu_style_1.2)%2C%20(monochrome_1.1)%2C%20(crosshatching_1.3)%2C%20(upper_body_1.2)%2C%20(facing_camera_1.2)%2C%201girl%2C%20(detailed_armor_1.2)%2C%20ha.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/13012-4179249415-(Nixeu_style_1.2)%2C%20(monochrome_1.1)%2C%20(crosshatching_1.3)%2C%20(upper_body_1.2)%2C%20(facing_camera_1.2)%2C%201girl%2C%20(detailed_armor_1.2)%2C%20ha.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01078-3200491935-(Nixeu_style_1.2)%2Cportrait%2C%20(geisha%20robot_1.5)%2C%20%20beautiful%20and%20elegant%2C%20attractive%2C%20masterpiece%2C%20by%20greg%20rutkowski%20and%20ruan%20jia%2C.png" width="50%"/>

<img src="https://huggingface.co/Akumetsu971/SD_Anime_Futuristic_Armor/resolve/main/01100-368521415-(Nixeu_style_1.2)%2C%20close-up%20portrait%2C%20(geisha%20robot_1.6)%2C%20%20(geisha_1.2)%2C%20(dark_hair)%2C%20breast%2C%20smiling%2C%20beautiful%20and%20elegant%2C%20at.png" width="50%"/>

