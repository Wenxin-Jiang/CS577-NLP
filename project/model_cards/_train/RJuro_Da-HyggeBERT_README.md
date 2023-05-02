---
language: da
tags:
- danish
- bert
- sentiment
- text-classification
- Maltehb/danish-bert-botxo
- Helsinki-NLP/opus-mt-en-da
- go-emotion
- Certainly
license: cc-by-4.0
datasets:
- go_emotions
metrics:
- Accuracy
widget:
- text: "Det er så sødt af dig at tænke på andre på den måde ved du det?"
- text: "Jeg vil gerne have en playstation."
- text: "Jeg elsker dig"
- text: "Hvordan håndterer jeg min irriterende nabo?"
---

# Danish-Bert-GoÆmotion

Danish Go-Emotions classifier. [Maltehb/danish-bert-botxo](https://huggingface.co/Maltehb/danish-bert-botxo) (uncased) finetuned on a translation of the [go_emotions](https://huggingface.co/datasets/go_emotions) dataset using [Helsinki-NLP/opus-mt-en-da](https://huggingface.co/Helsinki-NLP/opus-mt-de-en). Thus, performance is obviousely dependent on the translation model.

## Training
- Translating the training data with MT: [Notebook](https://colab.research.google.com/github/RJuro/Da-HyggeBERT-finetuning/blob/main/HyggeBERT_translation_en_da.ipynb)
- Fine-tuning danish-bert-botxo: coming soon...

## Training Parameters:

```
Num examples = 189900
Num Epochs = 3
Train batch = 8
Eval batch = 8
Learning Rate = 3e-5
Warmup steps = 4273
Total optimization steps = 71125
```

## Loss
### Training loss
![](wb_loss.png)

### Eval. loss
```
0.1178 (21100 examples)
```


## Using the model with `transformers`
Easiest use with `transformers` and `pipeline`:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model = AutoModelForSequenceClassification.from_pretrained('RJuro/Da-HyggeBERT')
tokenizer = AutoTokenizer.from_pretrained('RJuro/Da-HyggeBERT')

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

classifier('jeg elsker dig')
```

`[{'label': 'kærlighed', 'score': 0.9634820818901062}]`

## Using the model with `simpletransformers`

```python
from simpletransformers.classification import MultiLabelClassificationModel

model = MultiLabelClassificationModel('bert', 'RJuro/Da-HyggeBERT')

predictions, raw_outputs = model.predict(df['text'])
```