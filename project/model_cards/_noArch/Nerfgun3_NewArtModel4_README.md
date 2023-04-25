---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%201.png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# NewArtModel Version 4

## Why NewArtModel?

The model itself is mainly based on [Waifu-Diffusion 3](https://huggingface.co/hakurei/waifu-diffusion) and was finetuned using a dataset of my own artwork and collected artwork of others. 

I hope you enjoy the model. If you have any questions, you can ask me anything via Discord: "Nerfgun3#7508"

<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%201.png"/>

# Use Cases

The model itself is very good in itself and produces high quality images from landscapes to portraits to anime. However, it shines the most when merged with other models.

Here are a few examples:
1. Generally all models from [andite](https://huggingface.co/andite)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Token
This model was trained on a token **m_style** like the Dreambooth models, but as can be seen in the sample prompts, it is not needed, and since merging is one of its strengths, it is not essential.

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%204.png"/>

```
1girl, animal_ears, bangs, (masterpiece:1.2), (highly detailed), (looking at viewer), ((best quality)), (ultra-detailed), black_hair, black_skirt, red_ribbon, blurry, blurry_background, collared_shirt, facial_mark, flower, fox_ears, grey_flower, hair_flower, hair_ornament, highres, league_of_legends, long_hair, looking_at_viewer, neck_ribbon, nixeu, orange_eyes, pleated_skirt, ribbon, shirt, sitting, skirt, solo, whisker_markings, white_shirt
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%203.png"/>

```
m_style, 1girl, (masterpiece:1.2), ((best quality)), (ultra-detailed), (barbosa_style:0.8)
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%202.png"/>

```
m_style, 1girl, (masterpiece:1.2), ((best quality)), (ultra-detailed)
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 4**
<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%205.png"/>

```
(Glowing neon:1.1) (lineart:1.3), 1girl, highly detailed face, (mystical bioluminescent flowers:1.3), mid shot, full body, a somber expression, sadness, (dark background:1.2), (darkness:1.2), a beautiful vortex of energy swirling around her, vibrant colors, finding beauty in the darkness, superb, 8k wallpaper, extremely detailed, (thick brush strokes:1.3), intricate, (oil painting:0.9), limited palette
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 5**
<img alt="Showcase" src="https://huggingface.co/Nerfgun3/NewArtModel4/resolve/main/preview/Preview%206.png"/>

```
A beautiful picture of a girl with cat ears and wings, cat ears, anime girl, mosaic, aurora, pixalated, anime, illustration, intricate, high detailed face, cinematic lighting, highly detailed, octane, digital painting, wavy hair, full body shot, Polychromatic noir, paper cut art, tenebrism, reflection, sharp focus, vibrant colours
Steps: 32, Sampler: Euler a, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)