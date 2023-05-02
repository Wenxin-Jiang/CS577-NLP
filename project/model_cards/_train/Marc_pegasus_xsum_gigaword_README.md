---
language: 
- English
-
thumbnail: 
tags:
- 
-
- 
license: 
datasets:
- XSUM 
- Gigaword
metrics:
- Rouge
-
---

# Pegasus XSUM Gigaword

## Model description

Pegasus XSUM model finetuned to Gigaword Summarization task, significantly better performance than pegasus gigaword, but still doesn't match model paper performance.  

## Intended uses & limitations
Produces short summaries with the coherence of the XSUM Model
#### How to use

```python
# You can include sample code which will be formatted
```

#### Limitations and bias

Still has all the biases of any of the abstractive models, but seems a little less prone to hallucination. 
## Training data

Initialized with pegasus-XSUM

## Training procedure

Trained for 11500 iterations on Gigaword corpus using OOB seq2seq (from hugging face using the default parameters)

## Eval results
Evaluated on Gigaword test set (from hugging face using the default parameters)
run_summarization.py     --model_name_or_path pegasus-xsum/checkpoint-11500/   --do_predict   --dataset_name gigaword   --dataset_config "3.0.0"     --source_prefix "summarize: "     --output_dir  pegasus-xsum    --per_device_train_batch_size=8     --per_device_eval_batch_size=8     --overwrite_output_dir     --predict_with_generate

| Metric      | Score |
| ----------- | ----------- |
| eval_rouge1 | 34.1958   |
| eval_rouge2 | 15.4033   |
| eval_rougeL | 31.4488  |


run_summarization.py     --model_name_or_path google/pegasus-gigaword   --do_predict   --dataset_name gigaword   --dataset_config "3.0.0"     --source_prefix "summarize: "     --output_dir  pegasus-xsum    --per_device_train_batch_size=8     --per_device_eval_batch_size=8     --overwrite_output_dir     --predict_with_generate

| Metric      | Score |
| ----------- | ----------- |
| eval_rouge1 | 20.8111   |
| eval_rouge2 | 8.766   |
| eval_rougeL | 18.4431  |


### BibTeX entry and citation info

```bibtex
@inproceedings{...,
  year={2020}
}
```
