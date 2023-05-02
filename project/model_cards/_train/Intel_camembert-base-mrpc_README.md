---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: camembert-base-mrpc
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - type: accuracy
      value: 0.8504901960784313
      name: Accuracy
    - type: f1
      value: 0.8927943760984183
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: validation
    metrics:
    - type: accuracy
      value: 0.8504901960784313
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWJjOGZiMzBlNjhhNTZlMjEzNTE5MDM2OTJmYzZhZTE2YzE0MWM0ZmY2Zjk5ZTkxYWE0NTEyMDVlMDI5N2MwZiIsInZlcnNpb24iOjF9.dLsmgphn4jg1LbcOwDagIBRtQJ3spLTOcPxOpVnNqE-oU6ttKxW-Ypg7arQxOV-swVu4xpl3SDGaqEDE5sZnCw
    - type: precision
      value: 0.8758620689655172
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2ZiY2ZiODZmOTJkN2I4YzYxY2NmMDc1NzQyMmI0MTI0MDlmYzkzNDhjMTA4NmIzNzNjNjE4NmMwMjI1MDRjMyIsInZlcnNpb24iOjF9.94XqLpsB43QQqsnh5ykt_jZuKXOjSbtwFgEUscatZzJdwIt0WBHY7oNpoodbZbk0eUDzTIoZyNoN59glXmlEAg
    - type: recall
      value: 0.910394265232975
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTY3MDljNGM4ZjYxZjc1YmYyZTkwNjc4MTRmOTFjZjYyZDdlY2EyZTc4OWE0NWQ3ODIxY2NmODIzY2IxMWY5YiIsInZlcnNpb24iOjF9.BGacWdlFR1hw98mwV6P1UPbBInb4Z8XIpRkqqZdeQPpH9RBBdGoaiKuKx7FJKGDgMLEaqwleER4n6FSC7KaQDg
    - type: auc
      value: 0.9029062821260871
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDU0ZjdjZGNjNjAxZWM3NzNlYmM2NWFlZmYwZTY5ZDI2ZTY2ZTk0YTVhODc0NzcyMjNjOGFjOTY0YjYzMmU2ZCIsInZlcnNpb24iOjF9.jalnocWEmIaPkl1l-kHZm9I49WumqCay5T5C3_5RKhPZMCidPIRB14Y7a6klepf19-__EmP34QS3HxEl5iVMBA
    - type: f1
      value: 0.8927943760984183
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2I1MGVmODRlYTNjZTJmYWRiYTA5YzEyODkxYjQ2ZGNlMTliODAwMzMwNGEzMWQ2ZGRhYmYwZjVjMTgwNGU2NCIsInZlcnNpb24iOjF9.QgvEjsEulus1kvcBkHqV3RrcigOSNcfCbkKa6JWPCRxIyzbiFpNCvkFubSHbVPe0SX2h9vjgjmECv-SapMLKDg
    - type: loss
      value: 0.42868512868881226
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjIwMjNiYzI4NzgwZGI5MWU2NDgzYTQzNTYwNGUwMmZlNmViODhhYWIzZGE1ZWIxYzExMzRiOTU1YzFhNWQ0OSIsInZlcnNpb24iOjF9.NUgxlMh9Z0EyRqeKRr3BYYk9L02EdmJM-alLPPecPkML_ZdcbWHW-JOQN_vUTgYNda80dUBKRj_FmJ4kRF4yAQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-mrpc

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4286
- Accuracy: 0.8505
- F1: 0.8928
- Combined Score: 0.8716

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu102
- Datasets 2.1.0
- Tokenizers 0.11.6
