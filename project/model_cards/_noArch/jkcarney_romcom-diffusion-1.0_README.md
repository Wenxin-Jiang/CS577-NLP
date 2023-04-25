---
language:
  - en
thumbnail: "https://huggingface.co/jkcarney/romcom-diffusion-1.0/blob/main/samples1.png"
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - safetensors
  - diffusers
inference: true
---

![samples1](./samples1.png)

[*CKPT DOWNLOAD LINK*](https://huggingface.co/jkcarney/romcom-diffusion-1.0/blob/main/romcom-diffusion-1.0.ckpt)

[*SAFETENSORS DOWNLOAD LINK*](https://huggingface.co/jkcarney/romcom-diffusion-1.0/blob/main/romcom-diffusion-1.0.safetensors)

romcom-diffusion is a Dreambooth model fine tuned on cropped 512x512 stills from various 1990s era romantic comedy movies. These stills are primarily of human subjects, but there are also samples of wide shots, crowds, and cars. Currently the list of movies used is:

1. 10 Things I Hate About You (64)
2. Clueless (45)
3. American Pie (37)

In the future I may release a new version with more movie stills from additional movies. My hope is that more samples from more movies would increase facial fidelity and style.

In the prompt, use activation token: `romcom style`

Trained using Stable Diffusion 1.5 as a base.

I also recommend including `movie still` in your prompt; it was the class prompt for regularization images and I found it produces the best results. 

I've found the best results using the `DPM++ 2S a Karras` sampler as well, but obviously feel free to experiment. 

Sample image generation parameters can be found in `prompts.txt`


![samples1](./samples2.png)