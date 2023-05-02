---
license: apache-2.0
tags:
- int8
- Intel® Neural Compressor
- neural-compressor
- PostTrainingDynamic
datasets: 
- cnn-news
metrics:
- accuracy
---

# INT8 T5 small finetuned on CNN-News

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [shivaniNK8/t5-small-finetuned-cnn-news](https://huggingface.co/shivaniNK8/t5-small-finetuned-cnn-news).

The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.

The linear modules **lm.head**, fall back to fp32 for less than 1% relative accuracy loss.

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rouge1)** | 38.9981 |39.2142|
| **Model size**  |154M|242M|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/t5-small-finetuned-cnn-news-int8-dynamic',
)
```
