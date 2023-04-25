---
tags:
- text-classification
library_name: generic
---

# Text Classification repository template

This is a template repository for Text Classification to support generic inference with Hugging Face Hub generic Inference API. There are two required steps:

1. Specify the requirements by defining a `requirements.txt` file.
2. Implement the `pipeline.py` `__init__` and `__call__` methods. These methods are called by the Inference API. The `__init__` method should load the model and preload all the elements needed for inference (model, processors, tokenizers, etc.). This is only called once. The `__call__` method performs the actual inference. Make sure to follow the same input/output specifications defined in the template for the pipeline to work.

## How to start
First create a repo in https://hf.co/new. 
Then clone this template and push it to your repo.
```
git clone https://huggingface.co/templates/text-classification
cd text-classification
git remote set-url origin https://huggingface.co/$YOUR_USER/$YOUR_REPO_NAME
git push --force
```