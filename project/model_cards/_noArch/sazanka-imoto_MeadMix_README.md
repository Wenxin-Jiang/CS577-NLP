---
language:
- en
tags:
- stable-diffusion
license: creativeml-openrail-m
pipeline_tag: text-to-image
---
# MeadMix
![TitleImage](https://huggingface.co/sazanka-imoto/MaedMix/resolve/main/examples/13486-3096934695-masterpiece%201%20girl%20smile%20blush%20standing%20Dirndl%20blonde%20hair%20blue%20eys%20mead%20bottle%20Taverns%20middle%20ages%20anime3839bcfb487f3d164c8fcf80d50c9fa6b72ee7b8.png)
MeadMix is a merged model that creates a range of expressions, from anime to semi-realistic, with the aim of producing visually appealing images with simple prompts. It can be used with tools such as StableDiffusionWebui:Automatic1111 and others.

Please note that this model includes NSFW content. If you do not want to see NSFW content, please include "nsfw," "nude," etc. in the negative prompt.

It is highly recommended to use the WD's kl-f8-anime VAE for generating images. Generating images without using the VAE will result in poor saturation and contrast.

To generate anime expressions, add "masterpiece, anime" to the prompt and "realistic" to the negative prompt. To generate semi-realistic expressions, simply add "realistic" to the prompt.
<br>

# Examples
![example01](https://huggingface.co/sazanka-imoto/MaedMix/resolve/main/examples/example01.png)
```
1girl, solo, hat, witch hat, skirt, long hair, thighhighs, bow, flask, red bow, book, long sleeves, black footwear, open mouth, black hair, holding, shirt, indoors, flower, test tube, pleated skirt, black headwear, bangs, vial, purple flower, :d, looking at viewer, boots, smile, crystal, brown eyes, sitting, round-bottom flask, hat bow, magic circle, blue skirt, magic, open book, window, witch, puffy sleeves, black shirt, gem, red thighhighs, belt, orb, potion, brown thighhighs, purple skirt, asymmetrical legwear, ribbon, plant, buckle, thighhighs under boots
Negative prompt: (worst quality:1.4), (low quality:1.4),
```
```
1girl, pirate hat, skirt, epaulettes, pirate, solo, pink hair, hairclip, hat, hair ornament, long hair, open mouth, blue eyes, weapon, ascot, smile, hand on hip, sword, belt, pleated skirt, looking at viewer, :d, hat feather, cape, skull and crossbones, cowboy shot, miniskirt, coat, jacket, long sleeves, black headwear, black coat, bangs, blue sky
Negative prompt: (worst quality:1.4), (low quality:1.4),
```
<br>

![example02](https://huggingface.co/sazanka-imoto/MaedMix/resolve/main/examples/example02.png)
```
1girl, book, solo, hat, gloves, thighhighs, long hair, bow, striped, striped thighhighs, flower, watch, ((clock)), hair bow, ((pocket watch)), ribbon, frills, very long hair, open book, looking at viewer, capelet
Negative prompt: (worst quality:1.4), (low quality:1.4),
```

```
masterpiece, 1girl, solo, planet, space, astronaut, spacesuit, earth (planet), sun, solo, spacecraft, science fiction, realistic, helmet,anime
Negative prompt: (worst quality:1.4), (low quality:1.4),
```
<br>

![example03](https://huggingface.co/sazanka-imoto/MaedMix/resolve/main/examples/example03.png)
```
masterpiece, weapon, fire, 1 girl, horse, armor, riding, polearm, soldier, scenery, castle, war, battle, helmet, cloud, holding, fantasy, horseback riding, holding weapon, banner
Negative prompt: (worst quality:1.4), (low quality:1.4),
```

```
armor, weapon, sword, helmet, solo, 1boy, gauntlets, full armor, outdoors, male focus, shoulder armor, pauldrons, cape, breastplate, standing, blurry background, snow, blurry, day, blood
Negative prompt: (worst quality:1.4), (low quality:1.4),
```