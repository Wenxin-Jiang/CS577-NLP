---
language:
- tr
thumbnail:
tags:
- gpt2
- turkish

license: apache-2.0
datasets:
- wikipedia-turkish
metrics:
- perplexity
- accuracy

widget:
- text: Bu yazıyı bir bilgisayar yazdı. Yazarken
  context: ''
- text: İnternete kolay erişim sayesinde dünya daha da küçüldü. Bunun sonucunda
  context: ''
---

# Turkish GPT2 Model Finetuned 
# Türkçe GPT2 Modeli

## Model description

This is a GPT2-Small English based model finetuned and additionaly trainied with Wikipedia Articles in Turkish as of 28-10-2020

Live demo based on this work at : https://www.metayazar.com/

Fine tuned writer on this model: https://huggingface.co/gorkemgoknar/gpt2-turkish-writer

Work has been done on Pierre Guillou tutorial as on this page.
(https://github.com/piegu/fastai-projects/blob/master/finetuning-English-GPT2-any-language-Portuguese-HuggingFace-fastaiv2.ipynb) 

Code is converted to work with Fastai 2.X .

Using Google Colab for training. 

Additional tutorial and source will be in https://github.com/gorkemgoknar in later stage.

Current accuracy 33 %  , Perplexity : 51.88

Models are available:

* [gpt2-small-tuned-tr] (https://huggingface.co/gorkemgoknar/gpt2-small-turkish)
* [gpt2-small-turkish-writer] (https://huggingface.co/gorkemgoknar/gpt2-turkish-writer)

## Intended uses & limitations

#### How to use

#### Install

```python
from transformers import AutoTokenizer, AutoModelWithLMHead
import torch

tokenizer = AutoTokenizer.from_pretrained("gorkemgoknar/gpt2-small-turkish")
model = AutoModelWithLMHead.from_pretrained("gorkemgoknar/gpt2-small-turkish")

# Get sequence length max of 1024
tokenizer.model_max_length=1024 

model.eval()  # disable dropout (or leave in train mode to finetune)

```

#### Generate 1 word
```python
# input sequence
text = "Bu yazıyı bilgisayar yazdı."
inputs = tokenizer(text, return_tensors="pt")

# model output
outputs = model(**inputs, labels=inputs["input_ids"])
loss, logits = outputs[:2]
predicted_index = torch.argmax(logits[0, -1, :]).item()
predicted_text = tokenizer.decode([predicted_index])

# results
print('input text:', text)
print('predicted text:', predicted_text)

# input text: 
# predicted text:  

```

#### Generate Full Sequence
```python
# input sequence
text = "Bu yazıyı bilgisayar yazdı."
inputs = tokenizer(text, return_tensors="pt")

# model output using Top-k sampling text generation method
sample_outputs = model.generate(inputs.input_ids,
                                pad_token_id=50256,
                                do_sample=True, 
                                max_length=50, # put the token number you want
                                top_k=40,
                                num_return_sequences=1)

# generated sequence
for i, sample_output in enumerate(sample_outputs):
    print(">> Generated text {}\\\\
\\\\
{}".format(i+1, tokenizer.decode(sample_output.tolist())))

# >> Generated text
#    

```

#### Limitations and bias

The training data used for this model come from Turkish Wikipedia. We know it contains a lot of unfiltered content from the internet, which is far from neutral. 


## Training data

Wikipedia Turkish article dump as of 28-10-2020

## Training procedure


## Eval results

| epoch\\\\t|train_loss\\\\t|valid_loss\\\\t|accuracy\\\\t|perplexity\\\\t|time   |
| ----- | --------      |---------      | ----------    | ---------     | ----- |
|0\\\\t|4.777015\\\\t|4.621834\\\\t|0.292547\\\\t|101.680367\\\\t|2:42:05|
|1\\\\t|4.509412\\\\t|4.403999\\\\t|0.305574\\\\t|81.777267\\\\t|1:09:38|
|2\\\\t|4.169529\\\\t|4.120755\\\\t|0.324908\\\\t|61.605747\\\\t|1:07:45|
|3\\\\t|4.293973\\\\t|4.177899\\\\t|0.317211\\\\t|65.228653\\\\t|1:07:02|
|4\\\\t|4.049848\\\\t|3.949103\\\\t|0.338347\\\\t|51.888783\\\\t|1:05:53|

#Epoch 0 on Tesla T4, others on V100

```

