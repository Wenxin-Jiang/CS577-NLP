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

This model is a BERT bi-encoder model trained for similarity of title-abstract pairs in biomedical scientific papers. The model is **initialized with the SPECTER encoder**. This model inputs the title and abstract of a paper and represents it with a single vector obtained by a scalar mix of the CLS token at every layer of the base encoder. These scalar mix parameters can be important for performance in some datasets. Importantly, these scalar mix weights are not included as part of this HF model, if you wish to use these parameters please download the full model at: [`aspire-biencoder-biomed-spec-full.zip`](https://drive.google.com/file/d/1MDCv9Fc33eP015HTWKi50WYXixh72h5c/view?usp=sharing).

### Training data 

The model is trained on pairs of co-cited papers in a contrastive learning setup. The model is trained on 1.2 million biomedical paper pairs. In training the model negative examples for the contrastive loss are obtained as random in-batch negatives. Co-citations are obtained from the full text of papers, for example - the papers in brackets below are all co-cited and each pairs title and abstracts would be used as a training pair:

> The idea of distant supervision has been proposed and used widely in Relation Extraction (Mintz et al., 2009; Riedel et al., 2010; Hoffmann et al., 2011; Surdeanu et al., 2012) , where the source of labels is an external knowledge base.


### Training procedure

The model was trained with the Adam Optimizer and a learning rate of 1e-5 with 1000 warm-up steps followed by linear decay of the learning rate. The model training convergence is checked with the loss on a held out dev set consisting of co-cited paper pairs.

### Intended uses & limitations

This model is trained for document similarity tasks in **biomedical** scientific text using a single vector per document. Here, the documents are the title and abstract of a paper. With appropriate fine-tuning the model can also be used for other tasks such as classification. Since the training data comes primarily from biomedicine, performance on other domains may be poorer.

### How to use

Follow instructions for use detailed on the model github repo: https://github.com/allenai/aspire#specter-cocite

### Variable and metrics
This model is evaluated on information retrieval datasets with document level queries. Here we report performance on RELISH (biomedical/English), and TRECCOVID (biomedical/English). These are detailed on [github](https://github.com/allenai/aspire) and in our [paper](https://arxiv.org/abs/2111.08366). These datasets represent a abstract level retrieval task, where given a query scientific abstract the task requires the retrieval of relevant candidate abstracts. 

We rank documents by the L2 distance between the query and candidate documents.

### Evaluation results

The released model `aspire-biencoder-biomed-spec` (and `aspire-biencoder-biomed-spec-full`) is compared against `allenai/specter`. `aspire-biencoder-biomed-spec-full`<sup>*</sup> is the performance reported in our paper by averaging over 3 re-runs of the model. The released models `aspire-biencoder-biomed-spec` and `aspire-biencoder-biomed-spec-full` are the single best run among the 3 re-runs.

|                                            | TRECCOVID  |    TRECCOVID    | RELISH  |     RELISH   |
|-------------------------------------------:|:---------:|:-------:|:------:|:-------:|
|                                            |    MAP    | NDCG%20 |   MAP  | NDCG%20 |
|                               `specter`    |    28.24  | 59.28   |   60.62| 77.20   |
| `aspire-biencoder-biomed-spec-full`<sup>*</sup> |    28.59  | 60.07   |   61.43| 77.96   |
|             `aspire-biencoder-biomed-spec` |    26.07  | 54.89   |   61.47| 78.34   |
|        `aspire-biencoder-biomed-spec-full` |    28.87  | 60.47   |   61.69| 78.22   |

Note that the absence of linear mixing parameters in the `aspire-biencoder-biomed-spec` hurts performance substantially compared to `aspire-biencoder-biomed-spec-full` in TRECCOVID - this dataset contains a larger candidate set than RELISH (~9000 vs 60). Consider the more performant Alternative models below for usage.


**Alternative models:**

Besides the above models consider these alternative models also released in the Aspire paper:

[`aspire-biencoder-compsci-spec`](https://huggingface.co/allenai/aspire-biencoder-compsci-spec): If you wanted to run on computer science papers.

[`aspire-biencoder-biomed-scib`](https://huggingface.co/allenai/aspire-biencoder-biomed-scib): This is an alternative bi-encoder model identical to the above model, except that it is initialized with SciBERT instead of SPECTER. The above model underperforms this model, `allenai/aspire-biencoder-biomed-scib` (even better, `aspire-biencoder-biomed-scib-full`) is recommended for use.