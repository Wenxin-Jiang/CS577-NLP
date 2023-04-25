---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---

# Stable Diffusion v1.5 fine tuned on Waltz with Bashir screencaps

Use prompt: 'wltzwthbshr'

[Waltz with  Bashir on IMDB](https://www.imdb.com/title/tt1185616)

### Output Samples: 
Settings used: "wltzwthbshr SUBJECT", euler a, 35 steps, cfg 7, 1024x1024, high res fix on, sd-vae-ft-mse-original (AUTOMATIC1111 webui)
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000797-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669066999379-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067001297-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067002574-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067002737-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000480-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669066999949-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067002829-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000524-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669066998455-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067001216-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000265-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000984-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000421-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067003066-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067000476-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067002688-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067001859-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067002184-637bef89ca8542a0ba8cd54b.png" width="100%"/>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1669067003006-637bef89ca8542a0ba8cd54b.png" width="100%"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at [Stable diffusion Pipelines](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "mikesmodels/Waltz_with_Bashir_Diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "wltzwthbshr dwayne johnson"
image = pipe(prompt).images[0]
image.save("./dwayne_johnson.png")
```