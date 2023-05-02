---
tags:
- generated_from_trainer
datasets:
- nielsr/funsd-layoutlmv3
pipeline_tag: object-detection
widget:
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png"
  example_title: invoice
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/contract.jpeg"
  example_title: contract
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-funsd
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: nielsr/funsd-layoutlmv3
      type: nielsr/funsd-layoutlmv3
      args: funsd
    metrics:
    - name: Precision
      type: precision
      value: 0.9026198714780029
    - name: Recall
      type: recall
      value: 0.913
    - name: F1
      type: f1
      value: 0.9077802634849614
    - name: Accuracy
      type: accuracy
      value: 0.8330271015158475
duplicated_from: nielsr/layoutlmv3-finetuned-funsd
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-funsd

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the nielsr/funsd-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1164
- Precision: 0.9026
- Recall: 0.913
- F1: 0.9078
- Accuracy: 0.8330

The script for training can be found here: https://github.com/huggingface/transformers/tree/main/examples/research_projects/layoutlmv3

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 10.0  | 100  | 0.5238          | 0.8366    | 0.886  | 0.8606 | 0.8410   |
| No log        | 20.0  | 200  | 0.6930          | 0.8751    | 0.8965 | 0.8857 | 0.8322   |
| No log        | 30.0  | 300  | 0.7784          | 0.8902    | 0.908  | 0.8990 | 0.8414   |
| No log        | 40.0  | 400  | 0.9056          | 0.8916    | 0.905  | 0.8983 | 0.8364   |
| 0.2429        | 50.0  | 500  | 1.0016          | 0.8954    | 0.9075 | 0.9014 | 0.8298   |
| 0.2429        | 60.0  | 600  | 1.0097          | 0.8899    | 0.897  | 0.8934 | 0.8294   |
| 0.2429        | 70.0  | 700  | 1.0722          | 0.9035    | 0.9085 | 0.9060 | 0.8315   |
| 0.2429        | 80.0  | 800  | 1.0884          | 0.8905    | 0.9105 | 0.9004 | 0.8269   |
| 0.2429        | 90.0  | 900  | 1.1292          | 0.8938    | 0.909  | 0.9013 | 0.8279   |
| 0.0098        | 100.0 | 1000 | 1.1164          | 0.9026    | 0.913  | 0.9078 | 0.8330   |


### Framework versions

- Transformers 4.19.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6
