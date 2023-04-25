---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
inference: true
---
# Wall Street Journal Hedcut Style for Stable Diffusion
Readers of the Wall Street Journal (WSJ) are familiar with the distinctive style used to create portaits of their writers and subjects. This is a fine-tuned stable
diffusion model that can be used to create hedcut-styled images using the prompt **_wsj hedcut of \<subject\>_**. This model can also be used in a DreamBooth environment
to train a face or other subject for custom and unique hedcuts.

#### *If you use this model, please make an effort to attribute the principal artist of the training images, Noli Novak, along with the other disclosures and restrictions required by the license.


```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch
model_id = "dmillar/wsj-hedcut-v1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "wsj hedcut of a woman"
image = pipe(prompt).images[0]
image.save("./woman_hedcut.png")
```

## Sample Images
![Hepburn](https://huggingface.co/dmillar/wsj-hedcut-v1/resolve/main/hepburn.png)
Prompt: "wsj hedcut of audrey hepburn, portrait, detailed, sharp, black and white, pleasing, white background", Steps: 20, Sampler: "Euler a", CFG scale: 7, Seed: 231828633
![Mbappe](https://huggingface.co/dmillar/wsj-hedcut-v1/resolve/main/mbappe.png)
Prompt: "wsj hedcut of the Kylian Mbappe, male, portrait, detailed, sharp, black and white, pleasing, white background", Steps: 20, Sampler: "Euler a", CFG scale: 7, Seed: 1863052262
![Hanks](https://huggingface.co/dmillar/wsj-hedcut-v1/resolve/main/hanks.png)
Prompt: "wsj hedcut of tom hanks, portrait, detailed, sharp, black and white, pleasing, white background", Steps: 20, Sampler: Euler a, CG scale: 7, Seed: 224907260
![Dog](https://huggingface.co/dmillar/wsj-hedcut-v1/resolve/main/dog.png)
![Cat](https://huggingface.co/dmillar/wsj-hedcut-v1/resolve/main/cat.png)

