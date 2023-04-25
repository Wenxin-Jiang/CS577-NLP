---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: a cartoon digital art of FunnyShihTzu dog smiling
---

# DreamBooth model for the FunnyShihTzu concept trained by Tiemi on the Tiemi/FunnyShihTzu dataset.

This is a Stable Diffusion model fine-tuned on photos of my dog with DreamBooth 🐕.

It can be used by modifying the `instance_prompt` and keeping the tag FunnyShihTzu.

**Examples of prompts:**
- a cartoon digital art of FunnyShihTzu dog smiling
- a photo of FunnyShihTzu dog laying in the couch
- a funko pop of FunnyShihTzu dog smiling
 
Each time you run the prompt you'll see a different image (even with the same text).

If you enjoy this model, please give it a like ❤️.

## Description

This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.

## Photo of my dog:
<img src="https://s3.amazonaws.com/moonup/production/uploads/1672671005943-6192492551e3de53a3628c6b.jpeg" alt="shih_tzu" width="200"/>


## Examples of generated images:
![shih-tzu-funkopop](https://s3.amazonaws.com/moonup/production/uploads/1674651472459-6192492551e3de53a3628c6b.jpeg)
![shih-tzu-drawing.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1672350721131-6192492551e3de53a3628c6b.jpeg) 
![shih-tzu-wearing-crown.png](https://s3.amazonaws.com/moonup/production/uploads/1672351831323-6192492551e3de53a3628c6b.png)
![shih-tzu-wearing-crown-2.png](https://s3.amazonaws.com/moonup/production/uploads/1672351830953-6192492551e3de53a3628c6b.png)
![shih-tzu-cartoon-smiling-3.png](https://s3.amazonaws.com/moonup/production/uploads/1672351830966-6192492551e3de53a3628c6b.png)
![shih-tzu-cartoon-smiling.png](https://s3.amazonaws.com/moonup/production/uploads/1672351831343-6192492551e3de53a3628c6b.png)
![shih-tzu-acropolis.jpg](https://s3.amazonaws.com/moonup/production/uploads/1672351829105-6192492551e3de53a3628c6b.jpeg)

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Tiemi/FunnyShihTzu-dog')
image = pipeline().images[0]
image
```

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!