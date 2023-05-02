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

# INT8 DistilBart finetuned on CNN DailyMail

### Post-training dynamic quantization

This is an INT8  PyTorch model quantized with [huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) through the usage of [Intel® Neural Compressor](https://github.com/intel/neural-compressor). 

The original fp32 model comes from the fine-tuned model [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6).

Below linear modules (21/133) are fallbacked to fp32 for less than 1% relative accuracy loss:

**'model.decoder.layers.2.fc2'**, **'model.encoder.layers.11.fc2'**, **'model.decoder.layers.1.fc2'**, **'model.decoder.layers.0.fc2'**, **'model.decoder.layers.4.fc1'**, **'model.decoder.layers.3.fc2'**, **'model.encoder.layers.8.fc2'**, **'model.decoder.layers.3.fc1'**, **'model.encoder.layers.11.fc1'**, **'model.encoder.layers.0.fc2'**, **'model.encoder.layers.3.fc1'**, **'model.encoder.layers.10.fc2'**, **'model.decoder.layers.5.fc1'**, **'model.encoder.layers.1.fc2'**, **'model.encoder.layers.3.fc2'**, **'lm_head'**, **'model.encoder.layers.7.fc2'**, **'model.decoder.layers.0.fc1'**, **'model.encoder.layers.4.fc1'**, **'model.encoder.layers.10.fc1'**, **'model.encoder.layers.6.fc1'**

### Evaluation result

|   |INT8|FP32|
|---|:---:|:---:|
| **Accuracy (eval-rougeLsum)** | 41.4707 | 41.8117 |
| **Model size**  |722M|1249M|
### Load with optimum:

```python
# transformers <= 4.23.0
from optimum.intel.neural_compressor.quantization import IncQuantizedModelForSeq2SeqLM
int8_model = IncQuantizedModelForSeq2SeqLM.from_pretrained(
    'Intel/distilbart-cnn-12-6-int8-dynamic',
)
```