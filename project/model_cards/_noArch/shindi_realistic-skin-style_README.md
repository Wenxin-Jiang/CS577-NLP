---
license: creativeml-openrail-m
tags:
- text-to-image
widget:
- text: jqkz
---
### Realistic-Skin- Style Dreambooth model trained by shindi with [Hugging Face Dreambooth Training Space](https://huggingface.co/spaces/multimodalart/dreambooth-training) with the v2-1-768 base model

You run your new concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb). Don't forget to use the concept prompts! 


# RealisticSkinStyle

This is my (Saleh) experiment with training on detailed photos of people featured textured skin. I noticed typically in my generations, 
skin looks airbrushed and smoonth which gives away that it's AI. Hoping to use this as a base model for further fine tunes so that models
can look more realistic.

🚨
This is V1 of this exploration. Ideas for further exploration is annotating the training data as described here: 
https://www.reddit.com/r/StableDiffusion/comments/zcr644/make_better_dreambooth_style_models_by_using/

Note that you can use parenthesis (like this) to increase attention on a word or phrase. For example "A woman with ((blue eyes)) wearing a (((Hijab))), jqkz". More parentheses means more attention. 

## Sample prompts:

"A smiling black woman, jqkz"

"A white woman wearing a white shirt, jqkz style"

"A photograph of an old man wearing a black shirt, jqkz style"

"A young man with a cigarette, jqkz"

"A woman with ((blue eyes)) wearing a (((Hijab))), jqkz"

## Example Outputs
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/27.jpeg)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/3.jpeg)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/9.png)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/11.png)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/15.png)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/17.png)
![hello](https://huggingface.co/shindi/realisticskinstyle/resolve/main/18.jpeg)


