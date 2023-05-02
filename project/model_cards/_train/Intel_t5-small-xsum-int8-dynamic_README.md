---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingDynamic
datasets: 
- mnli
metrics:
- accuracy
---

# INT8 T5 small finetuned on XSum

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [adasnew/t5-small-xsum](https://huggingface.co/adasnew/t5-small-xsum).

The linear modules **lm.head**, fall back to fp32 for less than 1% relative accuracy loss.

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rouge1)** | 29.9008 |29.9592|
| **Model size**  |154M|242M|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/t5-small-xsum-int8-dynamic',
)
```
