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

**Note**: In the context of the paper, this model is referred to as `Specter-CoCite_Spec` and represents a baseline bi-encoder for scientific document similarity. This model is similar in architecture to the [`allenai/specter`](https://github.com/allenai/specter) model but is trained on co-citation data instead of citation data.

## Model Card

### Model description

This model is a BERT bi-encoder model trained for similarity of title-abstract pairs in biomedical scientific papers. The model is **initialized with the SPECTER model**. This model inputs the title and abstract of a paper and represents it with a single vector obtained by a scalar mix of the CLS token at every layer of the base encoder. These scalar mix parameters can be important for performance in some datasets. Importantly, these scalar mix weights are not included as part of this HF model, if you wish to use these parameters please download the full model at: [`aspire-biencoder-compsci-spec-full.zip`](https://drive.google.com/file/d/1AHtzyEpyn7DeFYOdt86ik4n0tGaG5kMC/view?usp=sharing).

### Training data 

The model is trained on pairs of co-cited papers in a contrastive learning setup. The model is trained on 1.2 million biomedical paper pairs. In training the model negative examples for the contrastive loss are obtained as random in-batch negatives. Co-citations are obtained from the full text of papers, for example - the papers in brackets below are all co-cited and each pairs title and abstracts would be used as a training pair:

> The idea of distant supervision has been proposed and used widely in Relation Extraction (Mintz et al., 2009; Riedel et al., 2010; Hoffmann et al., 2011; Surdeanu et al., 2012) , where the source of labels is an external knowledge base.


### Training procedure

The model was trained with the Adam Optimizer and a learning rate of 2e-5 with 1000 warm-up steps followed by linear decay of the learning rate. The model training convergence is checked with the loss on a held out dev set consisting of co-cited paper pairs.

### Intended uses & limitations

This model is trained for document similarity tasks in **computer science** scientific text using a single vector per document. Here, the documents are the title and abstract of a paper. With appropriate fine-tuning the model can also be used for other tasks such as classification. Since the training data comes primarily from computer science, performance on other domains may be poorer.

### How to use

Follow instructions for use detailed on the model github repo: https://github.com/allenai/aspire#specter-cocite

### Variable and metrics
This model is evaluated on information retrieval datasets with document level queries. Performance here is reported on CSFCube (computer science/English). This is detailed on [github](https://github.com/allenai/aspire) and in our [paper](https://arxiv.org/abs/2111.08366). CSFCube presents a finer-grained query via selected sentences in a query abstract based on which a finer-grained retrieval must be made from candidate abstracts. The bi-encoder above ignores the finer grained query sentences and uses the whole abstract - this presents a baseline in the paper.

We rank documents by the L2 distance between the query and candidate documents.

### Evaluation results

The released model `aspire-biencoder-compsci-spec` (and `aspire-biencoder-compsci-spec-full`) is compared against `allenai/specter`. `aspire-biencoder-compsci-spec-full`<sup>*</sup> is the performance reported in our paper by averaging over 3 re-runs of the model. The released models `aspire-biencoder-compsci-spec` and `aspire-biencoder-compsci-spec-full` are the single best run among the 3 re-runs.

|                                             | CSFCube aggregated |    CSFCube aggregated|
|--------------------------------------------:|:---------:|:-------:|
|                                             |    MAP    | NDCG%20 |
|                               `specter`     |   34.23   | 53.28   |
| `aspire-biencoder-compsci-spec-full`<sup>*</sup> |  37.90    | 58.16   |
|             `aspire-biencoder-compsci-spec` |  37.17    | 57.91   |
|        `aspire-biencoder-compsci-spec-full` |  37.67    | 59.26   |


**Alternative models:**

Besides the above models consider these alternative models also released in the Aspire paper:

[`aspire-biencoder-biomed-scib`](https://huggingface.co/allenai/aspire-biencoder-biomed-scib): If you wanted to run on biomedical papers.
