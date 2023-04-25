---
tags:
- feature-extraction
- endpoints-template
license: bsd-3-clause
library_name: generic
---
# Fork of [salesforce/BLIP](https://github.com/salesforce/BLIP) for a `feature-extraction` task on 🤗Inference endpoint.
This repository implements a `custom` task for `feature-extraction` for 🤗 Inference Endpoints. The code for the customized pipeline is in the [pipeline.py](https://huggingface.co/florentgbelidji/blip-embeddings/blob/main/pipeline.py).
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
        b64 = base64.b64encode(i.read())
    payload = {"inputs": {"image": b64.decode("utf-8")}}
    response = r.post(
        ENDPOINT_URL, headers={"Authorization": f"Bearer {HF_TOKEN}"}, json=payload
    )
    return response.json()
prediction = predict(
    path_to_image="palace.jpg"
)
```
expected output
```python
{'feature_vector': [0.016450975090265274,
  -0.5551009774208069,
  0.39800673723220825,
  -0.6809228658676147,
  2.053842782974243,
  -0.4712907075881958,...]
 }
```