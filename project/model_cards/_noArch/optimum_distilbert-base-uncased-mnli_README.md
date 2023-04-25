---
language: en
pipeline_tag: zero-shot-classification
tags:
- distilbert
datasets:
- multi_nli
metrics:
- accuracy
---

# ONNX convert typeform/distilbert-base-uncased-mnli

## Conversion of [typeform/distilbert-base-uncased-mnli](typeform/distilbert-base-uncased-mnli)



This is the [uncased DistilBERT model](https://huggingface.co/distilbert-base-uncased) fine-tuned on [Multi-Genre Natural Language Inference](https://huggingface.co/datasets/multi_nli) (MNLI) dataset for the zero-shot classification task. The model is not case-sensitive, i.e., it does not make a difference between "english" and "English".

## Training

Training is done on a [p3.2xlarge](https://aws.amazon.com/ec2/instance-types/p3/) AWS EC2 instance (1 NVIDIA Tesla V100 GPUs), with the following hyperparameters:

```
$ run_glue.py \
    --model_name_or_path distilbert-base-uncased \
    --task_name mnli \
    --do_train \
    --do_eval \
    --max_seq_length 128 \
    --per_device_train_batch_size 16 \
    --learning_rate 2e-5 \
    --num_train_epochs 5 \
    --output_dir /tmp/distilbert-base-uncased_mnli/
```

## Evaluation results

| Task | MNLI | MNLI-mm |
|:----:|:----:|:----:|
|      | 82.0 | 82.0 |