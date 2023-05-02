Hugging Face's logo
---
language: yo
datasets:
- JW300 + [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
---
# mT5_base_yoruba_adr
## Model description
**mT5_base_yoruba_adr** is a **automatic diacritics restoration** model for Yorùbá language based on a fine-tuned  mT5-base  model.  It achieves the **state-of-the-art performance** for adding the correct diacritics or tonal marks to Yorùbá texts.  

Specifically, this model is a *mT5_base* model that was fine-tuned on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for ADR.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("")
model = AutoModelForTokenClassification.from_pretrained("")
nlp = pipeline("", model=model, tokenizer=tokenizer)
example = "Emir of Kano turban Zhang wey don spend 18 years for Nigeria"
ner_results = nlp(example)
print(ner_results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt) dataset

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (BLEU score)
64.63 BLEU on [Global Voices test set](https://arxiv.org/abs/2003.10564)
70.27 BLEU on [Menyo-20k test set](https://arxiv.org/abs/2103.08647)

### BibTeX entry and citation info
By Jesujoba Alabi and David Adelani
```

```


