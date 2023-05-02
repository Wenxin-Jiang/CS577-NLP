---
license: afl-3.0
---
A MacBERTh model fine-tuned on SQuAD_v2. Hopefully, this will allow the model to perform well on QA tasks on historical texts.
Finetune parameters:

```
training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=3e-5,
        per_device_train_batch_size=64,
        per_device_eval_batch_size=64,
        num_train_epochs=2,
        weight_decay=0.01,
        lr_scheduler_type=SchedulerType.LINEAR,
        warmup_ratio=0.2
    )
```

Evaluation metrics on the validation set of SQuAD_v2:
```
{'exact': 49.49886296639434, 'f1': 53.9199170778635, 'total': 11873, 'HasAns_exact': 60.08771929824562, 'HasAns_f1': 68.94250598270429, 'HasAns_total': 5928, 'NoAns_exact': 38.940285954583686, 'NoAns_f1': 38.940285954583686, 'NoAns_total': 5945, 'best_exact': 50.5095595047587, 'best_exact_thresh': 0.0, 'best_f1': 51.75825524534494, 'best_f1_thresh': 0.0}
```