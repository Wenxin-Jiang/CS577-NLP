---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---
# Core ML Converted Model:

  - This model was converted to [Core ML for use on Apple Silicon devices](https://github.com/apple/ml-stable-diffusion). Conversion instructions can be found [here](https://github.com/godly-devotion/MochiDiffusion/wiki/How-to-convert-ckpt-or-safetensors-files-to-Core-ML).<br>
  - Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>
  - `split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
  - `original` version is only compatible with CPU & GPU option.<br>
  
# Note: Some models do not have the [unet split into chunks](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).

# Shady Art OFFICIAL:
Source(s): [Hugging Face](https://huggingface.co/ShadyART/Shady_Art_Official) - [CivitAI](https://civitai.com/models/4515/shady-art-official)

This is my personal model based on SD 1.5.

I have personally tested it creating more than 10000 unique images and it has always met my expectations. Positive and negative prompts affect the image in exactly the same way, so you'll have to play around with it!

Info:

-Close-up portraits, half-length photos and full-body photos give the best results but you can generate everything.

-The faces and in particular the eyes, if described properly, are surreal in how beautiful they are as this model generates beautiful faces by default, therefore positive prompts like "symmetrical face, perfect face, symmetrical eyes etc..." are useless and sometimes compromise the result, if necessary use negative prompts like "deformed, disfigured etc..." and the face will come out perfect.

-This model has the ability to also create landscape images (fantasy or not) but you will have to waste more time on it, as it is focused on"subjects".

-Be creative, describe the image in great detail, this guarantees a better overall result. 

-NSFW have wonderful results both in txt2image and in img2img, if you want to transform a non-NSFW image into NSFW and img2img does not give good results, use Inpaint and you will succeed 100%.

-Euler a, DPM++ 2M a Karras and DDIM seem to give the best results

Special thanks to sovereignrk and logoth for helping me with some new prompts!