---
thumbnail: https://imgur.com/DkGWTA2.png
language:
- en
tags:
- stable-diffusion
- text-to-image
license: creativeml-openrail-m
inference: false

---

# Diffusion model
This model is trained with detailed semi realistic images via my anime model.

# Sample generations
This model is made to get semi realistic, realistic results with a lot of detail.

```
Positive:1girl, aura, blue_fire, electricity, energy, fire, flame, glowing, glowing_eyes, green_eyes, hitodama, horns, lightning, long_hair, magic, male_focus, solo, spirit
Negative:lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a, CFG scale: 8, Seed: 2526294281, Size: 896x768
```
<img src=https://imgur.com/HHdOmIF.jpg width=75% height=75%>


```
Positive: a girl,Phoenix girl,fluffy hair,war,a hell on earth, Beautiful and detailed costume, blue glowing eyes, masterpiece, (detailed hands), (glowing), twintails, smiling, beautiful detailed white gloves, (upper_body), (realistic)
Negative: lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a Karras, CFG scale: 8, Seed: 2495938777/2495938779, Size: 896x768
```
<img src=https://imgur.com/bHiTlAu.png width=75% height=75%>
<img src=https://imgur.com/dGFn0uV.png width=75% height=75%>


```
Positive:1girl, blurry, bracelet, breasts, dress, earrings, fingernails, grey_eyes, jewelry, lips, lipstick, looking_at_viewer, makeup, nail_polish, necklace, petals, red_lips, short_hair, solo, white_hair
Negative:lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 20, Sampler: DPM++ 2S a, CFG scale: 8, Seed: 3149099819, Size: 704x896
```

<img src=https://imgur.com/tnGOZz8.png width=75% height=75%>

Img2img results:

```
Positive:1girl, anal_hair, black_pubic_hair, blurry, blurry_background, brown_eyes, colored_pubic_hair, excessive_pubic_hair, female_pubic_hair, forehead, grass, lips, looking_at_viewer, male_pubic_hair, mismatched_pubic_hair, pov, pubic_hair, realistic, solo, stray_pubic_hair, teeth
Negative:lowres, bad anatomy, ((bad hands)), text, error, ((missing fingers)), cropped, jpeg artifacts, worst quality, low quality, signature, watermark, blurry, deformed, extra ears, deformed, disfigured, mutation, censored, ((multiple_girls))
Steps: 35, Sampler: Euler a, CFG scale: 9, Seed: 2148680457, Size: 512x512, Denoising strength: 0.6, Mask blur: 4
```
<img src=https://imgur.com/RVl7Xxd.png width=75% height=75%>


## Disclaimer
If you get anime images not semi realistic ones try some prompts like semi realistic, 
realistic or (SemiRealImg). Usually helps. This model also works nicely with 
landscapes like my previous one. However I recommend my other anime model for landscapes.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)