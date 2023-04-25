---
license: openrail
tags:
  - text-to-image
---
# El Risitas model
This is the fine-tuned Stable Diffusion model trained on images from El Risitas.

Use **Elrisitas** in your prompts.

Update : V2 is out
![image.png](https://s3.amazonaws.com/moonup/production/uploads/1675435580813-635749860725c2f190a76e88.png)

### Sample images:
![output Samples](https://s3.amazonaws.com/moonup/production/uploads/1666666375549-635749860725c2f190a76e88.png)
![output Samples](https://s3.amazonaws.com/moonup/production/uploads/1666827671053-635749860725c2f190a76e88.png)
Based on StableDiffusion 1.5 model

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "Fictiverse/ElRisita"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Elrisitas smiling"
image = pipe(prompt).images[0]

image.save("./Elrisitas.png")
```