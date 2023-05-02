---
license: mit
tags:
- generated_from_trainer
datasets:
- ManpreetK/NDD_NER
model-index:
- name: BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-NDD-NER
  results: []
---

# BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-NDD-NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the ManpreetK/NDD_NER dataset.
It achieves the following results on the evaluation set:
- Overall Precision: 0.6297
- Overall Recall: 0.7068
- Overall F1: 0.6660
- Overall Accuracy: 0.9044
  
- Loss: 0.3763
  
- Associated_Problem Precision/Recall/F1: 0.6316/0.5294/0.576
- Associated_Problem Number: 68
  
- Condition Precision/Recall/F1: 0.8052/0.8921/0.8464
- Condition Number: 139

- Intervention Precision/Recall/F1: 0.5159/0.6633/0.5804
- Intervention Number: 98
  
- Patient_Group Precision/Recall/F1: 0.5512/0.8046/0.6542
- Patient_Group Number: 87
  
- Test Precision/Recall/F1: 0.5882/0.4878/0.5333
- Test Number: 82


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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Associated Problem Precision | Associated Problem Recall | Associated Problem F1 | Associated Problem Number | Condition Precision | Condition Recall | Condition F1 | Condition Number | Intervention Precision | Intervention Recall | Intervention F1 | Intervention Number | Patient Group Precision | Patient Group Recall | Patient Group F1 | Patient Group Number | Test Precision | Test Recall | Test F1 | Test Number | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:----------------------------:|:-------------------------:|:---------------------:|:-------------------------:|:-------------------:|:----------------:|:------------:|:----------------:|:----------------------:|:-------------------:|:---------------:|:-------------------:|:-----------------------:|:--------------------:|:----------------:|:--------------------:|:--------------:|:-----------:|:-------:|:-----------:|:-----------------:|:--------------:|:----------:|:----------------:|
| 1.4014        | 1.0   | 11   | 0.7804          | 0.0                          | 0.0                       | 0.0                   | 68                        | 0.0                 | 0.0              | 0.0          | 139              | 0.0                    | 0.0                 | 0.0             | 98                  | 0.0                     | 0.0                  | 0.0              | 87                   | 0.0            | 0.0         | 0.0     | 82          | 0.0               | 0.0            | 0.0        | 0.7808           |
| 0.7625        | 2.0   | 22   | 0.5575          | 0.0                          | 0.0                       | 0.0                   | 68                        | 0.7468              | 0.8273           | 0.7850       | 139              | 0.3333                 | 0.1429              | 0.2             | 98                  | 0.7627                  | 0.5172               | 0.6164           | 87                   | 0.4286         | 0.1098      | 0.1748  | 82          | 0.6630            | 0.3861         | 0.488      | 0.8546           |
| 0.5152        | 3.0   | 33   | 0.4489          | 0.2222                       | 0.0588                    | 0.0930                | 68                        | 0.7011              | 0.9281           | 0.7988       | 139              | 0.4674                 | 0.4388              | 0.4526          | 98                  | 0.5528                  | 0.7816               | 0.6476           | 87                   | 0.5758         | 0.4634      | 0.5135  | 82          | 0.5839            | 0.5949         | 0.5893     | 0.8820           |
| 0.3621        | 4.0   | 44   | 0.4020          | 0.2727                       | 0.1324                    | 0.1782                | 68                        | 0.7716              | 0.8993           | 0.8306       | 139              | 0.4538                 | 0.5510              | 0.4977          | 98                  | 0.5752                  | 0.7471               | 0.65             | 87                   | 0.7059         | 0.4390      | 0.5414  | 82          | 0.6046            | 0.6097         | 0.6071     | 0.8900           |
| 0.252         | 5.0   | 55   | 0.3764          | 0.5                          | 0.5588                    | 0.5278                | 68                        | 0.8219              | 0.8633           | 0.8421       | 139              | 0.5426                 | 0.5204              | 0.5312          | 98                  | 0.5610                  | 0.7931               | 0.6571           | 87                   | 0.5641         | 0.5366      | 0.55    | 82          | 0.6228            | 0.6793         | 0.6498     | 0.9014           |
| 0.1988        | 6.0   | 66   | 0.3839          | 0.4918                       | 0.4412                    | 0.4651                | 68                        | 0.7590              | 0.9065           | 0.8262       | 139              | 0.4161                 | 0.6327              | 0.5020          | 98                  | 0.552                   | 0.7931               | 0.6509           | 87                   | 0.5606         | 0.4512      | 0.5     | 82          | 0.5714            | 0.6835         | 0.6225     | 0.8961           |
| 0.1623        | 7.0   | 77   | 0.3669          | 0.4941                       | 0.6176                    | 0.5490                | 68                        | 0.8105              | 0.8921           | 0.8493       | 139              | 0.4667                 | 0.6429              | 0.5408          | 98                  | 0.5702                  | 0.7931               | 0.6635           | 87                   | 0.5634         | 0.4878      | 0.5229  | 82          | 0.5982            | 0.7131         | 0.6506     | 0.9020           |
| 0.1319        | 8.0   | 88   | 0.3763          | 0.6316                       | 0.5294                    | 0.576                 | 68                        | 0.8052              | 0.8921           | 0.8464       | 139              | 0.5159                 | 0.6633              | 0.5804          | 98                  | 0.5512                  | 0.8046               | 0.6542           | 87                   | 0.5882         | 0.4878      | 0.5333  | 82          | 0.6297            | 0.7068         | 0.6660     | 0.9044           |
| 0.117         | 9.0   | 99   | 0.3834          | 0.6481                       | 0.5147                    | 0.5738                | 68                        | 0.8158              | 0.8921           | 0.8522       | 139              | 0.4923                 | 0.6531              | 0.5614          | 98                  | 0.5738                  | 0.8046               | 0.6699           | 87                   | 0.5909         | 0.4756      | 0.5270  | 82          | 0.6336            | 0.7004         | 0.6653     | 0.9030           |
| 0.1125        | 10.0  | 110  | 0.3854          | 0.5441                       | 0.5441                    | 0.5441                | 68                        | 0.8170              | 0.8993           | 0.8562       | 139              | 0.4737                 | 0.6429              | 0.5455          | 98                  | 0.5635                  | 0.8161               | 0.6667           | 87                   | 0.5882         | 0.4878      | 0.5333  | 82          | 0.6131            | 0.7089         | 0.6575     | 0.9028           |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.0+cu116
- Datasets 2.8.0
- Tokenizers 0.12.1
