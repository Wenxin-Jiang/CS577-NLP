---
language:
- es
tags:
- question-answering # Example: audio
datasets:
- IIC/bioasq22_es
metrics:
- f1

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: beto-base-cased-bioasq
  results:
  - task: 
      type: question-answering # Required. Example: automatic-speech-recognition
      name: question-answering  # Optional. Example: Speech Recognition
    dataset:
      type: SQAC # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: IIC/bioasq22_es  # Required. Example: Common Voice zh-CN
    metrics:
      - type: f1
        value: 
        name: f1
---
This model was trained on the [bioasq22_es](https://huggingface.co/datasets/IIC/bioasq22_es) dataset, provided by [IIC](https://www.iic.uam.es/). It is an automatically translated version of the [bioasq](https://huggingface.co/datasets/kroshan/BioASQ) dataset. As for the model, it is a fine-tuned version of [BETO](https://github.com/dccuchile/beto), a spanish BERT developed by the Catholic University of Chile.

For training the model, we followed the recommendations given in [this paper](https://arxiv.org/abs/2107.07253). 
You can use the model like this:
```python
from transformers import RobertaTokenizer, RobertaForQuestionAnswering
import torch
tokenizer = RobertaTokenizer.from_pretrained("IIC/beto-base-cased-bioasq")
model = RobertaForQuestionAnswering.from_pretrained("IIC/beto-base-cased-bioasq")
question, text = "Quién es el padre de Luke Skywalker?", "En la famosa película, Darth Veider le dice a Luke Skywalker aquella frase que todos recordamos: yo soy tu padre."
inputs = tokenizer(question, text, return_tensors="pt")
start_positions = torch.tensor([1])
end_positions = torch.tensor([3])

outputs = model(**inputs, start_positions=start_positions, end_positions=end_positions)
loss = outputs.loss
start_scores = outputs.start_logits
end_scores = outputs.end_logits
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.