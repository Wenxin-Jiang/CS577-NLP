XLM-RoBERTa base (`xlm-roberta-base`) finetuned on squad v1.1.

**Training-specifications:**

- training_epochs: 3.0
- max_seq_length: 384
- batch_size: 16
- dataset_name: squad
- doc_stride 128 


**Train-results:**

```
{
    "epoch": 3.0,
    "init_mem_cpu_alloc_delta": 991453184,
    "init_mem_cpu_peaked_delta": 0,
    "init_mem_gpu_alloc_delta": 1109893120,
    "init_mem_gpu_peaked_delta": 0,
    "train_mem_cpu_alloc_delta": 14753792,
    "train_mem_cpu_peaked_delta": 0,
    "train_mem_gpu_alloc_delta": 3330195456,
    "train_mem_gpu_peaked_delta": 8287144960,
    "train_runtime": 11376.3034,
    "train_samples": 89597,
    "train_samples_per_second": 1.477
}
```

**Eval-results:**

```
{
    "epoch": 3.0,
    "eval_samples": 10918,
    "exact_match": 82.06244087038789,
    "f1": 89.09539709124654
}
```

