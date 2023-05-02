
---
language: Cszech   
tags:
- classification Cszech model
datasets:
- jrc-acquis
widget:
- text: "Bez námitek k navrhovanému spojení (Případ č. COMP/M.4169 – Virgin/CPW/JV) (2006/C 103/16) (Text s významem pro EHP) Dne 29. března 2006 se Komise rozhodla nevznést námitky proti výše uvedenému spojení a prohlásit ho za slučitelné se společným trhem. Toto rozhodnutí je založeno na čl. 6 odst. 1 písm. b) nařízení Rady (ES) č. 139/2004. Celý text rozhodnutí je přístupný pouze v angličtině a bude uveřejněn poté, co bude zbaven obchodního tajemství, které může případně obsahovat. Text bude dosažitelný: - na webové stránce Europa – hospodářská soutěž (http://europa.eu.int/comm/competition/mergers/cases/). Tato webová stránka umožňuje vyhledat jednotlivá rozhodnutí o spojení, a to včetně společnosti, čísla případu, data a indexu odvětví hospodářství. - v elektronické podobě na webové stránce EUR-Lex, pod dokumentem č. 32006M4169. EUR-Lex umožňuje přístup k Evropskému právu přes Internet. (http://europa.eu.int/eur-lex/lex) --------------------------------------------------"

---

# legal_t5_small_cls_cs model

Model for classification of legal text written in Cszech. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_cls_cs is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for classification of legal texts written in Cszech.

### How to use

Here is how to use this model to classify legal text written in Cszech in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_cls_cs"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_cls_cs", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

cs_text = "Bez námitek k navrhovanému spojení (Případ č. COMP/M.4169 – Virgin/CPW/JV) (2006/C 103/16) (Text s významem pro EHP) Dne 29. března 2006 se Komise rozhodla nevznést námitky proti výše uvedenému spojení a prohlásit ho za slučitelné se společným trhem. Toto rozhodnutí je založeno na čl. 6 odst. 1 písm. b) nařízení Rady (ES) č. 139/2004. Celý text rozhodnutí je přístupný pouze v angličtině a bude uveřejněn poté, co bude zbaven obchodního tajemství, které může případně obsahovat. Text bude dosažitelný: - na webové stránce Europa – hospodářská soutěž (http://europa.eu.int/comm/competition/mergers/cases/). Tato webová stránka umožňuje vyhledat jednotlivá rozhodnutí o spojení, a to včetně společnosti, čísla případu, data a indexu odvětví hospodářství. - v elektronické podobě na webové stránce EUR-Lex, pod dokumentem č. 32006M4169. EUR-Lex umožňuje přístup k Evropskému právu přes Internet. (http://europa.eu.int/eur-lex/lex) --------------------------------------------------"

pipeline([cs_text], max_length=512)
```

## Training data

The legal_t5_small_cls_cs model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 18 Thousand texts.

## Training procedure


The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 64). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for classification test dataset, achieves the following results:

Test results :

| Model | F1 score |
|:-----:|:-----:|
|   legal_t5_small_cls_cs | 0.6297|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
