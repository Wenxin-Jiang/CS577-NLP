---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
## p-AI-nter -- v0.2 

Core model is SD-1.5, trained on artworks of different painters (Rob Hefferan, Anna Marinova, Omar Ortiz, Thomas Saliot, Serge Marshennikov). Use the token 'oil painting' in your prompts for better effect. 

> Trained with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook.

You can test it via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb) or via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb).

## Sample pictures:

![0](https://huggingface.co/Gourieff/p-AI-nter_v0.2/resolve/main/sample_images/01.jpg)

## Prompt and settings for samples

```
(portrait photo)++ of (young)+ woman on river bank, dressed in silk shirt, golden and white and bronze color scheme, (oil painting)+, (epic composition)+, intricate, Highly Detailed, Sharp focus, dramatic light, (high bun black hair)++, (bokeh)+, (deep eyes)+, (sunset)++, (model pose)+, (ideal hands)++, (ray tracing)++, (cleavage)+, (ideal breast)+
```

__negative:__
```
Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, extra limb, ugly, poorly drawn hands, missing limb, blurry, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, mutated hands and fingers, fat, overweight, multiple heads, group of people, three or more legs, cross-eye, nude, naked, naked, (extra fingers)+, (fused fingers)+
```

* Steps: 50
* Scale: 9
* Sampler: Euler_A
    - - -