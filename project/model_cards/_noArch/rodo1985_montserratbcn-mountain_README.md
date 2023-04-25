---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a photo of montserratbcn mountain trending on artstation, hdr, fireworks
---

# DreamBooth model for the montserratbcn concept trained by rodo1985 on the rodo1985/montserrat_mountain_dataset dataset

This is a Stable Diffusion model fine-tuned on `mountain` images for the landscape theme. It can be used by modifying the `instance_prompt`: **a photo of montserratbcn mountain**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


Montserrat is a mountain range located near Barcelona, Spain. Montserrat mountain is known for its distinctive, jagged peaks, which are made of conglomerate rock and rise to an elevation of over 4,000 feet (1,200 meters) above sea level. The mountain's unique geology is a result of its location at the convergence of the Catalan Coastal Range and the Pre-Coastal Range. The peaks of Montserrat are formed by layers of sedimentary rock that have been pushed up and eroded over time, creating a series of steep cliffs and pinnacles. The mountain's highest peak is Sant Jeroni, which stands at an elevation of 4,051 feet (1,235 meters). There are several marked trails on Montserrat mountain that offer spectacular views of the surrounding landscape and the Mediterranean Sea.
The mountain is home to the Montserrat Monastery, a Benedictine abbey that was founded in the 11th century and is known for its stunning location, historical significance, and cultural importance. The mountain itself is a popular destination for hikers and climbers, due to its rugged and varied terrain. It is also home to a number of notable landmarks and attractions, including the Montserrat Museum, which houses a collection of art and artifacts, and the Basilica of Montserrat, which contains a museum and a chapel. The mountain is named after the Virgin of Montserrat, the patron saint of Catalonia, whose statue is housed in the abbey.



## Real image
![montserrat](img/real_montserrat.png)

## Examples of generated images

![montserratbcn-mountain](img/montserrat_0.png)


![montserratbcn-mountain](img/montserrat_1.png)

![montserratbcn-mountain](img/montserrat_2.png)


![montserratbcn-mountain](img/montserrat_3.png)


![montserratbcn-mountain](img/montserrat_4.png)



## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('rodo1985/montserratbcn-mountain')
image = pipeline().images[0]
image
```
