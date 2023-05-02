---
language:
- multilingual
- sv
license: apache-2.0
datasets: KBLab/sucx3_ner
---

# mBERT swedish distilled base model (cased)

This model is a distilled version of [mBERT](https://huggingface.co/bert-base-multilingual-cased). It was distilled using Swedish data, the 2010-2015 portion of the [Swedish Culturomics Gigaword Corpus](https://spraakbanken.gu.se/en/resources/gigaword). The code for the distillation process can be found [here](https://github.com/AddedK/swedish-mbert-distillation/blob/main/azureML/pretrain_distillation.py). This was done as part of my Master's Thesis: [*Task-agnostic knowledge distillation of mBERT to Swedish*](https://kth.diva-portal.org/smash/record.jsf?aq2=%5B%5B%5D%5D&c=2&af=%5B%5D&searchType=UNDERGRADUATE&sortOrder2=title_sort_asc&language=en&pid=diva2%3A1698451&aq=%5B%5B%7B%22freeText%22%3A%22added+kina%22%7D%5D%5D&sf=all&aqe=%5B%5D&sortOrder=author_sort_asc&onlyFullText=false&noOfRows=50&dswid=-6142).


## Model description
This is a 6-layer version of mBERT, having been distilled using the [LightMBERT](https://arxiv.org/abs/2103.06418) distillation method, but without freezing the embedding layer.


## Intended uses & limitations
You can use the raw model for either masked language modeling or next sentence prediction, but it's mostly intended to
be fine-tuned on a downstream task. 


## Training data

The data used for distillation was the 2010-2015 portion of the [Swedish Culturomics Gigaword Corpus](https://spraakbanken.gu.se/en/resources/gigaword).
The tokenized data had a file size of approximately 9 GB.

## Evaluation results

When evaluated on the [SUCX 3.0 ](https://huggingface.co/datasets/KBLab/sucx3_ner) dataset, it achieved an average F1 score of 0.859 which is competitive with the score mBERT obtained, 0.866.

When evaluated on the [English WikiANN](https://huggingface.co/datasets/wikiann) dataset, it achieved an average F1 score of 0.826 which is competitive with the score mBERT obtained, 0.849. 

Additional results and comparisons are presented in my Master's Thesis

