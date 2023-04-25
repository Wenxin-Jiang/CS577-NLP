---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

The embeddings in this repository were trained for the 512px [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model. The embeddings should work on any model that uses SD v1.5 as a base.

For Stable Diffusion v2.x, see my [KnollingCase embeddings for SD 2.0](https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v2-0).


**Knollingcase v1**

The v1 embeddings were trained for 4000 iterations with a batch size of 4 and a text dropout of 10%, using Automatic1111's WebUI. A total of 147 training images with high quality captions were used.

Embeddings are provided for steps 1000, 2000, 3000, & 4000.


<div align="center">
<img src="https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v1-5/resolve/main/v1_size_512_t4x4.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/knollingcase-embeddings-sd-v1-5/resolve/main/v1_size_512_t4x4.png)


**Usage**

To use the embeddings, download and then rename the files to whatever trigger word you want to use. They were trained with kc16, but any trigger word should work.

The knollingcase style is considered to be a concept inside a sleek (sometimes scifi) display case with transparent walls, and a minimalistic background.
