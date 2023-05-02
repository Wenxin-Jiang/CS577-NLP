---
tags: 
- autotrain
- pre-trained
- finbert
- fill-mask
language: unk
widget:
- text: Tesla remains one of the highest [MASK] stocks on the market. Meanwhile, Aurora Innovation is a pre-revenue upstart that shows promise.
- text: Asian stocks [MASK] from a one-year low on Wednesday as U.S. share futures and oil recovered from the previous day's selloff, but uncertainty over the impact of the Omicron
- text: U.S. stocks were set to rise on Monday, led by [MASK] in Apple which neared $3 trillion in market capitalization, while investors braced for a Federal Reserve meeting later this week.
---

`FinBERT` is a BERT model pre-trained on financial communication text. The purpose is to enhance financial NLP research and practice. 

### Pre-training
It is trained on the following three financial communication corpus. The total corpora size is 4.9B tokens.

- Corporate Reports 10-K & 10-Q: 2.5B tokens
- Earnings Call Transcripts: 1.3B tokens
- Analyst Reports: 1.1B tokens

The entire training is done using an **NVIDIA DGX-1** machine. The server has 4 Tesla P100 GPUs, providing a total of 128 GB of GPU memory. This machine enables us to train the BERT models using a batch size of 128. We utilize Horovord framework for multi-GPU training. Overall, the total time taken to perform pretraining for one model is approximately **2 days**.


More details on `FinBERT`'s pre-training process can be found at: https://arxiv.org/abs/2006.08097

`FinBERT` can be further fine-tuned on downstream tasks. Specifically, we have fine-tuned `FinBERT` on an analyst sentiment classification task, and the fine-tuned model is shared at [https://huggingface.co/demo-org/auditor_review_model](https://huggingface.co/demo-org/auditor_review_model)

### Usage
Load the model directly from Transformers:
```
from transformers import AutoModelForMaskedLM
model = AutoModelForMaskedLM.from_pretrained("demo-org/finbert-pretrain", use_auth_token=True)
```

### Questions
Please contact the Data Science COE if you have more questions about this pre-trained model

### Demo Model
This model card is for demo purposes.  The original model card for this model is [https://huggingface.co/yiyanghkust/finbert-pretrain](https://huggingface.co/yiyanghkust/finbert-pretrain).