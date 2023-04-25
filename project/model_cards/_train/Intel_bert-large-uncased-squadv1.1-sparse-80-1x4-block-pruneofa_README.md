---
language: en
license: apache-2.0
---
# 80% 1x4 Block Sparse BERT-Large (uncased) Fine Tuned on SQuADv1.1
This model is a result of fine-tuning a Prune OFA 80% 1x4 block sparse pre-trained BERT-Large combined with knowledge distillation.
This model yields the following results on SQuADv1.1 development set:<br>
`{"exact_match": 84.673, "f1": 91.174}`

For further details see our paper, [Prune Once for All: Sparse Pre-Trained Language Models](https://arxiv.org/abs/2111.05754), and our open source implementation available [here](https://github.com/IntelLabs/Model-Compression-Research-Package/tree/main/research/prune-once-for-all).
