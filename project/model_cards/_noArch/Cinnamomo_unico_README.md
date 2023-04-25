---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: cc-by-nc-sa-4.0
inference: true
pipeline_tag: text-to-image
---

# i modelli 'Unico'

<img src=https://i.imgur.com/5KfDOik.png
width=100%  height=100%>
Unico is the series of custom mixed models. Based on Inizio Unico and AbyssOrange2 models with U-Net Merge, and support .safetensors format only.

[WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)-amicable

## Summary
This model repository includes 4 main models currently:

1.
| Model: A | Model: B | Merge Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| [Inizio Fantasma+Inizio Inseguitore+Inizio Foschia](https://huggingface.co/Cinnamomo/inizio) | [Inizio Replicante+Inizio Skinjob+Inizio Deckard](https://huggingface.co/Cinnamomo/inizio) | weighted, M=0.66666666+M=0.66666666 | N/A | *Unico* |

Unico is another form of [Inizio Unico](https://huggingface.co/Cinnamomo/inizio).

2.
| Model: A | Model: B | Merge Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| [Inizio Unico](https://huggingface.co/Cinnamomo/inizio) | [AbyssOrange2 SFW](https://huggingface.co/WarriorMama777/OrangeMixs) | weighted, M=0.75. | N/A | *Unico Arancia* |

Unico Arancia('Orange🍊') is the closest model from AbyssOrange2 SFW. Anime~Semi-realistic.

3.
| Model: A | Model: B | U-Net Merge Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| Unico Arancia | [Openniji](https://huggingface.co/Korakoe/OpenNiji) | 1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1 | 0 | *Unico Bergamotto* |

Unico Bergamotto('Bergamot🍊') is significantly improved model of Unico Arancia for lightning and hand details. Anime~Semi-realistic.

4.
| Model: A | Model: B | U-Net Merge Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| Unico Vaniglia | [Openniji](https://huggingface.co/Korakoe/OpenNiji) | 1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1 | 0 | *Unico Vaniglia 1.5* |

Unico Vaniglia('Vanilla🍦') 1.5 is significantly improved model of Unico Vaniglia for lightning and hand details. Anime~Semi-realistic.

5.
| Model: A | Model: B | U-Net Merge Weight | Base alpha | Merge Name |
| --- | --- | --- | --- | --- |
| Unico Arancia+[Camellia Mix](https://civitai.com/models/14667/camelliamix) | [Night Sky YOZORA Style Origin](https://civitai.com/models/12262/night-sky-yozora-style-model) | experimental mix | 0 | *Unico Ranginak* |

Unico Ranginak('Persian Date Cake🍰') is advanced model of Unico Arancia for pastel tone with super high resolution-ready. Anime~Semi-realistic.

- NOTE: Another models are moved to legacy folder.

## Setting Reccomendation
```
##Basic prompts for anime
"txt2img/Prompt/value": "(best quality, extreme intricate detailed, octane render, cinematic light), (/*place tags*/), (solo girl/*character tags*/), (/*pose tags*/), (big breasts, big pelvis, best ratio four finger and one thumb, /*body tags*/), (beautiful eyes and bishoujo face), (/*colour of hair tag*/ hair, /*colour of eyes*/ eyes, thick lips, lip gloss), (/*clothing tags*/)",

"txt2img/Negative prompt/value": "(nsfw, worst quality, low quality:1.4), (greyscale), (fingers(missing, fused, interlocked, abnormal, too many, bad anatomy, fused, fusion, lose, bad detailed, mutated), digit(extra, fewer), hands(greater than 4 fingers, less than 4 fingers, cropped, mutated):1.4), (fat, chubby, curvy, watermark, signature:1.4), (3d, realistic)"
```
- Variational Automatic Encoder: [SD MSE 840k.vae.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)
- Clip Skip: 2
- Resolution: 1024x576 w/ HighRes. Fix
- HighRes. Fix: R-ESRGAN General WDN 4xV3; upscale by 1.25

## Sample Images

>
> <img src=https://i.imgur.com/CvjtsXx.jpg
> width=100%  height=100%>
> ▲ X/Y Plot #1
>
> <img src=https://i.imgur.com/aYIyVFJ.png
> width=100%  height=100%>
>
> <img src=https://i.imgur.com/pKNd2XO.png
> width=100%  height=100%>
>
> <img src=https://i.imgur.com/GknH4e0.png
> width=100%  height=100%>
>
> <img src=https://i.imgur.com/rVblL4d.png
> width=100%  height=100%>
> ▲ Unico Arancia
>
> <img src=https://i.imgur.com/8vCjbUK.png
> width=100%  height=100%>
>
> <img src=https://i.imgur.com/HKvXAFx.png
> width=100%  height=100%>
> ▲ Unico Bergamotto

## License Information

This model follows CC-BY-NC-SA 4.0 & Creative ML Open RAIL-M: [Stable Diffusion License](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
You may use whatever you want except commercial purposes to sell models, create images without permission request.

## Contact
*vitorriofungi@gmail.com* or [*Find Cinnamomo on Arcalive AI Art Channel*](https://arca.live/b/aiart)