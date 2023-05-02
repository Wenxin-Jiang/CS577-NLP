[roberta-base](https://huggingface.co/roberta-base) fine-tuned on the [SQuAD2](https://rajpurkar.github.io/SQuAD-explorer) dataset for 2 epochs. 

The fine-tuning process was performed on a single NVIDIA Tesla T4 GPU (15GB). The hyperparameters are:

```
max_seq_length=512
per_device_train_batch_size=8
gradient_accumulation_steps=4
total train batch size (w. parallel, distributed & accumulation) = 32
learning_rate=3e-5
```

## Evaluation results

```
"eval_exact": 80.33352985766024,
"eval_f1": 83.38322909593009,

"eval_HasAns_exact": 77.81713900134953,
"eval_HasAns_f1": 83.925283241562,
"eval_HasAns_total": 5928,
"eval_NoAns_exact": 82.84272497897393,
"eval_NoAns_f1": 82.84272497897393,
"eval_NoAns_total": 5945,
"eval_best_exact": 80.33352985766024,
"eval_best_exact_thresh": 0.0,
"eval_best_f1": 83.38322909593005,
"eval_best_f1_thresh": 0.0,
"eval_samples": 11955,
"eval_total": 11873,
```

## More information

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering. (https://rajpurkar.github.io/SQuAD-explorer/)