---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- Graphcore/gqa-lxmert
metrics:
- accuracy
model-index:
- name: gqa
  results:
  - task:
      name: Question Answering
      type: question-answering
    dataset:
      name: Graphcore/gqa-lxmert
      type: Graphcore/gqa-lxmert
      args: gqa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5933514030612245
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Graphcore/lxmert-gqa-uncased

BERT (Bidirectional Encoder Representations from Transformers) is a transformers model which is designed to pretrain bidirectional representations from unlabeled texts. It enables easy and fast fine-tuning for different downstream task such as Sequence Classification, Named Entity Recognition, Question Answering, Multiple Choice and MaskedLM. 

It was trained with two objectives in pretraining : Masked language modeling(MLM) and Next sentence prediction(NSP). First, MLM is different from traditional LM which sees the words one after another while BERT allows the model to learn a bidirectional representation.  In addition to MLM, NSP is used for jointly pertaining text-pair representations.

It reduces the need of many engineering efforts for building task specific architectures through pre-trained representation. And achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks.


## Model description

LXMERT is a transformer model for learning vision-and-language cross-modality representations. It has a Transformer model that has three encoders: object relationship encoder, a language encoder, and a cross-modality encoder. It is pretrained via a combination of masked language modelling, visual-language text alignment, ROI-feature regression, masked visual-attribute modeling, masked visual-object modelling, and visual-question answering objectives. It achieves the state-of-the-art results on VQA anad GQA. 

Paper link : [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/pdf/1908.07490.pdf)

## Intended uses & limitations


This model is a fine-tuned version of [unc-nlp/lxmert-base-uncased](https://huggingface.co/unc-nlp/lxmert-base-uncased) on the [Graphcore/gqa-lxmert](https://huggingface.co/datasets/Graphcore/gqa-lxmert) dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9326
- Accuracy: 0.5934

## Training and evaluation data

- [Graphcore/gqa-lxmert](https://huggingface.co/datasets/Graphcore/gqa-lxmert) dataset

## Training procedure

Trained on 16 Graphcore Mk2 IPUs using [optimum-graphcore](https://github.com/huggingface/optimum-graphcore).

Command line:

```
python examples/question-answering/run_vqa.py \
  --model_name_or_path unc-nlp/lxmert-base-uncased \
  --ipu_config_name Graphcore/lxmert-base-ipu \
  --dataset_name Graphcore/gqa-lxmert \
  --do_train \
  --do_eval \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --num_train_epochs 4 \
  --dataloader_num_workers 64 \
  --logging_steps 5 \
  --learning_rate 1e-5 \
  --lr_scheduler_type linear \
  --loss_scaling 16384 \
  --weight_decay 0.01 \
  --warmup_ratio 0.1 \
  --output_dir /tmp/gqa/ \
  --dataloader_drop_last \
  --replace_qa_head \
  --pod_type pod16

```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: IPU
- total_train_batch_size: 64
- total_eval_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4.0
- training precision: Mixed Precision

### Training results
```
***** train metrics *****
  "epoch": 4.0,
  "train_loss": 0.6123406731570221,
  "train_runtime": 29986.2288,
  "train_samples": 943000,
  "train_samples_per_second": 125.791,
  "train_steps_per_second": 1.965

***** eval metrics *****
  "eval_accuracy": 0.5933514030612245,
  "eval_loss": 1.9326171875,
  "eval_samples": 12576,
```


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 2.0.0
- Tokenizers 0.11.6
