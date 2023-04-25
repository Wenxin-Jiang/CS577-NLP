---
license: creativeml-openrail-m
language:
- en
thumbnail: "https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00012-2889043694-best%20quality%2C.png"
tags:
- stable-diffusion
- text-to-image
inference: true
widget:
  - text: >-
      masterpiece, best quality, hatsune miku, 1girl
---

# Yohan Diffusion

**Welcome to Yohan Diffusion** - a latent diffusion model that has been trained on a Japanese artist's artworks, [yohan1754/Free Style](https://www.pixiv.net/en/users/4446354). This model has been fine-tuned with a learning rate of `2.0e-6` for `20000 training steps` on `226 images` collected from Danbooru. 

The model is trained using [NovelAI Aspect Ratio Bucketing Tool](https://github.com/NovelAI/novelai-aspect-ratio-bucketing) so that it can be trained at non-square resolutions. Like other anime-style Stable Diffusion models, it also supports Danbooru tags to generate images. It is finetuned using [Anything V3](https://huggingface.co/Linaqruf/anything-v3.0) as base model.

**Cocoa**

Recipe:

(Add Difference 1)Yohan-Diffusion + F222 + S.D. 1.4 = YohanMix

(Weighted Sum 0.3) YohanMix + Blossom-extract = Cocoa

**Latte**

Recipe:

(Weighted Sum 0.5) Cocoa + AbyssOrangeMix2_Hard = Latte

**Butter**

Recipe:

(Weighted Sum 0.5) Cocoa + AbyssOrangeMix2_nsfw = Butter

## MUST DO:

Use Clip Skip 2.

(Optional) It is best not to use "masterpiece" in the prompt since that keyword enforces NAI-ish style, meaning the artstyles would clash each other.

# Dataset

You can find `datasets` used for the model [here](https://huggingface.co/datasets/andite/yohan-tag).

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "andite/yohan-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "hatsune_miku"
image = pipe(prompt).images[0]

image.save("./hatsune_miku.png")
```

## Examples

Below are some examples of images generated using this model:

![Yohan Example 1](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00000-927419423-best%20quality%2C%20.png)
![Yohan Example 2](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00002-3561518470-best%20quality%2C.png)
![Yohan Example 3](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00004-669322297-best%20quality%2C%20.png)
![Yohan Example 4](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00005-1274771037-best%20quality%2C.png)
![Yohan Example 5](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00012-1270904169-best%20quality%2C.png)
![Yohan Example 6](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00013-3905726485-best%20quality%2C.png)
![Yohan Example 7](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00015-1191281675-best%20quality%2C.png)
![Yohan Example 8](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00016-2912484114-best%20quality%2C.png)
![Yohan Example 9](https://huggingface.co/andite/yohan-diffusion/resolve/main/example_images/00019-3943606695-best%20quality%2C.png)

### Prompt and settings for Example Images

**Example 1 and 2**
```
best quality, cinematic lighting, dark, 1girl, breasts, large breasts, solo, gloves, underboob, short hair, navel, brown hair, goggles, fire, hair between eyes, black gloves, looking at viewer, fingerless gloves, goggles on head, cleavage, holding, bare shoulders, bangs, choker, belt, elbow gloves, green eyes, helmet, parted lips, abs, bandaged arm, pants, hammer, sweat, blue eyes, bandages
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 927419423, 3561518470, Size: 512x768, Model hash: 783d0732, Model: yohan-diffusion, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
**Example 3 and 4**
```
best quality, 1girl, breasts, swimsuit, thighhighs, bikini, long hair, large breasts, navel, solo, white bikini, side-tie bikini bottom, brown hair, looking at viewer, black thighhighs, choker, smile, holding, phone, braid, parted lips, bangs, string bikini, cleavage, thighs, very long hair, underboob, bare shoulders, stomach, hair between eyes, arm support, orange eyes, sitting, bracelet, jewelry, grin, holding phone, cellphone
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 669322297, 1274771037, Size: 512x768, Model hash: 783d0732, Model: yohan-diffusion, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
**Example 5 and 6**
```
best quality, cinematic lighting, 1girl, breasts, purple hair, long hair, large breasts, cleavage, navel, sitting, underwear, solo, looking at viewer, very long hair, panties, tattoo, lamp, bare shoulders, smile, blue eyes, thighs, bangs, open mouth, stomach, holding, food, arm support, bare arms, purple eyes, indoors, black panties, pillow, collarbone
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1270904169, 3905726485, Size: 512x768, Model hash: 783d0732, Model: yohan-diffusion, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
**Example 7**
```
best quality, cinematic lighting, pov, 1girl, solo, breasts, thighhighs, navel, shirt, lying, looking at viewer, on side, bikini, swimsuit, blue eyes, open clothes, black thighhighs, white shirt, black bikini, open shirt, pillow, hair ornament, long sleeves, white hair, couch, side-tie bikini bottom, hairclip, large breasts, stomach, cleavage, short hair, bangs, closed mouth, on couch, string bikini, thighs, skindentation, hair between eyes
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1191281675, Size: 512x768, Model hash: 783d0732, Model: yohan-diffusion, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
**Example 8**
```
best quality, cinematic lighting, 1girl, breasts, solo, long hair, thighhighs, red eyes, black hair, dress, chinese clothes, cleavage cutout, cleavage, china dress, smile, large breasts, clothing cutout, hand fan, ahoge, sitting, folding fan, red dress, twintails, bangs, black thighhighs, blush, looking at viewer, holding fan, bare shoulders, holding, very long hair, hair ribbon, hair between eyes, bottle, ribbon, folded fan, sleeveless, closed mouth, pelvic curtain, panties, underwear, thighs, blurry background, side-tie panties, crossed bangs, side slit, indoors, sleeveless dress
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2912484114, Size: 512x768, Model hash: 783d0732, Model: yohan-diffusion, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
**Example 9**
```
best quality, cinematic lighting, from above, 1girl, breasts, long hair, braid, brown hair, blue eyes, solo, wet, sitting, twin braids, waterfall, navel, large breasts, cleavage, panties, underwear, water, very long hair, thighs, see-through, collarbone, shirt, bangs, side-tie panties, wet clothes, looking at viewer, white panties, open clothes, hair between eyes, bikini, white shirt, blush, swimsuit, long sleeves, rock
Negative prompt: lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts))
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3943606695, Size: 512x768, Model hash: 783d0732, Model: yohan-20000, Denoising strength: 0.7, ENSD: 31337, First pass size: 0x0
```
## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Credit
- [yohan1754/Free Style](https://www.pixiv.net/en/users/4446354)

## Big Thanks to
- [Kohya](https://twitter.com/kohya_ss) with their [Kohya Trainer](https://note.com/kohya_ss/n/ne17e34dd51bf)
- [Linaqruf](https://huggingface.co/Linaqruf), he's a really huge help and responds to my questions thoughtfully even though I've been asking alot xD.