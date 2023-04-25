---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
- en
- English
inference: true
widget:
- text: 1girl, detailed, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, by dan mumford, yusuke murata, makoto shinkai, ross tran
  example_title: example 1girl
---

# Olivia V1.0 

Welcome to Olivia V1.0 This model is for educational and testing purposes only. 

## 🧨 Diffusers

This model can be used like any other model. [Click to read more](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion)

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "ShibaDeveloper/olivia-v1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "1girl, beautiful girl, face, yellow eyes, black hair"
image = pipe(prompt).images[0]

image.save("./olivia_img.png")
```
## ✨ Examples

Examples of images generated using Olivia V1.0 :

![Girl](https://huggingface.co/ShibaDeveloper/olivia-v1.0/resolve/main/girl.png)
```
Prompt: 1girl, detailed, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, by dan mumford, yusuke murata, makoto shinkai, ross tran
Steps: 50, Sampler: DDIM, CFG scale: 12
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)