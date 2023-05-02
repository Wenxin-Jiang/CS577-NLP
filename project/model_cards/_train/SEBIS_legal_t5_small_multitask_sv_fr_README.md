
---
language: Swedish French  
tags:
- translation Swedish French  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "Europaparlamentet understryker att det stora antalet kvinnor och barn bland flyktingar och internt fördrivna som registrerats av internationella organ som resultat av väpnade konflikter och inbördeskrig är mycket oroväckande."

---

# legal_t5_small_multitask_sv_fr model

Model on translating legal text from Swedish to French. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). The model is parallely trained on the three parallel corpus with 42 language pair
from jrc-acquis, europarl and dcep along with the unsupervised task where the model followed the task of prediction in a masked language model.


## Model description

No pretraining is involved in case of legal_t5_small_multitask_sv_fr model, rather the unsupervised task is added with all the translation task
to realize the multitask learning scenario.

## Intended uses & limitations

The model could be used for translation of legal texts from Swedish to French.

### How to use

Here is how to use this model to translate legal text from Swedish to French in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_multitask_sv_fr"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_multitask_sv_fr", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

sv_text = "Europaparlamentet understryker att det stora antalet kvinnor och barn bland flyktingar och internt fördrivna som registrerats av internationella organ som resultat av väpnade konflikter och inbördeskrig är mycket oroväckande."

pipeline([sv_text], max_length=512)
```

## Training data

The legal_t5_small_multitask_sv_fr model (the supervised task which involved only the corresponding langauge pair and as well as unsupervised task where all of the data of all language pairs were available) model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 8 Million parallel texts.

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
|   legal_t5_small_multitask_sv_fr | 45.790|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
