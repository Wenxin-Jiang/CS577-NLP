---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a photo of fruins ruins in Paris in front of the Arc de triomphe, mdjrny-v4
    style
---

# DreamBooth model for the fruins concept trained on the CCMat/db-forest-ruins dataset.

This is a Stable Diffusion model fine-tuned on the fruins concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of fruins ruins**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `ruins` images for the landscape theme.<br>
Concept: **fruins** : forest ruins, greenery ruins<br>
Pretrained Model: [prompthero/openjourney](https://huggingface.co/prompthero/openjourney)<br>
Learning rate: 1e-6<br>


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('CCMat/fruins-ruins')
image = pipeline().images[0]
image
```

## Samples

Prompt: "a photo fruins ruins in Paris in front of the Arc de triomphe, in the 1970s, vivid colors"
![example images](images/9b71b776595a3682dd7b6bbcedb59978.png)
<br>

Prompt: "high quality photo of Rome in fruins ruins with the Colosseum in the background"
![example images](images/4b742a116f32a5fc241015ea5f388714.png)
<br>

Prompt: "fruins ruins in London near the Tower Bridge, professional photograph"
![example images](images/c956bbac9db3b8e204354da745a6d882.png)
<br>

Prompt: "A futiristic post-apocalyptic town in fruins ruins trending on artstation, nostalgic lightning, unreal engine 5"
![example images](images/7d7205604a87927cd244eba0f6f29693.png)
<br>

Prompt: "fruins ruins in Saint Petersburg, Sovietwave"
![example images](images/19d5894d6dc82162562a8fbd8f25fc5e.png)
