---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/amazon-reviews-input-output
metrics:
- accuracy
model-index:
- name: amazon-reviews-input-output-1.3b
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/amazon-reviews-input-output
      type: AlekseyKorshuk/amazon-reviews-input-output
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.03550813008130081
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amazon-reviews-input-output-1.3b

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the AlekseyKorshuk/amazon-reviews-input-output dataset.
It achieves the following results on the evaluation set:
- Loss: 3.5488
- Accuracy: 0.0355
- Samples: 100
- Perplexity: 34.7725
- Table: <wandb.data_types.Table object at 0x7ffa3c3fd700>

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 64
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.2024        | 0.06  | 1    | 2.9121          | 0.0385   |
| 3.1226        | 0.12  | 2    | 2.9121          | 0.0385   |
| 3.1321        | 0.19  | 3    | 2.8477          | 0.0394   |
| 2.9875        | 0.25  | 4    | 2.8477          | 0.0394   |
| 2.9717        | 0.31  | 5    | 2.8555          | 0.0391   |
| 2.9341        | 0.38  | 6    | 2.8438          | 0.0392   |
| 3.0376        | 0.44  | 7    | 2.8184          | 0.0396   |
| 2.8164        | 0.5   | 8    | 2.7988          | 0.0395   |
| 3.0857        | 0.56  | 9    | 2.7988          | 0.0394   |
| 2.9492        | 0.62  | 10   | 2.7969          | 0.0395   |
| 2.8633        | 0.69  | 11   | 2.7969          | 0.0395   |
| 2.8994        | 0.75  | 12   | 2.7910          | 0.0398   |
| 3.0024        | 0.81  | 13   | 2.7812          | 0.0401   |
| 2.937         | 0.88  | 14   | 2.7812          | 0.0399   |
| 2.9963        | 0.94  | 15   | 2.7812          | 0.0399   |
| 3.0168        | 1.0   | 16   | 2.7754          | 0.04     |
| 2.2589        | 1.06  | 17   | 2.7715          | 0.0397   |
| 2.2568        | 1.12  | 18   | 2.7793          | 0.0395   |
| 2.3138        | 1.19  | 19   | 2.8027          | 0.0393   |
| 2.2759        | 1.25  | 20   | 2.8184          | 0.0393   |
| 2.5137        | 1.31  | 21   | 2.8262          | 0.0390   |
| 2.2997        | 1.38  | 22   | 2.8320          | 0.0388   |
| 2.2693        | 1.44  | 23   | 2.8359          | 0.0392   |
| 2.204         | 1.5   | 24   | 2.8379          | 0.0387   |
| 2.3713        | 1.56  | 25   | 2.8359          | 0.0391   |
| 2.3448        | 1.62  | 26   | 2.8340          | 0.0391   |
| 2.217         | 1.69  | 27   | 2.8359          | 0.0391   |
| 2.3082        | 1.75  | 28   | 2.8379          | 0.0385   |
| 2.2878        | 1.81  | 29   | 2.8379          | 0.0386   |
| 2.2429        | 1.88  | 30   | 2.8379          | 0.0385   |
| 2.2838        | 1.94  | 31   | 2.8359          | 0.0385   |
| 2.4038        | 2.0   | 32   | 2.8379          | 0.0387   |
| 1.8481        | 2.06  | 33   | 2.8555          | 0.0384   |
| 1.657         | 2.12  | 34   | 2.8965          | 0.0382   |
| 1.6996        | 2.19  | 35   | 2.9590          | 0.0380   |
| 1.6741        | 2.25  | 36   | 3.0312          | 0.0379   |
| 1.594         | 2.31  | 37   | 3.0410          | 0.0380   |
| 1.5201        | 2.38  | 38   | 3.0156          | 0.0381   |
| 1.5149        | 2.44  | 39   | 3.0137          | 0.0380   |
| 1.5521        | 2.5   | 40   | 3.0176          | 0.0379   |
| 1.5364        | 2.56  | 41   | 3.0273          | 0.0378   |
| 1.5385        | 2.62  | 42   | 3.0391          | 0.0380   |
| 1.4794        | 2.69  | 43   | 3.0488          | 0.0380   |
| 1.4313        | 2.75  | 44   | 3.0527          | 0.0378   |
| 1.5071        | 2.81  | 45   | 3.0469          | 0.0378   |
| 1.4799        | 2.88  | 46   | 3.0449          | 0.0378   |
| 1.521         | 2.94  | 47   | 3.0371          | 0.0380   |
| 1.4603        | 3.0   | 48   | 3.0410          | 0.0379   |
| 1.25          | 3.06  | 49   | 3.0859          | 0.0381   |
| 1.0411        | 3.12  | 50   | 3.1797          | 0.0375   |
| 1.0385        | 3.19  | 51   | 3.2969          | 0.0371   |
| 1.0254        | 3.25  | 52   | 3.3613          | 0.0367   |
| 0.9656        | 3.31  | 53   | 3.3633          | 0.0368   |
| 1.036         | 3.38  | 54   | 3.3359          | 0.0366   |
| 0.9366        | 3.44  | 55   | 3.2949          | 0.0366   |
| 0.9712        | 3.5   | 56   | 3.2695          | 0.0367   |
| 1.0066        | 3.56  | 57   | 3.2676          | 0.0366   |
| 0.9952        | 3.62  | 58   | 3.2773          | 0.0368   |
| 1.0352        | 3.69  | 59   | 3.2891          | 0.0367   |
| 1.0212        | 3.75  | 60   | 3.3164          | 0.0362   |
| 0.9468        | 3.81  | 61   | 3.3203          | 0.0360   |
| 0.9155        | 3.88  | 62   | 3.3223          | 0.0366   |
| 0.8552        | 3.94  | 63   | 3.3262          | 0.0370   |
| 0.9575        | 4.0   | 64   | 3.3340          | 0.0370   |
| 0.6384        | 4.06  | 65   | 3.375           | 0.0370   |
| 0.6436        | 4.12  | 66   | 3.4453          | 0.0364   |
| 0.5752        | 4.19  | 67   | 3.5391          | 0.0358   |
| 0.6542        | 4.25  | 68   | 3.6016          | 0.0354   |
| 0.6724        | 4.31  | 69   | 3.6016          | 0.0354   |
| 0.591         | 4.38  | 70   | 3.5938          | 0.0359   |
| 0.5346        | 4.44  | 71   | 3.5801          | 0.0361   |
| 0.5112        | 4.5   | 72   | 3.5762          | 0.0361   |
| 0.5443        | 4.56  | 73   | 3.5840          | 0.0362   |
| 0.5689        | 4.62  | 74   | 3.6152          | 0.0358   |
| 0.5667        | 4.69  | 75   | 3.6328          | 0.0358   |
| 0.554         | 4.75  | 76   | 3.6348          | 0.0357   |
| 0.6087        | 4.81  | 77   | 3.625           | 0.0355   |
| 0.5236        | 4.88  | 78   | 3.6152          | 0.0355   |
| 0.5458        | 4.94  | 79   | 3.5781          | 0.0355   |
| 0.5702        | 5.0   | 80   | 3.5488          | 0.0355   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
