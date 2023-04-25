---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### TaylorSwift Dreambooth model trained by taytay4eva with [TheLastBen's fast-DreamBooth](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast-DreamBooth.ipynb) notebook using the StableDiffusionv1.5 model

CREATOR NOTE 1: The keyword for this model is <b>taySwift</b>

CREATOR NOTE 2: "Taylor Berry" is a blend of the original model as put through further iterations of DreamBooth and Berry_mix at a 7:3 ratio. It provides a bit better mesh of images and, I think, an overall smoother final product, but whichever you like is what you should go with!

Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

![Sample Image of TaylorSwiftv2](https://huggingface.co/sd-dreambooth-library/taylorswift/blob/main/concept_images/indexaa.png)

positive prompt: <b>taySwift</b>, Masterpiece, cinematic lighting, photorealistic, realistic, extremely detailed, (fancy clothes, puffy sleeves, Lacy shirt, thigh high boots, leather boots, short skirt), cheerful attitude, happy woman, excited woman), artgerm, greg rutkowski, alphonse mucha

negative prompt: Ugly, lowres, duplicate, morbid, mutilated, out of frame, extra fingers, extra limbs, extra legs, extra heads, extra arms, extra breasts, extra nipples, extra head, extra digit, poorly drawn hands, poorly drawn face, mutation, mutated hands, bad anatomy, long neck, signature, watermark, username, blurry, artist name, deformed, distorted fingers, distorted limbs, distorted legs, distorted heads, distorted arms, distorted breasts, distorted nipples, distorted head, distorted digit

Steps: 85, CFG scale: 7, Seed: 1903506130, Face restoration: CodeFormer, Size: 576x832, Model hash: ad57baac, Denoising strength: 0.75, Mask blur: 4

Upscale: 2, visibility: 1.0, model:ESRGAN_4x

![Sample Image of Taylor Berry](https://huggingface.co/sd-dreambooth-library/taylorswift/blob/main/00143-3262192747-oil%20painting%2C%20sensual%2C%20(full%20body)%2C%20taySwift%2C%20princess%2C%20(auburn%20hair)%2C%20erotic%2C%20fantasy%20princess%2C%20tavern%20wench%2C%20bar%2C%20magical%2C%20bus.png)

positive prompt: oil painting, sensual, (full body), <b>taySwift</b>, princess, (auburn hair), erotic, fantasy princess, tavern wench, bar, magical, busty, huge titties, curvy, full red lips, kiss, sensual clothes, off the shoulder dress, lace, ((blue) and green floor length dress), (Albert Lynch), J. C. Leyendecker, Ruan Jia, Gaston Bussiere, Alexandre Cabanel, WLOP, best quality

negative prompt: (blonde hair), (ugly:1.3), (duplicate:1.3), (morbid), (mutilated), out of frame, extra fingers, mutated hands, (poorly drawn hands), (poorly drawn face), (mutation:1.3), (deformed:1.3), (amputee:1.3), blurry, bad anatomy, bad proportions, (extra limbs), cloned face, (disfigured:1.3), gross proportions, (malformed limbs), (missing arms), (missing legs), (extra arms), (extra legs), mutated hands, (fused fingers), (too many fingers), (long neck:1.3), lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, black and white, monochrome, censored

Steps: 42, CFG scale: 11, Denoising Strength: 0.75, Seed: 3262192735
