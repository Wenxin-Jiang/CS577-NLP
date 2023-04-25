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
- text: a cute bunny, mazapan
  example_title: "Bunny"
- text: a cute robot made of mazapan
  example_title: "Robot"
- text: a photograph of a cute dog, mazapan
  example_title: "Dog"
datasets:
- kokuma/figuritas-de-mazapan
---

# DreamBooth model for the `mazapan` concept trained by kokuma on the `kokuma/figuritas-de-mazapan` dataset.
This is a Stable Diffusion model fine-tuned on the `mazapan` concept with DreamBooth for the food theme.\
This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

#### Prompts
- **a cute X, mazapan**: `a cute bunny, mazapan`
- **a cute X made of mazapan**: `a cute robot made of mazapan`
- **a photograph of a cute X, mazapan**: `a photograph of a cute dog, mazapan`

#### Suggested parameters
- **CFG scale**: Between 6 and 8
- **Samplers**: Euler a, Euler, DPM2 a, DPM++ SDE, DPM fast, DPM adaptive, DPM2 a Karras
  
## Examples
| a cute dog, mazapan | a cute sparrow, mazapan | a cute bear, mazapan |
| -- | -- | -- |
| ![](images/00012-3020517259-a-cute-dog,-mazapan.png) | ![](images/00015-2412980111-a-cute-sparrow,-mazapan.png) | ![](images/00020-4193097991-a-cute-bear,-mazapan.png) |

| a cute koala, mazapan | a cute robot made of mazapan | a cute fox, mazapan |
| -- | -- | -- |
| ![](images/00021-3687677306-a-cute-koala,-mazapan.png) | ![](images/00081-1016725166-a-cute-robot-made-of-mazapan.png) | ![](images/00151-901443973-a-cute-fox,-mazapan.png) |


## Usage
```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('kokuma/mazapan')
image = pipeline().images[0]
image
```