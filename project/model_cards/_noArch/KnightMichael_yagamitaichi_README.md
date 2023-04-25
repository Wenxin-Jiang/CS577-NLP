---
language:
- en
thumbnail: "https://huggingface.co/KnightMichael/yagamitaichi/resolve/main/README-FILES/yagamitaichi-thumbnail.jpg"
datasets:
- KnightMichael/yagamitaichi
tags:
- yagami-taichi
- tai-kamiya
- hypernetwork
- boy
- character
- model
- digimon
- adventure
- "1999"
- anime
- anything-3.0
- stable-diffusion
- text-to-image
- deepbooru
- tags
- 1boy
---

# Yagami Taichi (Tai Kamiya) Hypernetwork Boy Character Model from Digimon Adventure (1999) Anime for Anything 3.0

![Yagami Taichi (Tai Kamiya)](/KnightMichael/yagamitaichi/resolve/main/README-FILES/yagamitaichi.webp)

# Base Model

- Checkpoint: [Anything-V3.0-pruned.ckpt](/Linaqruf/anything-v3.0/blob/main/Anything-V3.0-pruned.ckpt)
- VAE: [Anything-V3.0.vae.pt](/Linaqruf/anything-v3.0/blob/main/Anything-V3.0.vae.pt)

# Hypernetwork Parameters

- Modules: 768, 1024, 320, 640, 1280
- Layer structure: 1, 2, 1
- Activation function: Linear
- Layer weights initialization: Normal
- Layer normalization: No
- Dropout: No

# Training Parameters

- Learning rate: 0.00001
- Batch size: 1
- Gradient accumulation steps: 1
- Dataset: [yagamitaichi](/datasets/KnightMichael/yagamitaichi)
- Prompt template file: [hypernetwork.txt](README-FILES/hypernetwork.txt)
- Width: 512
- Height: 512
- Steps: [100000](yagamitaichi-100000.pt), [125000](yagamitaichi-125000.pt), [150000](yagamitaichi-150000.pt), [175000](yagamitaichi-175000.pt), [200000](yagamitaichi-200000.pt)

# Dataset Creation

- 296 images of Tai alone captured from episodes 1 to 21.
- Manually cropped to 1:1 and resized to 512x512 using Birme.
- Automatically tagged by DeepBooru.

# How to Use

[Recommended Colab](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)

1. Set up the [Anything 3.0](/Linaqruf/anything-v3.0) model. I will specifically use the model [Anything-V3.0-pruned.ckpt](/Linaqruf/anything-v3.0/blob/main/Anything-V3.0-pruned.ckpt), since it was the same model that I used for training the hypernetwork. In the [recommended Colab](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb), paste the following link in the "Link_CKPT" field and execute all cells except the last one:
   
   ```
   https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt
   ```
   
2. Optional, but recommended: Set up the [Anything 3.0 VAE](/Linaqruf/anything-v3.0/blob/main/Anything-V3.0.vae.pt). The hypernetwork model was trained using this VAE, but is not 100% necessary. However, the examples shown here were generated using it. The most significant difference I have noticed is more vivid colors in generated images when using the VAE. In the [recommended Colab](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb), add a new code cell, paste the following command line inside and execute it:
   
   ```
   !wget -O /content/gdrive/MyDrive/sd/stable-diffusion-webui/models/VAE/Anything-V3.0.vae.pt https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0.vae.pt
   ```
   
3. Set up the desired hypernetwork model PT file. There are 5 different models. The number in the file name indicates the amount of training steps. I recommend to use the model with highest number of steps, since it was training for a longer time. If you want to compare the training steps performance, feel free to try the other models too. The examples shown here were generated using the 200000 steps version.
   
   - [yagamitaichi-200000.pt (Recommended)](yagamitaichi-200000.pt)
   - [yagamitaichi-175000.pt](yagamitaichi-175000.pt)
   - [yagamitaichi-150000.pt](yagamitaichi-150000.pt)
   - [yagamitaichi-125000.pt](yagamitaichi-125000.pt)
   - [yagamitaichi-100000.pt](yagamitaichi-100000.pt)
   
   In the [recommended Colab](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb), add a new code cell, paste the following command lines inside and execute it:
   
   ```
   !mkdir /content/gdrive/MyDrive/sd/stable-diffusion-webui/models/hypernetworks
   !wget -O /content/gdrive/MyDrive/sd/stable-diffusion-webui/models/hypernetworks/yagamitaichi-200000.pt https://huggingface.co/KnightMichael/yagamitaichi/resolve/main/yagamitaichi-200000.pt
   ```
   
4. In the [recommended Colab](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb), now you can execute the last cell, wait until the link to the web UI appears and get in.
   
5. In the web UI, go to "Settings" tab and set the following:
   
   - SD VAE to the Anything VAE. (Only if you did the step 2)
   - Hypernetwork to the "yagamitaichi" model.
   
   Then, click the "Apply settings" button.
   
# Prompting

Include in your prompt the tags contained in the [dataset](/datasets/KnightMichael/yagamitaichi) TXT files that best describe the character's aspects you want to reflect in the output. Here is a list with all the 335 existing tags in the dataset sorted by number of occurrences:

- 290: brown_hair
- 266: solo
- 237: smile
- 229: male_focus
- 226: brown_eyes
- 221: goggles
- 209: goggles_on_head
- 188: 1boy
- 184: open_mouth
- 183: eyewear_on_head
- 132: :d
- 125: spiked_hair
- 107: sky
- 102: gloves
- 99: blue_headwear
- 99: star_\(symbol\)
- 95: hat
- 93: outdoors
- 85: goggles_on_headwear
- 80: day
- 70: sunglasses
- 69: face
- 58: cloud
- 52: tree
- 51: shirt
- 50: short_sleeves
- 47: looking_at_viewer
- 47: white_gloves
- 45: blue_shirt
- 45: brown_shorts
- 42: 1girl
- 38: blue_vest
- 35: shorts
- 28: snow
- 27: star_print
- 26: close-up
- 25: blue_sky
- 25: closed_mouth
- 22: black_eyes
- 22: brick_wall
- 22: tile_floor
- 22: tiles
- 21: palm_tree
- 20: multiple_boys
- 19: blue_background
- 19: night
- 19: star_\(sky\)
- 19: tile_wall
- 18: night_sky
- 16: light_particles
- 15: bare_tree
- 15: eyewear_on_headwear
- 15: grass
- 15: snowing
- 15: starfish
- 15: visor_cap
- 14: beach
- 14: chain-link_fence
- 14: nature
- 14: plant
- 14: starry_sky
- 14: sweat
- 14: teeth
- 13: clenched_hand
- 13: from_behind
- 13: honeycomb_\(pattern\)
- 13: honeycomb_background
- 13: raimon
- 13: shoes
- 13: simple_background
- 12: 2boys
- 12: closed_eyes
- 12: short_hair
- 11: brick_floor
- 11: fence
- 11: full_body
- 11: grin
- 11: moon
- 11: road
- 11: socks
- 11: space
- 11: standing
- 11: stone_floor
- 11: wall
- 10: bathroom
- 10: indoors
- 10: pavement
- 10: water
- 9: bush
- 9: forest
- 9: hexagon
- 9: leaf
- 9: mountain
- 9: sand
- 9: window
- 9: yellow_background
- 8: dark_skin
- 8: hilbert_\(pokemon\)
- 8: outstretched_arm
- 8: pants
- 8: pine_tree
- 8: shooting_star
- 8: stone_wall
- 8: sweatdrop
- 8: yellow-framed_eyewear
- 7: beret
- 7: brick
- 7: desert
- 7: long_hair
- 7: potted_plant
- 7: starry_background
- 7: tanabata
- 7: upper_body
- 6: aurora
- 6: branch
- 6: clenched_hands
- 6: cloudy_sky
- 6: computer
- 6: floor
- 6: milky_way
- 6: sneakers
- 6: spider_web
- 6: starry_sky_print
- 6: tan
- 5: bubble
- 5: dark-skinned_female
- 5: desk
- 5: door
- 5: foreshortening
- 5: hairband
- 5: headband
- 5: laptop
- 5: outstretched_hand
- 5: palm_leaf
- 5: sailor_moon_redraw_challenge
- 5: shaded_face
- 5: sitting
- 5: soccer_uniform
- 5: sportswear
- 5: tongue
- 4: bamboo
- 4: blue_footwear
- 4: blurry
- 4: building
- 4: cliff
- 4: earth_\(planet\)
- 4: eyelashes
- 4: full_moon
- 4: gradient
- 4: gradient_background
- 4: in_tree
- 4: island
- 4: jacket
- 4: ocean
- 4: planet
- 4: shore
- 4: silk
- 4: tanzaku
- 4: toilet
- 4: yellow_sky
- 3: baseball_cap
- 3: black_hair
- 3: blue_headband
- 3: blurry_foreground
- 3: ceiling
- 3: chimney
- 3: cracked_wall
- 3: depth_of_field
- 3: endou_mamoru
- 3: facing_away
- 3: footprints
- 3: forehead
- 3: from_side
- 3: galaxy
- 3: locker
- 3: lying
- 3: profile
- 3: rock
- 3: rooftop
- 3: sitting_in_tree
- 3: snowflakes
- 3: vest
- 3: winter
- 2: aerial_fireworks
- 2: against_tree
- 2: air_bubble
- 2: argyle_background
- 2: ash_ketchum
- 2: back-to-back
- 2: bangs
- 2: blur_censor
- 2: blurry_background
- 2: bokeh
- 2: boots
- 2: chromatic_aberration
- 2: crack
- 2: crossed_arms
- 2: dappled_sunlight
- 2: debris
- 2: field
- 2: figure
- 2: fireworks
- 2: flower
- 2: focused
- 2: horizon
- 2: lake
- 2: locker_room
- 2: map
- 2: mole
- 2: monitor
- 2: motion_blur
- 2: net
- 2: on_grass
- 2: one_eye_closed
- 2: orange_background
- 2: orange_sky
- 2: outstretched_arms
- 2: parody
- 2: path
- 2: photo_\(medium\)
- 2: pointing
- 2: ponytail
- 2: pov
- 2: pov_hands
- 2: raimon_soccer_uniform
- 2: reaching
- 2: reaching_out
- 2: restroom
- 2: roto
- 2: sakaguchi_karina
- 2: sand_castle
- 2: sand_sculpture
- 2: seashell
- 2: shell
- 2: shower_\(place\)
- 2: skyscraper
- 2: snorkel
- 2: solo_focus
- 2: spread_fingers
- 2: sunset
- 2: tail
- 2: television
- 2: tree_shade
- 2: tree_stump
- 2: underwater
- 2: white_footwear
- 2: white_headwear
- 2: white-framed_eyewear
- 1: :3
- 1: ^_^
- 1: against_wall
- 1: aircraft
- 1: animal
- 1: armband
- 1: belt
- 1: blue_jacket
- 1: blue_sailor_collar
- 1: book
- 1: brown_belt
- 1: bug
- 1: buttons
- 1: cabbie_hat
- 1: chain
- 1: character_name
- 1: checkered_background
- 1: cherry_blossoms
- 1: chibi
- 1: christmas_tree
- 1: city
- 1: city_lights
- 1: coconut
- 1: constellation
- 1: copyright_name
- 1: cosplay
- 1: crying
- 1: cum
- 1: curtain_grab
- 1: curtains
- 1: dark-skinned_male
- 1: digimon_\(creature\)
- 1: diving_mask
- 1: eye_focus
- 1: facial
- 1: fangs
- 1: film_grain
- 1: fire
- 1: fireflies
- 1: food
- 1: forehead_protector
- 1: from_below
- 1: fruit
- 1: gakuran
- 1: giant
- 1: green_background
- 1: grey_eyes
- 1: helmet
- 1: hood
- 1: indian_style
- 1: keyboard_\(computer\)
- 1: layered_sleeves
- 1: leaf_background
- 1: lily_pad
- 1: looking_back
- 1: meme
- 1: nate_\(pokemon\)
- 1: nishizumi_miho
- 1: on_ground
- 1: perspective
- 1: pillar
- 1: pillow
- 1: pink_background
- 1: pink_hair
- 1: police
- 1: pool
- 1: racket
- 1: refrigerator
- 1: serious
- 1: shelf
- 1: short_over_long_sleeves
- 1: simon_\(ttgl\)
- 1: sleeves_rolled_up
- 1: street
- 1: sun
- 1: sweating_profusely
- 1: tears
- 1: traditional_media
- 1: uniform
- 1: vines
- 1: water_drop
- 1: watermelon
- 1: waves
- 1: white_background
- 1: white_flower
- 1: yellow_scarf
- 1: yellow_shirt

Note that not all the tags refer to the character itself. The tags that allude environment elements, can be ignored. Tags with more occurrences are better.

![Prompting](/KnightMichael/yagamitaichi/resolve/main/README-FILES/prompting.png)

```
1boy, male_focus, brown_eyes, brown_hair, blue_headwear, goggles, goggles_on_head, :d
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 19990801, Size: 512x512, Model hash: 2700c435, Hypernet: yagamitaichi-200000
```

# Hypernetwork Strength

Adjust the "Hypernetwork strength" parameter to get better results. This parameter can be found in the "Settings" tab below the "Hypernetwork" parameter. The hypernetwork strength indicates how much influence the hypernetwork model has against the base model. The values go from "0" to "1", where "0" is no influence (same as set the "Hypernetwork" to "None") and "1" is total influence. Don't forget to apply changes.

![Hypernetwork Strength](/KnightMichael/yagamitaichi/resolve/main/README-FILES/hypernetwork-strength.webp)

# Examples

![Example 3](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-3.png)

```
a portrait of a 1boy, brown_eyes, brown_hair, headband, goggles_on_head, blue_shirt, star_\(symbol\), brown_shorts, standing in a sunflower field, crying, clutching his chest
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3647976317, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.7
```

![Example 4](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-4.png)

```
a portrait of a 1boy, brown_eyes, brown_hair, headband, goggles_on_head, blue_shirt, star_\(symbol\), brown_shorts, white_gloves, socks, shoes, standing on a snowy peak looking up, take from below, aurora borealis
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3595266551, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.7
```

![Example 5](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-5.png)

```
1boy, brown_eyes, brown_hair, headband, goggles_on_head, standing in bright city at night
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3910907477, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.7
```

![Example 6](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-6.png)

```
1boy, brown_eyes, brown_hair, blue_headwear, goggles_on_head, wearing an open shirt hoodie, eating a popsicle in the beach
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1135025946, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.6
```

![Example 1](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-1.png)

```
1boy, brown_hair, headband, blue_shirt, star_\(symbol\), brown_shorts, white_gloves, socks, shoes, from_behind, standing on a cliff, cumulonimbus clouds, sunrise
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4240373175, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.7
```

![Example 2](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-2.png)

```
a portrait of a 1boy, brown_eyes, brown_hair, headband, goggles_on_head, blue_shirt, star_\(symbol\), brown_shorts, white_gloves, socks, shoes, sitting on a rock on the beach at sunset
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 441170169, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.6
```

![Example 7](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-7.png)

```
a portrait of a 1boy, brown_eyes, brown_hair, headband, goggles_on_head, brown_shorts, shirtless, surfist, standing in a tropical island
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2856886676, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.6
```

![Example 8](/KnightMichael/yagamitaichi/resolve/main/README-FILES/example-8.png)

```
1boy, brown_eyes, brown_hair, headband, goggles_on_head, blue_shirt, star_\(symbol\), brown_shorts, white_gloves, socks, shoes, open_mouth, sitting at a school desk
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1027287060, Size: 768x1024, Model hash: 2700c435, Hypernet: yagamitaichi-200000, Hypernet strength: 0.7
```