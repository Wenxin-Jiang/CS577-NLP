
---
license: apache-2.0
---

# HPD-TinyBERT-F128

This repository contains the pre-trained models for our paper [Compressing Sentence Representation for Semantic Retrieval via Homomorphic Projective Distillation](https://arxiv.org/abs/2203.07687). The sentence embedding model contains only 14M parameters and the model size is only 55MB. 

## Overview

We propose **H**omomorphic **P**rojective **D**istillation (HPD) to learn compressed sentence embeddings. Our method augments a small Transformer encoder model with learnable projection layers to produce compact representations while mimicking a large pre-trained language model to retain the sentence representation quality.

## Details

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 128 dimensional dense vector space and can be used for tasks like clustering or semantic search.

The teacher model is [`princeton-nlp/sup-simcse-roberta-large`](https://huggingface.co/princeton-nlp/sup-simcse-bert-base-uncased) and the student model is [`nreimers/TinyBERT_L-4_H-312_v2`](https://huggingface.co/nreimers/TinyBERT_L-4_H-312_v2).

## Usage

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

After installing the package, you can simply load our model
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('Xuandong/HPD-TinyBERT-F128')
```

Then you can use our model for **encoding sentences into embeddings**
```python
sentences = ['He plays guitar.', 'A street vendor is outside.']
sentence_embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
```

## Evaluation Results

We evaluate our model on semantic textual similarity (STS) tasks. The results are:


| STS12 | STS13 | STS14 | STS15 | STS16 | STS-B | SICK-R |  Avg. |
|-------|-------|-------|-------|-------|--------------|-----------------|-------|
| 74.29 | 83.05 | 78.80 | 84.62 | 81.17 |    84.36     |      80.83      | 81.02 |


## Training

Please refer to the github repo (https://github.com/XuandongZhao/HPD) for the details about the training.


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 312, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Dense({'in_features': 312, 'out_features': 128, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
)
```

## Citation

Please cite our paper if you use HPD in your work:

```bibtex
@article{zhao2022compressing,
  title={Compressing Sentence Representation for Semantic Retrieval via Homomorphic Projective Distillation},
  author={Zhao, Xuandong and Yu, Zhiguo and Wu, Ming and Li, Lei},
  journal={arXiv preprint arXiv:2203.07687},
  year={2022}
}
```