---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
datasets:
- ProGamerGov/StableDiffusion-v1-5-Regularization-Images
---

**Object-Taped-To-Wall-Diffusion**

This fine-tuned Stable Diffusion v1.5 model was trained for 2000 iterations with a batch size of 4, on a selection of photos of things taped to a wall. Training was performed using [ShivamShrirao/diffusers](https://github.com/ShivamShrirao/diffusers) with full precision, prior-preservation loss, the train-text-encoder feature, and the new [1.5 MSE VAE from Stability AI](https://huggingface.co/stabilityai/sd-vae-ft-mse). A total of 2100 regularization / class images were used from [here](https://huggingface.co/datasets/ProGamerGov/StableDiffusion-v1-5-Regularization-Images). Regularization images were generated using the prompt "artwork style" with 50 DPM++ 2S a Karras steps and a CFG of 7, using the MSE VAE. A negative prompt of "text" was also used for this dataset.

Use the tokens **ttw style** in your prompts for the effect. Note that the effect also appears to occur at a much weaker strength on prompts that steer the output towards specific artistic styles.

This model will likely not perform well on taping objects that are not traditionally able to be taped to walls.


<div align="center">
<img src="https://huggingface.co/ProGamerGov/Object-Taped-To-Wall-Diffusion-V1/resolve/main/v1_size_512x512_t4x8.png">
</div>

* [Full Image](https://huggingface.co/ProGamerGov/Object-Taped-To-Wall-Diffusion-V1/resolve/main/v1_size_512x512_t4x8.png)


Example images were generated with the v1 2000 iteration model using DPM++ 2S a Karras:
 
```
ttw style, <object> taped to wall
```


This model was inspired by the 2019 art piece [*Comedian* by Italian artist Maurizio Cattelan](https://en.wikipedia.org/wiki/Comedian_(artwork\)), where a banana was duct taped to a wall.
