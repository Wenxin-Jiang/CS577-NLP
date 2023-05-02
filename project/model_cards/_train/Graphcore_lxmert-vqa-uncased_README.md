---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- Graphcore/vqa-lxmert
metrics:
- accuracy
model-index:
- name: vqa
  results:
  - task:
      name: Question Answering
      type: question-answering
    dataset:
      name: Graphcore/vqa-lxmert
      type: Graphcore/vqa-lxmert
      args: vqa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7242196202278137
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Graphcore/lxmert-vqa-uncased

Optimum Graphcore is a new open-source library and toolkit that enables developers to access IPU-optimized models certified by Hugging Face. It is an extension of Transformers, providing a set of performance optimization tools enabling maximum efficiency to train and run models on Graphcore’s IPUs - a completely new kind of massively parallel processor to accelerate machine intelligence. Learn more about how to take train Transformer models faster with IPUs at [hf.co/hardware/graphcore](https://huggingface.co/hardware/graphcore).

Through HuggingFace Optimum, Graphcore released ready-to-use IPU-trained model checkpoints and IPU configuration files to make it easy to train models with maximum efficiency in the IPU. Optimum shortens the development lifecycle of your AI models by letting you plug-and-play any public dataset and allows a seamless integration to our State-of-the-art hardware giving you a quicker time-to-value for your AI project.


## Model description

LXMERT is a transformer model for learning vision-and-language cross-modality representations. It has a Transformer model that has three encoders: object relationship encoder, a language encoder, and a cross-modality encoder. It is pretrained via a combination of masked language modelling, visual-language text alignment, ROI-feature regression, masked visual-attribute modelling, masked visual-object modelling, and visual-question answering objectives. It achieves the state-of-the-art results on VQA and GQA. 

Paper link : [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/pdf/1908.07490.pdf) 

## Intended uses & limitations

This model is a fine-tuned version of [unc-nlp/lxmert-base-uncased](https://huggingface.co/unc-nlp/lxmert-base-uncased) on the [Graphcore/vqa-lxmert](https://huggingface.co/datasets/Graphcore/vqa-lxmert) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0009
- Accuracy: 0.7242

## Training and evaluation data

- [Graphcore/vqa-lxmert](https://huggingface.co/datasets/Graphcore/vqa-lxmert) dataset

## Training procedure

Trained on 16 Graphcore Mk2 IPUs using [optimum-graphcore](https://github.com/huggingface/optimum-graphcore).

Command line:

```
python examples/question-answering/run_vqa.py \
  --model_name_or_path unc-nlp/lxmert-base-uncased \
  --ipu_config_name Graphcore/lxmert-base-ipu \
  --dataset_name Graphcore/vqa-lxmert \
  --do_train \
  --do_eval \
  --max_seq_length 512 \
  --per_device_train_batch_size 1 \
  --num_train_epochs 4 \
  --dataloader_num_workers 64 \
  --logging_steps 5 \
  --learning_rate 5e-5 \
  --lr_scheduler_type linear \
  --loss_scaling 16384 \
  --weight_decay 0.01 \
  --warmup_ratio 0.1 \
  --output_dir /tmp/vqa/ \
  --dataloader_drop_last \
  --replace_qa_head \
  --pod_type pod16
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
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
  "train_loss": 0.0060005393999575125,
  "train_runtime": 13854.802,
  "train_samples": 443757,
  "train_samples_per_second": 128.116,
  "train_steps_per_second": 2.002

***** eval metrics *****
  "eval_accuracy": 0.7242196202278137,
  "eval_loss": 0.0008745193481445312,
  "eval_samples": 214354,
```

### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 2.0.0
- Tokenizers 0.11.6
