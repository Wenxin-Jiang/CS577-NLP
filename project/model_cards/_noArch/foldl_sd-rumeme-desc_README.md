---
license: cc-by-sa-4.0
datasets:
- foldl/rumeme-desc
language:
- ru
library_name: diffusers
pipeline_tag: text-to-image
---

# ruMeme Description model


## Example

*Use `Diffusers` >=0.8.0, do not support lower versions.*

```python
from diffusers import StableDiffusionPipeline
import torch

model_path = "foldl/sd-rumeme-desc"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16)
pipe.to("cuda")

image = pipe(prompt="кот").images[0]
image.save("cat".jpg)
```

## Training

### Training Procedure 

Model was trained on 1 P100 GPU for 10k steps.

Base model - https://huggingface.co/OFA-Sys/small-stable-diffusion-v0

Training notebook here - https://www.kaggle.com/code/nukeee/meme-diffusion
  
### Training Data  
  - https://huggingface.co/datasets/foldl/rumeme-desc
  - Same dataset at [Kaggle](https://www.kaggle.com/datasets/nukeee/rumemes-descriptions)