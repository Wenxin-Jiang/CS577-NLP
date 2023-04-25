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

# 8528-diffusion final
Source: [Hugging Face](https://huggingface.co/852wa/8528-diffusion) (The release of the source model has ended.)

8528-diffusion is a latent text-to-image diffusion model, conditioned by fine-tuning to colorful character images.
8528 Diffusion is a fine-tuning model of Stable Diffusion v1.4 with AI output images (t2i and t2i with i2i).

I recommend entering "low quality,worst quality," for Negative prompt and Clip skip: 2. 

<!--
<img src=https://i.imgur.com/vCn02tM.jpg >
!-->
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/vCn02tM.jpg)

((ultra-detailed)), ((illustration)), Silver hair, red eyes, beautiful eyes, dress, Queen,Anime style, pretty face, pretty eyes, pretty, girl,High resolution, beautiful girl,octane render, realistic, hyper detailed ray tracing, 8k,classic style,Rococo
Negative prompt: (low quality, worst quality:1.4) concept art
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 241379229, Size: 512x768, Model hash: 31cd036c, Clip skip: 2



# 8528-diffusion v0.4

<!--
<img src=https://i.imgur.com/X2zFoeA.jpg >
!-->
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/X2zFoeA.jpg)


# 8528-diffusion v0.3

<!--
<img src=https://i.imgur.com/QQuNpYl.png >
<img src=https://i.imgur.com/u785LlC.png >
!-->
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/QQuNpYl.png)
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/u785LlC.png)

# 8528-diffusion v0.2

8528-diffusion is a latent text-to-image diffusion model, conditioned by fine-tuning to colorful character images.
8528 Diffusion v0.2 & v0.1 is a fine-tuning model of Waifu Diffusion with AI output images (t2i and t2i with i2i).

<!--
<img src=https://i.imgur.com/z4sFctp.png >
!-->
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/z4sFctp.png)

# 8528-diffusion v0.1
<!--
<img src=https://i.imgur.com/8chXeif.png >
!-->
![](https://huggingface.co/coreml/coreml-8528-diffusion/resolve/main/example_images.md/8chXeif.png)

[google colab](https://colab.research.google.com/drive/1ksRxO84CMbXrW_p-x5Vuz74AHnrWpe_u)

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

<!-- Discord Server has been stopped.
## Discord

https://discord.gg/ax9KgpUMUP
!-->