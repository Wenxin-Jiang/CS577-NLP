---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- endpoints-template
inference: true
---

# Fork of [CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4)

> Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
> For more information about how Stable Diffusion functions, please have a look at [🤗's Stable Diffusion with 🧨Diffusers blog](https://huggingface.co/blog/stable_diffusion).

For more information about the model, license and limitations check the original model card at [CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4).

### License (CreativeML OpenRAIL-M)

The full license can be found here: https://huggingface.co/spaces/CompVis/stable-diffusion-license

---

This repository implements a custom `handler` task for `text-to-image` for 🤗 Inference Endpoints. The code for the customized pipeline is in the [pipeline.py](https://huggingface.co/philschmid/stable-diffusion-v1-4-endpoints/blob/main/handler.py).

There is also a [notebook](https://huggingface.co/philschmid/stable-diffusion-v1-4-endpoints/blob/main/create_handler.ipynb) included, on how to create the `handler.py`

### expected Request payload
```json
{
    "inputs": "A prompt used for image generation"
}
```

below is an example on how to run a request using Python and `requests`.

## Run Request 
```python
import json
from typing import List
import requests as r
import base64
from PIL import Image
from io import BytesIO

ENDPOINT_URL = ""
HF_TOKEN = ""

# helper decoder
def decode_base64_image(image_string):
  base64_image = base64.b64decode(image_string)
  buffer = BytesIO(base64_image)
  return  Image.open(buffer)


def predict(prompt:str=None):
    payload = {"inputs": code_snippet,"parameters": parameters}
    response = r.post(
        ENDPOINT_URL, headers={"Authorization": f"Bearer {HF_TOKEN}"}, json={"inputs": prompt}
    )
    resp = response.json()
    return decode_base64_image(resp["image"])

prediction = predict(
    prompt="the first animal on the mars"
)
```
expected output

![sample](sample.jpg)
