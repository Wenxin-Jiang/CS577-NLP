---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---
# multi-QA_v1-mpnet-asymmetric-Q
## Model Description
SentenceTransformers is a set of models and frameworks that enable training and generating sentence embeddings from given data. The generated sentence embeddings can be utilized for Clustering, Semantic Search and other tasks. We used two separate pretrained [mpnet-base](https://huggingface.co/microsoft/mpnet-base) models and trained them using contrastive learning objective. Question and answer pairs from StackExchange and other datasets were used as training data to make the model robust to Question / Answer embedding similarity.
We developed this model during the 
[Community week using JAX/Flax for NLP & CV](https://discuss.huggingface.co/t/open-to-the-community-community-week-using-jax-flax-for-nlp-cv/7104), 
organized by Hugging Face. We developed this model as part of the project:
[Train the Best Sentence Embedding Model Ever with 1B Training Pairs](https://discuss.huggingface.co/t/train-the-best-sentence-embedding-model-ever-with-1b-training-pairs/7354). We benefited from efficient hardware infrastructure to run the project: 7 TPUs v3-8, as well
as assistance from Google’s Flax, JAX, and Cloud team members about efficient deep learning frameworks.
## Intended uses
This model set is intended to be used as a sentence encoder for a search engine. Given an input sentence, it ouptuts a vector which captures 
the sentence semantic information. The sentence vector may be used for semantic-search, clustering or sentence similarity tasks.
Two models should be used on conjunction for Semantic Search purposes.
1. [multi-QA_v1-mpnet-asymmetric-Q](https://huggingface.co/flax-sentence-embeddings/multi-QA_v1-mpnet-asymmetric-Q) - Model to encode Questions
1. [multi-QA_v1-mpnet-asymmetric-Q](https://huggingface.co/flax-sentence-embeddings/multi-QA_v1-mpnet-asymmetric-A) - Model to encode Answers
## How to use
Here is how to use this model to get the features of a given text using [SentenceTransformers](https://github.com/UKPLab/sentence-transformers) library:
```python
from sentence_transformers import SentenceTransformer
model_Q = SentenceTransformer('flax-sentence-embeddings/multi-QA_v1-mpnet-asymmetric-Q')
model_A = SentenceTransformer('flax-sentence-embeddings/multi-QA_v1-mpnet-asymmetric-A')
question = "Replace me by any question you'd like."
question_embbedding = model_Q.encode(text)
answer = "Replace me by any answer you'd like."
answer_embbedding = model_A.encode(text)
answer_likeliness = cosine_similarity(question_embedding, answer_embedding)
```
# Training procedure
## Pre-training 
We use the pretrained [`Mpnet-base`](https://huggingface.co/microsoft/mpnet-base). Please refer to the model
card for more detailed information about the pre-training procedure.
## Fine-tuning 
We fine-tune the model using a contrastive objective. Formally, we compute the cosine similarity from each possible sentence pairs from the batch.
We then apply the cross entropy loss by comparing with true pairs.
### Hyper parameters
We trained on model on a TPU v3-8. We train the model during 80k steps using a batch size of 1024 (128 per TPU core).
We use a learning rate warm up of 500. The sequence length was limited to 128 tokens. We used the AdamW optimizer with
a 2e-5 learning rate. The full training script is accessible in this current repository.
### Training data
We used the concatenation from multiple Stackexchange Question-Answer datasets to fine-tune our model. MSMARCO, NQ & other question-answer datasets were also used.
| Dataset                                                  | Paper                                    | Number of training tuples  |
|:--------------------------------------------------------:|:----------------------------------------:|:--------------------------:|
| [Stack Exchange QA - Title & Answer](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_best_voted_answer_jsonl) | - | 4,750,619 |
| [Stack Exchange](https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_title_body_jsonl) | - | 364,001 |
| [TriviaqQA](https://huggingface.co/datasets/trivia_qa) | - | 73,346 |
| [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/) | [paper](https://aclanthology.org/P18-2124.pdf) | 87,599 |
| [Quora Question Pairs](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs) | - | 103,663 |
| [Eli5](https://huggingface.co/datasets/eli5) | [paper](https://doi.org/10.18653/v1/p19-1346) | 325,475 |
| [PAQ](https://github.com/facebookresearch/PAQ) | [paper](https://arxiv.org/abs/2102.07033) | 64,371,441 |
| [WikiAnswers](https://github.com/afader/oqa#wikianswers-corpus) | [paper](https://doi.org/10.1145/2623330.2623677) | 77,427,422 |
| [MS MARCO](https://microsoft.github.io/msmarco/) | [paper](https://doi.org/10.1145/3404835.3462804) | 9,144,553 |
| [GOOAQ: Open Question Answering with Diverse Answer Types](https://github.com/allenai/gooaq) | [paper](https://arxiv.org/pdf/2104.08727.pdf) | 3,012,496 |
| [Yahoo Answers](https://www.kaggle.com/soumikrakshit/yahoo-answers-dataset) Question/Answer | [paper](https://proceedings.neurips.cc/paper/2015/hash/250cf8b51c773f3f8dc8b4be867a9a02-Abstract.html) | 681,164 |
| SearchQA | - | 582,261 |
| [Natural Questions (NQ)](https://ai.google.com/research/NaturalQuestions) | [paper](https://transacl.org/ojs/index.php/tacl/article/view/1455) | 100,231 |