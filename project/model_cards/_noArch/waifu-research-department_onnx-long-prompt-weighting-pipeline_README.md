---
language:
- en
library_name: diffusers
tags:
- stable-diffusion
- text-to-image
license: apache-2.0
inference: false
---

# OnnxStableDiffusionLongPromptWeightingPipeline

Onnx Pipeline for text-to-image and image-to-image generation using Stable Diffusion, without tokens length limit and support parsing weighting in prompt.

require diffusers>=0.10.0

> Now the pipeline has been contributed to the official diffusers community pipelines. You can use 
custom_pipeline="lpw_stable_diffusion_onnx" directly.

```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained(
    'CompVis/stable-diffusion-v1-4',
    custom_pipeline="waifu-research-department/onnx-long-prompt-weighting-pipeline",
    revision="onnx",
    provider="CUDAExecutionProvider"
)
pipe=pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars, best quality"
neg_prompt = "lowres, bad anatomy, error body, error hair, error arm, error hands, bad hands, error fingers, bad fingers, missing fingers, error legs, bad legs, multiple legs, missing legs, error lighting, error shadow, error reflection, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"

pipe.text2img(prompt, width=512,height=512,negative_prompt=neg_prompt,max_embeddings_multiples=3).images[0]
```

if you see
```
Token indices sequence length is longer than the specified maximum sequence length for this model ( 108 > 77 ) . Running this sequence through the model will result in indexing errors
```
This is normal, do not worry .