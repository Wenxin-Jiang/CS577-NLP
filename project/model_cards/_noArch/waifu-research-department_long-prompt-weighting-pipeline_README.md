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

# StableDiffusionLongPromptWeightingPipeline

Pipeline for text-to-image and image-to-image generation using Stable Diffusion, without tokens length limit and support parsing weighting in prompt.

require diffusers>=0.10.0

> Now the pipeline has been contributed to the official diffusers community pipelines. You can use 
custom_pipeline="lpw_stable_diffusion" directly.

```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained(
    'hakurei/waifu-diffusion',
    custom_pipeline="waifu-research-department/long-prompt-weighting-pipeline",
    revision="fp16",
    torch_dtype=torch.float16
)
pipe=pipe.to("cuda")

prompt = "best_quality (1girl:1.3) bow bride brown_hair closed_mouth frilled_bow frilled_hair_tubes frills (full_body:1.3) fox_ear hair_bow hair_tubes happy hood japanese_clothes kimono long_sleeves red_bow smile solo tabi uchikake white_kimono wide_sleeves cherry_blossoms"
neg_prompt = "lowres, bad_anatomy, error_body, error_hair, error_arm, error_hands, bad_hands, error_fingers, bad_fingers, missing_fingers, error_legs, bad_legs, multiple_legs, missing_legs, error_lighting, error_shadow, error_reflection, text, error, extra_digit, fewer_digits, cropped, worst_quality, low_quality, normal_quality, jpeg_artifacts, signature, watermark, username, blurry"

pipe.text2img(prompt, width=512,height=768,negative_prompt=neg_prompt,max_embeddings_multiples=3).images[0]
```

if you see
```
Token indices sequence length is longer than the specified maximum sequence length for this model ( 108 > 77 ) . Running this sequence through the model will result in indexing errors
```
This is normal, do not worry .

# Acknowledgments

Some code borrows from [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui):

https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/3246a2d6b898da6a98fe9df4dc67944635a41bd3/modules/sd_hijack_clip.py

https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/3246a2d6b898da6a98fe9df4dc67944635a41bd3/modules/prompt_parser.py