---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# stackoverflow_mpnet-base

This is a microsoft/mpnet-base model trained on 18,562,443 (title, body) pairs from StackOverflow. 

SentenceTransformers is a set of models and frameworks that enable training and generating sentence embeddings from given data. The generated sentence embeddings can be utilized for Clustering, Semantic Search and other tasks. We used a pretrained [microsoft/mpnet-base](https://huggingface.co/microsoft/mpnet-base) model and trained it using Siamese Network setup and contrastive learning objective. 18,562,443 (title, body) pairs from StackOverflow was used as training data. For this model, mean pooling of hidden states were used as sentence embeddings. See data_config.json and train_script.py in this respository how the model was trained and which datasets have been used.

We developed this model during the 
[Community week using JAX/Flax for NLP & CV](https://discuss.huggingface.co/t/open-to-the-community-community-week-using-jax-flax-for-nlp-cv/7104), 
organized by Hugging Face. We developed this model as part of the project:
[Train the Best Sentence Embedding Model Ever with 1B Training Pairs](https://discuss.huggingface.co/t/train-the-best-sentence-embedding-model-ever-with-1b-training-pairs/7354). We benefited from efficient hardware infrastructure to run the project: 7 TPUs v3-8, as well
as assistance from Google’s Flax, JAX, and Cloud team members about efficient deep learning frameworks.

## Intended uses

Our model is intended to be used as a sentence encoder for a search engine. Given an input sentence, it outputs a vector which captures 
the sentence semantic information. The sentence vector may be used for semantic-search, clustering or sentence similarity tasks.

## How to use

Here is how to use this model to get the features of a given text using [SentenceTransformers](https://github.com/UKPLab/sentence-transformers) library:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('flax-sentence-embeddings/stackoverflow_mpnet-base')
text = "Replace me by any question / answer you'd like."
text_embbedding = model.encode(text)
# array([-0.01559514,  0.04046123,  0.1317083 ,  0.00085931,  0.04585106,
#        -0.05607086,  0.0138078 ,  0.03569756,  0.01420381,  0.04266302 ...],
#        dtype=float32)
```

# Training procedure

## Pre-training 

We use the pretrained [microsoft/mpnet-base](https://huggingface.co/microsoft/mpnet-base). Please refer to the model
card for more detailed information about the pre-training procedure.

## Fine-tuning 

We fine-tune the model using a contrastive objective. Formally, we compute the cosine similarity from each possible sentence pairs from the batch.
We then apply the cross entropy loss by comparing with true pairs.

### Hyper parameters

We trained on model on a TPU v3-8. We train the model during 80k steps using a batch size of 1024 (128 per TPU core).
We use a learning rate warm up of 500. The sequence length was limited to 128 tokens. We used the AdamW optimizer with
a 2e-5 learning rate. The full training script is accessible in this current repository.

### Training data

We used 18,562,443 (title, body) pairs from StackOverflow as training data.

| Dataset                                                  | Paper                                    | Number of training tuples  |
|:--------------------------------------------------------:|:----------------------------------------:|:--------------------------:|
| StackOverflow title body pairs | - | 18,562,443 |

