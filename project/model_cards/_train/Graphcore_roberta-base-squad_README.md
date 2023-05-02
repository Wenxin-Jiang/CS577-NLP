---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: Graphcore/roberta-base-squad
  results: []
---


# Graphcore/roberta-base-squad

BERT (Bidirectional Encoder Representations from Transformers) is a transformers model which is designed to pretrain bidirectional representations from unlabelled texts. It enables easy and fast fine-tuning for different downstream tasks such as Sequence Classification, Named Entity Recognition, Question Answering, Multiple Choice and MaskedLM. 

It was trained with two objectives in pretraining : Masked language modelling (MLM) and Next sentence prediction(NSP). First, MLM is different from traditional LM which sees the words one after another while BERT allows the model to learn a bidirectional representation.  In addition to MLM, NSP is used for jointly pertaining text-pair representations.

It reduces the need of many engineering efforts for building task specific architectures through pre-trained representation. And achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks.


## Model description

RoBERTa is based on BERT pretraining approach and improves on it by carefully evaluating a number of design decisions of BERT pretraining which it found to cause the model to be undertrained. 

It suggested a way to improve the performance by training the model longer, with bigger batches over more data, removing the next sentence prediction objectives, training on longer sequences and dynamically changing the mask pattern applied to the training data.

As a result, it achieved state-of-the-art results on GLUE, RACE and SQuAD.


Paper link : [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/pdf/1907.11692.pdf)

## Intended uses & limitations

This model is a fine-tuned version of [HuggingFace/roberta-base](https://huggingface.co/roberta-base) on the SQuAD dataset.

## Training and evaluation data

Trained and evaluated on the SQuAD dataset:
- [HuggingFace/squad ](https://huggingface.co/datasets/squad).

## Training procedure

Trained on 16 Graphcore Mk2 IPUs using [optimum-graphcore](https://github.com/huggingface/optimum-graphcore).

Command line:

```
python examples/question-answering/run_qa.py \
  --ipu_config_name Graphcore/roberta-base-ipu \
  --model_name_or_path roberta-base \
  --dataset_name squad \
  --do_train \
  --do_eval \
  --num_train_epochs 2 \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 2 \
  --pod_type pod16 \
  --learning_rate 6e-5 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --seed 1984 \
  --lr_scheduler_type linear \
  --loss_scaling 64 \
  --weight_decay 0.01 \
  --warmup_ratio 0.25 \
  --logging_steps 1 \
  --save_steps -1 \
  --dataloader_num_workers 64 \
  --output_dir squad_roberta_base \
  --overwrite_output_dir \
  --push_to_hub
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 4
- eval_batch_size: 2
- seed: 1984
- distributed_type: IPU
- total_train_batch_size: 256
- total_eval_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.25
- num_epochs: 2.0
- training precision: Mixed Precision

### Training results

```
***** train metrics *****
  epoch                    =        2.0
  train_loss               =     1.2528
  train_runtime            = 0:02:14.50
  train_samples            =      88568
  train_samples_per_second =   1316.952
  train_steps_per_second   =       5.13

***** eval metrics *****
  epoch            =     2.0
  eval_exact_match = 85.2696
  eval_f1          = 91.7455
  eval_samples     =   10790
```

### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 2.0.0
- Tokenizers 0.11.6
