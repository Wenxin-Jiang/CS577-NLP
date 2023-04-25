---
license: creativeml-openrail-m
tags:
- coreml
- stable-diffusion
- text-to-image
---

# Core ML Converted Model

This model was converted to Core ML for use on Apple Silicon devices by following Apple's instructions [here](https://github.com/apple/ml-stable-diffusion#-converting-models-to-core-ml).<br>
Provide the model to an app such as [Mochi Diffusion](https://github.com/godly-devotion/MochiDiffusion) to generate images.<br>

`split_einsum` version is compatible with all compute unit options including Neural Engine.<br>
`original` version is only compatible with CPU & GPU option.

# Fruity Mix

For Realistic/Anime Type.

# Examples

Sample images have been upscaled using RealESRGAN.
```
Prompt: realistic, masterpiece, highest quality, full body, looking at viewers, highres, indoors, detailed face and eyes, wolf ears, brown hair, short hair, silver eyes, necklace, sneakers, parka jacket, solo focus
Negative: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
Steps: 12
Guidance Scale: 11
Sampler: DPM-Solver++
```
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/1.png" />
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/2.png" />
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/3.png" />
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/4.png" />
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/5.png" />
<img width="512" src="https://huggingface.co/godly-devotion/coreml-fruity-mix/resolve/main/images/6.png" />
