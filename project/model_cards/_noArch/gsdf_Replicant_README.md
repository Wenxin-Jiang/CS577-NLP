---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---
# Please enable hires. fix when using it. 
  
Replicant is built by merging several models with fine-tuning WD1.4 and photorealistic SD2.0 models that works with danbooru tags.I trained 4 models to merge and prepared several LoRa models for tuning.As with SD1.x, merging individually trained models is better quality than training many concepts at once.This model is a workflow test and is not good enough.  WD1.4 seems to vary greatly in quality with/without Hires. fix.In Replicant, the difference in quality is more noticeable because of the detailed drawings.So I recommend enabling Hires.fix for use.
  
# Example
Denoising strength 0.6 is a bit large. I like 0.57 better. 
The optimal CFG Scale value should also be examined.  
Hands often multiply. When this happens, increase the value of "extra hands".
  
 ![sample1](https://huggingface.co/gsdf/Replicant/resolve/main/sample_01.png)
((masterpiece, best quality)), 1girl, flower, solo, dress, holding, sky, cloud, hat, outdoors, bangs, bouquet, rose, expressionless, blush, pink hair, flower field, red flower, pink eyes, white dress, looking at viewer, midium hair, holding flower, small breasts, red rose, holding bouquet, sun hat, white headwear, depth of field  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit,(extra arms:1.2), extra hands, fewer digits ,long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 576x384, Denoising strength: 0.6, Hires upscale: 2, Hires upscaler: Latent  

    
![sample2](https://huggingface.co/gsdf/Replicant/resolve/main/sample_02.png)
((masterpiece, best quality)), 1girl, skirt, shoes, solo, jacket, holding, alley, sitting, can, sneakers, hood, bag, hoodie, squatting, bangs, shirt, black hair, black skirt, short hair, white jacket, looking away, white footwear, full body, red eyes, long sleeves, open jacket, open clothes, holding can,  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit,(extra arms:1.2), extra legs, extra hands, fewer digits , long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes,drinking  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 576x384, Denoising strength: 0.6, Hires upscale: 2, Hires upscaler: Latent  

    
![sample3](https://huggingface.co/gsdf/Replicant/resolve/main/sample_03.png)
((masterpiece, best quality)), 1girl, blood, solo, wings, halo, dress, socks, angel, long hair, shoes, standing, ribbon, long hair, blue eyes, angel wings, blood on clothes, white hair, full body, white wings, black footwear, white dress, feathered wings, white sock, white background, long sleeves, simple background,  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit,(extra arms:1.2), extra legs, extra hands, fewer digits , long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 384x576, Denoising strength: 0.57, Hires upscale: 2, Hires upscaler: Latent  

    
![sample4](https://huggingface.co/gsdf/Replicant/resolve/main/sample_04.png)
((masterpiece, best quality)), 1girl, car, solo, shorts, jacket, bangs, sitting, shirt, shoes, hairclip, socks, sneakers, denim, sidelocks, motor vehicle, long hair, ground vehicle,brown hair, looking at viewer, white shirt, black jacket, long sleeves, sports car, vehicle focus, aqua eyes, white socks, blue shorts, open clothes, black footwear, denim shorts, open jacket  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit, (extra arms:1.2), extra hands, fewer digits ,long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 384x576, Denoising strength: 0.6, Hires upscale: 2, Hires upscaler: Latent  

 
![sample5](https://huggingface.co/gsdf/Replicant/resolve/main/sample_05.png)
((masterpiece, best quality)), 1girl, solo, twintails, lollipop, smile, ahoge, hairclip, bow, holding, ribbon, frills, blush, shirt, :d, stuffed toy, pink hair, stuffed animal, red nails, hair ornament, open mouth, looking at viewer, stuffed bunny, nail polish, short sleeves, object hug, puffy sleeves, hair between eyes, upper body, light blue eyes, puffy short sleeves, holding stuffed toy, hair bow, white bow, doll hug, hair ribbon, streaked hair, white shirt  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit, (extra arms:1.2), extra hands, fewer digits ,long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 512x512, Denoising strength: 0.57, Hires upscale: 2, Hires upscaler: Latent  

  
 ![sample6](https://huggingface.co/gsdf/Replicant/resolve/main/sample_06.png)
((masterpiece, best quality)), 1girl, solo, tail, barefoot, skirt, sleeping, lying, grass, shirt, outdoors, socks, flower, long hair, on side, animal ears, blonde hair, cat tail, closed eyes, blue skirt, white shirt, cat ears, school uniform, dappled sunlight, short sleeves, bare legs, closed mouth, full body, pleated skirt  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit, (extra arms:1.2), extra hands, fewer digits ,long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 576x384, Denoising strength: 0.6, Hires upscale: 2, Hires upscaler: Latent  

  
![sample7](https://huggingface.co/gsdf/Replicant/resolve/main/sample_07.png)
((masterpiece, best quality)), 1girl, car, building, gun, weapon, outdoors, solo, military, day, city, standing, serious, pants, rifle, holding, jacket, motor vehicle, ground vehicle, brown hair, assault rifle, long hair, vehicle focus, holding gun, holding weapon, black footwear, military vehicle, full body, depth of field,  
Negative prompt: (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), inaccurate eyes, extra digit, (extra arms:1.2), extra hands, fewer digits ,long body, cropped, jpeg artifacts, signature, watermark, username, blurry, empty eyes  
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Size: 576x384, Denoising strength: 0.6, Hires upscale: 2, Hires upscaler: Latent  