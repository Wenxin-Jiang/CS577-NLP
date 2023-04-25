---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---


### Lichtspiel Diffusion 
This is a fine-tuned Stable Diffusion 1.5 model trained on stills from movies by celebrated cinematographers. It gives your images a cinematic look, muted colors, bloom and film grain. Sometimes it works great, sometimes not so well. 


Sample pictures of this concept:

![0](https://huggingface.co/FricktionMaster/lichtspiel-diffusion/resolve/main/sample.jpg)

Download the *.ckpt file from the "files and versions" tab into the Stable Diffusion models folder of your web-ui of choice. Rename it to model.ckpt and ... that's it.

Use the token Lichtspiel Style to activate the effect. It works particularly well for portraits and if you additionally reference specific films like Blade Runner, True Grit or The Revenant. 

The model was trained using dreambooth by TheLastBen based on the SD implementation by XavierXiao. 

Trained with 10.500 steps.



Test the model with A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)
Or you can run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

This model is open access with a CreativeML Open RAIL++-M License further specifying rights and usage -> https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL
