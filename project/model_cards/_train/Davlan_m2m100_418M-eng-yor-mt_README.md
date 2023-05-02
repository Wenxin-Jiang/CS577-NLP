Hugging Face's logo
---
language: 
- yo
- en
datasets:
- JW300 + [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
---
# m2m100_418M-eng-yor-mt
## Model description
**m2m100_418M-eng-yor-mt** is a **machine translation** model from English language to Yorùbá language based on a fine-tuned   facebook/m2m100_418M model.  It establishes a **strong baseline** for automatically translating texts from English to Yorùbá.  

Specifically, this model is a *facebook/m2m100_418M* model that was fine-tuned on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt). 

#### Limitations and bias
This model is limited by its training dataset. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on JW300 corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt) dataset

## Training procedure
This model was trained on NVIDIA V100 GPU

## Eval results on Test set (BLEU score)
Fine-tuning m2m100_418M achieves **13.39 BLEU** on [Menyo-20k test set](https://arxiv.org/abs/2103.08647) while mt5-base achieves 9.82

### BibTeX entry and citation info
By David Adelani
```

```


