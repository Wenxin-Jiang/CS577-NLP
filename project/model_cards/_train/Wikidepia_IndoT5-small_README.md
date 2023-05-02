---
language:
- id
datasets:
- allenai/c4
---
# Indonesian T5 Small


T5 (Text-to-Text Transfer Transformer) model pretrained on Indonesian mC4 with [extra filtering](https://github.com/Wikidepia/indonesian_datasets/tree/master/dump/mc4). This model is pre-trained only and needs to be fine-tuned to be used for specific tasks.

## Pretraining Details

Trained for 1M steps following [`google/t5-v1_1-small`](https://huggingface.co/google/t5-v1_1-small).

## Model Performance

TBD

## Limitations and bias

This model also has the problem of biased (unethical, harmful, biased) output results due to the bias of the content of the training data, which is associated with the language model using a large-scale corpus. There is potential. Assuming that this problem may occur, please be careful to use it only for applications that do not cause damage.

## Acknowledgement

Thanks to Tensorflow Research Cloud for providing TPU v3-8s.