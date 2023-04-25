---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
library_name: "EveryDream"
inference: false
---

![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/images/showcase_PoW_neverendingloop.jpg)

# Intro

This is a collection of models related to the "Picture of the Week" contest on Stable Diffusion discord.

I try to make a model out of all the submission for people to continue enjoy the theme after the even, and see a little of their designs in other people's creations. The token stays "PoW Style" and I balance the learning on the low side, so that it doesn't just replicate creations.

I also make smaller quality models to help make pictures for the contest itself, based on the theme.

# 29 novembre 2022, "The Stable Kitchen"

## Theme : Burgers and Fries

Welcome to the VERY FIRST edition of the most Stable Kitchen in the universe!

On today’s menu will be Sandwiches & Frie. Since you’re here for the first time, I will explain how it works! You can generate your orders and we will make them for you. Take a seat, flip through the menu, bring all of your favorite ingredients~

* The sandwich with the most cheddar? 5 beef burgers? An infinite fries generator?
* Serve us your best sandwich and fries combo! 

Not even the sky's the limit my friend, 

You want it?

You have it! 

As long as it's delicious, of course!

We’ll see you on the chopping block for this week’s Stable Kitchen!

![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/291122/images/theme.png)

## Models

### Burgy

![Burgy](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/291122/images/showcase_burgy.jpg)
* Burgers, burgers burgers
* training: 40 pictures, 6 epochs of 40 repeats, batch size 6, LR1e-6, EveryDream
* balance : Strong, burgers
* **Activation token :** `Burgy`
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/291122/ckpts/Burgy.ckpt)
* [Dataset](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/291122/dataset_Burgy.zip)

# 22 novembre 2022, "Imaginary Friend"

## Theme : Imaginary Friend

Do you remember putting your hands into what seemed as if it were just plain air and giggling like a child? Having conversations with someone who “wasn’t there”? Nowadays the term “Imaginary Friend” isn’t as frequently used as it used to be, right? Let’s bring it back.

* Can you build your Imaginary Friends actualized? 
* What traits do you recall of them? Are they still young? Have they grown up now? Do they resemble you, or a creature that isn’t human?
* Where would you find this Imaginary Friend? Where do they reside? What do they stand for?

Our prompt for this event was created by @Andrekerygma

"a boy drinking tea with a cute monster on the bedroom, disney infinity character design, pixar, artstation, vinyl, toy, figurine, 3 d model, cinema 4 d, substance 3 d painter, vray, unreal engine 5, octane render, cinematic"

![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/221122/images/theme.png)

## Models

### PoW ArtStyle 22-11-22

![PoW ArtStyle](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/221122/images/showcase_pow_imaginary_friend.jpg)
* based on all the submissions to the PoW
* training: 73 pictures, 6000 steps on batch 6, 1e-6 polynomial LR.
* balance : a little lighter on the style than last week, still manages to reproduce most participants
* **Activation token :** `PoW ArtStyle`
* Other noticable tokens : Your Discord username, if you participated. Also TMNT,NikeAir Shoes and Sid, Ice Age movie
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/221122/ckpts/PoWArtStyle_ImaginaryFriend.ckpt)
* [Dataset](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/221122/PoW_221122_dataset.zip)

### CharacterChan Style

![CharacterChan Style](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_CharacterChanStyle-v1.jpg)
* based on the "Character" dreamer community of the Stable Diffusion Discord
* training: 50 pictures, 160 total repeat, LR1e-6
* balance : correct, but some sub concepts have overtrain a little, like the clown.
* **Activation token :** `CharacterChan Style`
* [CKPT](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/CharacterChanStyle-v1.ckpt)
* [Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/CharacterChanStyle-v1.zip)
* [Model page](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection#characterchan-style)

### CreatureChan Style

![CreatureChan Style](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/images/showcase_CreatureChanStyle-v1.jpg)
* based on the "Creature" dreamer community of the Stable Diffusion Discord
* training: 50 pictures, 160 total repeat, LR1e-6
* balance : good
* **Activation token :** `CreatureChan Style`
* [CKPT](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/ckpt/CreatureChanStyle-v1.ckpt)
* [Dataset](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection/resolve/main/datasets/CreatureChanStyle-v1.zip)
* [Model page](https://huggingface.co/Guizmus/SD_DreamerCommunities_Collection#creaturechan-style)

# 14 novembre 2022, "The Never-Ending Loop"

## Theme : The Never-Ending Loop

It is a passed-down proverb that lines represent the flow of time itself. They converge and take shape. They twist, tangle, sometimes unravel, break, and then connect again. 

* Without words, how are we able to accurately represent this flow of time with only lines? geometrically, intricately, asymmetricaly, seamlessly, ornately...
* Think of a never-ending pattern, texture, or shape– looping on and on for what feels infinite.
* Just how detailed are you able to get with your patterns? 

Our prompt for this event was created by @Asukii !

"the fractal flow of time stretches towards the horizon, surreal fractal intertwined looping pathways, dramatic cinematic perspective, detailed delicate intricate ornate linework, geometric abstract masterwork digital art, quantum wavetracing, ink drawing, optical illusion"


![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/images/theme1.png)

![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/images/theme2.png)

## Models

### PoW Style 14-11-22

![PoW Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/images/showcase_PoW_neverendingloop.jpg)
* based on all the submissions to the PoW
* training: 101 pictures, 9000 steps on batch 6, 1e-6 polynomial LR.
* balance : a little strong on the style but it made it possible to differentiate each participants
* **Activation token :** `PoW Style`
* Other noticable tokens : Your Discord username, if you participated. Also Rick Roll and "fullbody shot"
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/ckpts/PoWStyle_NeverEndingLoop.ckpt)
* [Diffusers : Guizmus/SD_PoW_Collection/141122/diffusers](https://huggingface.co/Guizmus/SD_PoW_Collection/tree/main/141122/diffusers/)
* [Dataset](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/PoW_141122_2_dataset.zip)

### Fractime Style

![Fractime Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/images/showcase_FractimeStyle.jpg)
* based on the suggested prompt and theme
* training: 50 pictures, 1750 steps on batch 6, 1e-6 polynomial LR.
* balance : correct, but the style doesn't apply to every subject
* **Activation token :** `Fractime Style`
* Other noticable tokens : intricate, nebula, illusion, person, road, tree, boat
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/ckpts/FractimeStyle.ckpt)
* [Dataset](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/141122/PoW_141122_1_dataset.zip)


# 09 novembre 2022, "Abstralities"

## Theme : Abstract Realities

Glitch, warp, static, shape, flicker, break, bend, mend

Have you ever felt your reality shift out from under your feet? Our perception falters and repairs itself in the blink of an eye. Just how much do our brains influence what we perceive? How much control do we have over molding these realities?

With the introduction of AI and its rapid pace taking the world by storm, we are seeing single-handedly just how these realities can bring worlds into fruition.

* Can you show us your altered reality?
* Are these realities truly broken, or only bent?

Our example prompt for this event was created by @Aether !

"household objects floating in space, bedroom, furniture, home living, warped reality, cosmic horror, nightmare, retrofuturism, surrealism, abstract, illustrations by alan nasmith"


![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/AETHER.png)

![PoW](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/aether2.png)

## Models

### PoW Style 09-11-22

![PoW Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/showcase_pow_final.jpg)
* Main model based on all the results from the PoW
* training: 51 pictures, 3000 steps on 1e-6 polynomial LR.
* balanced on the light side, add attention/weight on the activation token
* **Activation token :** `PoW Style`
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/ckpts/PoWStyle_Abstralities.ckpt)
* [Diffusers : Guizmus/SD_PoW_Collection/091122/diffusers](https://huggingface.co/Guizmus/SD_PoW_Collection/tree/main/091122/diffusers/)
* [Dataset](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/dataset.zip)

### Bendstract Style

![Bendstract Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/showcase_bendstract.jpg)
* based on the suggested prompt
* training: 100 pictures, 7500 steps on 1e-6 polynomial LR. overtrained
* **Activation token :** `Bendstract Style`
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/ckpts/Bendstract-v1.ckpt)

### endingReality Style

![BendingReality Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/showcase_bendingreality.jpg)
* based on the suggested prompt
* training: 68 pictures, 6000 steps on 1e-6 polynomial LR. overtrained
* **Activation token :** `BendingReality Style`
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/ckpts/BendingReality_Style-v1.ckpt)

### PoW Style mid-submissions 09-11-22

![PoW Style](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/images/showcase_pow_midrun.jpg)
* based on the first few submissions
* training: 24 pictures, 2400 steps on 1e-6 polynomial LR. a little too trained
* **Activation token :** `PoW Style`
* [CKPT](https://huggingface.co/Guizmus/SD_PoW_Collection/resolve/main/091122/ckpts/PoWStyle_midrun.ckpt)


# License

These models are open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)