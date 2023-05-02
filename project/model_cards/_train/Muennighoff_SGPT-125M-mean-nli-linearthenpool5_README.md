---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# SGPT-125M-mean-nli-linearthenpool5

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to our paper: https://arxiv.org/abs/2202.08904

## Training
The model was trained with the parameters:

**DataLoader**:

`sentence_transformers.datasets.NoDuplicatesDataLoader.NoDuplicatesDataLoader` of length 8807 with parameters:
```
{'batch_size': 64}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 1,
    "evaluation_steps": 880,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 881,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 75, 'do_lower_case': False}) with Transformer model: GPTNeoModel 
  (1): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU', 'key_name': 'token_embeddings'})
  (2): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU', 'key_name': 'token_embeddings'})
  (3): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU', 'key_name': 'token_embeddings'})
  (4): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU', 'key_name': 'token_embeddings'})
  (5): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU', 'key_name': 'token_embeddings'})
  (6): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False})
)
```

## Citing & Authors

```bibtex
@article{muennighoff2022sgpt,
  title={SGPT: GPT Sentence Embeddings for Semantic Search},
  author={Muennighoff, Niklas},
  journal={arXiv preprint arXiv:2202.08904},
  year={2022}
}
```
