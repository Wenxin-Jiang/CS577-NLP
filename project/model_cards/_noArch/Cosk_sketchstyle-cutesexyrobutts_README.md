---
license: creativeml-openrail-m
language:
- en
pipeline_tag: text-to-image
tags:
- stable-diffusion
- art
- cutesexyrobutts
- style
- dreambooth
datasets:
- Cosk/cutesexyrobutts
library_name: diffusers
widget:
- text: portrait of a beautiful girl
- text: beautiful girl, playboy bunny, dark skin, black hair, blunt bangs, ponytail
---

# 'Sketchstyle' (cutesexyrobutts style)
Base model: https://huggingface.co/Linaqruf/anything-v3.0.</br>
Used 'fast-DreamBooth' on Google Colab and 768x768 images for all versions.

## NEW: Merges
*Merging sketchstyle models with other models will help to improve anatomy and other elements while also trying to keep the intended style as much as possible.</br>
I will upload from time to time new merges, if any of those improves on the previous ones. </br>
A 'weak' model means there is more weight to cutesexyrobutts style and a 'strong' model means there is a little more focus on the other model/models.</br>
Weak models might mantain a little more of the style but could have some anatomy problems, while strong models keep better anatomy though the style might become a little affected. Low CFG Scale (5-9) and using the "sketchstyle" token in the prompts might help with keeping the style on strong models.</br>*

**List of merges:**
- Pastelmix 0.2 + sketchstyle_v4-42k 0.8 weak (weighted sum, fp16)
- Pastelmix 0.4 + sketchstyle_v4-42k 0.6 strong (weighted sum, fp16)

**Versions:**
- V1: Trained with around 1300 images (from danbooru), automatically cropped.
- V2: Trained with 400 handpicked and handcropped images.
- V3: Trained with the same images as V2, but with 'style training' enabled.
- V4: Trained with 407 images, including 'captions' for each image.

**Recommended to use:**
- V4-42k (pretty good style and decent anatomy, might be the best)
- V3-40k (decent style and anatomy)
- V4-10k (best anatomy, meh style)
- V4-100k (good style, bad anatomy/hard to use, useful with img2img)

**Usage recommendations:**
- For V4, don't use CFG Scale over 11-12, as it will generate an overcooked image. Try between 6 to 9 at first. 9 seems to be the best if you're using the 'sketchstyle' in the prompt, if not, lower
- Generating specific characters might be hard, result in bad anatomy or not even work at all. If you want an specific character, the best is to use img2img with an image generated with another model
- Going over a certain resolution will generate incoherent results, so try staying close to 768x768 (examples: 640x896, 768x960, 640x1024, 832x640, and similar). Maybe Hires fix could help.
- Make sure to add nsfw/nipples/huge or large breasts in the negative prompts if you don't want any of those.
- Skin tone tends to be 'tan', use dark skin/tan on the negative prompts if its the case, and/or pale skin in the prompts.
- Using img2img to change the style of another image generally gives the best results, examples below.

Pay attention to this number. Normally going below 75 generates bad results, specially with models with high steps like V4-100k. Best with 100+
![Screenshot_1.png](https://s3.amazonaws.com/moonup/production/uploads/1671505643175-633520c031a2be3938c9f8f5.png)

Token: 'sketchstyle' (if used, anatomy may get affected, but it can be useful for models with low steps to get a better style)<br />

**Limitations and known errors:**
- Not very good anatomy
- Sometimes it generates artifacts, specially on the eyes and lips
- Tends to generate skimpy clothes, open clothes, cutouts, and similar
- Might generate unclear outlines
Try using inpainting and/or img2img to fix these.


# Comparison between different versions and models

As you can see, robutts tends to give less coherent results and might need more prompting/steps to get good results (tried on other things aswell with similar results)
![comparison.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671502776323-633520c031a2be3938c9f8f5.jpeg)

V2 with 10k steps or lower tends to give better anatomy results, and over that the style appears more apparent, so 10k is the 'sweet spot'.
![comparison2.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671504780023-633520c031a2be3938c9f8f5.jpeg)

Around 40 steps seems to be the best, but you should use 20 steps and, if you get an image you like, you increase the step count to 40 or 50.
![comparison3.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671509387599-633520c031a2be3938c9f8f5.jpeg)

Comparison between not completing that negative prompt and increasing the strength too much.
![comparison4.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671568686470-633520c031a2be3938c9f8f5.jpeg)

Comparison (using V3-5k) of token strength.
![comparison5.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671571773116-633520c031a2be3938c9f8f5.jpeg)

Another comparison of token strength using V3-15k.
![comparison6.jpg](https://s3.amazonaws.com/moonup/production/uploads/1671734192353-633520c031a2be3938c9f8f5.jpeg)

Comparison, from 1 to 30 steps, between NovelAI - Sketchstyle V3-27500 (img2img with NovelAI image) - Sketchstyle V3-27500. Using Euler sampler.
![comparison.gif](https://s3.amazonaws.com/moonup/production/uploads/1672115659361-633520c031a2be3938c9f8f5.gif)

# Examples:
![05144-1365838486-(masterpiece,best quality,ultra-detailed),((((face close-up)))),((profile)),((lips,pink_eyes)),((pink_hair,hair_slicked_back,hai.png](https://s3.amazonaws.com/moonup/production/uploads/1671513540474-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality,ultra-detailed),((((face close-up)))),((profile)),((lips,pink_eyes)),((pink_hair,hair_slicked_back,hair_strand)),(serious),portrait,frown,arms_up,adjusting_hair,eyelashes,parted_lips,(sportswear,crop_top),toned,collarbone,ponytail,1girl,solo,highres<br />
Negative prompt: (deformed,disfigured),(sitting,fat,thick,thick_thighs,nsfw),open_clothes,open_shirt,(jewelry,earrings,hair_ornament),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,realistic,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 70, Sampler: Euler, CFG scale: 12, Seed: 1365838486, Size: 768x768, Model: Sketchstyle V3-5k
```

_Eyes fixed with inpainting_:
![00609-996011741-(masterpiece,best quality,ultra-detailed),((((face close-up)))),((profile)),((lips,pink_eyes)),((pink_hair,hair_slicked_back,hai.png](https://s3.amazonaws.com/moonup/production/uploads/1671515050937-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality,ultra-detailed),((((face close-up)))),((profile)),((lips,pink_eyes)),((pink_hair,hair_slicked_back,hair_strand)),(serious),portrait,frown,arms_up,adjusting_hair,eyelashes,parted_lips,(sportswear,crop_top),toned,collarbone,ponytail,1girl,solo,highres<br />
Negative prompt: (deformed,disfigured),(sitting,fat,thick,thick_thighs,nsfw),open_clothes,open_shirt,(jewelry,earrings,hair_ornament),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,realistic,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 34, Sampler: Euler, CFG scale: 12, Seed: 996011741, Size: 768x768, Denoising strength: 0.6, Mask blur: 8, Model: Sketchstyle V2-10k
```

![05152-4172541433-sketchstyle,(masterpiece, best quality,beautiful lighting,stunning,ultra-detailed),(portrait,upper_body,parted_lips),1girl, (nip.png](https://s3.amazonaws.com/moonup/production/uploads/1671517158965-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: sketchstyle,(masterpiece, best quality,beautiful lighting,stunning,ultra-detailed),(portrait,upper_body,parted_lips),1girl, (nipples), (fox ears,animal_ear_fluff), (bare_shoulders,eyelashes,lips,orange eyes,blush),orange_hair,((onsen,indoors)),(toned),medium_breasts,navel,cleavage,looking at viewer,collarbone,hair bun, solo, highres,(nsfw)<br />
Negative prompt: (dark-skin,dark_nipples,extra_nipples),deformed,disfigured,(sitting,fat,thick,thick_thighs,nsfw),open_clothes,open_shirt,(jewelry,earrings,hair_ornament),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,realistic,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 30, Sampler: Euler, CFG scale: 12, Seed: 4172541433, Size: 640x832, Model: Sketchstyle V3-5k
```

![05111-4268937236-sketchstyle,(masterpiece, best quality,beautiful lighting,stunning,ultra-detailed),(portrait,upper_body),1girl, (nipples), (fox.png](https://s3.amazonaws.com/moonup/production/uploads/1671517508531-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: sketchstyle,(masterpiece, best quality,beautiful lighting,stunning,ultra-detailed),(portrait,upper_body),1girl, (nipples), (fox ears,animal_ear_fluff), (bare_shoulders,eyelashes,lips,orange eyes,ringed_eyes,shy,blush),onsen,indoors,medium_breasts, cleavage,looking at viewer,collarbone,hair bun, solo, highres,(nsfw)<br />
Negative prompt: Negative prompt: (huge_breasts,large_breasts),realistic,3D,3D Game,nsfw,lowres, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth<br />
Steps: 40, Sampler: Euler, CFG scale: 14, Seed: 4268937236, Size: 704x896, Model: Sketchstyle V3-5k
```

![05159-3765393440-(masterpiece,best quality,ultra detailed),(((facing_away,sitting,arm_support,thighs,legs))),(((from_behind,toned,ass,bare back,b.png](https://s3.amazonaws.com/moonup/production/uploads/1671519173074-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality,ultra detailed),(((facing_away,sitting,arm_support,thighs,legs))),(((from_behind,toned,ass,bare back,breasts))),((thong,garter_belt,garter_straps,lingerie)),(hair_flower,bed_sheet),(black_hair,braid,braided_ponytail,long_hair),1girl,grey_background,thighs,solo,highres<br />
Negative prompt: ((deformed)),((looking_back,looking_at_viewer,face)),((out_of_frame,cropped)),(fat,thick,thick_thighs),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, patreon_logo, patreon_username, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 50, Sampler: Euler, CFG scale: 12, Seed: 3765393440, Size: 640x832, Model: Sketchstyle V3-5k
```

![05195-2346086519-(masterpiece,best quality,ultra detailed),(((facing_away,sitting,arm_support,thighs,legs))),(((from_behind,toned,ass,bare back)).png](https://s3.amazonaws.com/moonup/production/uploads/1671561192018-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality,ultra detailed),(((facing_away,sitting,arm_support,thighs,legs))),(((from_behind,toned,ass,bare back))),((thong,garter_belt,garter_straps,lingerie)),(hair_flower,bed_sheet),(black_hair,braid,braided_ponytail,long_hair),1girl,grey_background,thighs,solo,highres<br />
Negative prompt: backboob,((deformed)),((looking_back,looking_at_viewer,face)),((out_of_frame,cropped)),(fat,thick,thick_thighs),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, patreon_logo, patreon_username, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 50, Sampler: Euler, CFG scale: 12, Seed: 2346086519, Size: 640x832, Model: Sketchstyle V3-5k
```

![05170-4024165718-(masterpiece,best quality,ultra-detailed),(sketchstyle),(arms_up,tying_hair),(large_breasts,nipples),(long_hair,blonde_hair,tied.png](https://s3.amazonaws.com/moonup/production/uploads/1671521055006-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality,ultra-detailed),(sketchstyle),(arms_up,tying_hair),(large_breasts,nipples),(long_hair,blonde_hair,tied_hair,ponytail,collarbone,navel,stomach,midriff,completely_nude,nude,toned),((cleft_of_venus,pussy)),cloudy_sky,1girl,solo,highres,(nsfw)<br />
Negative prompt: (deformed,disfigured,bad proportions,exaggerated),from_behind,(jewelry,earrings,hair_ornament),((sagging_breasts,huge_breasts,shiny,shiny_hair,shiny_skin,realistic,3D,3D game)),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),((fat,thick,thick_thighs)),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 40, Sampler: Euler, CFG scale: 12, Seed: 4024165718, Size: 704x960, Model: Sketchstyle V3-5k
```

![05177-4166887955-(masterpiece,best quality),(sketchstyle),((1boy,male_focus)),((close-up,portrait)),((black_shirt)),((((red collared_coat)))),((d.png](https://s3.amazonaws.com/moonup/production/uploads/1671522588038-633520c031a2be3938c9f8f5.png)
```bibtex
Prompt: (masterpiece,best quality),(sketchstyle),((1boy,male_focus)),((close-up,portrait)),((black_shirt)),((((red collared_coat)))),((dante_\(devil_may_cry\),devil may cry)),((medium_hair,parted_hair,parted_bangs,forehead,white_hair)),((stubble)),(facial_hair),(popped_collar,open_coat),(closed_mouth,smile),blue_eyes,looking_at_viewer,solo,highres<br />
Negative prompt: ((deformed)),(nsfw),(long_hair,short_hair,young,genderswap,1girl,female,breasts,androgynous),((choker)),(shiny,shiny_hair,shiny_skin,3D,3D game),((extra_limbs,extra_arms)),(loli,shota),(giant nipples),((fat,thick,thick_thighs)),long body,(lowres),(((poorly drawn fingers, poorly drawn hands))),((anatomic nonsense)),(extra fingers),(fused fingers),(((one hand with more than 5 fingers))),(((one hand with less than 5 fingers))),(bad eyes),(separated eyes),(long neck),((bad proportions)),long body,((poorly drawn eyes)),((poorly drawn)),((bad drawing)),blurry,((mutation)),((bad anatomy)),(multiple arms),((bad face)),((bad eyes)),bad tail,((more than 2 ears)),((poorly drawn face)), (extra limb), ((deformed hands)), (poorly drawn feet), (mutated hands and fingers), extra legs, extra ears, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face maskissing fingers, bad hands, extra digit, fewer digits, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled,monochrome, greyscale,face mask<br />
Steps: 50, Sampler: Euler, CFG scale: 12, Seed: 4166887955, Size: 768x768, Model: Sketchstyle V3-5k
```


# img2img style change examples:
![img2img-1.png](https://s3.amazonaws.com/moonup/production/uploads/1671510649616-633520c031a2be3938c9f8f5.png)
```bibtex
Original settings: Model: NovelAI, Steps: 30, Sampler: Euler a, CFG scale: 16, Seed: 3633297035, Size: 640x960<br />
Original prompt: masterpiece, best quality, 1girl, naked towel, fox ears, orange eyes, wet, ringed eyes, shy, medium breasts, cleavage, looking at viewer, hair bun, blush, solo, highres<br />
Original negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth<br />
New settings: Model: Sketchstyle V3 5k steps, Steps: 33, CFG scale: 12, Seed: 3311014108, Size: 640x960, Denoising strength: 0.6, Mask blur: 4<br />
New prompt: ((sketchstyle)),(masterpiece, best quality,beautiful lighting,stunning,ultra-detailed),(portrait,upper_body),1girl, (((naked_towel,towel))), (fox ears,animal_ear_fluff), (bare_shoulders,eyelashes,lips,orange eyes,ringed_eyes,shy,blush),onsen,indoors,medium_breasts, cleavage,looking at viewer,collarbone,hair bun, solo, highres<br />
New negative prompt: (nipples,huge_breasts,large_breasts),realistic,3D,3D Game,nsfw,lowres, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth<br />
```

![img2img-2.png](https://s3.amazonaws.com/moonup/production/uploads/1671523242721-633520c031a2be3938c9f8f5.png)
```bibtex
Original settings: Model: NovelAI, Steps: 30, Sampler: Euler a, CFG scale: 16, Seed: 764529639, Size: 640x960<br />
Prompt: masterpiece, highest quality, (1girl), (looking at viewer), ((pov)), fox ears, ((leaning forward)), [light smile], ((camisole)), short shorts, (cleavage), (((medium breasts))), blonde, (high ponytail), (highres)<br />
Negative prompt: ((deformed)), (duplicated), lowres, ((missing animal ears)), ((poorly drawn face)), ((poorly drawn eyes)), (extra limb), (mutation), ((deformed hands)), (((poorly drawn hands))), (poorly drawn feet), (fused toes), (fused fingers), (mutated hands and fingers), (one hand with more than 5 fingers), (one hand with less than 5 fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled, huge breasts, black and white, monochrome, 3D Game, 3D, realistic, realism, huge breasts<br />
New settings: Model: Sketchstyle V3 5k steps, Steps: 28, CFG scale: 12, Seed: 1866024520, Size: 640x960, Denoising strength: 0.7, Mask blur: 8
```

![img2img-3.png](https://s3.amazonaws.com/moonup/production/uploads/1671524129672-633520c031a2be3938c9f8f5.png)
```bibtex
Original settings: Model: NovelAI, Steps: 25, Sampler: Euler a, CFG scale: 11, Seed: 2604970030, Size: 640x896<br />
Original prompt: (masterpiece),(best quality),((sketch)),(ultra detailed),(1girl, teenage),((white hair, messy hair)),((expressionless)),(black jacket, long sleeves),((grey scarf)),((squatting)), (hands on own knees),((plaid_skirt, pleated skirt, miniskirt)),(fox ears, extra ears, white fox tail, fox girl, animal ear fluff),black ((boots)),full body,bangs,ahoge,(grey eyes),solo,absurdres<br />
Negative prompt: ((deformed)),((loli, young)),(kneehighs,thighhighs),long body, long legs),lowres,((((poorly drawn fingers, poorly drawn hands)))),((anatomic nonsense)),(extra fingers),((fused fingers)),(plaid scarf),(spread legs),((one hand with more than 5 fingers)), ((one hand with less than 5 fingers)),((bad eyes)),(twin, multiple girls, 2girls),(separated eyes),(long neck),((bad proportions)),(bad lips),((thick lips)),loli,long body,(((poorly drawn eyes))),((poorly drawn)),((bad drawing)),(blurry),(((mutation))),(((bad anatomy))),(((multiple arms))),(((bad face))),(((bad eyes))),bad tail,(((more than 2 ears)), (((poorly drawn face))), (extra limb), ((deformed hands)), (poorly drawn feet), (fused toes), (mutated hands and fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled, huge breasts, black and white, monochrome, 3D Game, 3D, (realistic), face mask<br />
New settings: Model: Sketchstyle V3 5k steps, Steps: 45, CFG scale: 12, Seed: 1073378414, Size: 640x896, Denoising strength: 0.6, Mask blur: 8<br />
New prompt: (masterpiece),(best quality),(sketchstyle),(ultra detailed),(1girl, teenage),((white hair, messy hair)),((expressionless)),(black jacket, long sleeves),((grey scarf)),((squatting)), (hands on own knees),((plaid_skirt, pleated skirt, miniskirt)),(fox ears, extra ears, white fox tail, fox girl, animal ear fluff),black ((boots)),full body,bangs,ahoge,(grey eyes),solo,absurdres<br />
```

![img2img-4.png](https://s3.amazonaws.com/moonup/production/uploads/1672003898152-633520c031a2be3938c9f8f5.png)
```bibtex
Original settings: Model: NovelAI, Steps: 30, Sampler: Euler a, CFG scale: 12, Seed: 3659534337, Size: 768x832<br />
Original prompt: ((masterpiece)), ((highest quality)),(((ultra-detailed))),(illustration),(1girl), portrait,((wolf ears)),(beautiful eyes),looking at viewer,dress shirt,shadows,((ponytail)), (white hair), ((sidelocks)),outdoors,bangs, solo, highres<br />
Original negative prompt: ((deformed)), lowres,loli,((monochrome)),(black and white),((lips)),long body,(((poorly drawn eyes))),((out of frame)),((poorly drawn)),((bad drawing)),(blurry),depth of field,(fused fingers),(((mutation))),((bad anatomy)),(((multiple arms))),(((bad face))),(((bad eyes))),bad tail,(((more than 2 ears)), (((poorly drawn face))), (extra limb), ((deformed hands)), (((poorly drawn hands))), (poorly drawn feet), (fused toes), (mutated hands and fingers), (one hand with more than 5 fingers), (one hand with less than 5 fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled, huge breasts, black and white, monochrome, 3D Game, 3D, realism, face mask<br />
New settings: Model: Sketchstyle V3-20k 2000steps text encoder, Steps: 80, CFG scale: 12, Seed: 3001145714, Size: 768x832, Denoising strength: 0.5, Mask blur: 4<br />
New prompt: ((sketchstyle)),(masterpiece,best quality,highest quality,illustration),((ultra-detailed)),1girl,(portrait,close-up),((wolf_girl,wolf_ears)),(eyelashes,detailed eyes,beautiful eyes),looking at viewer,(collared-shirt,white_shirt),((ponytail)), (white hair), ((sidelocks)),(blue eyes),closed_mouth,(shadows,outdoors,sunlight,grass,trees),hair_between_eyes,bangs,solo,highres<br />
New negative prompt: ((deformed)),(less than 5 fingers, more than 5 fingers,bad hands,bad hand anatomy,missing fingers, extra fingers, mutated hands, disfigured hands, deformed hands),lowres,loli,((monochrome)),(black and white),((lips)),long body,(((poorly drawn eyes))),((out of frame)),((poorly drawn)),((bad drawing)),(blurry),depth of field,(fused fingers),(((mutation))),((bad anatomy)),(((multiple arms))),(((bad face))),(((bad eyes))),bad tail,(((more than 2 ears)), (((poorly drawn face))), (extra limb), ((deformed hands)), (((poorly drawn hands))), (poorly drawn feet), (fused toes), (mutated hands and fingers), (one hand with more than 5 fingers), (one hand with less than 5 fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored, blurry lines, wacky outlines, unclear outlines, doubled, huge breasts, black and white, monochrome, 3D Game, 3D, realism, face mask<br />
```

![img2img-5.png](https://s3.amazonaws.com/moonup/production/uploads/1672122599787-633520c031a2be3938c9f8f5.png)
```bibtex
Original settings: Model: NovelAI, Steps: 20, Sampler: Euler, CFG scale: 11, Seed: 2413712316, Size: 768x768<br />
Original prompt: (masterpiece,best quality,ultra-detailed,detailed_eyes),(sketch),((portrait,face focus)),(((shaded eyes))),(wavy hair),(((ringed eyes,red_hair))),((black hair ribbon)),((hair behind ear)),(((short ponytail))),(blush lines),(good anatomy),(((hair strands))),(bangs),((lips)),[teeth, tongue],yellow eyes,(eyelashes),shirt, v-neck,collarbone,cleavage,breasts,(medium hair),(sidelocks),looking at viewer,(shiny hair),1girl,solo,highres<br />
Original negative prompt: ((deformed)),lowres,(black hair),(formal),earrings,(twin, multiple girls, 2girls),(braided bangs),((big eyes)),((close up, eye focus)),(separated eyes),(multiple eyebrows),((eyebrows visible through hair)),(long neck),(bad lips),(tongue out),((thick lips)),(from below),loli,long body,(((poorly drawn eyes))),((poorly drawn)),((bad drawing)),((blurry)),depth of field,(fused fingers),(((mutation))),(((bad anatomy))),(((multiple arms))),(((bad face))),(((bad eyes))),bad tail,(((more than 2 ears)), (((poorly drawn face))), (extra limb), ((deformed hands)), (((poorly drawn hands))), (poorly drawn feet), (fused toes), (mutated hands and fingers), (one hand with more than 5 fingers), (one hand with less than 5 fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored,doubled, huge breasts, black and white, monochrome, 3D Game, 3D, (realistic), face mask<br />
New settings: (img2img with original image, then again with the new generated image, inpainted to fix the neck) Model: Sketchstyle V3-27.5k 2000steps text encoder, Steps: 80, CFG scale: 12, Seed: 1237755461 / 1353966202, Size: 832x832, Denoising strength: 0.5 / 0.3, Mask blur: 4<br />
New prompt: sketchstyle,(masterpiece,best quality,ultra-detailed,detailed_eyes),(((portrait,face focus,close-up))),(((shaded eyes))),(wavy hair),(((ringed eyes,red_hair))),((black hair ribbon)),((hair behind ear)),(((short ponytail))),(blush lines),(good anatomy),(((hair strands))),(bangs),((lips)),[teeth, tongue],(yellow eyes,eyelashes,tsurime,slanted_eyes),shirt, v-neck,collarbone,breasts,(medium hair),(sidelocks),looking at viewer,(shiny hair),1girl,solo,highres<br />
New negative prompt: ((deformed)),((loli,young)),lowres,(black hair),(formal),earrings,(twin, multiple girls, 2girls),(braided bangs),((big eyes)),((close up, eye focus)),(separated eyes),(multiple eyebrows),((eyebrows visible through hair)),(long neck),(bad lips),(tongue out),((thick lips)),(from below),loli,long body,(((poorly drawn eyes))),((poorly drawn)),((bad drawing)),((blurry)),depth of field,(fused fingers),(((mutation))),(((bad anatomy))),(((multiple arms))),(((bad face))),(((bad eyes))),bad tail,(((more than 2 ears)), (((poorly drawn face))), (extra limb), ((deformed hands)), (((poorly drawn hands))), (poorly drawn feet), (fused toes), (mutated hands and fingers), (one hand with more than 5 fingers), (one hand with less than 5 fingers), extra toes, missing toes, extra feet, extra legs, extra ears, missing ear, extra hands, bad feet, bad anatomy, bad hands, text, error, missing fingers, bad hands, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, bad face, bad mouth, animal hands, censored,doubled, huge breasts, black and white, monochrome, 3D Game, 3D, (realistic), face mask<br />
```