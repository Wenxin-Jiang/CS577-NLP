---
language:
  - en
thumbnail: "https://huggingface.co/jkcarney/source4_v1.0/blob/main/images/woman1.png"
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - safetensors
  - diffusers
inference: true
---

![samples1](./images/source4-women1.jpg)

[*CKPT DOWNLOAD LINK*](https://huggingface.co/jkcarney/source4_v1.0/blob/main/source4_v1.0.ckpt)

[*SAFETENSORS DOWNLOAD LINK*](https://huggingface.co/jkcarney/source4_v1.0/blob/main/source4_v1.0.safetensors)

# Introduction

Source4 is a Stable Diffusion 1.5/Dreambooth model trained on portraits with dramatic, multicolored lighting. These portraits are heavily inspired by modern, multicolored theatrical lighting (hence the name Source4). This model was fine tuned without prior preservation loss for 8000 steps on over 90 high quality 512x512 images. 

In the prompt, use activation token `source4 style`

![samples2](./images/fantasy_examples2..png)

# Recommendations

I recommend experimenting with different colors in your prompt. For example, adding `teal tones` or `red tones` to your prompt bring those respective colors out. Also try a smaller weight on the `source4 style` prompt (ie, `(source4 style:0.8)`), for a slightly less pronounced but more realistic effect. 

`Euler a` and `DPM++ 2S a Karras` for 25-30 steps have typically given me the highest quality images. Euler a typically gives me more "dreamy" portraits while DPM++ 2S a Karras gives me more realistic portraits.

If the effect is too pronounced or faces are totally blurred out, I recommend decreasing the weight of the activation token. An alternative is to specify `detailed face` in the prompt to ensure a face is actually drawn.

# Additional Samples

![samplese](./images/source4-men1.jpg)

![samples3](./images/source4-women2.jpg)

![fantasy1](./images/fantasy_examples1.png)

![samples4](./images/woman1.png)

![samples5](./images/woman2.png)

![samples6](./images/woman3.png)


Welcome to the technicolored world.

