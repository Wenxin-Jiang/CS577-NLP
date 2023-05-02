---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
language: en
datasets:
- quora
- embedding-data/WikiAnswers
- flax-sentence-embeddings/stackexchange_xml
license: cc-by-nc-sa-4.0
---

# All-mpnet-base-v2 model fine-tuned for questions clustering 

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

This model is named **all-mpnet-base-questions-clustering-en** since it is a Sentence Transformers model specifically fine-tuned for a questions clustering task. Three public dataset (Quora, WikiAnswer and StackExchange) has been used to enhance the model performance specifically in mapping questions with similar meanings.    

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('aiknowyou/all-mpnet-base-questions-clustering-en')
embeddings = model.encode(sentences)
print(embeddings)
```



## Evaluation Results

The present model has been evaluated by employing a test set belonging to the WikiAnswer dataset. The evaluation results are the following:

[
  {
    "epoch": 1,
    "cossim_accuracy": 0.9931843415744172,
    "cossim_accuracy_threshold": 0.35143423080444336,
    "cossim_f1": 0.9897547191636324,
    "cossim_precision": 0.9913437348280885,
    "cossim_recall": 0.9881707893839572,
    "cossim_f1_threshold": 0.35143423080444336,
    "cossim_ap": 0.9989950013637923,
    "manhattan_accuracy": 0.9934042015236294,
    "manhattan_accuracy_threshold": 24.160316467285156,
    "manhattan_f1": 0.9900818249442103,
    "manhattan_precision": 0.9920113508380628,
    "manhattan_recall": 0.9881597905828264,
    "manhattan_f1_threshold": 24.160316467285156,
    "manhattan_ap": 0.9990576126715013,
    "euclidean_accuracy": 0.9931843415744172,
    "euclidean_accuracy_threshold": 1.1389167308807373,
    "euclidean_f1": 0.9897547191636324,
    "euclidean_precision": 0.9913437348280885,
    "euclidean_recall": 0.9881707893839572,
    "euclidean_f1_threshold": 1.1389167308807373,
    "euclidean_ap": 0.9989921332302106,
    "dot_accuracy": 0.9931843415744172,
    "dot_accuracy_threshold": 0.35143429040908813,
    "dot_f1": 0.9897547191636324,
    "dot_precision": 0.9913437348280885,
    "dot_recall": 0.9881707893839572,
    "dot_f1_threshold": 0.35143429040908813,
    "dot_ap": 0.9989933009226604
  }
]

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 34123 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 51184 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.OnlineContrastiveLoss.OnlineContrastiveLoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 2,
    "evaluation_steps": 0,
    "evaluator": "sentence_transformers.evaluation.SequentialEvaluator.SequentialEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 1000,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 384, 'do_lower_case': False}) with Transformer model: MPNetModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Normalize()
)
```

## Contribution

Thanks to [@tradicio](https://huggingface.co/tradicio) for adding this model.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
