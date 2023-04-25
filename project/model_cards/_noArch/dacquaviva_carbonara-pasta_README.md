---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
widget:
- text: a photo of carbonara pasta
---

# DreamBooth model for the carbonara concept trained by dacquaviva on the dacquaviva/carbonara dataset.

This is a Stable Diffusion model fine-tuned on the carbonara concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of carbonara pasta**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on `pasta carbonara` images for the food theme. 

Spaghetti Carbonara, one of the most famous Pasta Recipes of Roman Cuisine, is made only with 5 simple ingredients: spaghetti seasoned with browned guanciale, black pepper, pecorino Romano and beaten eggs.

In the authentic Italian recipe for carbonara, the ingredients are very few and of excellent quality. The high quality of ingredients is a necessary condition for the success of this recipe.

In spite of many beliefs, the ingredients of the traditional recipe are only 5: guanciale, pecorino Romano, eggs, pepper and spaghetti. To make the best carbonara of your life, you don’t need any other ingredients, so
DO NOT USE garlic, parsley, onion, cream, milk, parmigiano, pancetta, bacon. :).


## Examples of generated images:
carbonara pasta with view of roman colosseum| carbonara pasta with view of roman colosseum | supermatio eating carbonara pasta at the roman colosseum
:-------------------------:|:-------------------------:|:-------------------------:
![](https://drive.google.com/uc?export=view&id=1igjnySzdQJ8biJ3uYtBRg0Co21xRxNYA)  |  ![](https://drive.google.com/uc?export=view&id=1X8ETR7V_kCvHGNxuHM7sHwWfgMMsqz7d)  |  ![](https://drive.google.com/uc?export=view&id=1yEY_IPt5Z3sf4IjZe4c1rhn84I1ZAKxU)     

supermario eating carbonara pasta|pope francis eating carbonara pasta|pope francis eating carbonara pasta
:-------------------------:|:-------------------------:|:-------------------------:
![](https://drive.google.com/uc?export=view&id=1m9i_y031rkHjF6kvJ0ib55I7eO1yIslV)  |  ![](https://drive.google.com/uc?export=view&id=1MYHLIfqkbUMZ5fH4zCoQo4v23zDi0Or5)  |  ![](https://drive.google.com/uc?export=view&id=1v0jlWEWOW2Bo40NBO9xtY__L3DGaDoVp)     

carbonara pasta with panoramic view of rome at sunset|carbonara pasta with panoramic view of rome at sunset| painting of vespa bike next to a carbonara pasta
:-------------------------:|:-------------------------:|:-------------------------:
![](https://drive.google.com/uc?export=view&id=1ZcgU9qlJa6LJdxu7CLCXimKs_RclI6Zz)  |  ![](https://drive.google.com/uc?export=view&id=1DLlMINWbeNDyqR_XTSqQcBoVvaazhr1k)  |  ![](https://drive.google.com/uc?export=view&id=1FKiYHqYn43aA448G0IVT5mr4291wZNxy)     


## Usage
```python
from diffusers import StableDiffusionPipeline

prompt = "carbonara pasta with panoramic view of rome at sunset"
pipeline = StableDiffusionPipeline.from_pretrained('dacquaviva/carbonara-pasta').to("cuda")
image = pipeline(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
image.save("./image.png")
```
