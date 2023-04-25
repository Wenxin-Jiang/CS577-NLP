---
tags:
- audio-to-audio
library_name: generic
---

# Audio to Audio repository template

This is a template repository for Audio to Audio to support generic inference with Hugging Face Hub generic Inference API. Examples of Audio to Audio are Source Separation and Speech Enhancement. There are two required steps:

1. Specify the requirements by defining a `requirements.txt` file.
2. Implement the `pipeline.py` `__init__` and `__call__` methods. These methods are called by the Inference API. The `__init__` method should load the model and preload all the elements needed for inference (model, processors, tokenizers, etc.). This is only called once. The `__call__` method performs the actual inference. Make sure to follow the same input/output specifications defined in the template for the pipeline to work.

Example repos
* https://huggingface.co/osanseviero/ConvTasNet_Libri1Mix_enhsingle_16k

## How to start

First create a repo in https://hf.co/new. 
Then clone this template and push it to your repo.

```
git clone https://huggingface.co/templates/audio-to-audio
cd audio-to-audio
git remote set-url origin https://huggingface.co/$YOUR_USER/$YOUR_REPO_NAME
git push --force
```