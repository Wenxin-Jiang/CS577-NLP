# bert-base-buddhist-sanskrit

Version 2 of the BERT model described in the paper 'Embeddings models for Buddhist Sanskrit' published at LREC 2022 (https://aclanthology.org/2022.lrec-1.411/). 
Same training methodology has been used as for version 1, the only difference is that the model has been trained on a slightly bigger buddhist snaskrit corpus.

## Model description

The model has the bert-base architecture and configuration and was pretrained from scratch as a masked language model 
on the Sanskrit reference corpus, and fine-tuned on the smaller corpus of Buddhist Sanskrit. 

## How to use it

```
model = AutoModelForMaskedLM.from_pretrained("Matej/bert-base-buddhist-sanskrit")
tokenizer = AutoTokenizer.from_pretrained("Matej/bert-base-buddhist-sanskrit", use_fast=True)
```

## Intended uses & limitations

MIT license, no limitations

## Training and evaluation data

See the paper 'Embeddings models for Buddhist Sanskrit' for details on the corpora and the evaluation procedure.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 24
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 200

### Framework versions

- Transformers 4.20.0
- Pytorch 1.9.0
- Datasets 2.3.2
- Tokenizers 0.12.1

