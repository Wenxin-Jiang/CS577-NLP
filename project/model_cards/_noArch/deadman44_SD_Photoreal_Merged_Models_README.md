---
license: cc0-1.0
tags:
  - stable-diffusion
  - text-to-image
---
---
## -Specializing in Japanese girls
## -Merged photo-real model mixed 5000+ Twitter images.

for Stable Diffusion Webui Automatic1111</br>
type: .safetensors(ckpt)</br>
CFG Scale: middle-low</br>

## Negative prompts are rarely needed.
example.</br>
low quality, worst quality, bad anatomy, bad proportions

## Recommended Sampler
UniPC, Dpm++ (2M/SDE) Karras, DDIM<br/>
Steps: 10～24

## Recommended VAE
vae-ft-mse-840000-ema-pruned

---
# El Zipang
-Mixed 5000+images

[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_pruned_fp16.safetensors)<br/>
Civitai:[(E)l (Z)ipang](https://civitai.com/models/20143/ez) -Why was it ban?
- Photo-Real</br>
photo realistic:+++++</br>
portrait:++++</br>
pose:+++</br>
hand:++</br>

[<img src=https://i.imgur.com/bh1To6tm.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/bh1To6t)[<img src=https://i.imgur.com/Zk5rWc0m.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/Zk5rWc0)[<img src=https://i.imgur.com/oKi7o17m.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/oKi7o17)[<img src=https://i.imgur.com/Of7YoTxm.png.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/Of7YoTx)[<img src=https://i.imgur.com/t11u8xfm.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/t11u8xf)[<img src=https://i.imgur.com/J74LwDMm.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/J74LwDM)

## example
[<img src=https://i.imgur.com/wfH7XgJl.png>](https://i.imgur.com/wfH7XgJ)

```jsx
realistic, photorealistic, detailed, beautiful, RAW photo, film grain, (natural lighting :1.2), (wrinkled skin:1.1),
japanese, 1girl, happy, short black hair, brown eyes, bangs, camisole, close-up, facing viewer, photo background
Negative prompt: (worst quality, low quality, normal quality:1.8), painting, drawing
Steps: 28, Sampler: UniPC, CFG scale: 3.5, Seed: 2272109148, Size: 512x768, Model hash: b7cbea183c, Denoising strength: 0.18, Hires upscale: 2, Hires upscaler: SwinIR_4x
```
-Recommended prompt:
```jsx
japanese, 1girl, realistic, photorealistic, detailed, beautiful, RAW photo, film grain, natural lighting, wrinkled skin,
Negative prompt:
(worst quality, low quality, normal quality:1.8), painting, drawing
CFG scale: 3-7
Hires: 2-4x
```
-
Anything4.5(base trained) + uncanny valley(my other model:Any3.0+EZ test series) Brock Weight Merged
---

# OLD TestVersion
-Specializing in Japanese girls Test Model
-Merged photo-real model mixed 1000+ Twitter images.


# El Zipang_test1.4
-Mixed 2000+images<br/>
-The composition and the human body are even less fragile. Maybe...

[test_no_zipang.safetensors](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/test_no_zipang.safetensors) + [El Zipang_test1.3.safetensors](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test1.3.safetensors) -> Simple Merge!!!

-
test no Zipang
Anything3.0(base trained) + EZ test1.0 Brock Weight Merged
----

# El Zipang_test1.3
[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test1.3.safetensors)<br/>
-Just changed the block-weighted merge ratio.<br/>
-Better hands and better poses than 1.0. Maybe...<br/>
thanks, supermerger!!!<br/>
http://github.com/hako-mikan/sd-webui-supermerger/<br/>

[<img src=https://i.imgur.com/GyKs8Up.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/GyKs8Up)
[<img src=https://i.imgur.com/sXnAGF8.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/sXnAGF8)
[<img src=https://i.imgur.com/zE77vws.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/zE77vws)

-
EZ test1.0 + Anything3.0 Merged
----

# El Zipang_test1.0(test01)
[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test01.safetensors)<br/>
- Photo-Real</br>
photo realistic:+++++</br>
portrait:+++++</br>
pose:+</br>
hand:+</br>

[<img src=https://i.imgur.com/MK6MUu0.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/MK6MUu0)[<img src=https://i.imgur.com/HmSC45w.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/HmSC45w)[<img src=https://i.imgur.com/Qs1DJyS.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/Qs1DJyS)[<img src=https://i.imgur.com/G0KhpMu.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/G0KhpMu)[<img src=https://i.imgur.com/wk69lFK.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/wk69lFK)[<img src=https://i.imgur.com/dYG6xTp.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/dYG6xTp)

## example
<img src=https://i.imgur.com/KuWcOxX.png>

```jsx
japanese, 1girl, solo, looking at viewer, long hair, couch, black hair, smile, realistic, bangs, long sleeves, black eyes, brown eyes, upper body, sitting, fingernails, lips, school uniform, closed mouth
Negative prompt: low contrast, lowers, normal quality, low quality, worst quality, bad anatomy, bad proportions
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 5, Seed: 185236819, Size: 512x768, Model hash: c785dff0
```
-Recommended prompt:
```jsx
japanese, realistic, 1girl, 
Negative prompt:
normal quality, low quality, worst quality, bad anatomy, bad proportions, 
CFG scale: 4-8
```
-
SD1.5(base trained) + F222 + Cafe Insta Merged
----



