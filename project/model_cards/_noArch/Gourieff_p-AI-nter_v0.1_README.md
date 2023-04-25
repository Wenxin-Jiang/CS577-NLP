---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
## p-AI-nter -- v0.1 

Core model is SD-1.5, trained on artworks of different painters (Rob Hefferan, Anna Marinova, Omar Ortiz, Thomas Saliot, Serge Marshennikov). Use the token 'oil painting' in your prompts for better effect. 

> Trained with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook.

You can test it via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb) or via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb).

## Sample pictures of this concept:

![0](https://huggingface.co/Gourieff/p-AI-nter_v0.1/resolve/main/sample_images/01.jpg)
    ![1](https://huggingface.co/Gourieff/p-AI-nter_v0.1/resolve/main/sample_images/02.jpg)
    ![2](https://huggingface.co/Gourieff/p-AI-nter_v0.1/resolve/main/sample_images/03.jpg)
    ![3](https://huggingface.co/Gourieff/p-AI-nter_v0.1/resolve/main/sample_images/04.jpg)

## Prompt and settings for samples

```
oil painting, portrait of (beautiful woman)+, dress, medium breast, brunette, 8k, ultra high quality, (highly detailed face)+++, (ultra realistic eyes)++, interior on background, bokeh, cinematic light
```

__negative:__
```
Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, extra limb, ugly, poorly drawn hands, missing limb, blurry, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, mutated hands and fingers, fat, overweight, multiple heads, group of people
```

* Steps: 50
* Scale: 9
* Sampler: Euler_A
    - - -