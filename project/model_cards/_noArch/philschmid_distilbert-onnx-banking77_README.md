---
tags:
- text-classification
- endpoints-template
- optimum
library_name: generic
---

# Optimized and Quantized DistilBERT with a custom pipeline with handler.py

> NOTE: Blog post coming soon

This is a template repository for Text Classification using Optimum and onnxruntime to support generic inference with Hugging Face Hub generic Inference API. There are two required steps:

1. Specify the requirements by defining a `requirements.txt` file.
2. Implement the `handler.py` `__init__` and `__call__` methods. These methods are called by the Inference API. The `__init__` method should load the model and preload the optimum model and tokenizers as well as the `text-classification` pipeline needed for inference. This is only called once. The `__call__` method performs the actual inference. Make sure to follow the same input/output specifications defined in the template for the pipeline to work.

add 
```
library_name: generic
```
to the readme.

_note: the `generic` community image currently only support `inputs` as parameter and no parameter._