---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
datasets:
- ProGamerGov/StableDiffusion-v1-5-Regularization-Images
---

**Min-Illust-Background-Diffusion**

This fine-tuned Stable Diffusion v1.5 model was trained for 2250 iterations with a batch size of 4, on a selection of artistic works by Sin Jong Hun. Training was performed using [ShivamShrirao/diffusers](https://github.com/ShivamShrirao/diffusers) with full precision, prior-preservation loss, the train-text-encoder feature, and the new [1.5 MSE VAE from Stability AI](https://huggingface.co/stabilityai/sd-vae-ft-mse). A total of 4120 regularization / class images were used from [here](https://huggingface.co/datasets/ProGamerGov/StableDiffusion-v1-5-Regularization-Images). Regularization images were generated using the prompt "artwork style", 50 DDIM steps, and a CFG of 7.

Use the tokens **sjh style** in your prompts for the effect. Note that the effect also appears to occur at a much weaker strength on prompts that steer the output towards specific artistic styles.

This model will likely not perform well on generating portraits and related tasks, as the training data was primarily composed of landscapes.


<div align="center">
<img src="https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_size_512x768_t3x4.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_size_512x768_t3x4.png)

<div align="center">
<img src="https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_size_512x512_t4x10.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_size_512x512_t4x10.png)

<div align="center">
<img src="https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_512x512_t4x5.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/Min-Illust-Background-Diffusion/resolve/main/v1_512x512_t4x5.png)


Example images were generated with the v1 2250 iteration model using 50 steps of DPM++ 2M Karras with a format of:
 
```
<prompt>, sjh style
```
