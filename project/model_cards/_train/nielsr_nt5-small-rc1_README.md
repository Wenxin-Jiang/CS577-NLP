---
license: apache-2.0
tags:
datasets:
- drop
---

# NT5, a T5 model trained to perform numerical reasoning

T5-small model pre-trained on 3 million (partly synthetic) texts and fine-tuned on [DROP](https://allennlp.org/drop.html). It was introduced in the paper [NT5?! Training T5 to Perform Numerical Reasoning](https://arxiv.org/abs/2104.07307) by Yang et al. and first released in [this repository](https://github.com/lesterpjy/numeric-t5). As the original implementation was in Tensorflow 2, I've converted the weigths to PyTorch. This model corresponds to RC Experiment 1 (see the paper), their best performing model.

Disclaimer: The team releasing NT5 did not write a model card for this model so this model card has been written by me.

## Model description

The NT5 model is a T5 model, in other words, an encoder-decoder Transformer. In order to encourage numerical reasoning, the model was further pre-trained on three datasets designed to strengthen skills necessary for numerical reasoning over text (NRoT) and general reading comprehension before being fine-tuned on the Discrete Reasoning over Text (DROP) dataset.

## Intended uses & limitations

You can use the model for numerical reasoning over text. 

### How to use

Here is how to use this model:

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

context = """Saint Jean de Brébeuf was a French Jesuit missionary who
travelled to New France in 1625. There he worked primarily with the Huron
for the rest of his life, except for a few years in France from 1629 to
1633. He learned their language and culture, writing extensively about
each to aid other missionaries. In 1649, Br´ebeuf and another missionary
were captured when an Iroquois raid took over a Huron village . Together
with Huron captives, the missionaries were ritually tortured and killed
on March 16, 1649. Br´ebeuf was beatified in 1925 and among eight Jesuit
missionaries canonized as saints in the Roman Catholic Church in 1930."""

question = "How many years did Saint Jean de Brébeuf stay in New France 
before he went back to France for a few years?"

tokenizer = T5Tokenizer.from_pretrained("nielsr/nt5-small-rc1")
model = T5ForConditionalGeneration.from_pretrained("nielsr/nt5-small-rc1")

# encode context & question
input_text = f"answer_me: {question} context: {context}"
encoded_query = tokenizer(
                    input_text, 
                    return_tensors='pt', 
                    padding='max_length', 
                    truncation=True, 
                    max_length=512)

# generate answer
generated_answer = model.generate(input_ids=encoded_query["input_ids"], 
                                  attention_mask=encoded_query["attention_mask"], 
                                  max_length=54)

decoded_answer = tokenizer.decode(generated_answer.numpy()[0])
print("T5 Answer: ", decoded_answer)
T5 Answer: 4
```

## Evaluation results

This model achieves an F1 score of 0.7031 and exact match of 0.6687 on the development set of DROP. 


### BibTeX entry and citation info

```bibtex
@misc{yang2021nt5,
      title={NT5?! Training T5 to Perform Numerical Reasoning}, 
      author={Peng-Jian Yang and Ying Ting Chen and Yuechan Chen and Daniel Cer},
      year={2021},
      eprint={2104.07307},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@article{DBLP:journals/corr/abs-1903-00161,
  author    = {Dheeru Dua and
               Yizhong Wang and
               Pradeep Dasigi and
               Gabriel Stanovsky and
               Sameer Singh and
               Matt Gardner},
  title     = {{DROP:} {A} Reading Comprehension Benchmark Requiring Discrete Reasoning
               Over Paragraphs},
  journal   = {CoRR},
  volume    = {abs/1903.00161},
  year      = {2019},
  url       = {http://arxiv.org/abs/1903.00161},
  archivePrefix = {arXiv},
  eprint    = {1903.00161},
  timestamp = {Wed, 03 Jul 2019 07:17:04 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1903-00161.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
a service of Schloss Dagstuhl - Leibniz Center for Informatics\\\\thomebrowsesearchabout

```