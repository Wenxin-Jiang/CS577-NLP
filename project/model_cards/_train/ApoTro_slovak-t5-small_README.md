---
language: sk
license: mit
datasets:
- oscar
---

# SlovakT5-small
This model was trained on slightly adapted code from [run_t5_mlm_flax.py](https://github.com/huggingface/transformers/tree/main/examples/flax/language-modeling). 
If you want to know about training details or evaluation results, see [SlovakT5_report.pdf](https://huggingface.co/ApoTro/slovak-t5-small/resolve/main/SlovakT5_report.pdf). For evaluation, you can also run [SlovakT5_eval.ipynb](https://colab.research.google.com/github/richardcepka/notebooks/blob/main/SlovakT5_eval.ipynb).

### How to use
SlovakT5-small can be fine-tuned for a lot of different downstream tasks. For example, NER: 
```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("ApoTro/slovak-t5-small")
model = T5ForConditionalGeneration.from_pretrained("ApoTro/slovak-t5-small")

input_ids = tokenizer("ner veta: Do druhého kola postúpili Robert Fico a Andrej Kiska s rozdielom 4,0%.", return_tensors="pt").input_ids
labels = tokenizer("per: Robert Fico | per: Andrej Kiska", return_tensors="pt").input_ids

# the forward function automatically creates the correct decoder_input_ids
loss = model(input_ids=input_ids, labels=labels).loss
loss.item()
```