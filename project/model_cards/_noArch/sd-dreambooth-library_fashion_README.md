---
license: apache-2.0
tags:
- dreambooth-hackathon
- Text-to-image
- stable-diffusion
pipeline_tag: text-to-image
---
https://civitai.com/models/21642/fashion3d

import torch

from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("sd-dreambooth-library/fashion")  

pipe = pipe.to("cuda")

prompt = "a photograph of an astronaut riding a horse"

image = pipe(prompt).images[0]

image.save(f"astronaut_rides_horse.png")

![image](https://s3.amazonaws.com/moonup/production/uploads/1669885576067-63044d493926de1f7ec709f4.png)
![image](https://s3.amazonaws.com/moonup/production/uploads/1669885940159-63044d493926de1f7ec709f4.png)
![de123af26a6c184d137487276175858.png](https://s3.amazonaws.com/moonup/production/uploads/1669886049338-63044d493926de1f7ec709f4.png)
![55aa13dfd7e61edbe61d1fba5affc0e.png](https://s3.amazonaws.com/moonup/production/uploads/1669886100601-63044d493926de1f7ec709f4.png)