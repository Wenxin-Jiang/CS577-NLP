---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: Graphcore/bert-base-uncased-squad
  results: []
---

# Graphcore/bert-base-uncased-squad

Optimum Graphcore is a new open-source library and toolkit that enables developers to access IPU-optimized models certified by Hugging Face. It is an extension of Transformers, providing a set of performance optimization tools enabling maximum efficiency to train and run models on Graphcore’s IPUs - a completely new kind of massively parallel processor to accelerate machine intelligence. Learn more about how to take train Transformer models faster with IPUs at [hf.co/hardware/graphcore](https://huggingface.co/hardware/graphcore).

Through HuggingFace Optimum, Graphcore released ready-to-use IPU-trained model checkpoints and IPU configuration files to make it easy to train models with maximum efficiency in the IPU. Optimum shortens the development lifecycle of your AI models by letting you plug-and-play any public dataset and allows a seamless integration to our State-of-the-art hardware giving you a quicker time-to-value for your AI project.

## Model description

BERT (Bidirectional Encoder Representations from Transformers) is a transformers model which is designed to pretrain bidirectional representations from unlabelled texts. It enables easy and fast fine-tuning for different downstream tasks such as Sequence Classification, Named Entity Recognition, Question Answering, Multiple Choice and MaskedLM. 

It was trained with two objectives in pretraining : Masked language modelling (MLM) and Next sentence prediction(NSP). First, MLM is different from traditional LM which sees the words one after another while BERT allows the model to learn a bidirectional representation.  In addition to MLM, NSP is used for jointly pertaining text-pair representations.

It reduces the need of many engineering efforts for building task specific architectures through pre-trained representation. And achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks.


## Intended uses & limitations

This model is a fine-tuned version of [Graphcore/bert-base-uncased](https://huggingface.co/Graphcore/bert-base-uncased) on the squad dataset.

## Training and evaluation data

Trained on squad dataset:

- [HuggingFace/squad](https://huggingface.co/datasets/squad)

## Training procedure

Model was trained on 16 Graphcore Mk2 IPUs using the [optimum-graphcore](https://github.com/huggingface/optimum-graphcore) library.

Command line:

```
python examples/question-answering/run_qa.py \
  --model_name_or_path Graphcore/bert-base-uncased \
  --ipu_config_name Graphcore/bert-base-ipu \
  --dataset_name squad \
  --do_train \
  --do_eval \
  --num_train_epochs 3 \
  --per_device_train_batch_size 2 \
  --per_device_eval_batch_size 2 \
  --gradient_accumulation_steps 16 \
  --pod_type pod16 \
  --learning_rate 9e-5 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --seed 42\
  --lr_scheduler_type linear \
  --loss_scaling 64 \
  --weight_decay 0.01 \
  --warmup_ratio 0.2 \
  --logging_steps 1 \
  --save_steps 50 \
  --dataloader_num_workers 64 \
  --ipu_config_overrides "embedding_serialization_factor=2" \
  --output_dir squad_v2_bert_base \
  --overwrite_output_dir
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 256
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0
- training precision: Mixed Precision

### Training results

```
{ 
    "epoch": 3.0,
    "eval_exact_match": 81.79754020813624,
    "eval_f1": 88.84840994541061,
    "eval_samples": 10784
}
```


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 1.18.4
- Tokenizers 0.11.6
