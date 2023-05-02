
---
language: Italian Spanish  
tags:
- translation Italian Spanish  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "considerando che il 28 marzo 2002 il Consiglio di sicurezza dell'ONU si è dichiarato favorevole all'attuazione integrale del Protocollo di Lusaka e si è detto disposto a cooperare con tutte le parti in conflitto per raggiungere tale obiettivo, nonché ad avviare consultazioni con il governo dell'Angola per ricercare i mezzi con cui modificare le sanzioni imposte all'UNITA attraverso la risoluzione 1127 (1997), e ciò al fine di agevolare i colloqui di pace,"

---

# legal_t5_small_trans_it_es_small_finetuned model

Model on translating legal text from Italian to Spanish. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is first pretrained all the translation data over some unsupervised task. Then the model is trained on three parallel corpus from jrc-acquis, europarl and dcep.


## Model description

legal_t5_small_trans_it_es_small_finetuned is initially pretrained on unsupervised task with the all of the data of the training set. The unsupervised task was "masked language modelling". legal_t5_small_trans_it_es_small_finetuned is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for translation of legal texts from Italian to Spanish.

### How to use

Here is how to use this model to translate legal text from Italian to Spanish in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_trans_it_es_small_finetuned"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_trans_it_es", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

it_text = "considerando che il 28 marzo 2002 il Consiglio di sicurezza dell'ONU si è dichiarato favorevole all'attuazione integrale del Protocollo di Lusaka e si è detto disposto a cooperare con tutte le parti in conflitto per raggiungere tale obiettivo, nonché ad avviare consultazioni con il governo dell'Angola per ricercare i mezzi con cui modificare le sanzioni imposte all'UNITA attraverso la risoluzione 1127 (1997), e ciò al fine di agevolare i colloqui di pace,"

pipeline([it_text], max_length=512)
```

## Training data

The legal_t5_small_trans_it_es_small_finetuned (the supervised task which involved only the corresponding langauge pair and as well as unsupervised task where all of the data of all language pairs were available) model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 9 Million parallel texts.

## Training procedure

The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 4096). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining

The pre-training data was the combined data from all the 42 language pairs. The task for the model was to predict the portions of a sentence which were masked randomly.


## Evaluation results

When the model is used for translation test dataset, achieves the following results:

Test results :

| Model | BLEU score |
|:-----:|:-----:|
|   legal_t5_small_trans_it_es_small_finetuned | 49.083|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
