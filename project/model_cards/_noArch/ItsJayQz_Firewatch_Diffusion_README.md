---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- diffusers
inference: true
---

### Firewatch Diffusion
This model was trained on in-game footages, and some game posters by Olly Moss. 
The model can make good looking nature sceneries similar to the game art style, with some objects.
It can not make portraits at all, since throughout the game you don't actually meet any characters.

To reference the art style, use the token: fwatch style

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run Firewatch_Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/ItsJayQz/Firewatch_Diffusion)

Here are some samples.

**Sceneries**
![fwatch.png](https://s3.amazonaws.com/moonup/production/uploads/1670473030496-635eafb49f24f6db0a1eafd1.png)
![fwatch2.png](https://s3.amazonaws.com/moonup/production/uploads/1670473031879-635eafb49f24f6db0a1eafd1.png)

Prompt used:
Beautiful *mountain/lake/beach/etc* in fwatch style
Guidance: 7
Steps: 65 using DDIM

I'm not a prompt wizard so you can definitely get better results with some tuning.

**Objects**
![fwatch3.png](https://s3.amazonaws.com/moonup/production/uploads/1670473031927-635eafb49f24f6db0a1eafd1.png)

**Disclaimers**
- I'm in no way affliated with Campo Santo, or any entities relating to the ownership of the game artworks.
- The phrase Firewatch is simply a reference for accessibility.
- This was created entirely for research, and entertainment purpose.
- I did not plan, or is planning on turning this model into a commercial product, or use for commercial purposes.
- I do not condone the usage of the model for making counterfeit products that might infringe on Campo Santo/Olly Moss's copyrights/trademarks.

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