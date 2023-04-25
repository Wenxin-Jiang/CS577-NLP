---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
## p-AI-nter -- v0.3 

__p-AI-nter v0.3__ = [p-AI-nter v0.2](https://huggingface.co/Gourieff/p-AI-nter_v0.2) merged with [protogen_v2.2](https://huggingface.co/Gourieff/protogen_v2.2_reconverted) by [darkstorm2150](https://huggingface.co/darkstorm2150) in the ratio of 85% (p-AI-nter v0.2) to 15% (protogen_v2.2). 
Core model of p-AI-nter v0.2 is SD-1.5 trained on artworks of different painters (Rob Hefferan, Anna Marinova, Omar Ortiz, Thomas Saliot, Serge Marshennikov). Use the token 'oil painting' in your prompts for better effect. 

## Sample pictures:

![0](https://huggingface.co/Gourieff/p-AI-nter_v0.3/resolve/main/sample_images/01.jpg)

## Prompt and settings for samples

```
(oil painting)+ of a Girl with black wavy hair bathing in a lake, (intricate)+ drawing, Highly Detailed, Sharp focus, green and blue and orange color scheme, (rocks)+, dynamic angle, moss, ultra sharp photorealistic, 8K, stunning, hdr, subsurface scattering, dramatic light, (bokeh)+, (deep eyes)+, (sunset)++, (model pose)+, (ideal hands)++, (ray tracing)++, (cleavage)++, (ideal breast)++
```

__negative:__
```
Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, extra limb, ugly, poorly drawn hands, missing limb, blurry, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, mutated hands and fingers, fat, overweight, multiple heads, group of people, three or more legs, cross-eye, nude, naked, naked, (extra fingers)+, (fused fingers)+
```

* Steps: 50
* Scale: 9
* Sampler: Euler_A
    - - -