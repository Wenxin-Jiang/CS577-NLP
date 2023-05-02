Hugging Face's logo
---
language: 
- yo
- en
datasets:
- JW300 + [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
---
# mbart50-large-eng-yor-mt
## Model description
**mbart50-large-eng-yor-mt** is a **machine translation** model from English language to Yorùbá language based on a fine-tuned   facebook/mbart-large-50 model.  It establishes a **strong baseline** for automatically translating texts from English to Yorùbá.  

Specifically, this model is a *mbart-large-50* model that was fine-tuned on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt). The model was trained using Swahili(sw_KE) as the language since the pre-trained model does not initially support Yorùbá. Thus, you need to use the sw_KE for language code when evaluating the model. 

#### Limitations and bias
This model is limited by its training dataset. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on on  JW300 corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt) dataset

## Training procedure
This model was trained on NVIDIA V100 GPU

## Eval results on Test set (BLEU score)
Fine-tuning mbarr50-large achieves **13.39 BLEU** on [Menyo-20k test set](https://arxiv.org/abs/2103.08647) while mt5-base achieves 9.82

### BibTeX entry and citation info
By David Adelani
```

```


