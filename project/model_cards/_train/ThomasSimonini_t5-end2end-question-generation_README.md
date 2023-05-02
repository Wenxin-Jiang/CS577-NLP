---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: t5-end2end-question-generation
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: squad
      type: squad
      args: plain_text
---

# t5-end2end-question-generation

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the squad dataset to generate questions based on a context. 


👉 If you want to learn how to fine-tune the t5 model to do the same, you can follow this [tutorial](https://colab.research.google.com/drive/1z-Zl2hftMrFXabYfmz8o9YZpgYx6sGeW?usp=sharing)


For instance:
```
Context: "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
```
```
Questions:

    Who created Python?,
    When was Python first released?
    What is Python's design philosophy?
```

It achieves the following results on the evaluation set:
- Loss: 1.5691


## Use the Model
```
from transformers import T5ForConditionalGeneration, T5TokenizerFast

hfmodel = T5ForConditionalGeneration.from_pretrained("ThomasSimonini/t5-end2end-question-generation")

text= "The abolition of feudal privileges by the National Constituent Assembly on 4 August 1789 and the Declaration \\nof the Rights of Man and of the Citizen (La Déclaration des Droits de l'Homme et du Citoyen), drafted by Lafayette \\nwith the help of Thomas Jefferson and adopted on 26 August, paved the way to a Constitutional Monarchy \\n(4 September 1791 – 21 September 1792). Despite these dramatic changes, life at the court continued, while the situation \\nin Paris was becoming critical because of bread shortages in September. On 5 October 1789, a crowd from Paris descended upon Versailles \\nand forced the royal family to move to the Tuileries Palace in Paris, where they lived under a form of house arrest under \\nthe watch of Lafayette's Garde Nationale, while the Comte de Provence and his wife were allowed to reside in the \\nPetit Luxembourg, where they remained until they went into exile on 20 June 1791."

def run_model(input_string, **generator_args):
  generator_args = {
  "max_length": 256,
  "num_beams": 4,
  "length_penalty": 1.5,
  "no_repeat_ngram_size": 3,
  "early_stopping": True,
  }
  input_string = "generate questions: " + input_string + " </s>"
  input_ids = tokenizer.encode(input_string, return_tensors="pt")
  res = hfmodel.generate(input_ids, **generator_args)
  output = tokenizer.batch_decode(res, skip_special_tokens=True)
  output = [item.split("<sep>") for item in output]
  return output
  
run_model(text)

=> [['When did the National Constituent Assembly abolish feudal privileges?',
  ' Who drafted the Declaration of the Rights of Man and of the Citizen?',
  ' When was the Constitutional Monarchy established?',
  ' What was the name of the Declaration that paved the way to a constitutional monarchy?',
  '']]

```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.5834        | 0.34  | 100  | 1.9107          |
| 1.9642        | 0.68  | 200  | 1.7227          |
| 1.8526        | 1.02  | 300  | 1.6627          |
| 1.7383        | 1.36  | 400  | 1.6354          |
| 1.7223        | 1.69  | 500  | 1.6154          |
| 1.6871        | 2.03  | 600  | 1.6096          |
| 1.6309        | 2.37  | 700  | 1.6048          |
| 1.6242        | 2.71  | 800  | 1.5923          |
| 1.6226        | 3.05  | 900  | 1.5855          |
| 1.5645        | 3.39  | 1000 | 1.5874          |
| 1.5705        | 3.73  | 1100 | 1.5822          |
| 1.5543        | 4.07  | 1200 | 1.5817          |
| 1.5284        | 4.41  | 1300 | 1.5841          |
| 1.5275        | 4.75  | 1400 | 1.5741          |
| 1.5269        | 5.08  | 1500 | 1.5715          |
| 1.5079        | 5.42  | 1600 | 1.5701          |
| 1.4876        | 5.76  | 1700 | 1.5754          |
| 1.498         | 6.1   | 1800 | 1.5699          |
| 1.4852        | 6.44  | 1900 | 1.5693          |
| 1.4776        | 6.78  | 2000 | 1.5691          |


### Framework versions

- Transformers 4.10.3
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
