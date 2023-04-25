---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- diffusers
- game
---
## BreathOfTheWild Diffusion
This model was trained on screenshots from Botw and a few from Hyrule warrior, but because I don't actually play both of them, it was pretty hard to get decent training images.
The portraits still contain resemblance of link and zelda, this can sometimes be avoided by prompting "portrait of", and the model isn't exactly easily modifiable through prompting.
The landscapes are pretty good though.

To reference the art style, use the token: botw style

You can also check out the higher quality, but trickier V2 on [Civitai](https://civitai.com/models/4676/breathofthewild-diffusion).

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run BreathOfTheWild_Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/ItsJayQz/BreathOfTheWild_Diffusion?logs=build)

Here are some samples.

**Portraits**
![botw5.png](https://s3.amazonaws.com/moonup/production/uploads/1673980004637-635eafb49f24f6db0a1eafd1.png)
![botw1.png](https://s3.amazonaws.com/moonup/production/uploads/1673980004598-635eafb49f24f6db0a1eafd1.png)

Prompt used:
botw style A stunning intricate full color portrait of anad, epic character composition, wearing a white dress, brown hair, by ilya kuvshinov, alessio albi, nina masic, sharp focus, natural lighting, subsurface scattering, f2, 35mm, film grain
Negative: ((disfigured)), ((bad art)), ((deformed)), ((poorly drawn)), ((extra limbs)), ((close up)), ((b&amp;w)), weird colors, blurry
Guidance: 10
Steps:  30 using DPM++ 2M Karras

I'm not a prompt wizard so you can probably get better results with some tuning.


**Landscape**
![botw3.png](https://s3.amazonaws.com/moonup/production/uploads/1673929825968-635eafb49f24f6db0a1eafd1.png)
![botw2.png](https://s3.amazonaws.com/moonup/production/uploads/1673929825987-635eafb49f24f6db0a1eafd1.png)
![botw4.png](https://s3.amazonaws.com/moonup/production/uploads/1673929825997-635eafb49f24f6db0a1eafd1.png)

**Disclaimers**
- I'm in no way affliated with Nintendo, or any entities relating to the ownership of the game.
- The phrase Breath Of The Wild is simply a reference for accessibility.
- This was created entirely for research, and entertainment purpose.
- I did not plan, or is planning on turning this model into a commercial product, or use for commercial purposes.
- I do not condone the usage of the model for making counterfeit products that might infringe on Nintendo's copyrights/trademarks.

**License**
- This model is under Creative OpenRAIL-M.
- This means the model can be used royalty-free, and flexible with the model usage, such as redistribution of the model, or of any derivatives of the model.
- However, there are restrictions on the openess of the license.
More info into the restrictions can be found [here](https://huggingface.co/spaces/CompVis/stable-diffusion-license).

**Responsibilities**
- By using/downloading the model, you are responsible for:
- All outputs/usage of the model.
- Understanding the Disclaimers.
- Upholding the terms of the license.

Thanks for checking out the model!