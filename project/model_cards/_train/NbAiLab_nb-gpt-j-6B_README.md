---
language:
- 'no'
- nb
- nn
tags:
- pytorch
- causal-lm
license: apache-2.0
datasets:
- NbAiLab/NCC
- mc4
- oscar
pipeline_tag: text-generation
---




- **Release ✨v1✨** (January 18th, 2023) *[Full-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1), [sharded](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1-sharded), [half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1-float16), and [mesh-transformers-jax](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1-mesh) weights*
<details><summary>All checkpoints</summary>

    - **Release v1beta5** (December 18th, 2022) *[Full-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta5), [sharded](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta5-sharded), and [half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta5-float16) weights*
    - **Release v1beta4** (October 28th, 2022) *[Full-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta4), [sharded](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta4-sharded), and [half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta4-float16) weights*
    - **Release v1beta3** (August 8th, 2022) *[Full-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta3), [sharded](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta3-sharded), and [half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta3-float16) weights*
    - **Release v1beta2** (June 18th, 2022) *[Full-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta2), [sharded](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/sharded), and [half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta2-float16) weights*
    - **Release v1beta1** (April 28th, 2022) *[Half-precision](https://huggingface.co/NbAiLab/nb-gpt-j-6B/tree/v1beta1-float16) weights*

</details>

# NB-GPT-J-6B

## Demo: https://ai.nb.no/demo/nb-gpt-j-6B/ (Be patient, it runs on CPU 😅)

## Model Description

NB-GPT-J-6B is a Norwegian finetuned version of GPT-J 6B, a transformer model trained using Ben Wang's [Mesh Transformer JAX](https://github.com/kingoflolz/mesh-transformer-jax/). "GPT-J" refers to the class of model, while "6B" represents the number of trainable parameters (6 billion parameters).

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

## Training data

NB-GPT-J-6B was finetuned on [NCC](https://huggingface.co/datasets/NbAiLab/NCC), the Norwegian Colossal Corpus, plus other Internet sources like Wikipedia, mC4, and OSCAR.

## Training procedure

This model was finetuned for 130 billion tokens over 1,000,000 steps on a TPU v3-8 VM. It was trained as an autoregressive language model, using cross-entropy loss to maximize the likelihood of predicting the next token correctly.

## Intended Use and Limitations

NB-GPT-J-6B learns an inner representation of the Norwegian language that can be used to extract features useful for downstream tasks. The model is best at what it was pretrained for however, which is generating text from a prompt.

### How to use

This model can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("NbAiLab/nb-gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("NbAiLab/nb-gpt-j-6B")
```

### Limitations and Biases

As the original GPT-J model, the core functionality of NB-GPT-J-6B is taking a string of text and predicting the next token. While language models are widely used for tasks other than this, there are a lot of unknowns with this work. When prompting NB-GPT-J-6B it is important to remember that the statistically most likely next token is often not the token that produces the most "accurate" text. Never depend upon NB-GPT-J-6B to produce factually accurate output.

The original GPT-J was trained on the Pile, a dataset known to contain profanity, lewd, and otherwise abrasive language. Depending upon use case GPT-J may produce socially unacceptable text. See [Sections 5 and 6 of the Pile paper](https://arxiv.org/abs/2101.00027) for a more detailed analysis of the biases in the Pile. A fine-grained analysis of the bias contained in the corpus used for fine-tuning is still pending.

As with all language models, it is hard to predict in advance how NB-GPT-J-6B will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results.

## Evaluation results

We still have to find proper datasets to evaluate the model, so help is welcome!

## Citation and Related Information

### BibTeX entry

To cite this model or the corpus used:
```bibtex
@inproceedings{kummervold2021operationalizing,
  title={Operationalizing a National Digital Library: The Case for a Norwegian Transformer Model},
  author={Kummervold, Per E and De la Rosa, Javier and Wetjen, Freddy and Brygfjeld, Svein Arne},
  booktitle={Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
  pages={20--29},
  year={2021},
  url={https://aclanthology.org/2021.nodalida-main.3/}
}
```

If you use this model, we would love to hear about it! Reach out on twitter, GitHub, Discord, or shoot us an email.

## Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions. When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence. In no event shall the owner of the models (The National Library of Norway) be liable for any results arising from the use made by third parties of these models.


## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/), as well as the Cloud TPU team for providing early access to the [Cloud TPU VM](https://cloud.google.com/blog/products/compute/introducing-cloud-tpu-vms) Alpha. Specially, to [Stella Biderman](https://www.stellabiderman.com) for her general openness, and [Ben Wang](https://github.com/kingoflolz/mesh-transformer-jax) for the main codebase.