---
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
inference: false
license: mit
---

# Hayashida Tamaki (GF Kari) on Waifu Diffusion v1.3.5

This is the `<wd135-hayashida-tamaki-gfkari>` concept taught to [Waifu Diffusion v1.3.5](https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/models/wd-1-3-5_80000-fp32.ckpt) via Textual Inversion.

## Credits

The model card follows the format commonly used by concepts stored at [Hugging Face SD Concepts Library](https://huggingface.co/sd-concepts-library).

The training images were taken from [GF Kari Database](https://gfkari.gamedbs.jp/).

## Concept Images

Here is the new concept you will be able to use as an `object`:

![<wd135-hayashida-tamaki-gfkari> 0](./concept_images/4122afac10afadfe2b8fe5d6f89630dc_512x512.png)
![<wd135-hayashida-tamaki-gfkari> 1](./concept_images/4437ab2e2a07e190e361ae72e2d96fb7_512x512.png)
![<wd135-hayashida-tamaki-gfkari> 2](./concept_images/5493041b67f2d5d67c476b541dc8663d_512x512.png)
![<wd135-hayashida-tamaki-gfkari> 3](./concept_images/75d1cf668cd02a5223f68312a0657167_512x512.png)
![<wd135-hayashida-tamaki-gfkari> 4](./concept_images/profile_3_512x512.png)

## Output Examples

!["best quality masterpiece, <wd135-hayashida-tamaki-gfkari> collarbone bare shoulders bare legs shiny skin standing, frilled white summer dress, ocean beach sunny day sunlight, cowboy shot, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn] " -s 64 -S 4020064356 -W 512 -H 768 -C 12 -A k_dpmpp_2](./examples/000049.d1659a74.4020064356.png)
```json
{
  "model": "stable diffusion",
  "model_weights": "waifu-diffusion-1.3.5",
  "model_hash": "b438efac4434af4e482d20cdfcea64067f8dfec438628261d2f2aa60ffc41452",
  "app_id": "invoke-ai/InvokeAI",
  "app_version": "2.2.5",
  "image": {
    "prompt": [
      {
        "prompt": "best quality masterpiece, <wd135-hayashida-tamaki-gfkari> collarbone bare shoulders bare legs shiny skin standing, frilled white summer dress, ocean beach sunny day sunlight, cowboy shot, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn] ",
        "weight": 1
      }
    ],
    "steps": 64,
    "cfg_scale": 12,
    "threshold": 0,
    "perlin": 0,
    "height": 768,
    "width": 512,
    "seed": 4020064356,
    "seamless": false,
    "hires_fix": false,
    "type": "txt2img",
    "postprocessing": null,
    "sampler": "k_dpmpp_2",
    "variations": []
  }
}
```

!["best quality masterpiece, <wd135-hayashida-tamaki-gfkari> collarbone bare shoulders bare legs shiny skin standing, frilled white summer dress, ocean beach sunny day sunlight, cowboy shot, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn] " -s 64 -S 4020064356 -W 512 -H 768 -C 12 -A k_dpmpp_2_a](./examples/000050.e968c45d.4020064356.png)
```json
{
  "model": "stable diffusion",
  "model_weights": "waifu-diffusion-1.3.5",
  "model_hash": "b438efac4434af4e482d20cdfcea64067f8dfec438628261d2f2aa60ffc41452",
  "app_id": "invoke-ai/InvokeAI",
  "app_version": "2.2.5",
  "image": {
    "prompt": [
      {
        "prompt": "best quality masterpiece, <wd135-hayashida-tamaki-gfkari> collarbone bare shoulders bare legs shiny skin standing, frilled white summer dress, ocean beach sunny day sunlight, cowboy shot, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn] ",
        "weight": 1
      }
    ],
    "steps": 64,
    "cfg_scale": 12,
    "threshold": 0,
    "perlin": 0,
    "height": 768,
    "width": 512,
    "seed": 4020064356,
    "seamless": false,
    "hires_fix": false,
    "type": "txt2img",
    "postprocessing": null,
    "sampler": "k_dpmpp_2_a",
    "variations": []
  }
}
```

!["best quality masterpiece, <wd135-hayashida-tamaki-gfkari>, school uniform collared shirt pleated skirt, lying on back on bed, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn]" -s 64 -S 3329130038 -W 512 -H 768 -C 12 -A k_dpmpp_2](./examples/000061.00d75711.3329130038.png)
```json
{
  "model": "stable diffusion",
  "model_weights": "waifu-diffusion-1.3.5",
  "model_hash": "b438efac4434af4e482d20cdfcea64067f8dfec438628261d2f2aa60ffc41452",
  "app_id": "invoke-ai/InvokeAI",
  "app_version": "2.2.5",
  "image": {
    "prompt": [
      {
        "prompt": "best quality masterpiece, <wd135-hayashida-tamaki-gfkari>, school uniform collared shirt pleated skirt, lying on back on bed, [bad anatomy, bad hands, bad perspective, bad proportions, blurry, censored, cropped, error, extra arms, extra ears, fewer digits, jpeg artifacts, lowres, multiple legs, out of frame, poorly drawn]",
        "weight": 1
      }
    ],
    "steps": 64,
    "cfg_scale": 12,
    "threshold": 0,
    "perlin": 0,
    "height": 768,
    "width": 512,
    "seed": 3329130038,
    "seamless": false,
    "hires_fix": false,
    "type": "txt2img",
    "postprocessing": null,
    "sampler": "k_dpmpp_2",
    "variations": []
  }
}
```

## License

[MIT](./LICENSE).
