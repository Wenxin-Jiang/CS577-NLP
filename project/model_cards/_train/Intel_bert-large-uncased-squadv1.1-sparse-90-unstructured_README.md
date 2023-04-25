---
language: en
---
# 90% Sparse BERT-Large (uncased) Fine Tuned on SQuADv1.1
This model is a result of fine-tuning a Prune OFA 90% sparse pre-trained BERT-Large combined with knowledge distillation.
This model yields the following results on SQuADv1.1 development set:<br>
`{"exact_match": 83.56669820245979, "f1": 90.20829352733487}`

For further details see our paper, [Prune Once for All: Sparse Pre-Trained Language Models](https://arxiv.org/abs/2111.05754), and our open source implementation available [here](https://github.com/IntelLabs/Model-Compression-Research-Package/tree/main/research/prune-once-for-all).
