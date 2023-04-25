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

# Dreamlike Photoreal 2.0:
Source(s): [Hugging Face](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0) - [CivitAI](https://civitai.com/models/3811/dreamlike-photoreal-v2)

Dreamlike Photoreal 2.0 is SD 1.5 fine tuned on high quality photos, made by dreamlike.art

Warning: This model is horny! Add "nude, naked" to the negative prompt if want to avoid NSFW.

You can add photo to your prompt to make your gens more photorealistic.


Non-square aspect ratios work better for some prompts. If you want a portrait photo, try using a vertical aspect ratio. If you want a landscape photo, try using a horizontal aspect ratio.


This model was trained on 768x768px images, so use 768x768px, 640x896px, 896x640px, etc. It also works pretty good with higher resolutions such as 768x1024px or 1024x768px.