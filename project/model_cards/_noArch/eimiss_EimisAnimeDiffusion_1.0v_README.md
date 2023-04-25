---
thumbnail: https://imgur.com/6ztDBPR.png
language:
- en
tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers
license: creativeml-openrail-m
inference: true

---
# Check out v2 of the model:
https://huggingface.co/eimiss/EimisAnimeDiffusion_2.0v

# Diffusion model
This model is trained with high quality and detailed anime images.

## Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI run EimisAnimeDiffusion_1.0v:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/EimisAnimeDiffusion_1.0v)

# Sample generations
This model works well on anime and landscape generations.<br>
Anime:<br>
There are some sample generations:<br>

```
Positive:a girl, Phoenix girl, fluffy hair, war, a hell on earth, Beautiful and detailed explosion, Cold machine, Fire in eyes, burning, Metal texture, Exquisite cloth, Metal carving, volume, best quality, normal hands, Metal details, Metal scratch, Metal defects, masterpiece, best quality, best quality, illustration, highres, masterpiece, contour deepening, illustration,(beautiful detailed girl),beautiful detailed glow
Negative:lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a, CFG scale: 8, Seed: 4186044705/4186044707, Size: 704x896
```
<img src=https://imgur.com/2U295w3.png width=75% height=75%>
<img src=https://imgur.com/2jtF376.png width=75% height=75%>


```
Positive:(1girl), cute, walking in the park, (night), full moon, north star, blue shirt, red skirt, detailed shirt, jewelry, autumn, dark blue hair, shirt hair, (magic:1.5), beautiful blue eyes
Negative: lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 35, Sampler: Euler a, CFG scale: 9, Seed: 296195494, Size: 768x960
```
<img src=https://imgur.com/gudKxQe.png width=75% height=75%>

```
Positive:night , ((1 girl)), alone, masterpiece, 8k wallpaper, highres, absurdres, high quality background, short hair, black hair, multicolor hair, beautiful frozen village, (full bright moon), blue dress, detailed dress, jewelry dress, (magic:1.2), blue fire, blue eyes, glowing eyes, fire, ice goddess, (blue detailed beautiful crown), electricity, blue electricity, blue light particles
Negative: lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a Karras, CFG scale: 9, Seed: 2118767319, Size: 768x832
```
<img src=https://imgur.com/lJL4CJL.png width=75% height=75%>

Want to generate some amazing backgrounds? No problem:
```
Positive: above clouds, mountains, (night), full moon, castle, huge forest, forest between mountains, beautiful, masterpiece
Negative: lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a Karras, CFG scale: 9, Seed: 83644543, Size: 896x640
```
<img src=https://imgur.com/XfxAx0S.png width=75% height=75%>

## Disclaimer
Some prompts might not work perfectly (mainly colors), so add some more prompts for it to work, or try these -->().
Usually they help. Also works well with img2img if you want to add detail.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)