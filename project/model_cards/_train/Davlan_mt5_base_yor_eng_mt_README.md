Hugging Face's logo
---
language: 
- yo
- en
datasets:
- JW300 + [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
---
# mT5_base_yor_eng_mt
## Model description
**mT5_base_yor_eng_mt** is a **machine translation** model from Yorùbá language to English language based on a fine-tuned  mT5-base  model.  It establishes a **strong baseline** for automatically translating texts from Yorùbá to English.  

Specifically, this model is a *mT5_base* model that was fine-tuned on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt)
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for MT.
```python
from transformers import MT5ForConditionalGeneration, T5Tokenizer

model = MT5ForConditionalGeneration.from_pretrained("Davlan/mt5_base_yor_eng_mt")
tokenizer = T5Tokenizer.from_pretrained("google/mt5-base")
input_string = "Akọni ajìjàgbara obìnrin tó sun àtìmalé torí owó orí"
inputs = tokenizer.encode(input_string, return_tensors="pt")
generated_tokens = model.generate(inputs)
results = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on on  JW300 Yorùbá corpus and [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt) dataset

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (BLEU score)
15.57 BLEU on [Menyo-20k test set](https://arxiv.org/abs/2103.08647)

### BibTeX entry and citation info
By David Adelani
```

```


