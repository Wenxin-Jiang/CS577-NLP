---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---
# Core ML Converted Model:

  - This model was converted to [Core ML for use on Apple Silicon devices](https://github.com/apple/ml-stable-diffusion). Conversion instructions can be found [here](https://github.com/godly-devotion/MochiDiffusion/wiki/How-to-convert-ckpt-or-safetensors-files-to-Core-ML).<br>
  - Provide the model to an app such as Mochi Diffusion [Github](https://github.com/godly-devotion/MochiDiffusion) - [Discord](https://discord.gg/x2kartzxGv) to generate images.<br>
  - `split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
  - `original` version is only compatible with CPU & GPU option.<br>
  - Custom resolution versions are tagged accordingly.<br>
  - `vae` tagged files have a vae embedded into the model.<br>
  - Descriptions are posted as-is from original model source. Not all features and/or results may be available in CoreML format.<br>
  - This model was converted with `vae-encoder` for i2i.
  
# Note: Some models do not have the [unet split into chunks](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).

# EvoArt-Mj4DreamMix:
Source(s): [CivitAI](https://civitai.com/models/4042/evoart-mj4dreammix)

It is a Remix Model of some MJ4 style models like openjourney-v2 and other amazing models, specially with 3DKX model,and a little more 768+model in weight. so it can handle high-resolution output well.

I found it is a good effect when two similar style plus together. so you may look it as the mJ4-enhanced model.

To enhance the output,you can use "midjourney style" in the beginning of your prompt as trigger. Hypernetwork is not suggested，but <0.3 may lead to a different effect.