---
language: id
tags:
- roberta
license: mit
datasets:
- indonlu
widget:
- text: "Hal-hal baik akan datang."
---

# Indo RoBERTa Emotion Classifier

Indo RoBERTa Emotion Classifier is emotion classifier based on [Indo-roberta](https://huggingface.co/flax-community/indonesian-roberta-base) model. It was trained on the trained on [IndoNLU EmoT](https://huggingface.co/datasets/indonlu) dataset. The model used was [Indo-roberta](https://huggingface.co/flax-community/indonesian-roberta-base) and was transfer-learned to an emotion classifier model. Based from the [IndoNLU bencmark](https://www.indobenchmark.com/), the model achieve an f1-macro of 72.05%, accuracy of 71.81%, precision of 72.47% and recall of 71.94%.

## Model

The model was trained on 7 epochs with learning rate 2e-5. Achieved different metrics as shown below.

| Epoch | Training Loss | Validation Loss | Accuracy | F1       | Precision | Recall   |
|-------|---------------|-----------------|----------|----------|-----------|----------|
|     1 |      1.300700 |        1.005149 | 0.622727 | 0.601846 |  0.640845 | 0.611144 |
|     2 |      0.806300 |        0.841953 | 0.686364 | 0.694096 |  0.701984 | 0.696657 |
|     3 |      0.591900 |        0.796794 | 0.686364 | 0.696573 |  0.707520 | 0.691671 |
|     4 |      0.441200 |        0.782094 | 0.722727 | 0.724359 |  0.725985 | 0.730229 |
|     5 |      0.334700 |        0.809931 | 0.711364 | 0.720550 |  0.718318 | 0.724608 |
|     6 |      0.268400 |        0.812771 | 0.718182 | 0.724192 |  0.721222 | 0.729195 |
|     7 |      0.226000 |        0.828461 | 0.725000 | 0.733625 |  0.731709 | 0.735800 |

## How to Use
### As Text Classifier
```python
from transformers import pipeline
pretrained_name = "StevenLimcorn/indonesian-roberta-base-emotion-classifier"
nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)
nlp("Hal-hal baik akan datang.")
```
## Disclaimer
Do consider the biases which come from both the pre-trained RoBERTa model and the `EmoT` dataset that may be carried over into the results of this model.
## Author
Indonesian RoBERTa Base Emotion Classifier was trained and evaluated by [Steven Limcorn](https://github.com/stevenlimcorn). All computation and development are done on Google Colaboratory using their free GPU access.