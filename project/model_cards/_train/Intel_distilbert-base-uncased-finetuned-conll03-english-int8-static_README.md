---
language:
- en
license: apache-2.0
tags:
- token-classfication
- int8
- Intel® Neural Compressor
- PostTrainingStatic
datasets:
- conll2003
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-conll03-english-int8-static
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Conll2003
      type: conll2003
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9858650364082395
---
# INT8 distilbert-base-uncased-finetuned-conll03-english

###  Post-training static quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [elastic/distilbert-base-uncased-finetuned-conll03-english](https://huggingface.co/elastic/distilbert-base-uncased-finetuned-conll03-english).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

### Test result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-accuracy)** |0.9859|0.9882|
| **Model size (MB)**  |64.5|253|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForTokenClassification
int8_model = IncQuantizedModelForTokenClassification.from_pretrained(
    'Intel/distilbert-base-uncased-finetuned-conll03-english-int8-static',
)
```
