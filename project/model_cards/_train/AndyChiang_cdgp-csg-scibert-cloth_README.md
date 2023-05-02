---
license: mit
language: en
tags:
- bert
- cloze
- distractor
- generation
datasets:
- cloth
widget:
- text: "I feel [MASK] now. [SEP] happy"
- text: "The old man was waiting for a ride across the [MASK]. [SEP] river"
---

# cdgp-csg-scibert-cloth

## Model description

This model is a Candidate Set Generator in **"CDGP: Automatic Cloze Distractor Generation based on Pre-trained Language Model", Findings of EMNLP 2022**.

Its input are stem and answer, and output is candidate set of distractors. It is fine-tuned by [**CLOTH**](https://www.cs.cmu.edu/~glai1/data/cloth/) dataset based on [**allenai/scibert_scivocab_uncased**](https://huggingface.co/allenai/scibert_scivocab_uncased) model.

For more details, you can see our **paper** or [**GitHub**](https://github.com/AndyChiangSH/CDGP).

## How to use?

1. Download the model by hugging face transformers.
```python
from transformers import BertTokenizer, BertForMaskedLM, pipeline

tokenizer = BertTokenizer.from_pretrained("AndyChiang/cdgp-csg-scibert-cloth")
csg_model = BertForMaskedLM.from_pretrained("AndyChiang/cdgp-csg-scibert-cloth")
```

2. Create a unmasker.
```python
unmasker = pipeline("fill-mask", tokenizer=tokenizer, model=csg_model, top_k=10)
```

3. Use the unmasker to generate the candidate set of distractors.
```python
sent = "I feel [MASK] now. [SEP] happy"
cs = unmasker(sent)
print(cs)
```

## Dataset

This model is fine-tuned by [CLOTH](https://www.cs.cmu.edu/~glai1/data/cloth/) dataset, which is a collection of nearly 100,000 cloze questions from middle school and high school English exams. The detail of CLOTH dataset is shown below.

| Number of questions | Train | Valid | Test  |
| ------------------- | ----- | ----- | ----- |
| Middle school       | 22056 | 3273  | 3198  |
| High school         | 54794 | 7794  | 8318  |
| Total               | 76850 | 11067 | 11516 |

You can also use the [dataset](https://huggingface.co/datasets/AndyChiang/cloth) we have already cleaned.

## Training

We use a special way to fine-tune model, which is called **"Answer-Relating Fine-Tune"**. More detail is in our paper.

### Training hyperparameters

The following hyperparameters were used during training:

- Pre-train language model: [allenai/scibert_scivocab_uncased](https://huggingface.co/allenai/scibert_scivocab_uncased)
- Optimizer: adam
- Learning rate: 0.0001
- Max length of input: 64
- Batch size: 64
- Epoch: 1
- Device: NVIDIA® Tesla T4 in Google Colab 

## Testing

The evaluations of this model as a Candidate Set Generator in CDGP is as follows:

| P@1  | F1@3 | F1@10 | MRR   | NDCG@10 |
| ---- | ---- | ----- | ----- | ------- |
| 8.10 | 9.13 | 12.22 | 19.53 | 28.76   |

## Other models

### Candidate Set Generator

| Models      | CLOTH                                                                               | DGen                                                                             |
| ----------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **BERT**    | [cdgp-csg-bert-cloth](https://huggingface.co/AndyChiang/cdgp-csg-bert-cloth)        | [cdgp-csg-bert-dgen](https://huggingface.co/AndyChiang/cdgp-csg-bert-dgen)       |
| **SciBERT** | [*cdgp-csg-scibert-cloth*](https://huggingface.co/AndyChiang/cdgp-csg-scibert-cloth)  | [cdgp-csg-scibert-dgen](https://huggingface.co/AndyChiang/cdgp-csg-scibert-dgen) |
| **RoBERTa** | [cdgp-csg-roberta-cloth](https://huggingface.co/AndyChiang/cdgp-csg-roberta-cloth) | [cdgp-csg-roberta-dgen](https://huggingface.co/AndyChiang/cdgp-csg-roberta-dgen) |
| **BART**    | [cdgp-csg-bart-cloth](https://huggingface.co/AndyChiang/cdgp-csg-bart-cloth)        | [cdgp-csg-bart-dgen](https://huggingface.co/AndyChiang/cdgp-csg-bart-dgen)       |

### Distractor Selector

**fastText**: [cdgp-ds-fasttext](https://huggingface.co/AndyChiang/cdgp-ds-fasttext)


## Citation

None