---
language: en
license: apache-2.0
datasets:
- conll2003
model-index:
- name: elastic/distilbert-base-uncased-finetuned-conll03-english
  results:
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: validation
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9854480753649896
      verified: true
    - name: Precision
      type: precision
      value: 0.9880928983228512
      verified: true
    - name: Recall
      type: recall
      value: 0.9895677847945542
      verified: true
    - name: F1
      type: f1
      value: 0.9888297915932504
      verified: true
    - name: loss
      type: loss
      value: 0.06707527488470078
      verified: true
---

[DistilBERT base uncased](https://huggingface.co/distilbert-base-uncased), fine-tuned for NER using the [conll03 english dataset](https://huggingface.co/datasets/conll2003). Note that this model is **not** sensitive to capital letters — "english" is the same as "English". For the case sensitive version, please use [elastic/distilbert-base-cased-finetuned-conll03-english](https://huggingface.co/elastic/distilbert-base-cased-finetuned-conll03-english).

## Versions

- Transformers version: 4.3.1
- Datasets version: 1.3.0

## Training

```
$ run_ner.py \
  --model_name_or_path distilbert-base-uncased \
  --label_all_tokens True \
  --return_entity_level_metrics True \
  --dataset_name conll2003 \
  --output_dir /tmp/distilbert-base-uncased-finetuned-conll03-english \
  --do_train \
  --do_eval
```

After training, we update the labels to match the NER specific labels from the
dataset [conll2003](https://raw.githubusercontent.com/huggingface/datasets/1.3.0/datasets/conll2003/dataset_infos.json)
