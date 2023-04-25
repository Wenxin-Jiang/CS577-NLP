---
license: creativeml-openrail-m
inference: true
thumbnail: https://s3.amazonaws.com/moonup/production/uploads/1674263031698-6305db1fcfbde33ef7d480ff.png
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
---

# Plat Diffusion v1.3.1

Plat Diffusion v1.3.1 is a latent model fine-tuned on [Waifu Diffusion v1.4 Anime Epoch 2](https://huggingface.co/hakurei/waifu-diffusion-v1-4) with images from niji・journey and some generative AI.

`.safetensors` file is [here](https://huggingface.co/p1atdev/pd-archive/tree/main).

[kl-f8-anime2.ckpt](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt) is recommended for VAE.

![eyecatch](https://s3.amazonaws.com/moonup/production/uploads/1674263031698-6305db1fcfbde33ef7d480ff.png)


### Recomended Negative Prompt

```
nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digits, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
```

# Samples

![sample1](https://huggingface.co/p1atdev/plat-diffusion/resolve/main/samples/sample1.jpg)

```
masterpiece, best quality, high quality, 1girl, solo, brown hair, green eyes, looking at viewer, autumn, cumulonimbus cloud, lighting, blue sky, autumn leaves, garden, ultra detailed illustration, intricate detailed
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

---

(This model is not good at male, sorry)

![sample2](https://huggingface.co/p1atdev/plat-diffusion/resolve/main/samples/sample2.jpg)


```
masterpiece, best quality, high quality, 1boy, man, male, brown hair, green eyes, looking at viewer, autumn, cumulonimbus cloud, lighting, blue sky, autumn leaves, garden, ultra detailed illustration, intricate detailed
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

---

![sample3](https://huggingface.co/p1atdev/plat-diffusion/resolve/main/samples/sample3.jpg)


```
masterpiece, best quality, 1girl, pirate, gloves, parrot, bird, looking at viewer,
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, 3d
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

---

![sample4](https://huggingface.co/p1atdev/plat-diffusion/resolve/main/samples/sample4.jpg)


```
masterpiece, best quality, scenery, starry sky, mountains, no humans
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

# 🧨 Diffusers

```py
from diffusers import StableDiffusionPipeline
import torch

model_id = "p1atdev/plat-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32) # not working with float16
pipe = pipe.to("cuda")

prompt = "masterpiece, best quality, 1girl, solo, short hair, looking at viewer, japanese clothes, blue hair, portrait, kimono, bangs, colorful, closed mouth, blue kimono, butterfly, blue eyes, ultra detailed illustration"
negative_prompt = "nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry"
image = pipe(prompt, negative_prompt=negative_prompt).images[0]  
    
image.save("girl.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
