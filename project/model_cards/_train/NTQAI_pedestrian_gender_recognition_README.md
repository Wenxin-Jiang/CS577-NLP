---
license: apache-2.0
tags:
- image-classification
- vision
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: outputs
  results:
  - task:
      name: Image Classification
      type: image-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9107332624867163
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# outputs

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) on the [PETA dataset](http://mmlab.ie.cuhk.edu.hk/projects/PETA_files/Pedestrian%20Attribute%20Recognition%20At%20Far%20Distance.pdf) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2170
- Accuracy: 0.9107

## Model description

More information needed

#### How to use

You can use this model with Transformers *pipeline* .

```python
from transformers import pipeline
gender_classifier = pipeline(model="NTQAI/pedestrian_gender_recognition")
image_path = "abc.jpg"

results = gender_classifier(image_path)
print(results)
```

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 1337
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5193        | 1.0   | 2000  | 0.3346          | 0.8533   |
| 0.337         | 2.0   | 4000  | 0.2892          | 0.8778   |
| 0.3771        | 3.0   | 6000  | 0.2493          | 0.8969   |
| 0.3819        | 4.0   | 8000  | 0.2275          | 0.9100   |
| 0.3581        | 5.0   | 10000 | 0.2170          | 0.9107   |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).