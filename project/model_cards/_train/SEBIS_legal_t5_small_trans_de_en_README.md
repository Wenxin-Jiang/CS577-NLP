
---
language: Deustch English  
tags:
- translation Deustch English  model
datasets:
- dcep europarl jrc-acquis
widget:
- text: "(2) Die Richtlinie 80/987/EWG des Rates(4) soll den Arbeitnehmern im Fall der Zahlungsunfähigkeit ihres Arbeitgebers einen Mindestschutz gewähren. Deshalb verpflichtet sie die Mitgliedstaaten zur Schaffung einer Einrichtung, die die Befriedigung der nicht erfuellten Arbeitnehmeransprüche garantiert."

---

# legal_t5_small_trans_de_en model

Model on translating legal text from Deustch to English. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis, europarl and dcep.


## Model description

legal_t5_small_trans_de_en is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for translation of legal texts from Deustch to English.

### How to use

Here is how to use this model to translate legal text from Deustch to English in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_trans_de_en"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_trans_de_en", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

de_text = "Eisenbahnunternehmen müssen Fahrkarten über mindestens einen der folgenden Vertriebswege anbieten: an Fahrkartenschaltern oder Fahrkartenautomaten, per Telefon, Internet oder jede andere in weitem Umfang verfügbare Informationstechnik oder in den Zügen."

pipeline([de_text], max_length=512)
```

## Training data

The legal_t5_small_trans_de_en model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html), [EUROPARL](https://www.statmt.org/europarl/), and [DCEP](https://ec.europa.eu/jrc/en/language-technologies/dcep) dataset consisting of 5 Million parallel texts.

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
|   legal_t5_small_trans_de_en | 49.1|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
