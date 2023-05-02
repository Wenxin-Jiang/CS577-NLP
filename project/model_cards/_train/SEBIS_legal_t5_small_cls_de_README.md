
---
language: Deustch   
tags:
- classification Deustch model
datasets:
- jrc-acquis
widget:
- text: "BESCHLUSS DES RATES vom 17. Dezember 1999 über den Abschluß des Abkommens in Form eines Briefwechsels zwischen der Europäischen Gemeinschaft und der Tunesischen Republik über die Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft (1999/873/EG) DER RAT DER EUROPÄISCHEN UNION - gestützt auf den Vertrag zur Gründung der Europäischen Gemeinschaft, insbesondere auf Artikel 133 in Verbindung mit Artikel 300 Absatz 2 Unterabsatz 1, auf Vorschlag der Kommission, in Erwägung nachstehender Gründe: (1) Zwischen der Europäischen Gemeinschaft und der Tunesischen Republik wurde ein Abkommen in Form eines Briefwechsels ausgehandelt, um die Geltungsdauer der Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft, die in Artikel 3 des Protokolls Nr. 1 des Europa-Mittelmeer-Abkommens zur Gründung einer Assoziation zwischen der Europäischen Gemeinschaft und ihren Mitgliedstaaten einerseits und der Tunesischen Republik andererseits(1) vorgesehen ist, für die Zeit vom 1. Januar bis zum 31. Dezember 2000 zu verlängern. (2) Das Abkommen sollte im Namen der Gemeinschaft genehmigt werden - BESCHLIESST: Artikel 1 Das Abkommen in Form eines Briefwechsels zwischen der Europäischen Gemeinschaft und der Tunesischen Republik über die Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft wird im Namen der Gemeinschaft genehmigt. Der Wortlaut des Abkommens ist diesem Beschluß beigefügt. Artikel 2 Der Präsident des Rates wird ermächtigt, die Person zu bestellen, die befugt ist, das Abkommen rechtsverbindlich für die Gemeinschaft zu unterzeichnen. Geschehen zu Brüssel am 17. Dezember 1999. Im Namen des Rates Der Präsident K. HEMILÄ (1) ABl. L 97 vom 30.3.1998, S. 1."

---

# legal_t5_small_cls_de model

Model for classification of legal text written in Deustch. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_cls_de is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for classification of legal texts written in Deustch.

### How to use

Here is how to use this model to classify legal text written in Deustch in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_cls_de"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_cls_de", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

de_text = "BESCHLUSS DES RATES vom 17. Dezember 1999 über den Abschluß des Abkommens in Form eines Briefwechsels zwischen der Europäischen Gemeinschaft und der Tunesischen Republik über die Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft (1999/873/EG) DER RAT DER EUROPÄISCHEN UNION - gestützt auf den Vertrag zur Gründung der Europäischen Gemeinschaft, insbesondere auf Artikel 133 in Verbindung mit Artikel 300 Absatz 2 Unterabsatz 1, auf Vorschlag der Kommission, in Erwägung nachstehender Gründe: (1) Zwischen der Europäischen Gemeinschaft und der Tunesischen Republik wurde ein Abkommen in Form eines Briefwechsels ausgehandelt, um die Geltungsdauer der Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft, die in Artikel 3 des Protokolls Nr. 1 des Europa-Mittelmeer-Abkommens zur Gründung einer Assoziation zwischen der Europäischen Gemeinschaft und ihren Mitgliedstaaten einerseits und der Tunesischen Republik andererseits(1) vorgesehen ist, für die Zeit vom 1. Januar bis zum 31. Dezember 2000 zu verlängern. (2) Das Abkommen sollte im Namen der Gemeinschaft genehmigt werden - BESCHLIESST: Artikel 1 Das Abkommen in Form eines Briefwechsels zwischen der Europäischen Gemeinschaft und der Tunesischen Republik über die Regelung für die Einfuhr von nicht behandeltem Olivenöl mit Ursprung in Tunesien in die Gemeinschaft wird im Namen der Gemeinschaft genehmigt. Der Wortlaut des Abkommens ist diesem Beschluß beigefügt. Artikel 2 Der Präsident des Rates wird ermächtigt, die Person zu bestellen, die befugt ist, das Abkommen rechtsverbindlich für die Gemeinschaft zu unterzeichnen. Geschehen zu Brüssel am 17. Dezember 1999. Im Namen des Rates Der Präsident K. HEMILÄ (1) ABl. L 97 vom 30.3.1998, S. 1."

pipeline([de_text], max_length=512)
```

## Training data

The legal_t5_small_cls_de model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 23 Thousand texts.

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
|   legal_t5_small_cls_de | 0.6358|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
