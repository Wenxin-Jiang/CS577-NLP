
---
language: Cszech Swedish  
tags:
- translation Cszech Swedish  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "Hračky určené pro častý kontakt s kůží obsahující alergenní látky jiné než vonné, které jsou známé vyvoláváním vážných nebo dokonce osudných účinků na zdraví dětí (například látky, které mohou vyvolat anafylaktický šok), musí být v souladu s ustanoveními týkajícími se označování uvedenými ve směrnici Komise 2006/125/ES ze dne 5. prosince 2006 o obilných a ostatních příkrmech pro kojence a malé děti."

---

# legal_t5_small_multitask_cs_sv model

Model on translating legal text from Cszech to Swedish. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). The model is parallely trained on the three parallel corpus with 42 language pair
from jrc-acquis, europarl and dcep along with the unsupervised task where the model followed the task of prediction in a masked language model.


## Model description

No pretraining is involved in case of legal_t5_small_multitask_cs_sv model, rather the unsupervised task is added with all the translation task
to realize the multitask learning scenario.

## Intended uses & limitations

The model could be used for translation of legal texts from Cszech to Swedish.

### How to use

Here is how to use this model to translate legal text from Cszech to Swedish in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_multitask_cs_sv"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_multitask_cs_sv", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

cs_text = "Hračky určené pro častý kontakt s kůží obsahující alergenní látky jiné než vonné, které jsou známé vyvoláváním vážných nebo dokonce osudných účinků na zdraví dětí (například látky, které mohou vyvolat anafylaktický šok), musí být v souladu s ustanoveními týkajícími se označování uvedenými ve směrnici Komise 2006/125/ES ze dne 5. prosince 2006 o obilných a ostatních příkrmech pro kojence a malé děti."

pipeline([cs_text], max_length=512)
```

## Training data

The legal_t5_small_multitask_cs_sv model (the supervised task which involved only the corresponding langauge pair and as well as unsupervised task where all of the data of all language pairs were available) model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 5 Million parallel texts.

## Training procedure

The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 4096). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining


## Evaluation results

When the model is used for translation test dataset, achieves the following results:

Test results :

| Model | BLEU score |
|:-----:|:-----:|
|   legal_t5_small_multitask_cs_sv | 35.871|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
