---
language: en
license: apache-2.0
---


## Overview

Model included in a paper for modeling fine grained similarity between documents:

**Title**: "Multi-Vector Models with Textual Guidance for Fine-Grained Scientific Document Similarity"

**Authors**: Sheshera Mysore, Arman Cohan, Tom Hope

**Paper**: https://arxiv.org/abs/2111.08366

**Github**: https://github.com/allenai/aspire 

**Note**: In the context of the paper, this model is referred to as `cosentbert` and represents a baseline sentence encoder for scientific text. The paper trains two versions of `cosentbert`, one for biomedical scientific text and another one for computer science text. This released model is trained on a union of all available data across scientific domains in the Semantic Scholar Open Research Corpus (S2ORC) dataset. This difference in training data leads to different, though close, evaluation performance than in the paper.

## Model Card

**Model description:** This model represents a SciBERT based sentence encoder pre-trained for scientific text similarity. The model represents a sentence with a single vector obtained by reading the CLS token for the sentence.

**Training data:** The model is trained on sets of co-citation context sentences referencing the same set of papers in a contrastive learning setup. These sentences can often be considered as paraphrases since co-citation sentences citing the same papers often describe similar aspects of the co-cited papers. The model is trained on 4.3 million sentence pairs of this type. In training the model negative examples for the contrastive loss are obtained as random in-batch negatives. An example pair of sentences used for training is as follows:

> "The idea of distant supervision has been proposed and used widely in Relation Extraction (Mintz et al., 2009; Riedel et al., 2010; Hoffmann et al., 2011; Surdeanu et al., 2012) , where the source of labels is an external knowledge base."
>
> "Distant supervision [31, 43, 21, 49] generates training data automatically by aligning texts and a knowledge base (KB) (see Fig. 1 )."

**Training procedure:** The model was trained with the Adam Optimizer and a learning rate of 2e-5 with 1000 warm-up steps followed by linear decay of the learning rate. The model training convergence is checked with the loss on a held out dev set consisting of co-citation context pairs. All the training data used was in English.

**Intended uses & limitations:** This model is trained for sentence similarity tasks in scientific text and is best used as a sentence encoder. However with appropriate fine-tuning the model can also be used for other tasks such as classification. Note that about 50% of the training data consists of text from biomedical text and performance may be superior on text from bio-medicine and similar domains.


**How to use:** This model can be used as a BERT model via the `transformers` library:

```
from transformers import AutoModel, AutoTokenizer
aspire_sent = AutoModel.from_pretrained('allenai/aspire-sentence-embedder')
aspire_tok = AutoTokenizer.from_pretrained('allenai/aspire-sentence-embedder')
s='We present a new scientific document similarity model based on matching fine-grained aspects of texts.'
inputs = aspire_tok(s, padding=True, truncation=True, return_tensors="pt", max_length=512)
result = aspire_sent(\*\*inputs)
clsrep = result.last_hidden_state[:,0,:]
```

OR via the `sentence_transformers` library:

```
from sentence_transformers import SentenceTransformer, models
word_embedding_model = models.Transformer('allenai/aspire-sentence-embedder', max_seq_length=512)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(), pooling_mode='cls')
aspire_sb = SentenceTransformer(modules=[word_embedding_model, pooling_model])
clsrep_sb = sentbert_model.encode([s])
```

**Variable and metrics:**
Since the paper this model was trained for proposes methods for similarity of scientific abstracts, this model is evaluated on information retrieval datasets with document level queries. The datasets used for the paper include RELISH (biomedical/English), TRECCOVID (biomedical/English), and CSFCube (computer science/English). These are all detailed on [github](https://github.com/allenai/aspire) and in our [paper](https://arxiv.org/abs/2111.08366). RELISH and TRECCOVID represent a abstract level retrieval task, where given a query scientific abstract the task requires the retrieval of relevant candidate abstracts. CSFCube presents a slightly different task and presents a set of finer-grained sentences in the abstract based on which a finer-grained retrieval must be made. This task represents the closest task to a sentence similarity task.

In using this sentence level model for abstract level retrieval we rank documents by the minimal L2 distance between the sentences in the query and candidate abstract.

**Evaluation results:**

The released model `aspire-sentence-embedder` is compared against 1) `all-mpnet-base-v2` a sentence-bert model trained on ~1 billion training examples, 2) `paraphrase-TinyBERT-L6-v2` a sentence-bert model trained on paraphrase pairs, and 3) the `cosentbert` models used in our paper.

|                                            | CSFCube aggregated |   CSFCube aggregated     | TRECCOVID  |    TRECCOVID    | RELISH  |     RELISH   |
|-------------------------------------------:|:------------------:|:-------:|:---------:|:-------:|:------:|:-------:|
|                                            |         MAP        | NDCG%20 |    MAP    | NDCG%20 |   MAP  | NDCG%20 |
|                `all-mpnet-base-v2` |        34.64       |  54.94  |   17.35   |  43.87  |  52.92 |  69.69  |
| `paraphrase-TinyBERT-L6-v2` |        26.77       |  48.57  |   11.12   |  34.85  |  50.80 |  67.35  |
|                                 `cosentbert` |        28.95       |  50.68  |   12.80   |  38.07  |  50.04 |  66.35  |
|                   `aspire-sentence-embedder` |        30.58       |  53.86  |   11.64   |  36.50  |  50.36 |  66.63  |

The released model sees similar performance across datasets to the per-domain `cosentbert` models used in our paper (and reported above).