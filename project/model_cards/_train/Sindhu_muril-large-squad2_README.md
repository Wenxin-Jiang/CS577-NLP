# Muril Large Squad2
This model is finetuned for QA task on Squad2 from [Muril Large checkpoint](https://huggingface.co/google/muril-large-cased).

## Hyperparameters
```
Batch Size: 4
Grad Accumulation Steps = 8
Total epochs = 3
MLM Checkpoint = google/muril-large-cased
max_seq_len = 256
learning_rate = 1e-5
lr_schedule = LinearWarmup
warmup_ratio = 0.1
doc_stride = 128
```

## Squad 2 Evaluation stats:
Generated from [the official Squad2 evaluation script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/)

```json
{
  "exact": 82.0180240882675,
  "f1": 85.10110304685352,
  "total": 11873,
  "HasAns_exact": 81.6970310391363,
  "HasAns_f1": 87.87203044454981,
  "HasAns_total": 5928,
  "NoAns_exact": 82.3380992430614,
  "NoAns_f1": 82.3380992430614,
  "NoAns_total": 5945
}
```

## Limitations
MuRIL is specifically trained to work on 18 Indic languages and English. This model is not expected to perform well in any other languages. See the MuRIL checkpoint for further details.

For any questions, you can reach out to me [on Twitter](https://twitter.com/batw0man)