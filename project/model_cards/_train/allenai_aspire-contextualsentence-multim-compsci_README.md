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

**Note**: In the context of the paper, this model is referred to as `tsAspire` and represents the papers proposed multi-vector model for fine-grained scientific document similarity.

## Model Card

### Model description

This model is a BERT based multi-vector model trained for fine-grained similarity of computer science papers. This model inputs the title and abstract of a paper and represents a paper with a contextual sentence vectors obtained by averaging the token representations of individual sentences - the whole title and abstract are encoded with cross-attention in the encoder block before obtaining sentence embeddings. The model is trained by minimizing an Wasserstein/Earth Movers Distance between sentence vectors for a pair of documents - in the process also learning a sparse alignment between sentences in both documents. Test time behavior ranks documents based on the Wasserstein Distance between all sentences of documents or a set of query sentences and a candidate documents sentences.

### Training data 

The model is trained on pairs of co-cited papers with their sentences aligned by the co-citation context in a contrastive learning setup. The model is trained on 1.2 million computer science paper pairs. In training the model, negative examples for the contrastive loss are obtained as random in-batch negatives. Co-citations are obtained from the full text of papers. For example - the papers in brackets below are all co-cited and each pair of papers would be used as a training pair:

> The idea of distant supervision has been proposed and used widely in Relation Extraction (Mintz et al., 2009; Riedel et al., 2010; Hoffmann et al., 2011; Surdeanu et al., 2012) , where the source of labels is an external knowledge base.


### Training procedure

The model was trained with the Adam Optimizer and a learning rate of 2e-5 with 1000 warm-up steps followed by linear decay of the learning rate. The model training convergence is checked with the loss on a held out dev set consisting of co-cited paper pairs.

### Intended uses & limitations

This model is trained for fine-grained document similarity tasks in **computer science** scientific text using multiple vectors per document. The model allows _multiple_ fine grained sentence-to-sentence similarities between documents. The model is well suited to an aspect conditional task formulation where a query might consist of sentence_s_ in a query document and candidates must be retrieved along the specified sentences. Here, the documents are the title and abstract of a paper. With appropriate fine-tuning the model can also be used for other tasks such as document or sentence level classification. Since the training data comes primarily from computer science, performance on other domains may be poorer.

### How to use

This model can be used via the `transformers` library, and some additional code to compute contextual sentence vectors and to make multiple matches using optimal transport.

View example usage and sample document matches in the model github repo: [`examples/demo-contextualsentence-multim.ipynb`](https://github.com/allenai/aspire/blob/main/examples/demo-contextualsentence-multim.ipynb)

### Variable and metrics
This model is evaluated on information retrieval datasets with document level queries. Performance here is reported on CSFCube (computer science/English). This is detailed on [github](https://github.com/allenai/aspire) and in our [paper](https://arxiv.org/abs/2111.08366). CSFCube presents a finer-grained query via selected sentences in a query abstract based on which a finer-grained retrieval must be made from candidate abstracts.

In using this model we rank documents by the Wasserstein distance between the query sentences and a candidates sentences.

### Evaluation results

The released model `aspire-contextualsentence-multim-compsci` is compared against `allenai/specter`, a bi-encoder baseline and `all-mpnet-base-v2` a strong non-contextual sentence-bert baseline model trained on ~1 billion training examples. `aspire-contextualsentence-multim-compsci`<sup>*</sup> is the performance reported in our paper by averaging over 3 re-runs of the model. The released models `aspire-contextualsentence-multim-compsci` is the single best run among the 3 re-runs.

|                                             | CSFCube aggregated |    CSFCube aggregated|
|--------------------------------------------:|:---------:|:-------:|
|                                             |    MAP    | NDCG%20 |
|                     `all-mpnet-base-v2`     |    34.64   |  54.94  |
|                               `specter`     |    34.23   |  53.28  |
| `aspire-contextualsentence-multim-compsci`<sup>*</sup> |   40.79   |  61.41  |
| `aspire-contextualsentence-multim-compsci` |     41.24 |  61.81 |



**Alternative models:**

Besides the above models consider these alternative models also released in the Aspire paper:

[`aspire-contextualsentence-multim-biomed`](https://huggingface.co/allenai/aspire-contextualsentence-multim-biomed): If you wanted to run on biomedical papers and want to use a model trained to match _multiple_ sentences between documents.

[`aspire-contextualsentence-singlem-biomed`](https://huggingface.co/allenai/aspire-contextualsentence-singlem-biomed): If you wanted to run on biomedical papers and want to use a model trained to match _single_ sentences between documents.

[`aspire-contextualsentence-singlem-compsci`](https://huggingface.co/allenai/aspire-contextualsentence-singlem-compsci): If you wanted to run on computer science papers and want to use a model trained to match _single_ sentences between documents.