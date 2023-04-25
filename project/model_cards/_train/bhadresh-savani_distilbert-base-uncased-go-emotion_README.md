---
language: 
- en
thumbnail: https://avatars3.githubusercontent.com/u/32437151?s=460&u=4ec59abc8d21d5feea3dab323d23a5860e6996a4&v=4
tags:
- text-classification
- go-emotion
- pytorch
license: apache-2.0
datasets:
- go_emotions
metrics:
- Accuracy
---
# Distilbert-Base-Uncased-Go-Emotion

## Model description:

**Not working fine**

## Training Parameters:
```
  Num Epochs = 3
  Instantaneous batch size per device = 32
  Total train batch size (w. parallel, distributed & accumulation) = 32
  Gradient Accumulation steps = 1
  Total optimization steps = 15831
```

## TrainOutput:
```
'train_loss': 0.105500
```

## Evalution Output:
```
 'eval_accuracy_thresh': 0.962023913860321,
 'eval_loss': 0.11090277135372162,
```

## Colab Notebook:
[Notebook](https://github.com/bhadreshpsavani/UnderstandingNLP/blob/master/go_emotion_of_transformers_multilabel_text_classification_v2.ipynb)