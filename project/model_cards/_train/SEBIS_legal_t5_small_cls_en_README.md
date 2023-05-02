
---
language: English   
tags:
- classification English model
datasets:
- jrc-acquis
widget:
- text: "Appointment of members of the Conciliation Body instituted by Commission Decision 94/442/EC of 1 July 1994 setting up a conciliation procedure in the context of the clearance of the accounts of the European Agricultural Guidance and Guarantee Fund (EAGGF) Guarantee Section (2006/C 193/09) (1) The Commission has renewed the term of office of: Mr José Luis SAENZ GARCIA-BAQUERO (ES) (from 1 August 2006 to 31 July 2007). (2) The Commission has appointed as members: - Mr Peter BAUMANN (DA) (from 1 August 2006 to 31 July 2009); - Mr Daniel PERRIN (FR) (from 1 August 2006 to 31 July 2009). (3) The Commission has appointed as substitute members: - Mr Robert BURIAN (A) (from 1 August 2006); - Mr Eduardo DIEZ PATIER (ES) (from 1 August 2006). --------------------------------------------------"

---

# legal_t5_small_cls_en model

Model for classification of legal text written in English. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_cls_en is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for classification of legal texts written in English.

### How to use

Here is how to use this model to classify legal text written in English in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_cls_en"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_cls_en", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

en_text = "Appointment of members of the Conciliation Body instituted by Commission Decision 94/442/EC of 1 July 1994 setting up a conciliation procedure in the context of the clearance of the accounts of the European Agricultural Guidance and Guarantee Fund (EAGGF) Guarantee Section (2006/C 193/09) (1) The Commission has renewed the term of office of: Mr José Luis SAENZ GARCIA-BAQUERO (ES) (from 1 August 2006 to 31 July 2007). (2) The Commission has appointed as members: - Mr Peter BAUMANN (DA) (from 1 August 2006 to 31 July 2009); - Mr Daniel PERRIN (FR) (from 1 August 2006 to 31 July 2009). (3) The Commission has appointed as substitute members: - Mr Robert BURIAN (A) (from 1 August 2006); - Mr Eduardo DIEZ PATIER (ES) (from 1 August 2006). --------------------------------------------------"

pipeline([en_text], max_length=512)
```

## Training data

The legal_t5_small_cls_en model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 19 Thousand texts.

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
|   legal_t5_small_cls_en | 0.6247|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
