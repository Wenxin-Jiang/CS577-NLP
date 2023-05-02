# Condenser for Vietnamese
Transformer architectures for dense retrieval pre-training on vietnamese dataset. Details can be found in our papers, [Condenser: a Pre-training Architecture for Dense Retrieval](https://arxiv.org/abs/2104.08253) and [Unsupervised Corpus Aware Language Model Pre-training for Dense Passage Retrieval
](https://arxiv.org/abs/2108.05540).

For example, to load Condenser weights,
```
from transformers import AutoModel
model = AutoModel.from_pretrained('NlpHUST/Condenser-phobert-base')
```