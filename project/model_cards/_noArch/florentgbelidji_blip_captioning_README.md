---
tags:
- image-to-text
- image-captioning
- endpoints-template
license: bsd-3-clause
library_name: generic
---

# Fork of [salesforce/BLIP](https://github.com/salesforce/BLIP) for a `image-captioning` task on 🤗Inference endpoint.

This repository implements a `custom` task for `image-captioning` for 🤗 Inference Endpoints. The code for the customized pipeline is in the [pipeline.py](https://huggingface.co/florentgbelidji/blip_captioning/blob/main/pipeline.py).
To use deploy this model a an Inference Endpoint you have to select `Custom` as task to use the `pipeline.py` file. -> _double check if it is selected_
### expected Request payload
```json
{
  "image": "/9j/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAMCAgICAgMC....", // base64 image as bytes
}
```
below is an example on how to run a request using Python and `requests`.
## Run Request 
1. prepare an image. 
```bash
!wget https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
```
2.run request

```python
import json
from typing import List
import requests as r
import base64

ENDPOINT_URL = ""
HF_TOKEN = ""

def predict(path_to_image: str = None):
    with open(path_to_image, "rb") as i:
        image = i.read()
    payload = {
        "inputs": [image],
        "parameters": {
                   "do_sample": True,
                   "top_p":0.9,
                   "min_length":5,
                   "max_length":20
        }
    }
    response = r.post(
        ENDPOINT_URL, headers={"Authorization": f"Bearer {HF_TOKEN}"}, json=payload
    )
    return response.json()
prediction = predict(
    path_to_image="palace.jpg"
)

```
Example parameters depending on the decoding strategy:

1. Beam search

``` 
        "parameters": {
                   "num_beams":5,
                   "max_length":20
        }
```

2. Nucleus sampling

``` 
        "parameters": {
                   "num_beams":1,
                   "max_length":20,
                   "do_sample": True,
                   "top_k":50,
                   "top_p":0.95
        }
```

3. Contrastive search

``` 
        "parameters": {
                   "penalty_alpha":0.6,
                   "top_k":4
                   "max_length":512
        }
```

See [generate()](https://huggingface.co/docs/transformers/v4.25.1/en/main_classes/text_generation#transformers.GenerationMixin.generate) doc for additional detail


expected output
```python
['buckingham palace with flower beds and red flowers']
```
