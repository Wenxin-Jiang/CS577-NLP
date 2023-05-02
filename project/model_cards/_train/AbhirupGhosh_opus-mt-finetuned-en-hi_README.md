---
language:
- en
- hi
- multilingual
license: apache-2.0
tags:
- translation
- Hindi
- generated_from_keras_callback
datasets:
- HindiEnglishCorpora
---

# opus-mt-finetuned-hi-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-hi-en](https://huggingface.co/Helsinki-NLP/opus-mt-hi-en) on [HindiEnglish Corpora](https://www.clarin.eu/resource-families/parallel-corpora)


## Model description

The model is a transformer model similar to the [Transformer](https://arxiv.org/abs/1706.03762?context=cs) as defined in Attention Is All You Need by Vaswani et al

## Training and evaluation data

More information needed

## Training procedure

The model was trained on 2 NVIDIA_TESLA_A100 GPU's on Google's vertex AI platform.

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: AdamWeightDecay
- training_precision: float32

### Training results



### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1
