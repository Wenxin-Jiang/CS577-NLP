Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Docs
Solutions
Pricing


---
language:
- en
license: other
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- photorealistic
- photoreal
- diffusers
inference: true
---



Make people look like they have Juggalo Face Makeup


### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "cledoux42/JUGGALO"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "A JUGGALO"
image = pipe(prompt).images[0]
image.save("./result.jpg")
```

# License

This model is licesed under a CreativeML OpenRAIL-M license.

