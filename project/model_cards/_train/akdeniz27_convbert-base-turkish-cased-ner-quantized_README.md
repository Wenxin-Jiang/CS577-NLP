---
language: tr
license: mit
---

# Turkish Named Entity Recognition (NER) Quantized Model

This model is the dynamically quantized version of the model
(https://akdeniz27/convbert-base-turkish-cased-ner)

# How to use: 
```
# First install "optimum[onnxruntime]":
!pip install "optimum[onnxruntime]"

# and import "ORTModelForTokenClassification":
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForTokenClassification

model_onnx = ORTModelForTokenClassification.from_pretrained("akdeniz27/convbert-base-turkish-cased-ner-quantized", file_name="model_quantized.onnx")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/convbert-base-turkish-cased-ner-quantized")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
ner("your text here")
```
Pls refer (https://github.com/akdeniz27/dynamic_quantization) for details of quantization. 