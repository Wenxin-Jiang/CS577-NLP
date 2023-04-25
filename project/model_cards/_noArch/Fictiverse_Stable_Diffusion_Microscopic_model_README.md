---
license: openrail
tags:
  - text-to-image
---
# Microscopic model V1
This is the fine-tuned Stable Diffusion model trained on microscopic images.

Use **Microscopic** in your prompts.

### Sample images:
![sample image](https://s3.amazonaws.com/moonup/production/uploads/1667894926121-635749860725c2f190a76e88.jpeg)
![sample image](https://s3.amazonaws.com/moonup/production/uploads/1667934752243-635749860725c2f190a76e88.png)

Image enhancing : Before/After
![sample gif](https://s3.amazonaws.com/moonup/production/uploads/1667935562197-635749860725c2f190a76e88.gif)
Based on StableDiffusion 1.5 model

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Fictiverse/Stable_Diffusion_PaperCut_Model"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "PaperCut R2-D2"
image = pipe(prompt).images[0]

image.save("./R2-D2.png")
```