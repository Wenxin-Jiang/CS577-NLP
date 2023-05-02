---
license: mit
---
Transformer model based on Vaswani et al., 2017 for Danish-English Neural Machine Translation. 

It has ~74M parameters and is a fine-tuned version of Helsinki-Opus-NLP da-en.


The model achieves a BLEU score of 49.16 on a hold-out test set for the TED2020 dataset (in-domain dataset).

The model achieves a BLEU score of 44.16 on a hold-out test set for the for CCAligned and Wikimatrix (out-of-domain dataset).


This outperforms the baseline Opus model, which achieved BLEU scores of 46.74 and 42.31 on the in-domain and out-of-domain data respectively.


Note: When running inference "_" characters can sometimes replace spaces.