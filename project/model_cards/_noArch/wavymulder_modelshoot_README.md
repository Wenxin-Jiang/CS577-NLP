---
language:
- en
thumbnail: "https://huggingface.co/wavymulder/modelshoot/resolve/main/images/page1.jpg"
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- safetensors
- diffusers
inference: true
---



**Modelshoot Style**
![Header](https://huggingface.co/wavymulder/modelshoot/resolve/main/images/page1.jpg)
[*CKPT DOWNLOAD LINK*](https://huggingface.co/wavymulder/modelshoot/resolve/main/modelshoot-1.0.ckpt)

Use `modelshoot style` in your prompt (I recommend at the start)

I also suggest your prompts include subject and location, for example "`amy adams at the construction site`" , as this helps the model to resolve backgrounds and small details.

Modelshoot is a Dreambooth model trained from 1.5 with VAE on a diverse set of photographs of people. The goal was to create a model focused on full to medium body shots, with an emphasis on cool clothing and a fashion-shoot aesthetic. A result of the composition is that when your subject is further away, their face will usually look worse (and for celebrities, less like them). This limitation of training on 512x512 can be fixed with inpainting, and I plan on revisiting this model at higher resolution in the future.

Modelshoot style works best when using a tall aspect ratio.

This model was inspired by all the great responses to Analog Diffusion, especially ones where you all trained yourselves in and created awesome, fashionable photos! I hope that this model allows even greater images :)

Please see [this document where I share the parameters (prompt, sampler, seed, etc.) used for all example images above.](https://huggingface.co/wavymulder/modelshoot/resolve/main/parameters_for_samples.txt)

See below a batch example and how the model helps ensure a fashion-shoot composition without any excessive prompting. No face restoration used for any examples on this page, for demonstration purposes.

![Bulk Example](https://huggingface.co/wavymulder/modelshoot/resolve/main/images/page2.jpg)

