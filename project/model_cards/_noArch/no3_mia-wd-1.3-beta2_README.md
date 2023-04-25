---
license: mit
tags:
- text-to-image
widget:
- text: sks_mia
---
### mia from [lost nova](https://store.steampowered.com/app/1603410) on waifu diffusion via Dreambooth
#### model by no3
This your the waifu diffusion model fine-tuned the mia-wd-1.5-beta1 concept taught to waifu diffusion with Dreambooth.
It can be used by modifying the `instance_prompt`: **sks_mia**
You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb), [Spaces with the Public Concepts loaded](https://huggingface.co/spaces/sd-dreambooth-library/stable-diffusion-dreambooth-concepts).
### note
If you want to convert diffusers to checkpoint ".ckpt" to use in UI like [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) or any UI that's uses .ckpt file, Use this [script](https://gist.github.com/Christopher-Hayes/636ba25e0ae2e7020722d5386ac2571b)

If you have issues or questions feel free to visit the Community Tab and start discussion about it.