---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: roberta-base-squad2
  results: []
---

# Graphcore/roberta-base-squad2


Optimum Graphcore is a new open-source library and toolkit that enables developers to access IPU-optimized models certified by Hugging Face. It is an extension of Transformers, providing a set of performance optimization tools enabling maximum efficiency to train and run models on Graphcore’s IPUs - a completely new kind of massively parallel processor to accelerate machine intelligence. Learn more about how to take train Transformer models faster with IPUs at [hf.co/hardware/graphcore](https://huggingface.co/hardware/graphcore).

Through HuggingFace Optimum, Graphcore released ready-to-use IPU-trained model checkpoints and IPU configuration files to make it easy to train models with maximum efficiency in the IPU. Optimum shortens the development lifecycle of your AI models by letting you plug-and-play any public dataset and allows a seamless integration to our State-of-the-art hardware giving you a quicker time-to-value for your AI project.


## Model description

RoBERTa is based on BERT pretraining approach and improves on it by carefully evaluating a number of design decisions of BERT pretraining which it found to cause the model to be undertrained. 

It suggested a way to improve the performance by training the model longer, with bigger batches over more data, removing the next sentence prediction objectives, training on longer sequences and dynamically changing the mask pattern applied to the training data.

As a result, it achieved state-of-the-art results on GLUE, RACE and SQuAD.


Paper link : [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/pdf/1907.11692.pdf)

## Intended uses & limitations

This model is a fine-tuned version of [HuggingFace/roberta-base](https://huggingface.co/roberta-base) on the squad_v2 dataset.

## Training and evaluation data

Trained and evaluated on the SQuAD v2 dataset:
- [HuggingFace/squad_v2](https://huggingface.co/datasets/squad_v2).

## Training procedure

Trained on 16 Graphcore Mk2 IPUs using [optimum-graphcore](https://github.com/huggingface/optimum-graphcore).

Command line:

```
python examples/question-answering/run_qa.py \
  --ipu_config_name Graphcore/roberta-base-ipu \
  --model_name_or_path roberta-base \
  --dataset_name squad_v2 \
  --version_2_with_negative \
  --do_train \
  --do_eval \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 2 \
  --pod_type pod16 \
  --learning_rate 7e-5 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --seed 1984 \
  --lr_scheduler_type linear \
  --loss_scaling 64 \
  --weight_decay 0.01 \
  --warmup_ratio 0.2 \
  --logging_steps 1 \
  --save_steps -1 \
  --dataloader_num_workers 64 \
  --output_dir roberta-base-squad2 \
  --overwrite_output_dir \
  --push_to_hub
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 4
- eval_batch_size: 2
- seed: 1984
- distributed_type: IPU
- total_train_batch_size: 256
- total_eval_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 3.0
- training precision: Mixed Precision

### Training results

```
***** train metrics *****
  epoch                    =        3.0
  train_loss               =     0.9982
  train_runtime            = 0:04:44.21
  train_samples            =     131823
  train_samples_per_second =    1391.43
  train_steps_per_second   =      5.425

***** eval metrics *****
  epoch                  =     3.0
  eval_HasAns_exact      = 78.1208
  eval_HasAns_f1         = 84.6569
  eval_HasAns_total      =    5928
  eval_NoAns_exact       = 82.0353
  eval_NoAns_f1          = 82.0353
  eval_NoAns_total       =    5945
  eval_best_exact        = 80.0809
  eval_best_exact_thresh =     0.0
  eval_best_f1           = 83.3442
  eval_best_f1_thresh    =     0.0
  eval_exact             = 80.0809
  eval_f1                = 83.3442
  eval_samples           =   12165
  eval_total             =   11873
```

### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 2.0.0
- Tokenizers 0.11.6
