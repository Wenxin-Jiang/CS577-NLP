This is the zero-shot baseline model in the paper ["GPL: Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval"](https://arxiv.org/abs/2112.07577)

The training setup:
1. Start from `distilbert-base-uncased`;
2. Mine 50 hard negatives for each query on MS MARCO with `sentence-transformers/msmarco-distilbert-base-v3` and `sentence-transformers/msmarco-MiniLM-L-6-v3`;
3. Do Margin-MSE training on the tuples (including queries, gold relevant, and hard negatives) with the teacher model `cross-encoder/ms-marco-MiniLM-L-6-v2` for 70K steps with batch size 75, max. sequence-length 350.
