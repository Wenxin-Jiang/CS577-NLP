---
language: de
widget:
- text: Hallo, ich bin ein Sprachmodell

license: gpl
---

<h2> GPT2 Model for German Language </h2>


Model Name: Tanhim/gpt2-model-de <br />
language: German or Deutsch  <br />
thumbnail: https://huggingface.co/Tanhim/gpt2-model-de <br />
datasets: Ten Thousand German News Articles Dataset <br />

### How to use
You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, I
set a seed for reproducibility:
```python
>>> from transformers import pipeline, set_seed
>>> generation= pipeline('text-generation', model='Tanhim/gpt2-model-de', tokenizer='Tanhim/gpt2-model-de')
>>> set_seed(42)
>>> generation("Hallo, ich bin ein Sprachmodell,", max_length=30, num_return_sequences=5)

```
Here is how to use this model to get the features of a given text in PyTorch:
```python
from transformers import AutoTokenizer, AutoModelWithLMHead 
tokenizer = AutoTokenizer.from_pretrained("Tanhim/gpt2-model-de") 
model = AutoModelWithLMHead.from_pretrained("Tanhim/gpt2-model-de") 
text = "Ersetzen Sie mich durch einen beliebigen Text, den Sie wünschen."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

Citation request:
If you use the model of this repository in your research, please consider citing the following way:
```python
@misc{GermanTransformer,
  author = {Tanhim Islam},
  title = {{PyTorch Based Transformer Machine Learning Model for German Text Generation Task}},
  howpublished = "\url{https://huggingface.co/Tanhim/gpt2-model-de}",
  year = {2021}, 
  note = "[Online; accessed 17-June-2021]"
}
```