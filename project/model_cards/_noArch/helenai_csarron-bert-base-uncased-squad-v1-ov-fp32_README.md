---
language:
- en
tags:
- openvino
---

# csarron/bert-base-uncased-squad-v1

This is the [csarron/bert-base-uncased-squad-v1](https://huggingface.co/csarron/bert-base-uncased-squad-v1) model converted to [OpenVINO](https://openvino.ai), for accellerated inference.

An example of how to do inference on this model:
```python
from optimum.intel.openvino import OVModelForQuestionAnswering
from transformers import AutoTokenizer, pipeline

# model_id should be set to either a local directory or a model available on the HuggingFace hub.
model_id = "helenai/csarron-bert-base-uncased-squad-v1-ov-fp32"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = OVModelForQuestionAnswering.from_pretrained(model_id)
pipe = pipeline("question-answering", model=model, tokenizer=tokenizer)
result = pipe("What is OpenVINO?", "OpenVINO is a framework that accelerates deep learning inferencing")
print(result)
```

