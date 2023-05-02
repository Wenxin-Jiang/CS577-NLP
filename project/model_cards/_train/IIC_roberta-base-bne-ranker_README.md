---
language:
- es
tags:
- sentence similarity  # Example: audio
- passage reranking  # Example: automatic-speech-recognition
datasets:
- IIC/msmarco_es

metrics:
- eval_MRR@10: 0.688

model-index:
- name: roberta-base-bne-ranker
  results:
  - task: 
      type: text similarity  # Required. Example: automatic-speech-recognition
      name: text similarity  # Optional. Example: Speech Recognition
    dataset:
      type: IIC/msmarco_es  # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: IIC/msmarco_es  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: MRR@10
        value: 0.688
        name: eval_MRR@10
---

This is a model to rank documents based on importance. It is trained on an [automatically translated version of MS Marco](https://huggingface.co/datasets/IIC/msmarco_es). After some experiments, the best configuration was to train for 2 epochs with learning rate 2e-5 and batch size 32. 

Example of use:

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("IIC/roberta-base-bne-ranker", device="cpu")

question = "¿Cómo se llama el rey?"

contexts = ["Me encanta la canción de el rey", "Cuando el rey fue a Sevilla, perdió su silla", "El rey se llama Juan Carlos y es conocido por sus escándalos"]

similarity_scores = model.predict([[question, context] for context in contexts])
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.