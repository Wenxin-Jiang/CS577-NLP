---
license: mit
tags:
- audio
- automatic-speech-recognition
- endpoints-template
library_name: generic
inference: false
duplicated_from: philschmid/openai-whisper-endpoint
---

# OpenAI [Whisper](https://github.com/openai/whisper) Inference Endpoint example

> Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.

For more information about the model, license and limitations check the original repository at [openai/whisper](https://github.com/openai/whisper).

---

This repository implements a custom `handler` task for `automatic-speech-recognition` for 🤗 Inference Endpoints using OpenAIs new Whisper model. The code for the customized pipeline is in the [pipeline.py](https://huggingface.co/philschmid/openai-whisper-endpoint/blob/main/handler.py).

There is also a [notebook](https://huggingface.co/philschmid/openai-whisper-endpoint/blob/main/create_handler.ipynb) included, on how to create the `handler.py`

###  Request 

The endpoint expects a binary audio file. Below is a cURL example and a Python example using the `requests` library.

**curl**

```bash
# load audio file
wget https://cdn-media.huggingface.co/speech_samples/sample1.flac

# run request
curl --request POST \
  --url https://{ENDPOINT}/ \
  --header 'Content-Type: audio/x-flac' \
  --header 'Authorization: Bearer {HF_TOKEN}' \
  --data-binary '@sample1.flac'
```

**Python**

```python
import json
from typing import List
import requests as r
import base64
import mimetypes

ENDPOINT_URL=""
HF_TOKEN=""

def predict(path_to_audio:str=None):
    # read audio file
    with open(path_to_audio, "rb") as i:
      b = i.read()
    # get mimetype
    content_type= mimetypes.guess_type(path_to_audio)[0]

    headers= {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": content_type
    }
    response = r.post(ENDPOINT_URL, headers=headers, data=b)
    return response.json()

prediction = predict(path_to_audio="sample1.flac")

prediction

```
expected output

```json
{"text": " going along slushy country roads and speaking to damp audiences in draughty school rooms day after day for a fortnight. He'll have to put in an appearance at some place of worship on Sunday morning, and he can come to us immediately afterwards."}
```
