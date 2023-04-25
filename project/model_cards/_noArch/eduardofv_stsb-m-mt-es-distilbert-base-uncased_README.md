---
language: es
datasets:
- stsb_multi_mt
tags:
- sentence-similarity
- sentence-transformers
---
# distilbert-base-uncased trained for Semantic Textual Similarity in Spanish

This is a test model that was fine-tuned using the Spanish datasets from [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt) in order to understand and benchmark STS models.

## Model and training data description

This model was built taking `distilbert-base-uncased` and training it on a Semantic Textual Similarity task using a modified version of the training script for STS from Sentece Transformers (the modified script is included in the repo). It was trained using the Spanish datasets from [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt) which are the STSBenchmark datasets automatically translated to other languages using deepl.com. Refer to the dataset repository for more details.

## Intended uses & limitations

This model was built just as a proof-of-concept on STS fine-tuning using Spanish data and no specific use other than getting a sense on how this training works.

## How to use

You may use it as any other STS trained model to extract sentence embeddings. Check Sentence Transformers documentation. 

## Training procedure

Use the included script to train in Spanish the base model. You can also try to train another model passing it's reference as first argument. You can also train in some other language of those included in the training dataset.

## Evaluation results

Evaluating `distilbert-base-uncased` on the Spanish test dataset before training results in:

```
Cosine-Similarity :	Pearson: 0.2980	Spearman: 0.4008
```

While the fine-tuned version with the defaults of the training script and the Spanish training dataset results in:

```
Cosine-Similarity :	Pearson: 0.7451	Spearman: 0.7364
```

In our [STS Evaluation repository](https://github.com/eduardofv/sts_eval) we compare the performance of this model with other models from Sentence Transformers and Tensorflow Hub using the standard STSBenchmark and the 2017 STSBenchmark Task 3 for Spanish.


## Resources

- Training dataset [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)
- Sentence Transformers [Semantic Textual Similarity](https://www.sbert.net/examples/training/sts/README.html)
- Check [sts_eval](https://github.com/eduardofv/sts_eval) for a comparison with Tensorflow and Sentence-Transformers models
- Check the [development environment to run the scripts and evaluation](https://github.com/eduardofv/ai-denv)
