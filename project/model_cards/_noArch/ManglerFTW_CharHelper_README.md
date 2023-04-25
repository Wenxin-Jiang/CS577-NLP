---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - text-to-image
---
<b>Introduction:</b>

This model was trained on a digital painting style mainly with characters and portraits. The main objective is to train a model to be a tool to help with character design ideas.
It's base is Stable Diffusion V2.1 and is trained with 768X768 images. You will need to add the .yaml file into the same directory as your model to use.

<b>V4:</b>
<br /><br />

File Name is CharHelperV4.safetensors<br />

CharHelper V4 is a merge of CharHelper V3 and a newly trained model. This update is to provide a base for future updates. <b>All older keywords from CharHelper V3 will still work.</b>

Training subjects on this model are Aliens, Zombies, Birds, Cute styling, Lighthouses, and Macro Photography. Mix and match the styles and keywords to push the model further.

## Usage

<b>Use Auto for the vae in settings. If you are using a vae based on a SDv1.5 model, you may not get the best results.</b>
<br />

This model has multiple keywords that can be mixed and matched together in order to acheive a multitude of different styles. However, keywords aren't necessarily needed but can help with styling.

<b>Keywords:</b>

<b>Character Styles:</b>
CHV3CZombie, CHV3CAlien, CHV3CBird

<b>Scenery/Styles:</b>
CHV3SLighthouse, CHV3SCute, CHV3SMacro

<b>V3 Keywords:</b>

<b>Character Styles:</b>
CHV3CKnight, CHV3CWizard, CHV3CBarb, CHV3MTroll, CHV3MDeath, CHV3CRogue, CHV3CCyberpunk, CHV3CSamurai, CHV3CRobot

<b>Scenery/Landscapes:</b>
CHV3SWorld, CHV3SSciFi

<b>WIPs (needs fine-tuning, but try it out):</b>
CHV3MDragon, CHV3CVehicle

## Examples

![Collage](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Collage.jpg)



![Alien](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10416-1751637417-CHV3CAlien%2C%20a%20portrait%20of%20a%20man%20in%20a%20cute%20alien%20creature%20costume%20inside%20a%20spaceship%2C%20a%20digital%20rendering%2C%20by%20Arthur%20Pan%2C%20predato.png)

<b>Aliens!</b>

CHV3CAlien, a portrait of a man in a cute alien creature costume inside a spaceship, a digital rendering, by Arthur Pan, predator, ultra detailed content, face, cockroach, avp, face shown, close-up shot, hastur, very detailed<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 8, Seed: 1751637417, Size: 768x768, Model hash: 0eb3318b, ENSD: 3<br /><br />

![Psychadelic Falcon](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10762-2894490509-A-portrait-of-an-anthropomorphic-falcon-in-knight's-armor-made-of-(crystal-stars)-with-big-eyes-surrounded-by-glowing-aura%2C-colo.jpg)

<b>Psychadelic Falcons!</b>

A portrait of an anthropomorphic falcon in knight's armor made of (crystal stars) with big eyes surrounded by glowing aura, colorful sparkle feathers, highly detailed intricated concept art, trending on artstation, 8k, anime style eyes, concept art, cinematic, art award, flat shading, inked lines, artwork by wlop and loish<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 11, Seed: 2894490509, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />

![Macro Mushroom](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10650-3958069384-CHV3SMacro%2C%20a%20nighttime%20macro%20photograph%20of%20a%20glowing%20mushroom%20with%20vibrant%20bioluminescent%20caps%20growing%20on%20tree%20bark%2C%20flat%20light.png)

<b>Macro Mushrooms!</b>

CHV3SMacro, a nighttime macro photograph of a glowing mushroom with vibrant bioluminescent caps growing on tree bark, flat lighting, under saturated, by Anna Haifisch, pexels, fine art, steampunk forest background, mobile wallpaper, roofed forest, trio, 4k vertical wallpaper, mid fall, high detail, cinematic, focus stacking, smooth, sharp focus, soft pastel colors, Professional, masterpiece, commissioned<br /><br />
Negative prompt: amateur, ((b&w)), ((close-up)), (((duplicate))), (((deformed))), blurry, (((bad proportions))), gross proportions, ugly, tiling, poorly drawn, mutation, mutated, disfigured, deformed, out of frame, blurry, bad art, text, logo, signature, watermark<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 7.5, Seed: 3958069384, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />

![Zombie](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10382-28710867-(CHV3CZombie_1.5)%2C%20(a%20medium%20range%20portrait%20of%20elon%20musk%20dressed%20as%20a%20(rotting%20zombie_1.2))%2C%20Professional%2C%20masterpiece%2C%20commissi.png)

<b>Zombies!</b>

(CHV3CZombie:1.5), (a medium range portrait of elon musk dressed as a (rotting zombie:1.2)), Professional, masterpiece, commissioned, Artwork by Shigeru Miyamoto, attractive face, facial expression, professional hands, professional anatomy, 2 arms and 2 legs<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 9, Seed: 28710867, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />

![Lighthouse](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10365-1984075962-CHV3SLighthouse%2C%20a%20painting%20of%20a%20lighthouse%20on%20a%20small%20island%2C%20polycount%20contest%20winner%2C%20cliffside%20town%2C%20gold%2C%20house%20background%2C.png)


<b>Lighthouses!</b>

CHV3SLighthouse, a painting of a lighthouse on a small island, polycount contest winner, cliffside town, gold, house background, highlands, tileable, artbook artwork, paid art assets, farm, crisp clean shapes, featured art, mountains, captain, dominant pose, serene landscape, warm color scheme art rendition, low detail, bay, painting, lowres, birds, cgsociety<br /><br />
Negative prompt: 3d, 3d render, b&w, bad anatomy, bad anatomy, bad anatomy, bad art, bad art, bad proportions, blurry, blurry, blurry, body out of frame, canvas frame, cartoon, cloned face, close up, cross-eye, deformed, deformed, deformed, disfigured, disfigured, disfigured, duplicate, extra arms, extra arms, extra fingers, extra legs, extra legs, extra limbs, extra limbs, extra limbs, extra limbs, fused fingers, gross proportions, long neck, malformed limbs, missing arms, missing legs, morbid, mutated, mutated hands, mutated hands, mutation, mutation, mutilated, out of frame, out of frame, out of frame, Photoshop, poorly drawn face, poorly drawn face, poorly drawn feet, poorly drawn hands, poorly drawn hands, tiling, too many fingers<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 7, Seed: 1984075962, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />


![Cute Creature](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10441-3708829983-CHV3SCute%2C%20CHV3CRogue%2C%20a%20cute%20cartoon%20fox%20in%20a%20rogue%20costume%20in%20a%20nordic%20marketplace%20in%20valhalla%2C%20concept%20art%2C%20deviantart%20contes.png)


<b>Cute Creatures!</b>

CHV3SCute, CHV3CRogue, a cute cartoon fox in a rogue costume in a nordic marketplace in valhalla, concept art, deviantart contest winner, glowing flowers, dofus, epic fantasty card game art, digital art render, dmt art, cute pictoplasma, atom, award winning concept art, at sunrise, engineered, gardening, glowing and epic, awesome, neuroscience<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 9, Seed: 3708829983, Size: 768x768, Model hash: 0eb3318b, ENSD: 3<br /><br />


![Landscape](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10736-2325208488-Studio%20ghibli's%2C%20castle%20in%20the%20sky%2C%20Professional%2C%20masterpiece%2C%20commissioned%2C%20CHV3SWorld%2C%20CHV3SLighthouse%2C%20CHV3SSciFi%2C%20pastel%20col.png)


<b>Cool Landscapes!</b>

Studio ghibli's, castle in the sky, Professional, masterpiece, commissioned, CHV3SWorld, CHV3SLighthouse, CHV3SSciFi, pastel color palette<br /><br />
Negative prompt: 3d, 3d render, b&w, bad anatomy, bad anatomy, bad anatomy, bad art, bad art, bad proportions, blurry, blurry, blurry, body out of frame, canvas frame, cartoon, cloned face, close up, cross-eye, deformed, deformed, deformed, disfigured, disfigured, disfigured, duplicate, extra arms, extra arms, extra fingers, extra legs, extra legs, extra limbs, extra limbs, extra limbs, extra limbs, fused fingers, gross proportions, long neck, malformed limbs, missing arms, missing legs, morbid, mutated, mutated hands, mutated hands, mutation, mutation, mutilated, out of frame, out of frame, out of frame, Photoshop, poorly drawn face, poorly drawn face, poorly drawn feet, poorly drawn hands, poorly drawn hands, tiling, too many fingers, over-saturated<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 8, Seed: 2325208488, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />


![Pretty Bird](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10513-1247149957-10mm%20focal%20length%2C%20a%20portrait%20of%20a%20cute%20style%20cat-bird%20that%20is%20standing%20in%20the%20snow%2C%20made%20of%20(crystal%20stars)%20with%20big%20eyes%20surro.png)


<b>Even more Psychadelic birds!</b>

10mm focal length, a portrait of a cute style cat-bird that is standing in the snow, made of (crystal stars) with big eyes surrounded by glowing aura, colorful sparkle feathers, highly detailed intricated concept art, trending on artstation, 8k, anime style eyes, concept art, cinematic, art award, flat shading, inked lines, artwork by wlop and loish, by Hans Werner Schmidt, flickr, arabesque, chile, green and orange theme, tim hildebrant, jasmine, h1024, gray, hummingbirds, loosely cropped, hd—h1024, green and gold, at home, diana levin, a beautiful mine, 2019<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 8, Seed: 1247149957, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />



![SpaceMan](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/10726-2298273614-(waste%20up)_1.3%20portrait%20of%20an%20attractive%20person%20dressed%20in%20a%20CHV3CCyberpunk.astronaut%20costume%2C%20forest%20in%20the%20background%2C%20smooth%2C.png)


<b>All the V3 Keywords still work nicely!</b>

(waste up):1.3 portrait of an attractive person dressed in a CHV3CCyberpunk.astronaut costume, forest in the background, smooth, sharp focus, Professional, masterpiece, commissioned, professionally drawn face, flat shading, trending on artstation, professional hands, professional anatomy, 2 arms and 2 legs, Artwork by Leonardo Davinci, and Frank Frazetta<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, amateur, ((b&w)), ((close-up)), (((duplicate))), (((deformed))), blurry, (((bad proportions))), gross proportions, ugly, tiling, poorly drawn, mutation, mutated, disfigured, deformed, out of frame, blurry, bad art, text, logo, signature, watermark, (fire)<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 7, Seed: 2298273614, Size: 768x896, Model hash: 0eb3318b, ENSD: 3<br /><br />







<b>V3:</b>
<br /><br />

File Name is CharHelperV3.ckpt -or- CharHelperV3.safetensors<br />

Completely retrained from the begining in a fundamentally different process from CharHelper V1 and 2. This new model is much more diverse in range and can output some amazing results.

It was trained on multiple subjects and styles including buildings, vehicles, and landscapes as well.

## Usage

<b>Use Auto for the vae in settings. If you are using a vae based on a SDv1.5 model, you may not get the best results.</b>
<br />

This model has multiple keywords that can be mixed and matched together in order to acheive a multitude of different styles. However, keywords aren't necessarily needed but can help with styling.

Keywords:

Character Styles:
CHV3CKnight, CHV3CWizard, CHV3CBarb, CHV3MTroll, CHV3MDeath, CHV3CRogue, CHV3CCyberpunk, CHV3CSamurai, CHV3CRobot

Scenery/Landscapes:
CHV3SWorld, CHV3SSciFi

WIPs (needs fine-tuning, but try it out):
CHV3MDragon, CHV3CVehicle

**Mix & Match Styles:**
![X/Y Grid](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/xy_grid-0179-1840075390-A%20realistic%20detail%20of%20a%20mid-range%2C%20full-torso%2C%20waist-up%20character%20portrait%20of%20a%20(CHV3CCyberpunk.grim%20reaper)%20costume%20with%20beauti.jpg)

<b>Mix & Match "CHV3CCyberpunk.grim reaper"</b>

A realistic detail of a mid-range, full-torso, waist-up character portrait of a (CHV3CCyberpunk.grim reaper) costume with beautiful artistic scenery in the background, trending on artstation, 8k, hyper detailed, artstation, concept art, hyper realism, ultra-real, digital painting, cinematic, art award, highly detailed, attractive face, professional hands, professional anatomy, (2 arms, 2 hands)<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 1840075390, Size: 768x896, Model hash: cba4df56, ENSD: 3

**Works with embeddings:**
![X/Y Grid E](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/xy_grid-0193-3079985019-.%2C%20CHV3CWizard%2C%20modelshoot%20style%20mid-range%20character%20detail%20of%20a%20beautiful%20young%20adult%20woman%20wearing%20an%20intricate%20sorceress%20gown.jpg)

<b>Mix & Match "."in the beginning with embedding keywords</b>

., CHV3CWizard, modelshoot style mid-range character detail of a beautiful young adult woman wearing an intricate sorceress gown (casting magical spells under the starry night sky), 23 years old, magical energy, trending on artstation, 8k, hyper detailed, artstation, hyper realism, ultra-real, commissioned professional digital painting, cinematic, art award, highly detailed, attractive face, professional anatomy, (2 professional arms, 2 professional hands), artwork by Leonardo Davinci<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 40, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 2891848182, Size: 768x896, Model hash: cba4df56, ENSD: 3

## Character Examples

![Magical Sorceress](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06502-3460729168-.%2C%20CHV3CWizard%2C%20CHV3CBarb%2C%20modelshoot%20style%20mid-range%20close-up%20of%20a%20beautiful%20young%20adult%20woman%20wearing%20an%20intricate%20sorceress%20g.png)

<b>Magical Sorceress</b>

., CHV3CWizard, CHV3CBarb, modelshoot style mid-range close-up of a beautiful young adult woman wearing an intricate sorceress gown casting magical spells under the starry night sky, magical energy, trending on artstation, 8k, hyper detailed, artstation, hyper realism, ultra-real, commissioned professional digital painting, cinematic, art award, highly detailed, attractive face, professional anatomy, (2 professional arms, 2 professional hands), artwork by Leonardo Davinci<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 3460729168, Size: 768x896, Model hash: cba4df56, ENSD: 3

![Female Death Troll](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/05936-1999542482-a%20(mid-range)%20portrait%20of%20an%20ugly%20green-skinned%20female%20Death%20Troll%20in%20a%20Samurai%20outfit%20in%20a%20dark%20spooky%20forest%2C%20cinematic%2C%20high.png)

<b>Female Death Troll</b>

a (mid-range) portrait of an ugly green-skinned female Death Troll in a Samurai outfit in a dark spooky forest, cinematic, high detail, artwork by wlop, and loish, Professional, masterpiece, commissioned, (attractive face), facial expression, 4k, polycount contest winner, trending on artstation, professional hands, professional anatomy, 2 arms and 2 legs, CHV3CSamurai, CHV3MTroll, CHV3MDeath, Artwork by Leonardo Davinci, Frank Frazetta, Loish and Wlop<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, ((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((close up)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop,  ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (((umbrella)))<br /><br />
Steps: 10, Sampler: DPM++ SDE, CFG scale: 9, Seed: 1999542482, Size: 768x896, Model hash: cba4df56, ENSD: 3

![Astronaut](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06265-1369534527-A%20realistic%20detail%20of%20a%20character%20portrait%20of%20a%20person%20in%20a(n)%20(CHV3CCyberpunk.astronaut)%20costume%20with%20beautiful%20scenery%20in%20the.png)

<b>Astronaut</b>

A realistic detail of a character portrait of a person in a(n) (CHV3CCyberpunk.astronaut) costume with beautiful scenery in the background, trending on artstation, 8k, hyper detailed, artstation, full body frame, complete body, concept art, hyper realism, ultra real, watercolor, cinematic, art award, highly detailed, attractive face, facial expression, professional hands, professional anatomy, 2 arms and 2 legs<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, ((disfigured)), ((bad art)), ((deformed)),((extra limbs)), ((extra barrel)),((close up)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (((tripod))), (((tube))), Photoshop,  ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (((umbrella)))<br /><br />
Steps: 40, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 1369534527, Size: 768x896, Model hash: cba4df56, ENSD: 3

![Cyberpunk Grim Reaper](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06377-1823979933-A%20realistic%20detail%20of%20a%20(mid-range)%20full%20torso%20character%20portrait%20of%20a(n)%20(CHV3CCyberpunk.grim%20reaper)%20costume%20with%20artistic%20sce.png)

<b>Cyberpunk Grim Reaper</b>

A realistic detail of a (mid-range) full torso character portrait of a(n) (CHV3CCyberpunk.grim reaper) costume with artistic scenery in the background, trending on artstation, 8k, hyper detailed, artstation, concept art, hyper realism, ultra-real, digital oil painting, cinematic, art award, highly detailed, attractive face, facial expression, professional hands, professional anatomy, 2 arms<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, amateur, ((extra limbs)), ((extra barrel)), ((b&w)), close-up, (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon<br /><br />
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 1823979933, Size: 768x896, Model hash: cba4df56, ENSD: 3

![>Beautiful Sorceress](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06487-785469078-.%2C%20CHV3CWizard%2C%20a%20close-up_.4%20of%20a%20beautiful%20woman%20wearing%20an%20intricate%20sorceress%20gown%20casting%20magical%20spells%20under%20the%20starry%20n.png)

<b>Beautiful Sorceress</b>

., CHV3CWizard, a close-up:.4 of a beautiful woman wearing an intricate sorceress gown casting magical spells under the starry night sky, magical energy, trending on artstation, 8k, hyper detailed, artstation, concept art, hyper realism, ultra-real, digital painting, cinematic, art award, highly detailed, attractive face, professional hands, professional anatomy, (2 arms, 2 hands)<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 785469078, Size: 768x896, Model hash: cba4df56, ENSD: 3

![>Tiger](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06588-1989203255-mid-range%20modelshoot%20style%20detail%2C%20(extremely%20detailed%208k%20wallpaper)%2C%20A%20detailed%20portrait%20of%20an%20anthropomorphic%20furry%20tiger%20in%20a.png)

<b>It does well with some animals</b>

mid-range modelshoot style detail, (extremely detailed 8k wallpaper), A detailed portrait of an anthropomorphic furry tiger in a suit and tie, by justin gerard and greg rutkowski, digital art, realistic painting, dnd, character design, trending on artstation, Smoose2, CHV3CBarb<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, 3d, 3d render, b&w, bad anatomy, bad anatomy, bad anatomy, bad art, bad art, bad proportions, blurry, blurry, blurry, body out of frame, canvas frame, cartoon, cloned face, close up, cross-eye, deformed, deformed, deformed, disfigured, disfigured, disfigured, duplicate, extra arms, extra arms, extra fingers, extra legs, extra legs, extra limbs, extra limbs, extra limbs, extra limbs, fused fingers, gross proportions, long neck, malformed limbs, missing arms, missing legs, morbid, mutated, mutated hands, mutated hands, mutation, mutation, mutilated, out of frame, out of frame, out of frame, Photoshop, poorly drawn face, poorly drawn face, poorly drawn feet, poorly drawn hands, poorly drawn hands, tiling, too many fingers<br /><br />
Steps: 30, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 1989203255, Size: 768x896, Model hash: cba4df56, ENSD: 3
<br /><br />

## Other Examples
Check out CHV3SSciFi, CHV3SWorld, and CHV3CVehicle for non character images<br />

![>Church in CHV3MDeath Styling](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06200-631476138-a%20((((toon))))%20style%20detail%20of%20a%20((fantasy%2C%20((((cartoon))))%20gothic%20church%20with%20beautiful%20landscaping%20in%20a%20dense%20forest%2C%20in%20the%20s.png)

<b>Church in CHV3MDeath Styling</b>

a ((((toon)))) style detail of a ((fantasy, ((((cartoon)))) gothic church with beautiful landscaping in a dense forest, in the style of CHV3SWorld and CHV3MDeath)) [ :, ((thick black ink outlines)), ((((penned lines, flat shading, doodled lines)))), anime style illustration, dofus style, stylized, digital painting, high detail, professional, masterpiece, Artwork by studio ghibli and Shigeru Miyamoto:.15]<br /><br />
Negative prompt: NegLowRes-2400, NegMutation-500, disfigured, distorted face, mutated, malformed, poorly drawn, ((odd proportions)), noise, blur, missing limbs, ((ugly)), text, logo, over-exposed, over-saturated, over-exposed, ((over-saturated))<br /><br />
Steps: 35, Sampler: Euler a, CFG scale: 13.5, Seed: 631476138, Size: 1024x768, Model hash: cba4df56, Denoising strength: 0.7, ENSD: 3, First pass size: 768x768

![>A group of people looking as a space ship](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/06559-2722466703-CHV3CVehicle%2C%20an%20artistic%20detail%20of%20a%20man%20standing%20on%20top%20of%20a%20lush%20green%20field%20with%20a%20giant%20spaceship%20in%20the%20sky%2C%20by%20Christophe.png)

<b>A group of people looking as a space ship</b>

CHV3CVehicle, an artistic detail of a man standing on top of a lush green field with a giant spaceship in the sky, by Christopher Balaskas, retrofuturism, retro spaceships parked outside, beeple and jeremiah ketner, shipfleet on the horizon, palace floating in the sky, lucasfilm jesper ejsing, of a family leaving a spaceship, highly detailed fantasy art, bonestell, stålenhag, trending on artstation, 8k, hyper detailed, artstation, hyper realism, ultra-real, commissioned professional digital painting, cinematic, art award, highly detailed, attractive face, professional anatomy, (2 professional arms, 2 professional hands), artwork by Leonardo Davinci<br /><br />
Negative prompt: amateur, ((extra limbs)), ((extra barrel)), ((b&w)), ((close-up)), (((duplicate))), ((mutilated)), extra fingers, mutated hands, (((deformed))), blurry, (((bad proportions))), ((extra limbs)), cloned face, out of frame, extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), (tripod), (tube), ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, crossed eyes, dead eyes, body out of frame, blurry, bad art, bad anatomy, (umbrella), weapon, sword, dagger, katana, cropped head<br /><br />
Steps: 40, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 2722466703, Size: 768x896, Model hash: cba4df56, ENSD: 3
<br /><br /><br />

<b>V2:</b>

Trained for an additional 5000 steps. Results will be much more stable and major improvement over V1. Don't forget to add the yaml file into your models directory.

V2 checkpoint filename is CharHelper_v2_ SDv2_1_768_step_8500.ckpt

## Usage

This model tends to like the higher CFG scale range. 7-15 will bring good results. Images come out well if they are 756X756 resolution size and up.

A good prompt to start with is:

(a cyberpunk rogue), charhelper, ((close up)) portrait, digital painting, artwork by leonardo davinci, high detail, professional, masterpiece, anime, stylized, face, facial expression, inkpunk, professional anatomy, professional hands, anatomically correct, colorful

Negative:
((bad hands)), disfigured, distorted face, mutated, malformed, bad anatomy, mutated feet, bad feet, poorly drawn, ((odd proportions)), noise, blur, missing fingers, missing limbs, long torso, ((ugly)), text, logo, over-exposed, over-saturated, ((bad anatomy)), over-exposed, ((over-saturated)), (((weapon))), long neck, black & white, ((glowing eyes))

Just substitute what's in the beginning parenthesis with your subject. You can also substitute "((close up))" with "((mid range))" as well. These worked best for me, but I'm excited to see what everyone else can do with it.

## Examples

Below are some examples of images generated using this model:


**A Woman with Los Muertos Skull Facepaint:**
![Woman with Los Muertos Skull Facepaint](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Skullgirl3.png)

**Rugged Samurai Man:**
![Rugged Samurai Man](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Chuck_Norris_Samurai.png)

**Space Girl:**
![Space Girl](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Space_Girl.png)

**Raver Girl with HeadPhones:**
![Raver Girl](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Cyberpunk_Woman_W_Headphones.png)

**CyberPunk Rogue:**
![CyberPunk Rogue](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/cyberpunk_rogue_in_a_thief_costume.png)

**Toon Animal:**
![Toon Animal](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Cartoon_Animal.png)

**Female Astronaut:**
![Female Astronaut](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Female_Astronaut.png)

**Japanese Samurai:**
![Japanese Samurai](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Japanese_Samurai.png)

**Bell Head:**
![Bell Head](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Bell_Head.png)

**Native American Chief:**
![Native American Chief](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/NativeAmerican_Chief.png)

**CyberPunk Buddha:**
![CyberPunk Buddha](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Cyberpunk_Buddha.png)

**Alien Boy:**
![Alien Boy](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Baby_Yoda.png)

**Los Muertos Facepaint 2:**
![Los Muertos Facepaint 2](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Skullgirl2.png)

**Robot Fighter:**
![Robot Fighter](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Robot_Fighter.png)


**Video Game Elf Character:**
![Video Game Elf Character](https://huggingface.co/ManglerFTW/CharHelper/resolve/main/Image_Samples/Videogame_Character.png)

<b>V1:</b>

Trained for 3500 steps on SD v2.1 using TheLastBen's Fast Dreambooth.
Usage:
Use CharHelper in prompt to bring out the style. Other prompts that work well are 'Character Art', 'Close-up/Mid-range Character portrait', 'Digital Painting', Digital Illustration', 'Stylized', and 'anime'.

Still needs work with anatomy and full body images may need inpainting to fix faces but there are plans to fine-tune the model further in hopes to improve functionality.