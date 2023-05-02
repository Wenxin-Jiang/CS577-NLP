---
language:
- en
tags:
- pytorch
- causal-lm
license: apache-2.0
datasets:
- the_pile
---

GPT-NeoX-20B is a 20 billion parameter autoregressive language model trained 
on [the Pile](https://pile.eleuther.ai/) using the [GPT-NeoX 
library](https://github.com/EleutherAI/gpt-neox). Its architecture intentionally 
resembles that of GPT-3, and is almost identical to that of [GPT-J-
6B](https://huggingface.co/EleutherAI/gpt-j-6B). Its training dataset contains 
a multitude of English-language texts, reflecting the general-purpose nature 
of this model. See the [accompanying paper](https://arxiv.org/abs/2204.06745) 
for details about model architecture (including how it differs from GPT-3), 
training procedure, and additional evaluations.

### Model details

- Developed by: [EleutherAI](http://eleuther.ai)
- Model type: Transformer-based Language Model
- Language: English
- Learn more: [GPT-NeoX-20B: An Open-Source Autoregressive Language 
Model](https://arxiv.org/abs/2204.06745). For details about the training dataset, 
see [the Pile paper](https://arxiv.org/abs/2101.00027), and [its data
sheet](https://arxiv.org/abs/2201.07311).
- License: Apache 2.0
- Contact: to ask questions about this model, join the [EleutherAI 
Discord](https://discord.gg/zBGx3azzUn), and post them in `#release-discussion`. 
Please read the existing GPT-NeoX-20B documentation before asking about the model 
on Discord. For general correspondence: [contact@eleuther.
ai](mailto:contact@eleuther.ai).

<figure style="width:30em">

| Hyperparameter         | Value       |
| ---------------------- | ----------- |
| n<sub>parameters</sub> | 20554567680 |
| n<sub>layers</sub>     | 44          |
| d<sub>model</sub>      | 6144        |
| n<sub>heads</sub>      | 64          |
| d<sub>head</sub>       | 96          |
| n<sub>vocab</sub>      | 50257       |
| Sequence Length        | 2048        |
| Learning Rate          | 0.97 x 10<sup>-5</sup> |
| Positional Encoding    | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864) |
</figure>

### Uses and limitations

#### Intended use

GPT-NeoX-20B was developed primarily for research purposes. It learns an inner 
representation of the English language that can be used to extract features 
useful for downstream tasks.

In addition to scientific uses, you may also further fine-tune and adapt 
GPT-NeoX-20B for deployment, as long as your use is in accordance with the 
Apache 2.0 license. This model works with the [Transformers 
Library](https://huggingface.co/docs/transformers/index). If you decide to use 
pre-trained GPT-NeoX-20B as a basis for your fine-tuned model, please note that 
you need to conduct your own risk and bias assessment. 

#### Out-of-scope use

GPT-NeoX-20B is **not** intended for deployment as-is. It is not a product 
and cannot be used for human-facing interactions without supervision.

GPT-NeoX-20B has not been fine-tuned for downstream tasks for which language 
models are commonly deployed, such as writing genre prose, or commercial 
chatbots. This means GPT-NeoX-20B will likely **not** respond to a given prompt 
the way products such as ChatGPT do. This is because, unlike GPT-NeoX-20B, 
ChatGPT was fine-tuned using methods such as Reinforcement Learning from Human 
Feedback (RLHF) to better “understand” human instructions and dialogue.

This model is English-language only, and thus cannot be used for translation
or generating text in other languages.

#### Limitations and biases

The core functionality of GPT-NeoX-20B is to take a string of text and predict 
the next token. Remember that the statistically most likely next token need 
not result in the most “accurate” text. Never rely on GPT-NeoX-20B to produce 
factually accurate output.

This model was trained on [the Pile](https://pile.eleuther.ai/), a dataset 
known to contain profanity and texts that are lewd or otherwise offensive. 
See [Section 6 of the Pile paper](https://arxiv.org/abs/2101.00027) for a 
discussion of documented biases with regards to gender, religion, and race. 
GPT-NeoX-20B may produce socially unacceptable or undesirable text, *even if*
 the prompt itself does not include anything explicitly offensive. 

We recommend curating the outputs of this model before presenting it to a human 
reader. Please inform your audience that you are using artificially generated 
text. 

#### How to use
 If you simply want to try out some prompts, check out [this 
 playground](https://20b.eleuther.ai/).
 
 GPT-NeoX-20B can be loaded using the `AutoModelForCausalLM` functionality:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b")
```

### Training

#### Training dataset

The Pile is a 825GiB general-purpose dataset in English. It was created by 
EleutherAI specifically for training large language models. It contains texts 
from 22 diverse sources, roughly broken down into five categories: academic 
writing (e.g. arXiv), internet (e.g. CommonCrawl), prose (e.g. Project 
Gutenberg), dialogue (e.g. YouTube subtitles), and miscellaneous (e.g. GitHub, 
Enron Emails). See [the Pile paper](https://arxiv.org/abs/2101.00027) for 
a breakdown of all data sources, methodology, and a discussion of ethical 
implications. Consult [the datasheet](https://arxiv.org/abs/2201.07311) for 
more detailed documentation about the Pile and its component datasets. The 
Pile can be downloaded from the [official website](https://pile.eleuther.ai/), 
or from a [community mirror](https://the-eye.eu/public/AI/pile/).

The Pile was **not** deduplicated before being used to train GPT-NeoX-20B.

#### Training procedure

GPT-NeoX-20B was trained with a batch size of approximately 3.15M tokens 
(1538 sequences of 2048 tokens each), for a total of 150,000 steps. Tensor 
parallelism and pipeline parallelism were used to distribute the model across 
GPUs. Additional details about the training procedure are in [Section 3 of 
the accompanying paper](https://arxiv.org/abs/2204.06745).


### Evaluations

<figure style="width:55em">

| Model         | OpenAI’s LAMBADA | SciQ          | PIQA          | TriviaQA      | ARC (Challenge) |
| ------------- | :--------------: | :-----------: | :-----------: | :-----------: | :-------------: |
| GPT-J-6B      | 0.683 ± 0.006    | 0.910 ± 0.009 | 0.752 ± 0.010 | 0.170 ± 0.004 | 0.340 ± 0.014   |
| FairSeq 6.7B  | 0.673 ± 0.007    | 0.895 ± 0.010 | 0.762 ± 0.010 | 0.221 ± 0.004 | 0.329 ± 0.014   |
| GPT-3 Curie   | 0.693 ± 0.006    | 0.918 ± 0.009 | 0.767 ± 0.010 | 0.196 ± 0.004 | 0.334 ± 0.014   |
| FairSeq 13B   | 0.709 ± 0.006    | 0.910 ± 0.009 | 0.769 ± 0.010 | 0.270 ± 0.004 | 0.345 ± 0.014   |
| GPT-NeoX-20B  | 0.720 ± 0.006    | 0.928 ± 0.008 | 0.779 ± 0.010 | 0.259 ± 0.004 | 0.380 ± 0.014   |
| GPT-3 DaVinci | 0.752 ± 0.006    | 0.949 ± 0.007 | 0.791 ± 0.009 | 0.409 ± 0.005 | 0.435 ± 0.014   |
<figcaption>Zero-shot performance on selected natural language tasks.</figcaption>
</figure>

This is a heavily abridged version of the evaluation results. Appendix D of the
 [GPT-NeoX-20B paper](https://arxiv.org/abs/2204.06745) compares more model 
sizes, and contains additional evaluations, including on: zero and five-shot 
natural language tasks, zero and five-shot Basic Arithmetic and MATH, 
and zero-shot Hendrycks tasks.

### BibTeX

To cite the GPT-NeoX-20B paper:

```
@misc{https://doi.org/10.48550/arxiv.2204.06745,
  doi = {10.48550/ARXIV.2204.06745},
  
  url = {https://arxiv.org/abs/2204.06745},
  
  author = {Black, Sid and Biderman, Stella and Hallahan, Eric and Anthony, Quentin and Gao, Leo and Golding, Laurence and He, Horace and Leahy, Connor and McDonell, Kyle and Phang, Jason and Pieler, Michael and Prashanth, USVSN Sai and Purohit, Shivanshu and Reynolds, Laria and Tow, Jonathan and Wang, Ben and Weinbach, Samuel},
  
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {GPT-NeoX-20B: An Open-Source Autoregressive Language Model},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {Creative Commons Attribution 4.0 International}
}
```
