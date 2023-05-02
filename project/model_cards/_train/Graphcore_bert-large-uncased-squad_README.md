---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: Graphcore/bert-large-uncased-squad
  results: []
---

# Graphcore/bert-large-uncased-squad
Optimum Graphcore is a new open-source library and toolkit that enables developers to access IPU-optimized models certified by Hugging Face. It is an extension of Transformers, providing a set of performance optimization tools enabling maximum efficiency to train and run models on Graphcore’s IPUs - a completely new kind of massively parallel processor to accelerate machine intelligence. Learn more about how to take train Transformer models faster with IPUs at [hf.co/hardware/graphcore](https://huggingface.co/hardware/graphcore).

Through HuggingFace Optimum, Graphcore released ready-to-use IPU-trained model checkpoints and IPU configuration files to make it easy to train models with maximum efficiency in the IPU. Optimum shortens the development lifecycle of your AI models by letting you plug-and-play any public dataset and allows a seamless integration to our State-of-the-art hardware giving you a quicker time-to-value for your AI project.



## Model description

BERT (Bidirectional Encoder Representations from Transformers) is a transformers model which is designed to pretrain bidirectional representations from unlabelled texts. It enables easy and fast fine-tuning for different downstream tasks such as Sequence Classification, Named Entity Recognition, Question Answering, Multiple Choice and MaskedLM. 

It was trained with two objectives in pretraining : Masked language modelling (MLM) and Next sentence prediction(NSP). First, MLM is different from traditional LM which sees the words one after another while BERT allows the model to learn a bidirectional representation.  In addition to MLM, NSP is used for jointly pertaining text-pair representations.

It reduces the need of many engineering efforts for building task specific architectures through pre-trained representation. And achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks.



## Intended uses & limitations

This model is a fine-tuned version of [Graphcore/bert-large-uncased](https://huggingface.co/Graphcore/bert-large-uncased) on the SQuAD dataset.

## Training and evaluation data
Trained on SQuAD dataset:
- [HuggingFace/squad](https://huggingface.co/datasets/squad)

## Training procedure

Model was trained on 16 Graphcore Mk2 IPUs using the [optimum-graphcore](https://github.com/huggingface/optimum-graphcore) library.

