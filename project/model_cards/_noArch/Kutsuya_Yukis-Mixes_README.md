---
tags:
- summarization
widget:
- text: "Yuki's Mixes"
---

# Yuki's Mixes
If you like these, you could buy me a ☕ and get me through another day: https://ko-fi.com/kutsuya_yuki

## Table of Contents
- [Strawberry Mix](#strawberry-mix)

## Strawberry Mix
| Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name |
|------|----------------------|-----------------|----------------------|----------------------|-----------------|
| 1 | Weighted Sum @ 0.25 | [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0/tree/main) | [Stable Diffusion 1.4](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/tree/main) | n/a | AnyV3-SD1.4 |
| 2 | Add Difference @ 1 | AnyV3-SD1.4 | [Zeipher F222](https://huggingface.co/Kutsuya/Yukis-Mixes/tree/main) | [Stable Diffusion 1.4](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/tree/main) | strawberry-lite |
| 3 | Weighted Sum @ 0.15 | strawberry-lite | [r34_e4](https://huggingface.co/acheong08/r34/tree/main) | n/a | **strawberry mix** |

**Examples**:

![02892-381606242-anime, masterpiece, best quality, illustration, sinon, 1girl, hair ornament, gloves, solo, blue hair, fingerless gloves, white b.png](https://s3.amazonaws.com/moonup/production/uploads/1671798081689-63242cab487a03710ee5a1db.png)
```
anime, masterpiece, best quality, illustration, sinon, 1girl, hair ornament, gloves, solo, blue hair, fingerless gloves, white background, hairclip, simple background, blue eyes, looking at viewer, jacket, short hair, upper body, long sleeves, green jacket
Negative prompt: lowres, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, out of frame, extra fingers, mutated hands, (poorly drawn hands), (poorly drawn face), (mutation), (deformed breasts), (ugly), blurry, (bad anatomy), (bad proportions), (extra limbs), cloned face, censored,(hair:1.2),(hat:1.2),bw,greyscale,naked,sword,sword,weapons,glasses
Steps: 19, Sampler: DPM++ 2M Karras, CFG scale: 8, Seed: 381606242, Size: 1280x768, Denoising strength: 0.7, Clip skip: 2, ENSD: 31337, First pass size: 0x0
```

![02889-1948959101-anime, masterpiece, best quality, illustration, 1girl, rumia, ribbon, shoes, blonde hair, short hair, mary janes, hair ribbon, o.png](https://s3.amazonaws.com/moonup/production/uploads/1671797947336-63242cab487a03710ee5a1db.png)
```
anime, masterpiece, best quality, illustration, 1girl, rumia, ribbon, shoes, blonde hair, short hair, mary janes, hair ribbon, open mouth, skirt, ascot, socks, white background, black skirt, full body, red footwear, solo, simple background, red ribbon, white legwear, long sleeves, vest, smile, red eyes, shirt, standing, frilled skirt, looking at viewer, blush
Negative prompt: lowres, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, out of frame, extra fingers, mutated hands, (poorly drawn hands), (poorly drawn face), (mutation), (deformed breasts), (ugly), blurry, (bad anatomy), (bad proportions), (extra limbs), cloned face, censored,(hair:1.2),(hat:1.2),bw,greyscale,naked,sword,sword,weapons,glasses
Steps: 19, Sampler: DPM++ 2M Karras, CFG scale: 8, Seed: 1948959101, Size: 1280x768, Denoising strength: 0.7, Clip skip: 2, ENSD: 31337, First pass size: 0x0
```

![02895-381606242-anime, masterpiece, best quality, illustration, tree, nature, forest, butterfly, bug, scenery, water, outdoors, grass, bush, day.png](https://s3.amazonaws.com/moonup/production/uploads/1671799581572-63242cab487a03710ee5a1db.png)
```
anime, masterpiece, best quality, illustration, tree, nature, forest, butterfly, bug, scenery, water, outdoors, grass, bush, day, flower, plant, sunlight, branch, tree shade,
Negative prompt: lowres, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, out of frame, extra fingers, mutated hands, (poorly drawn hands), (poorly drawn face), (mutation), (deformed breasts), (ugly), blurry, (bad anatomy), (bad proportions), (extra limbs), cloned face, censored,(hair:1.2),(hat:1.2),bw,greyscale,naked,sword,sword,weapons,glasses
Steps: 19, Sampler: DPM++ 2M Karras, CFG scale: 8, Seed: 381606242, Size: 1280x768, Denoising strength: 0.7, Clip skip: 3, ENSD: 31337, First pass size: 0x0
```


