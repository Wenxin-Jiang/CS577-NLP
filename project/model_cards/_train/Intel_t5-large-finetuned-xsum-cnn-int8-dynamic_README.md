---
license: mit
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

# INT8 T5 large finetuned on CNN DailyMail

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [sysresearch101/t5-large-finetuned-xsum-cnn](https://huggingface.co/sysresearch101/t5-large-finetuned-xsum-cnn).

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rougeLsum)** | 29.6346 |29.7451|
| **Model size**  |879M|3021M|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/t5-large-finetuned-xsum-cnn-int8-dynamic',
)
```