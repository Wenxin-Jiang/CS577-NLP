---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

The embeddings in this repository were trained for the 768px [Stable Diffusion v2.0](https://huggingface.co/stabilityai/stable-diffusion-2) model. The embeddings should work on any model that uses SD v2.0 as a base.


Currently the kc32-v4-5000.pt & kc16-v4-5000.pt embeddings seem to perform the best.


**Knollingcase v1**

The v1 embeddings were trained for 4000 iterations with a batch size of 2, a text dropout of 10%, & 16 vectors using Automatic1111's WebUI. A total of 69 training images with high quality captions were used.

**Knollingcase v2**

The v2 embeddings were trained for 5000 iterations with a batch size of 4 and a text dropout of 10%, & 16 vectors using Automatic1111's WebUI. A total of 78 training images with high quality captions were used.

**Knollingcase v3**

The v3 embeddings were trained for 4000-6250 iterations with a batch size of 4 and a text dropout of 10%, & 16 vectors using Automatic1111's WebUI. A total of 86 training images with high quality captions were used.

<div align="center">
<img src="https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v2-0/resolve/main/cruise_ship_on_wave_kc16-v3-6250.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v2-0/resolve/main/cruise_ship_on_wave_kc16-v3-6250.png)


**Knollingcase v4**

The v4 embeddings were trained for 4000-6250 iterations with a batch size of 4 and a text dropout of 10%, using Automatic1111's WebUI. A total of 116 training images with high quality captions were used.

<div align="center">
<img src="https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v2-0/resolve/main/v4_size_768_t4x11.jpg">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v2-0/resolve/main/v4_size_768_t4x11.jpg)

**Usage**

To use the embeddings, download and then rename the files to whatever trigger word you want to use. They were trained with kc8, kc16, kc32, but any trigger word should work.

The knollingcase style is considered to be a concept inside a sleek (sometimes scifi) display case with transparent walls, and a minimalistic background.


Suggested prompts:

```
<concept>, micro-details, photorealism, photorealistic, <kc-vx-iter>
photorealistic <concept>, very detailed, scifi case, <kc-vx-iter>
<concept>, very detailed, scifi transparent case, <kc-vx-iter>
```

Suggested negative prompts:

```
blurry, toy, cartoon, animated, underwater, photoshop
```

Suggested samplers:

DPM++ SDE Karras (used for the example images) or DPM++ 2S a Karras
