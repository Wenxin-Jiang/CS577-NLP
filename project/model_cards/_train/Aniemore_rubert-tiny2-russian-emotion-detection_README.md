---

license: mit
language: ["ru"]
tags:
- russian
- classification
- emotion
- emotion-detection
- emotion-recognition
- multiclass
widget:
- text: "Как дела?"
- text: "Дурак твой дед"
- text: "Только попробуй!!!"
- text: "Не хочу в школу("
- text: "Сейчас ровно час дня"
- text: "А ты уверен, что эти полоски снизу не врут? Точно уверен? Вот прям 100 процентов?"
datasets:
- Aniemore/cedr-m7
model-index:
- name: RuBERT tiny2 For Russian Text Emotion Detection by Ilya Lubenets
  results:
  - task:
      name: Multilabel Text Classification
      type: multilabel-text-classification
    dataset:
      name: CEDR M7
      type: Aniemore/cedr-m7
      args: ru
    metrics:
    - name: multilabel accuracy
      type: accuracy
      value: 85%
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: CEDR M7
      type: Aniemore/cedr-m7
      args: ru
    metrics:
    - name: accuracy
      type: accuracy
      value: 76%

---

# First - you should prepare few functions to talk to model

```python
import torch
from transformers import BertForSequenceClassification, AutoTokenizer

LABELS = ['neutral', 'happiness', 'sadness', 'enthusiasm', 'fear', 'anger', 'disgust']
tokenizer = AutoTokenizer.from_pretrained('Aniemore/rubert-tiny2-russian-emotion-detection')
model = BertForSequenceClassification.from_pretrained('Aniemore/rubert-tiny2-russian-emotion-detection')

@torch.no_grad()
def predict_emotion(text: str) -> str:
    """
        We take the input text, tokenize it, pass it through the model, and then return the predicted label
        :param text: The text to be classified
        :type text: str
        :return: The predicted emotion
    """
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
        
    return LABELS[predicted[0]]

@torch.no_grad()    
def predict_emotions(text: str) -> list:
    """
        It takes a string of text, tokenizes it, feeds it to the model, and returns a dictionary of emotions and their
        probabilities
        :param text: The text you want to classify
        :type text: str
        :return: A dictionary of emotions and their probabilities.
    """
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    emotions_list = {}
    for i in range(len(predicted.numpy()[0].tolist())):
        emotions_list[LABELS[i]] = predicted.numpy()[0].tolist()[i]
    return emotions_list
```

# And then - just gently ask a model to predict your emotion

```python
simple_prediction = predict_emotion("Какой же сегодня прекрасный день, братья")
not_simple_prediction = predict_emotions("Какой же сегодня прекрасный день, братья")

print(simple_prediction)
print(not_simple_prediction)
# happiness
# {'neutral': 0.0004941817605867982, 'happiness': 0.9979524612426758, 'sadness': 0.0002536600804887712, 'enthusiasm': 0.0005498139653354883, 'fear': 0.00025326196919195354, 'anger': 0.0003583927755244076, 'disgust': 0.00013807788491249084}
```

# Or, just simply use [our package (GitHub)](https://github.com/aniemore/Aniemore), that can do whatever you want (or maybe not)
🤗

# Citations
```
@misc{Aniemore,
  author = {Артем Аментес, Илья Лубенец, Никита Давидчук},
  title = {Открытая библиотека искусственного интеллекта для анализа и выявления эмоциональных оттенков речи человека},
  year = {2022},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.com/aniemore/Aniemore}},
  email = {hello@socialcode.ru}
}
```