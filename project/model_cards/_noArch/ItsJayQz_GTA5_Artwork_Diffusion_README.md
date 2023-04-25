---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- diffusers
- grand theft auto
- game
inference: true
---

### GTA5 Artwork Diffusion
This model was trained on the loading screens, gta storymode, and gta online DLCs artworks.
Which includes characters, background, chop, and some objects.
The model can do people and portrait pretty easily, as well as cars, and houses.
For some reasons, the model stills automatically include in some game footage, so landscapes tend to look a bit more game-like.
Please check out important informations on the usage of the model down bellow.

To reference the art style, use the token: gtav style

There is already an existing model that uses textual inversion. This is trained using Dreambooth instead, whether or not this method is better, I will let you judge.

### Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run GTA5_Artwork_Diffusion:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/ItsJayQz/GTA5_Artwork_Diffusion)

Here are some samples.

**Portraits**
![kreeves.png](https://s3.amazonaws.com/moonup/production/uploads/1670902497106-635eafb49f24f6db0a1eafd1.png)
![gta1.png](https://s3.amazonaws.com/moonup/production/uploads/1670900787088-635eafb49f24f6db0a1eafd1.png)
![gta3.png](https://s3.amazonaws.com/moonup/production/uploads/1670900787080-635eafb49f24f6db0a1eafd1.png)

Prompt used:
*name* in gtav style
Guidance: 7
Steps:  65 using DDIM

I'm not a prompt wizard so you can definitely get better results with some tuning.

**Landscapes**
![gta4.png](https://s3.amazonaws.com/moonup/production/uploads/1670901788979-635eafb49f24f6db0a1eafd1.png)

**Objects**
![gta2.png](https://s3.amazonaws.com/moonup/production/uploads/1670900787203-635eafb49f24f6db0a1eafd1.png)

**Disclaimers**
- I'm in no way affliated with Rockstar, or any entities relating to the ownership of the game artworks.
- The phrase GTA is simply a reference for accessibility.
- This was created entirely for research, and entertainment purpose.
- I did not plan, or is planning on turning this model into a commercial product, or use for commercial purposes.
- I do not condone the usage of the model for making counterfeit products that might infringe on Rockstar's copyrights/trademarks.

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