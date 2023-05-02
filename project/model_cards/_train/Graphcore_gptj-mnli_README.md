---
license: apache-2.0
language:
- en
model-index:
- name: Graphcore/gptj-mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MNLI
      type: glue
      split: validation_mismatched
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.825
      config: mnli_mismatched
datasets:
- glue
tags:
- pytorch
- causal-lm
- text-classification
- text-generation
pipeline_tag: text-generation
widget:
- text: "mnli hypothesis: Your contributions were of no help with our students' education. premise: Your contribution helped make it possible for us to provide our students with a quality education. target:"
---

# Graphcore/gptj-mnli
This model is the fine-tuned version of [EleutherAI/gpt-j-6B](https://huggingface.co/EleutherAI/gpt-j-6B) on the [GLUE MNLI dataset](https://huggingface.co/datasets/glue#mnli).
MNLI dataset consists of pairs of sentences, a *premise* and a *hypothesis*.
The task is to predict the relation between the premise and the hypothesis, which can be:
- `entailment`: hypothesis follows from the premise,
- `contradiction`: hypothesis contradicts the premise,
- `neutral`: hypothesis and premise are unrelated.

We finetune the model as a Causal Language Model (CLM): given a sequence of tokens, the task is to predict the next token.
To achieve this, we create a stylised prompt string, following the approach of [T5 paper](https://arxiv.org/pdf/1910.10683.pdf).
```shell
mnli hypothesis: {hypothesis} premise: {premise} target: {class_label} <|endoftext|>
```
For example:
```
mnli hypothesis: Your contributions were of no help with our students' education. premise: Your contribution helped make it possible for us to provide our students with a quality education. target: contradiction <|endoftext|>
```

## Model description

GPT-J 6B is a transformer model trained using Ben Wang's [Mesh Transformer JAX](https://github.com/kingoflolz/mesh-transformer-jax/). "GPT-J" refers to the class of model, while "6B" represents the number of trainable parameters.

<figure>

| Hyperparameter       | Value      |
|----------------------|------------|
| \\(n_{parameters}\\) | 6053381344 |
| \\(n_{layers}\\)     | 28&ast;    |
| \\(d_{model}\\)      | 4096       |
| \\(d_{ff}\\)         | 16384      |
| \\(n_{heads}\\)      | 16         |
| \\(d_{head}\\)       | 256        |
| \\(n_{ctx}\\)        | 2048       |
| \\(n_{vocab}\\)      | 50257/50400&dagger; (same tokenizer as GPT-2/3)  |
| Positional Encoding  | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864) |
| RoPE Dimensions      | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |
<figcaption><p><strong>&ast;</strong> Each layer consists of one feedforward block and one self attention block.</p>
<p><strong>&dagger;</strong> Although the embedding matrix has a size of 50400, only 50257 entries are used by the GPT-2 tokenizer.</p></figcaption></figure>

The model consists of 28 layers with a model dimension of 4096, and a feedforward dimension of 16384. The model
dimension is split into 16 heads, each with a dimension of 256. Rotary Position Embedding (RoPE) is applied to 64
dimensions of each head. The model is trained with a tokenization vocabulary of 50257, using the same set of BPEs as
GPT-2/GPT-3.

[EleutherAI/gpt-j-6B](https://huggingface.co/EleutherAI/gpt-j-6B), our starting point for finetuning, is trained on [the Pile](https://pile.eleuther.ai), a large-scale curated dataset created by [EleutherAI](https://www.eleuther.ai).

## Fine-tuning and validation data
Fine tuning is done using the `train` split of the GLUE MNLI dataset and the performance is measured using the [validation_mismatched](https://huggingface.co/datasets/glue#mnli_mismatched) split.

`validation_mismatched` means validation examples are not derived from the same sources as those in the training set and therefore not closely resembling any of the examples seen at training time.

Data splits for the mnli dataset are the following

|train |validation_matched|validation_mismatched|
|-----:|-----------------:|--------------------:|
|392702|              9815|                 9832|

## Fine-tuning procedure
Fine tuned on a Graphcore IPU-POD64 using `popxl`.     

Prompt sentences are tokenized and packed together to form 1024 token sequences, following [HF packing algorithm](https://github.com/huggingface/transformers/blob/v4.20.1/examples/pytorch/language-modeling/run_clm.py). No padding is used.
The packing process works in groups of 1000 examples and discards any remainder from each group that isn't a whole sequence.
For the 392,702 training examples this gives a total of 17,762 sequences per epoch. 

Since the model is trained to predict the next token, labels are simply the input sequence shifted by one token.
Given the training format, no extra care is needed to account for different sequences: the model does not need to know which sentence a token belongs to.

### Hyperparameters:
- optimiser: AdamW (beta1: 0.9, beta2: 0.999, eps: 1e-6, weight decay: 0.0, learning rate: 5e-6)
- learning rate schedule: warmup schedule (min: 1e-7, max: 5e-6, warmup proportion: 0.005995)
- batch size: 128
- training steps: 300. Each epoch consists of ceil(17,762/128) steps, hence 300 steps are approximately 2 epochs.  

## Performance
The resulting model matches SOTA performance with 82.5% accuracy.
```
Total number of examples                 9832
Number with badly formed result          0
Number with incorrect result             1725
Number with correct result               8107 
[82.5%]

example 0 = {'prompt_text': "mnli hypothesis: Your contributions were of no help with our students' education. premise: Your contribution helped make it possible for us to provide our students with a quality education. target:", 'class_label': 'contradiction'}
result = {'generated_text': ' contradiction'}

First 10 generated_text and expected class_label results:
 0: 'contradiction'                          contradiction
 1: 'contradiction'                          contradiction
 2: 'entailment'                             entailment
 3: 'contradiction'                          contradiction
 4: 'entailment'                             entailment
 5: 'entailment'                             entailment
 6: 'contradiction'                          contradiction
 7: 'contradiction'                          contradiction
 8: 'entailment'                             neutral
 9: 'contradiction'                          contradiction
```
## How to use
The model can be easily loaded using AutoModelForCausalLM.
You can use the pipeline API for text generation.

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')
hf_model = AutoModelForCausalLM.from_pretrained("Graphcore/gptj-mnli", pad_token_id=tokenizer.eos_token_id)
generator =  pipeline('text-generation', model=hf_model, tokenizer=tokenizer)
prompt = "mnli hypothesis: Your contributions were of no help with our students' education." \
         "premise: Your contribution helped make it possible for us to provide our students with a quality education. target:"
out = generator(prompt, return_full_text=False, max_new_tokens=5, top_k=1)
# [{'generated_text': ' contradiction'}]
```

You can create prompt-like inputs starting from GLUE MNLI dataset using functions provided in the `data_utils.py` script.
```python
from datasets import load_dataset
from data_utils import form_text, split_text

dataset = load_dataset('glue', 'mnli', split='validation_mismatched')
dataset = dataset.map(
    form_text, remove_columns=['hypothesis', 'premise','label', 'idx'])
# dataset[0] {'text': "mnli hypothesis: Your contributions were of no help with our students' education. premise: Your contribution helped make it possible for us to provide our students with a quality education. target: contradiction<|endoftext|>"}
dataset = dataset.map(split_text, remove_columns=['text'])
# dataset[0] {'prompt_text': "mnli hypothesis: Your contributions were of no help with our students' education. premise: Your contribution helped make it possible for us to provide our students with a quality education. target:",
#             'class_label': 'contradiction'}
```