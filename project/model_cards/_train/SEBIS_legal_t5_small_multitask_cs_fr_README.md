
---
language: Cszech French  
tags:
- translation Cszech French  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "Agentura USA pro ochranu životního prostředí ve své hodnotící studii v roce 2002 zjistila možnou systémovou toxicitu a karcinogenitu a údaje získané z krevních testů nasvědčují rozsáhlé expozici obyvatelstva."

---

# legal_t5_small_multitask_cs_fr model

Model on translating legal text from Cszech to French. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). The model is parallely trained on the three parallel corpus with 42 language pair
from jrc-acquis, europarl and dcep along with the unsupervised task where the model followed the task of prediction in a masked language model.


## Model description

No pretraining is involved in case of legal_t5_small_multitask_cs_fr model, rather the unsupervised task is added with all the translation task
to realize the multitask learning scenario.

## Intended uses & limitations

The model could be used for translation of legal texts from Cszech to French.

### How to use

Here is how to use this model to translate legal text from Cszech to French in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_multitask_cs_fr"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_multitask_cs_fr", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

cs_text = "Agentura USA pro ochranu životního prostředí ve své hodnotící studii v roce 2002 zjistila možnou systémovou toxicitu a karcinogenitu a údaje získané z krevních testů nasvědčují rozsáhlé expozici obyvatelstva."

pipeline([cs_text], max_length=512)
```

## Training data

The legal_t5_small_multitask_cs_fr model (the supervised task which involved only the corresponding langauge pair and as well as unsupervised task where all of the data of all language pairs were available) model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 5 Million parallel texts.

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
|   legal_t5_small_multitask_cs_fr | 47.588|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
