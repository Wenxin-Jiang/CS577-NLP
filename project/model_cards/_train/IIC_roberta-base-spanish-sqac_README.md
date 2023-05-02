---
language:
- es
tags:
- question-answering # Example: audio
datasets:
- PlanTL-GOB-ES/SQAC
metrics:
- f1

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: roberta-base-spanish_sqac
  results:
  - task: 
      type: question-answering # Required. Example: automatic-speech-recognition
      name: question-answering  # Optional. Example: Speech Recognition
    dataset:
      type: SQAC # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: PlanTL-GOB-ES/SQAC  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: f1
        value: 86.6 
        name: f1
---

This model was trained on the [SQAC](https://huggingface.co/datasets/BSC-TeMU/SQAC) dataset, provided by [BSC](https://www.bsc.es/). It is a question-answering dataset originally developed in Spanish. As for the model, it is a fine-tuned version of [MarIA-Roberta](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne), a spanish roberta also developed by BSC under the project MarIA.

For training the model, we followed the recommendations of the own authors in [their paper](https://arxiv.org/abs/2107.07253), performing a full grid search over the hyperparameter space provided in the paper, and selected the best model based on eval\_loss. 

You can use the model like this:

```python
from transformers import RobertaTokenizer, RobertaForQuestionAnswering
import torch

tokenizer = RobertaTokenizer.from_pretrained("IIC/roberta-base-spanish-sqac")
model = RobertaForQuestionAnswering.from_pretrained("IIC/roberta-base-spanish-sqac")

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