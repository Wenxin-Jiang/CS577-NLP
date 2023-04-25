---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
---
# Evt_M
Evt_M is a model derived from Evt_V4 EP06. 
It retains the characteristics of Evt_V4, and the batch generation of images with the same set of parameters is no longer rigid and monotonous, and has more possibilities.

## Examples

**Prompt1:**
![Prompt2](https://huggingface.co/haor/Evt_M/resolve/main/sample/1.png)
![Prompt2](https://huggingface.co/haor/Evt_M/resolve/main/sample/5.png)
![Prompt2](https://huggingface.co/haor/Evt_M/resolve/main/sample/3.png)
![Prompt2](https://huggingface.co/haor/Evt_M/resolve/main/sample/4.png)
```
{Masterpiece, Kaname_Madoka, tall and long double tails, well rooted hair, (pink hair), pink eyes, crossed bangs, ojousama, jk, thigh bandages, wrist cuffs, (pink bow: 1.2)}, plain color, sketch, masterpiece, high detail, masterpiece portrait, best quality, ray tracing, {:<, look at the edge}
Negative prompt: ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)),extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((bad proportions))), ((extra limbs)), (((deformed))), (((disfigured))), cloned face, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), too many fingers, (((long neck))), (((low quality))), normal quality, blurry, bad feet, text font ui, ((((worst quality)))), anatomical nonsense, (((bad shadow))), unnatural body, liquid body, 3D, 3D game, 3D game scene, 3D character, bad hairs, poorly drawn hairs, fused hairs, big muscles, bad face, extra eyes, furry, pony, mosaic, disappearing calf, disappearing legs, extra digit, fewer digit, fused digit, missing digit, fused feet, poorly drawn eyes, big face, long face, bad eyes, thick lips, obesity, strong girl, beard，Excess legs
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Clip skip: 2
```

**Prompt2:**
![Prompt1](https://huggingface.co/haor/Evt_M/resolve/main/sample/9.png)
![Prompt1](https://huggingface.co/haor/Evt_M/resolve/main/sample/2.png)
![Prompt1](https://huggingface.co/haor/Evt_M/resolve/main/sample/8.png)
```
best quality, illustration,highly detailed,1girl,upper body,beautiful detailed eyes, medium_breasts, long hair,grey hair, grey eyes, curly hair, bangs,empty eyes,expressionless, ((masterpiece)),twintails,beautiful detailed sky, beautiful detailed water, cinematic lighting, dramatic angle,((back to the viewer)),(an extremely delicate and beautiful),school uniform,black ribbon,light smile,
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,artist name,bad feet
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Clip skip: 2
```
## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)