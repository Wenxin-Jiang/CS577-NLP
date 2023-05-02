
---
language: Italian French  
tags:
- translation Italian French  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "Qualora gli emendamenti approvati dal Parlamento abbiano l'effetto di aumentare le spese iscritte nel progetto di bilancio oltre il tasso massimo previsto, la commissione competente per il merito sottopone al Parlamento una proposta intesa a fissare un nuovo tasso massimo in conformità del paragrafo 9, ultimo comma, degli articoli 78 del trattato CECA, 272 del trattato CE e 177 del trattato CEEA."

---

# legal_t5_small_trans_it_fr model

Model on translating legal text from Italian to French. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis, europarl and dcep.


## Model description

legal_t5_small_trans_it_fr is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for translation of legal texts from Italian to French.

### How to use

Here is how to use this model to translate legal text from Italian to French in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_trans_it_fr"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_trans_it_fr", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

it_text = "Qualora gli emendamenti approvati dal Parlamento abbiano l'effetto di aumentare le spese iscritte nel progetto di bilancio oltre il tasso massimo previsto, la commissione competente per il merito sottopone al Parlamento una proposta intesa a fissare un nuovo tasso massimo in conformità del paragrafo 9, ultimo comma, degli articoli 78 del trattato CECA, 272 del trattato CE e 177 del trattato CEEA."

pipeline([it_text], max_length=512)
```

## Training data

The legal_t5_small_trans_it_fr model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 5 Million parallel texts.

## Training procedure

The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 4096). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for translation test dataset, achieves the following results:

Test results :

| Model | BLEU score |
|:-----:|:-----:|
|   legal_t5_small_trans_it_fr | 50.559|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
