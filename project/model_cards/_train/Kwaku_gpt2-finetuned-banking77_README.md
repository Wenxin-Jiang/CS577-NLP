---
language: eng
datasets:
- banking77
---

# GPT2 Fine-Tuned Banking 77
This is a fine-tuned version of the GPT2 model. It's best suited for text-generation.

## Model Description
Kwaku/gpt2-finetuned-banking77 was fine tuned on the [banking77](https://huggingface.co/datasets/banking77) dataset, which is "composed of online banking queries annotated with their corresponding intents."

## Intended Uses and Limitations
Given the magnitude of the [Microsoft DialoGPT-large](https://huggingface.co/microsoft/DialoGPT-large) model, the author resorted to fine-tuning the gpt2 model for the creation of a chatbot. The intent was for the chatbot to emulate a banking customer agent, hence the use of the banking77 dataset. However, when the fine-tuned model was deployed in the chatbot, the results were undesirable. Its responses were inappropriate and unnecessarily long. The last word of its response is repeated numerously, a major glitch in it. The model performs better in text-generation but is prone to generating banking-related text because of the corpus it was trained on. 

### How to use

You can use this model directly with a pipeline for text generation:

```python
>>>from transformers import pipeline

>>> model_name = "Kwaku/gpt2-finetuned-banking77"
>>> generator = pipeline("text-generation", model=model_name)
>>> result = generator("My money is", max_length=15, num_return_sequences=2)
>>> print(result)

[{'generated_text': 'My money is stuck in ATM pending. Please cancel this transaction and refund it'}, {'generated_text': 'My money is missing. How do I get a second card, and how'}]
```

### Limitations and bias

For users who want a diverse text-generator, this model's tendency to generate mostly bank-related text will be a drawback. It also inherits [the biases of its parent model, the GPT2](https://huggingface.co/gpt2#limitations-and-bias).
