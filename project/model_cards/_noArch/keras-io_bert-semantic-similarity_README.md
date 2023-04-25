---
library_name: keras
tags:
 - sentence-similarity
---

## Model description

This repo contains the model and the notebook for fine-tuning BERT model on SNLI Corpus for Semantic Similarity. [Semantic Similarity with BERT](https://keras.io/examples/nlp/semantic_similarity_with_bert/).

Full credits go to [Mohamad Merchant](https://twitter.com/mohmadmerchant1)

Reproduced by [Vu Minh Chien](https://www.linkedin.com/in/vumichien/)

Motivation: Semantic Similarity determines how similar two sentences are, in terms of their meaning. In this tutorial, we can fine-tune BERT model and use it to predict the similarity score for two sentences.

## Training and evaluation data

This example demonstrates the use of the Stanford Natural Language Inference (SNLI) Corpus to predict semantic sentence similarity with Transformers.

- Total train samples: 100000

- Total validation samples: 10000

- Total test samples: 10000

Here are the "similarity" label values in SNLI dataset:

- Contradiction: The sentences share no similarity.

- Entailment: The sentences have a similar meaning.

- Neutral: The sentences are neutral.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | 9.999999747378752e-06 |
| decay | 0.0 |
| beta_1 | 0.8999999761581421 |
| beta_2 | 0.9990000128746033 |
| epsilon | 1e-07 |
| amsgrad | False |
| training_precision | float32 |


 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>