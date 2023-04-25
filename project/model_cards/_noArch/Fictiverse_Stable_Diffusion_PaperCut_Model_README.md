---
license: creativeml-openrail-m
tags:
  - text-to-image
---
# 🧩 Paper Cut model V1
This is the fine-tuned Stable Diffusion model trained on Paper Cut images.

Use **PaperCut** in your prompts.

### Sample images:
![PaperCut.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667910351389-635749860725c2f190a76e88.jpeg)
![PaperCut.jpg](https://s3.amazonaws.com/moonup/production/uploads/1667912285222-635749860725c2f190a76e88.jpeg)
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

### ✨ Community spotlight :
@PiyarSquare :
[![PiyarSquare video](https://img.youtube.com/vi/wQWHnZlxFj8/0.jpg)](https://www.youtube.com/watch?v=wQWHnZlxFj8)
@MrPlasm0 :
[![MrPlasm0 video](https://img.youtube.com/vi/J68hZ_-L6w4/0.jpg)](https://www.youtube.com/watch?v=J68hZ_-L6w4)
@omsk13 :
[![Omsk Music video](https://img.youtube.com/vi/BCZOD2AQCFg/0.jpg)](https://www.youtube.com/watch?v=BCZOD2AQCFg)