---
language: it
widget:
- text: "Quando nacque D'Annunzio?"
  context: "D'Annunzio nacque nel 1863"
---

# Italian Bert Base Uncased on Squad-it

## Model description

This model is the uncased base version of the italian BERT (which you may find at `dbmdz/bert-base-italian-uncased`) trained on the question answering task.

#### How to use

```python
from transformers import pipeline

nlp = pipeline('question-answering', model='antoniocappiello/bert-base-italian-uncased-squad-it')

# nlp(context="D'Annunzio nacque nel 1863", question="Quando nacque D'Annunzio?")
# {'score': 0.9990354180335999, 'start': 22, 'end': 25, 'answer': '1863'}
```

## Training data

It has been trained on the question answering task using [SQuAD-it](http://sag.art.uniroma2.it/demo-software/squadit/), derived from the original SQuAD dataset and obtained through the semi-automatic translation of the SQuAD dataset in Italian.

## Training procedure

```bash
python ./examples/run_squad.py \
    --model_type bert \
    --model_name_or_path dbmdz/bert-base-italian-uncased \
    --do_train \
    --do_eval \
    --train_file ./squad_it_uncased/train-v1.1.json \
    --predict_file ./squad_it_uncased/dev-v1.1.json \
    --learning_rate 3e-5 \
    --num_train_epochs 2 \
    --max_seq_length 384 \
    --doc_stride 128 \
    --output_dir ./models/bert-base-italian-uncased-squad-it/ \
    --per_gpu_eval_batch_size=3   \
    --per_gpu_train_batch_size=3   \
    --do_lower_case \
```

## Eval Results

| Metric | # Value   |
| ------ | --------- |
| **EM** | **63.8** |
| **F1** | **75.30** |

## Comparison

| Model                                                                                                                            | EM        | F1 score  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------- | --------- |
| [DrQA-it trained on SQuAD-it](https://github.com/crux82/squad-it/blob/master/README.md#evaluating-a-neural-model-over-squad-it)  | 56.1      | 65.9      |
| This one                                                                                                                         | **63.8** | **75.30** |