---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Guizmus/MosaicArt/resolve/main/showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
---
# Mosaic Art

## Details

![Showcase](https://huggingface.co/Guizmus/MosaicArt/resolve/main/showcase.jpg)
This is a Dreamboothed Stable Diffusion model trained on pictures of mosaic art.

The total dataset is made of 46 pictures. V2 was trained on [Stable diffusion 2.1 768](https://huggingface.co/stabilityai/stable-diffusion-2-1). I used [StableTuner](https://github.com/devilismyfriend/StableTuner) to do the training, using full caption on the pictures with almost no recurring word outside the main concept, so that no additionnal regularisation was needed. 6 epochs of 40 repeats on LR 1e-6 were used, with prior preservation.

V1 was trained on [runawayml 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) and the [new VAE](https://huggingface.co/stabilityai/sd-vae-ft-mse). I used [EveryDream](https://github.com/victorchall/EveryDream-trainer) to do the training, using full caption on the pictures with almost no recurring word outside the main concept, so that no additionnal regularisation was needed. Out of e0 to e11 epochs, e8 was selected as the best application of style while not overtraining. Prior preservation was constated as good. A total of 9 epochs of 40 repeats with a learning rate of 1e-6.

The token "Mosaic Art" will bring in the new concept, trained as a style.

The recommended sampling is k_Euler_a or DPM++ 2M Karras on 20 steps, CFGS 7.5 .


## Model v2

[CKPT v2](https://huggingface.co/Guizmus/MosaicArt/resolve/main/MosaicArt_v2.ckpt)

[YAML v2](https://huggingface.co/Guizmus/MosaicArt/resolve/main/MosaicArt_v2.yaml)


## Model v1

![Showcase](https://huggingface.co/Guizmus/MosaicArt/resolve/main/showcase.png)

[CKPT v1](https://huggingface.co/Guizmus/MosaicArt/resolve/main/MosaicArt_v1.ckpt)

[CKPT v1 with ema weights](https://huggingface.co/Guizmus/MosaicArt/resolve/main/MosaicArt_v1_ema.ckpt)

[Dataset](https://huggingface.co/Guizmus/MosaicArt/resolve/main/dataset_v1.zip)

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Guizmus/MosaicArt"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Mosaic Art dog on the moon"
image = pipe(prompt).images[0]

image.save("./MosaicArt.png")
```