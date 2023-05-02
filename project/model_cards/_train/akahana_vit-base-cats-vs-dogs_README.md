---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- cats_vs_dogs
metrics:
- accuracy
model-index:
- name: vit-base-cats-vs-dogs
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: cats_vs_dogs
      type: cats_vs_dogs
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9883257403189066
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-cats-vs-dogs

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the cats_vs_dogs dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0369
- Accuracy: 0.9883

## how to use
```python
from transformers import ViTFeatureExtractor, ViTModel
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTModel.from_pretrained('akahana/vit-base-cats-vs-dogs')
inputs = feature_extractor(images=image, return_tensors="pt")

outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 1337
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0949        | 1.0   | 2488 | 0.0369          | 0.9883   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
