---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikitext
model-index:
- name: clm_output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Graphcore/gpt2-wikitext-103

Optimum Graphcore is a new open-source library and toolkit that enables developers to access IPU-optimized models certified by Hugging Face. It is an extension of Transformers, providing a set of performance optimization tools enabling maximum efficiency to train and run models on Graphcore’s IPUs - a completely new kind of massively parallel processor to accelerate machine intelligence. Learn more about how to take train Transformer models faster with IPUs at [hf.co/hardware/graphcore](https://huggingface.co/hardware/graphcore).

Through HuggingFace Optimum, Graphcore released ready-to-use IPU-trained model checkpoints and IPU configuration files to make it easy to train models with maximum efficiency in the IPU. Optimum shortens the development lifecycle of your AI models by letting you plug-and-play any public dataset and allows a seamless integration to our State-of-the-art hardware giving you a quicker time-to-value for your AI project.


## Model description

GPT2 is a large transformer-based language model. It is built using transformer decoder blocks. BERT, on the other hand, uses transformer encoder blocks. It adds Layer normalisation to the input of each sub-block, similar to a pre-activation residual networks and an additional layer normalisation.  
 
Paper link : [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)  

## Intended uses & limitations


This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the [wikitext-103-raw-v1](https://huggingface.co/datasets/wikitext) dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9902


## Training and evaluation data

- [HuggingFace/wikitext-103-raw-v1](https://huggingface.co/datasets/wikitext) dataset

## Training procedure

Trained on 16 Graphcore Mk2 IPUs using [optimum-graphcore](https://github.com/huggingface/optimum-graphcore).

Command line:

```
python examples/language-modeling/run_clm.py \
  --model_name_or_path gpt2 \
  --ipu_config_name Graphcore/gpt2-small-ipu \
  --dataset_name wikitext \
  --dataset_config_name wikitext-103-raw-v1 \
  --do_train \
  --do_eval \
  --num_train_epochs 10 \
  --dataloader_num_workers 64 \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 128 \
  --output_dir /tmp/clm_output \
  --logging_steps 5 \
  --learning_rate 1e-5 \
  --lr_scheduler_type linear \
  --loss_scaling 16384 \
  --weight_decay 0.01 \
  --warmup_ratio 0.1 \
  --ipu_config_overrides="embedding_serialization_factor=4,optimizer_state_offchip=true,inference_device_iterations=5" \
  --dataloader_drop_last \
  --pod_type pod16
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 128
- total_train_batch_size: 1024
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0
- training precision: Mixed Precision

### Training results
```
***** train metrics *****
    "epoch": 10.0,
    "train_loss": 3.1787637246621623,
    "train_runtime": 4372.4031,
    "train_samples": 114248,
    "train_samples_per_second": 261.293,
    "train_steps_per_second": 0.254
    
***** eval metrics *****
    "eval_loss": 2.990234375,
    "eval_samples": 240,
    "perplexity": 19.89034374461794
```


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0+cpu
- Datasets 2.0.0
- Tokenizers 0.11.6
