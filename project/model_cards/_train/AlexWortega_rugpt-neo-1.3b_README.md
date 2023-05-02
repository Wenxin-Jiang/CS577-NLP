---
license: mit
datasets:
- wikipedia
- IlyaGusev/gazeta
language:
- ru
library_name: transformers
---
# ruGPT-Neo 1.3B [IN TRANING, 100k/2M NOT FINAL CHECKPOINT]

## Model Description

ruGPT-Neo 1.3B is a transformer model designed using EleutherAI's replication of the GPT-3 architecture. ruGPT-Neo refers to the class of models, while 1.3B represents the number of parameters of this particular pre-trained model.


## Training procedure

This model was trained on the wiki, gazeta summorization, for 38k steps, on 1*v100 gpu, still training . It was trained as a masked autoregressive language model, using cross-entropy loss.


### How to use

You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:

```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='AlexWortega/rugpt-neo-1.3b')
>>> generator("Как какать? Ответ:", do_sample=True, min_length=50)

[{'generated_text': 'Как какать? Ответ: Cпустите штаны и покакайте, затем воспользуйтесь бумагой'}]
```