# capreolus/electra-base-msmarco

## Model description
ELECTRA-Base model (`google/electra-base-discriminator`) fine-tuned on the MS MARCO passage classification task. It is intended to be used as a `ForSequenceClassification` model, but requires some modification since it contains a BERT classification head rather than the standard ELECTRA classification head. See the [TFElectraRelevanceHead](https://github.com/capreolus-ir/capreolus/blob/master/capreolus/reranker/TFBERTMaxP.py) in the Capreolus BERT-MaxP implementation for a usage example.

This corresponds to the ELECTRA-Base model used to initialize PARADE (ELECTRA) in [PARADE: Passage Representation Aggregation for Document Reranking](https://arxiv.org/abs/2008.09093) by Li et al. It was converted from the released [TFv1 checkpoint](https://zenodo.org/record/3974431/files/vanilla_electra_base_on_MSMARCO.tar.gz). Please cite the PARADE paper if you use these weights.
