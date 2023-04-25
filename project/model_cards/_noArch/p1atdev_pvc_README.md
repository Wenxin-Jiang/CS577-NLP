---
license: creativeml-openrail-m
thumbnail: https://huggingface.co/p1atdev/pvc/resolve/main/samples/v2-eyecatch.png
datasets:
- p1atdev/pvc
language:
- en
tags:
- stable-diffusion
- text-to-image
- safetensors
widget:
- text: masterpiece, best quality, high quality, 1girl, cat ears, silver, blue, frills, bow, looking at viewer, ultra detailed
  example_title: A girl with cat ears
- text: masterpiece, best quality, 1girl, green hair, sweater, beanie, turtleneck, looking at viewer, night
  example_title: A beanie girl
- text: masterpiece, best quality, high quality, 1girl, bob cut, cape, belt, gloves, looking at viewer, ultra detailed
  example_title: An adventurer girl
---

# PVC v2

![v2 eyecatch](https://huggingface.co/p1atdev/pvc/resolve/main/samples/v2-eyecatch.png)


```
masterpiece, best quality, high quality, 1girl, cat ears, silver, blue, frills, bow, looking at viewer, ultra detailed
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

This model is a latent diffusion model finetuned on [Waifu Diffusion v1.4 epoch 2](https://huggingface.co/hakurei/waifu-diffusion-v1-4) with [PVC figure images](https://huggingface.co/datasets/p1atdev/pvc) using LoRA method.
You can use Danbooru tags to generate images.


## Downloads

<div class="flex flex-wrap gap-4 my-4 ">
<a class="btn inline-flex" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v2.ckpt">Download model (ckpt)</a>
<a class="btn inline-flex" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v2.safetensors">Download model (safetensors)</a>
<a class="btn inline-flex" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v2-lora.pt">Download LoRA (pt)</a>
</div>

## Prompt guide

It is recommended to add the quality tags **"masterpiece, best quality"** at the beginning of the prompt when using this model, which is a derivative of the WD.

**Recommended negative prompt**
```
nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digits, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
```

## Samples

<div class="grid grid-cols-2 xl:grid-cols-3 gap-2 not-prose">
<div class="rounded-lg overflow-hidden gap-0">
<img class="m-0 p-0 w-full" src="https://huggingface.co/p1atdev/pvc/resolve/main/samples/v2-sample1.png"/>

<p class="px-4 py-3 w-full h-full from-gray-100-to-white bg-gradient-to-t">
masterpiece, best quality, 1girl, green hair, sweater, beanie, turtleneck, looking at viewer, night,
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
</p>
</div>

<div class="rounded-lg overflow-hidden">
<img class="m-0 p-0 w-full" src="https://huggingface.co/p1atdev/pvc/resolve/main/samples/v2-sample2.png"/>

<p class="px-4 py-3 w-full h-full from-gray-100-to-white bg-gradient-to-t">
masterpiece, best quality, high quality, 1girl, bob cut, cape, belt, gloves, looking at viewer, ultra detailed
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
</p>
</div>

<div class="rounded-lg overflow-hidden">
<img class="m-0 p-0 w-full" src="https://huggingface.co/p1atdev/pvc/resolve/main/samples/v2-sample3.png"/>

<p class="px-4 py-3 w-full h-full from-gray-100-to-white bg-gradient-to-t">
masterpiece, best quality, 1girl, annoyed, black hair, floating hair, gothic lolita, scythe, looking at viewer,
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
</p>
</div>
  
</div>

## License

This version (v2) model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)


## Training information

- Training script: kohya_ss/sd-scripts
- Number of images: 2110
- Traning steps: 21100
- Resolution: 768,768
- Learning rate:
  - U-Net: 1e-4
  - Text encoder: 5e-5
- Optimizer: AdamW8bit
- Max token length: 225
- Mixed precision: fp16
- Network dim: 16
- Xformers: enabled
- Bucketing: enabled

# Old versions

<details>
<summary class="text-xl">
PVC v1 (based on WDv1.4 e2)
</summary>

<div class="flex flex-wrap gap-4 my-4">
<a class="btn" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v1.ckpt">Download model (ckpt)</a>
<a class="btn" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v1.safetensors">Download model (safetensors)</a>
<a class="btn" href="https://huggingface.co/p1atdev/pvc/resolve/9771e2970e9574efe89910801861234a5f276aa2/pvc-v1-lora.pt">Download LoRA (pt)</a>
</div>


![eyecatch](https://huggingface.co/p1atdev/pvc/resolve/main/samples/miku.png)

This model is a latent diffusion model finetuned on [Waifu Diffusion v1.4 epoch 2](https://huggingface.co/hakurei/waifu-diffusion-v1-4) with [PVC figure images](https://huggingface.co/datasets/p1atdev/pvc) using LoRA method.
You can use Danbooru tags to generate images.

## Samples

![sample1](https://huggingface.co/p1atdev/pvc/resolve/main/samples/sample1.png)

```
masterpiece, best quality, 1girl, green hair, sweater, beanie, turtleneck, looking at viewer,
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7
```

---

![sample2](https://huggingface.co/p1atdev/pvc/resolve/main/samples/sample2.png)


```
masterpiece, best quality, 1girl, smile, black hair, long hair, school uniform, navel, pleated skirt, leaning forward, looking at viewer, wind
Negative prompt: nsfw, worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry,
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 10
```

---

![sample3](https://huggingface.co/p1atdev/pvc/resolve/main/samples/sample3.png)


```
masterpiece, best quality, 1girl, fascinator, hat, victorian, gothic, dress, frills, looking at viewer,
Negative prompt: worst quality, low quality, medium quality, deleted, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, censored, hetero
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

## License

This version (v1) model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)


## Training information

- Training script: kohya_ss/sd-scripts
- Number of images: 887
- Traning steps: 17740
- Resolution: 768,768
- Learning rate:
  - U-Net: 1e-4
  - Text encoder: 5e-5
- Optimizer: AdamW8bit
- Max token length: 225
- Mixed precision: fp16
- Network dim: 16
- Xformers: enabled
- Bucketing: enabled

</details>