# capreolus/bert-base-msmarco

## Model description
BERT-Base model (`google/bert_uncased_L-12_H-768_A-12`) fine-tuned on the MS MARCO passage classification task. It is intended to be used as a `ForSequenceClassification` model; see the [Capreolus BERT-MaxP implementation](https://github.com/capreolus-ir/capreolus/blob/master/capreolus/reranker/TFBERTMaxP.py) for a usage example.

This corresponds to the BERT-Base model used to initialize BERT-MaxP and PARADE variants in [PARADE: Passage Representation Aggregation for Document Reranking](https://arxiv.org/abs/2008.09093) by Li et al. It was converted from the released [TFv1 checkpoint](https://zenodo.org/record/3974431/files/vanilla_bert_base_on_MSMARCO.tar.gz). Please cite the PARADE paper if you use these weights.
