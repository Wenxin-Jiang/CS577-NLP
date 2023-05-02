---
language:
- multilingual
tags:
- question-answering
datasets:
- squad2
metrics:
- squad2
---

# Rembert Squad2
This model is finetuned for QA task on Squad2 from [Rembert checkpoint](https://huggingface.co/google/rembert).

## Hyperparameters
```
Batch Size: 4
Grad Accumulation Steps = 8
Total epochs = 3
MLM Checkpoint = "rembert"
max_seq_len = 256
learning_rate = 1e-5
lr_schedule = LinearWarmup
warmup_ratio = 0.1
doc_stride = 128
```

## Squad 2 Evaluation stats:

Metrics generated from [the official Squad2 evaluation script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/)
```json
{
  "exact": 84.51107554956624,
  "f1": 87.46644042781853,
  "total": 11873,
  "HasAns_exact": 80.97165991902834,
  "HasAns_f1": 86.89086491219469,
  "HasAns_total": 5928,
  "NoAns_exact": 88.04037005887301,
  "NoAns_f1": 88.04037005887301,
  "NoAns_total": 5945
}
```
For any questions, you can reach out to me [on Twitter](https://twitter.com/batw0man)