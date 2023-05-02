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

# INT8 DistilBart finetuned on CNN DailyMail

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn).

Below linear modules (40/193) are fallbacked to fp32 for less than 1% relative accuracy loss:

**'model.decoder.layers.10.fc1'**, **'model.decoder.layers.0.fc2'**, 
**'model.decoder.layers.4.fc2'**, **'model.decoder.layers.1.fc2'**, 
**'model.decoder.layers.6.fc2'**, **'model.decoder.layers.2.fc2'**, 
**'model.decoder.layers.3.fc2'**, **'model.encoder.layers.11.fc2'**, 
**'model.decoder.layers.9.fc1'**, **'model.decoder.layers.5.fc2'**, 
**'model.decoder.layers.7.fc1'**, **'model.decoder.layers.8.fc1'**, 
**'model.encoder.layers.0.fc2'**, **'model.decoder.layers.11.fc1'**, 
**'model.encoder.layers.8.fc2'**, **'model.encoder.layers.11.fc1'**, 
**'model.decoder.layers.8.fc2'**, **'model.decoder.layers.2.fc1'**, 
**'model.decoder.layers.11.self_attn.v_proj'**, **'model.encoder.layers.9.fc1'**, 
**'model.decoder.layers.9.fc2'**, **'model.decoder.layers.7.fc2'**, 
**'model.decoder.layers.6.fc1'**, **'model.decoder.layers.0.fc1'**, 
**'model.decoder.layers.1.self_attn.v_proj'**, **'model.encoder.layers.3.fc1'**, 
**'model.encoder.layers.2.fc2'**, **'model.encoder.layers.7.fc2'**, 
**'model.decoder.layers.3.fc1'**, **'model.encoder.layers.1.fc2'**, 
**'model.encoder.layers.10.fc2'**, **'model.encoder.layers.8.fc1'**, 
**'lm_head'**, **'model.decoder.layers.6.self_attn.v_proj'**, 
**'model.decoder.layers.11.self_attn.out_proj'**, **'model.decoder.layers.11.encoder_attn.v_proj'**, 
**'model.encoder.layers.10.fc1'**, **'model.encoder.layers.6.fc1'**, 
**'model.decoder.layers.4.fc1'**, **'model.decoder.layers.1.fc1'**

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rougeLsum)** | 41.2224 | 41.5274 |
| **Model size**  |625M|1669M|

### Load with optimum:

```python
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/bart-large-cnn-int8-dynamic',
)
```