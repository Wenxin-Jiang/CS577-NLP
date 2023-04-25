---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---
# Core ML Converted Model:

  - This model was converted to Core ML for use on Apple Silicon devices. Instructions can be found [here](https://github.com/godly-devotion/MochiDiffusion/wiki/How-to-convert-ckpt-files-to-Core-ML).<br>
  - Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>
  - `split_einsum` version is compatible with all compute unit options including Neural Engine.<br>

# Note: This model does not have the [unet split into chunks](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).

# GTA5 Artwork Diffusion:
Source(s): [Hugging Face](https://huggingface.co/ItsJayQz/GTA5_Artwork_Diffusion) - [CivitAI](https://civitai.com/models/1309/gta5-artwork-diffusion)

GTA5 Artwork Diffusion
This model was trained on the loading screens, gta storymode, and gta online DLCs artworks. Which includes characters, background, chop, and some objects. The model can do people and portrait pretty easily, as well as cars, and houses. For some reasons, the model stills automatically include in some game footage, so landscapes tend to look a bit more game-like. Please check out important informations on the usage of the model down bellow.

To reference the art style, use the token: gtav style

There is already an existing model that uses textual inversion. This is trained using Dreambooth instead, whether or not this method is better, I will let you judge.