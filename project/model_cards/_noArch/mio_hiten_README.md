---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/mio/hiten/resolve/main/example_images/1.jpeg"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
---

# Hiten Diffusion

**Welcome to Hiten Diffusion** - a latent diffusion model that has been trained on Chinese TaiWan Artist artwork, [hiten](https://www.pixiv.net/users/490219). The current model has been fine-tuned with a learning rate of `2.0e-6` for `10 Epochs` on `467 images` collected from Danbooru. The model is trained using [NovelAI Aspect Ratio Bucketing Tool](https://github.com/NovelAI/novelai-aspect-ratio-bucketing) so that it can be trained at non-square resolutions. Like other anime-style Stable Diffusion models, it also supports Danbooru tags to generate images.

e.g. **_1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden_** 

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "mio/hiten"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "1girl,solo,miku"
image = pipe(prompt).images[0]

image.save("./miku.png")
```

## Examples

Below are some examples of images generated using this model:

![AnimeGirl](https://huggingface.co/mio/hiten/resolve/main/example_images/1.jpeg)
![AnimeGirl](https://huggingface.co/mio/hiten/resolve/main/example_images/2.jpeg)
![AnimeGirl](https://huggingface.co/mio/hiten/resolve/main/example_images/3.jpeg)
![AnimeGirl](https://huggingface.co/mio/hiten/resolve/main/example_images/4.jpeg)

### Prompt and settings for Example Images

**Anime Girl:**
```
(((masterpiece))),(((best quality))),((ultra-detailed)), ((illustration)),floating, ((an extremely delicate and beautiful)),(beautiful detailed eyes),((disheveled hair)),1girl, bangs, black_hair, blue_sailor_collar, blurry, blurry_background, depth_of_field, eyebrows_visible_through_hair, long_hair, looking_at_viewer, parted_lips, sailor_collar, school_uniform, serafuku, shirt, solo, yoroizuka_mizore,medium_chest,colourful_stages,crown,masterpiece,full_body,white_thighhighs,extremely_detailed_CG_unity_8k_wallpaper,solo,1girl,lights

Negative prompt: nsfw,nipples,lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet, (((mutilated))),(((((too many fingers))))),((((fused fingers)))),(((extra fingers))),(((mutated hands))),extra limbs,(bad_prompt), (((mutilated))),(((((too many fingers))))),((((fused fingers)))),(((extra fingers)))

Steps: 24, Sampler: DPM2 a Karras, CFG scale: 7, Seed: 3722281017, Size: 512x768, Model hash: 53a39f6a, Model: hiten_epoch10, Batch size: 4, Batch pos: 3, Clip skip: 2, ENSD: 31337
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Big Thanks to
- [Linaqruf](https://huggingface.co/Linaqruf) for his first step.
- [Kohya](https://twitter.com/kohya_ss) with their [Kohya Trainer](https://note.com/kohya_ss/n/ne17e34dd51bf)