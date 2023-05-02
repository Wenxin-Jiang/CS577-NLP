---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingDynamic
datasets: 
- cnn_dailymail
metrics:
- rougeLsum
---

# INT8 T5 base finetuned on CNN DailyMail

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [flax-community/t5-base-cnn-dm](https://huggingface.co/flax-community/t5-base-cnn-dm).

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rougeLsum)** | 36.5661 |36.5959|
| **Model size**  |326M|892M|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/t5-base-cnn-dm-int8-dynamic',
)
```
