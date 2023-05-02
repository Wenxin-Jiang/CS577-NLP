---
license: mit
language: en
tags:
- bert
- cloze
- distractor
- generation
datasets:
- dgen
widget:
- text: "The only known planet with large amounts of water is [MASK]. [SEP] earth"
- text: "The products of photosynthesis are glucose and [MASK] else. [SEP] oxygen"
---

# cdgp-csg-bert-dgen

## Model description

This model is a Candidate Set Generator in **"CDGP: Automatic Cloze Distractor Generation based on Pre-trained Language Model", Findings of EMNLP 2022**.

Its input are stem and answer, and output is candidate set of distractors. It is fine-tuned by [**DGen**](https://github.com/DRSY/DGen) dataset based on [**bert-base-uncased**](https://huggingface.co/bert-base-uncased) model.

For more details, you can see our **paper** or [**GitHub**](https://github.com/AndyChiangSH/CDGP).

## How to use?

1. Download model by hugging face transformers.
```python
from transformers import BertTokenizer, BertForMaskedLM, pipeline

tokenizer = BertTokenizer.from_pretrained("AndyChiang/cdgp-csg-bert-dgen")
csg_model = BertForMaskedLM.from_pretrained("AndyChiang/cdgp-csg-bert-dgen")
```

2. Create a unmasker.
```python
unmasker = pipeline("fill-mask", tokenizer=tokenizer, model=csg_model, top_k=10)
```

3. Use the unmasker to generate the candidate set of distractors.
```python
sent = "The only known planet with large amounts of water is [MASK]. [SEP] earth"
cs = unmasker(sent)
print(cs)
```

## Dataset

This model is fine-tuned by [DGen](https://github.com/DRSY/DGen) dataset, which covers multiple domains including science, vocabulary, common sense and trivia. It is compiled from a wide variety of datasets including SciQ, MCQL, AI2 Science Questions, etc. The detail of DGen dataset is shown below.

| DGen dataset        | Train | Valid | Test | Total |
| ------------------- | ----- | ----- | ---- | ----- |
| **Number of questions** | 2321  | 300   | 259  | 2880  |

You can also use the [dataset](https://huggingface.co/datasets/AndyChiang/dgen) we have already cleaned.

## Training

We use a special way to fine-tune model, which is called **"Answer-Relating Fine-Tune"**. More details are in our paper.

### Training hyperparameters

The following hyperparameters were used during training:

- Pre-train language model: [bert-base-uncased](https://huggingface.co/bert-base-uncased)
- Optimizer: adam
- Learning rate: 0.0001
- Max length of input: 64
- Batch size: 64
- Epoch: 1
- Device: NVIDIA® Tesla T4 in Google Colab 

## Testing

The evaluations of this model as a Candidate Set Generator in CDGP is as follows:

| P@1   | F1@3 | MRR   | NDCG@10 |
| ----- | ---- | ----- | ------- |
| 10.81 | 7.72 | 18.15 | 24.47   |

## Other models

### Candidate Set Generator

| Models      | CLOTH                                                                               | DGen                                                                             |
| ----------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **BERT**    | [cdgp-csg-bert-cloth](https://huggingface.co/AndyChiang/cdgp-csg-bert-cloth)        | [*cdgp-csg-bert-dgen*](https://huggingface.co/AndyChiang/cdgp-csg-bert-dgen)       |
| **SciBERT** | [cdgp-csg-scibert-cloth](https://huggingface.co/AndyChiang/cdgp-csg-scibert-cloth)  | [cdgp-csg-scibert-dgen](https://huggingface.co/AndyChiang/cdgp-csg-scibert-dgen) |
| **RoBERTa** | [cdgp-csg-roberta-cloth](https://huggingface.co/AndyChiang/cdgp-csg-roberta-cloth) | [cdgp-csg-roberta-dgen](https://huggingface.co/AndyChiang/cdgp-csg-roberta-dgen) |
| **BART**    | [cdgp-csg-bart-cloth](https://huggingface.co/AndyChiang/cdgp-csg-bart-cloth)        | [cdgp-csg-bart-dgen](https://huggingface.co/AndyChiang/cdgp-csg-bart-dgen)       |

### Distractor Selector

**fastText**: [cdgp-ds-fasttext](https://huggingface.co/AndyChiang/cdgp-ds-fasttext)


## Citation

None