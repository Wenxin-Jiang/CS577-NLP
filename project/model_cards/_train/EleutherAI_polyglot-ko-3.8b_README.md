---
language:
- ko
tags:
- pytorch
- causal-lm
license: apache-2.0

---
# Polyglot-Ko-3.8B

## Model Description
Polyglot-Ko is a series of large-scale Korean autoregressive language models made by the EleutherAI polyglot team.

| Hyperparameter       | Value                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| \\(n_{parameters}\\) | 3,809,974,272                                                                                                                           |
| \\(n_{layers}\\)     | 32                                                                                                                                     |
| \\(d_{model}\\)      | 3,072                                                                                                                                   |
| \\(d_{ff}\\)         | 12,288                                                                                                                                   |
| \\(n_{heads}\\)      | 24                                                                                                                                     |
| \\(d_{head}\\)       | 128                                                                                                                                    |
| \\(n_{ctx}\\)        | 2,048                                                                                                                                   |
| \\(n_{vocab}\\)      | 30,003 / 30,080                                                                                                                        |
| Positional Encoding  | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864)                                                                   |
| RoPE Dimensions      | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |

The model consists of 32 transformer layers with a model dimension of 3072, and a feedforward dimension of 12288. The model
dimension is split into 24 heads, each with a dimension of 128. Rotary Position Embedding (RoPE) is applied to 64
dimensions of each head. The model is trained with a tokenization vocabulary of 30003.

## Training data

Polyglot-Ko-3.8B was trained on 863 GB of Korean language data (1.2TB before processing), a large-scale dataset curated by [TUNiB](https://tunib.ai/). The data collection process has abided by South Korean laws. This dataset was collected for the purpose of training Polyglot-Ko models, so it will not be released for public use.  

| Source                              |Size (GB) | Link                                  |
|-------------------------------------|---------|------------------------------------------|
| Korean blog posts                   | 682.3   | -                                        |
| Korean news dataset                 | 87.0  | -                                        |
| Modu corpus                         | 26.4  |corpus.korean.go.kr             |
| Korean patent dataset               | 19.0  | -                                        |
| Korean Q & A dataset                | 18.1  | -                                        |
| KcBert dataset                      | 12.7  | github.com/Beomi/KcBERT          |
| Korean fiction dataset              | 6.1   | -                                        |
| Korean online comments              | 4.2   | -                                    |
| Korean wikipedia                    | 1.4   | ko.wikipedia.org                 |
| Clova call                          | < 1.0   | github.com/clovaai/ClovaCall     |
| Naver sentiment movie corpus        | < 1.0   | github.com/e9t/nsmc              |
| Korean hate speech dataset          | < 1.0   | -                                        |
| Open subtitles                      | < 1.0  | opus.nlpl.eu/OpenSubtitles.php   |
| AIHub various tasks datasets        | < 1.0   |aihub.or.kr                 |
| Standard Korean language dictionary | < 1.0  | stdict.korean.go.kr/main/main.do |
                            
Furthermore, in order to avoid the model memorizing and generating personally identifiable information (PII) in the training data, we masked out the following sensitive information in the pre-processing stage:

* `<|acc|>` : bank account number
* `<|rrn|>` : resident registration number
* `<|tell|>` : phone number

## Training procedure
Polyglot-Ko-3.8B was trained for 219 billion tokens over 105,000 steps on 256 A100 GPUs with the [GPT-NeoX framework](https://github.com/EleutherAI/gpt-neox). It was trained as an autoregressive language model, using cross-entropy loss to maximize the likelihood of predicting the next token. 

## How to use

This model can be easily loaded using the `AutoModelForCausalLM` class:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/polyglot-ko-3.8b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/polyglot-ko-3.8b")
```

## Evaluation results

We evaluate Polyglot-Ko-3.8B on [KOBEST dataset](https://arxiv.org/abs/2204.04541), a benchmark with 5 downstream tasks, against comparable models such as skt/ko-gpt-trinity-1.2B-v0.5, kakaobrain/kogpt and facebook/xglm-7.5B, using the prompts provided in the paper. 

The following tables show the results when the number of few-shot examples differ. You can reproduce these results using the [polyglot branch of lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot) and the following scripts. For a fair comparison, all models were run under the same conditions and using the same prompts. In the tables, `n` refers to the number of few-shot examples. 

```console
python main.py \
   --model gpt2 \
   --model_args pretrained='EleutherAI/polyglot-ko-3.8b' \
   --tasks kobest_copa,kobest_hellaswag \
   --num_fewshot $YOUR_NUM_FEWSHOT \
   --batch_size $YOUR_BATCH_SIZE \
   --device $YOUR_DEVICE \
   --output_path $/path/to/output/
```

### COPA (F1)

| Model                                                                                        | params | n=0 | n=5 | n=10 | n=50 |
|----------------------------------------------------------------------------------------------|--------|--------|--------|---------|---------|
| [skt/ko-gpt-trinity-1.2B-v0.5](https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5)          | 1.2B   | 0.6696 | 0.6477 | 0.6419  | 0.6514  |
| [kakaobrain/kogpt](https://huggingface.co/kakaobrain/kogpt)                                  | 6.0B   | 0.7345 | 0.7287 | 0.7277  | 0.7479  |
| [facebook/xglm-7.5B](https://huggingface.co/facebook/xglm-7.5B)                              | 7.5B   | 0.6723 | 0.6731 | 0.6769  | 0.7119  |
| [EleutherAI/polyglot-ko-1.3b](https://huggingface.co/EleutherAI/polyglot-ko-1.3b)            | 1.3B   | 0.7196 | 0.7193 | 0.7204  | 0.7206  |
| **[EleutherAI/polyglot-ko-3.8b](https://huggingface.co/EleutherAI/polyglot-ko-3.8b) (this)** | **3.8B**   | **0.7595** | **0.7608** | **0.7638**  | **0.7788**  |
| [EleutherAI/polyglot-ko-5.8b](https://huggingface.co/EleutherAI/polyglot-ko-5.8b)            | 5.8B   | 0.7745 | 0.7676 | 0.7775  | 0.7887  |
| [EleutherAI/polyglot-ko-12.8b](https://huggingface.co/EleutherAI/polyglot-ko-12.8b)          | 12.8B  | 0.7937 | 0.8108 | 0.8037  | 0.8369  |

<img src="https://user-images.githubusercontent.com/19511788/233820235-6f617932-3b18-4534-be14-8df9e80b8a06.jpg" width="1000px">

### HellaSwag (F1)

| Model                                                                                          | params |n=0 | n=5 | n=10 | n=50 |
|------------------------------------------------------------------------------------------------|--------|--------|--------|---------|---------|
| [skt/ko-gpt-trinity-1.2B-v0.5](https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5)            | 1.2B   | 0.5243 | 0.5272 | 0.5166  | 0.5352  |
| [kakaobrain/kogpt](https://huggingface.co/kakaobrain/kogpt)                                    | 6.0B   | 0.5590 | 0.5833 | 0.5828  | 0.5907  |
| [facebook/xglm-7.5B](https://huggingface.co/facebook/xglm-7.5B)                                | 7.5B   | 0.5665 | 0.5689 | 0.5565  | 0.5622  |
| [EleutherAI/polyglot-ko-1.3b](https://huggingface.co/EleutherAI/polyglot-ko-1.3b)              | 1.3B   | 0.5247 | 0.5260 | 0.5278  | 0.5427  |
| **[EleutherAI/polyglot-ko-3.8b](https://huggingface.co/EleutherAI/polyglot-ko-3.8b) (this)**   | **3.8B** | **0.5707** | **0.5830** | **0.5670**  | **0.5787**  |
| [EleutherAI/polyglot-ko-5.8b](https://huggingface.co/EleutherAI/polyglot-ko-5.8b)              | 5.8B   | 0.5976 | 0.5998 | 0.5979  | 0.6208  |
| [EleutherAI/polyglot-ko-12.8b](https://huggingface.co/EleutherAI/polyglot-ko-12.8b)            | 12.8B  | 0.5954 | 0.6306 | 0.6098  | 0.6118  |

<img src="https://user-images.githubusercontent.com/19511788/233820233-0127983e-4b37-48ce-89e5-51509ed9b1f2.jpg" width="1000px">

## Limitations and Biases

Polyglot-Ko has been trained to optimize next token prediction. Language models such as this are often used for a wide variety of tasks and it is important to be aware of possible unexpected outcomes. For instance, Polyglot-Ko will not always return the most factual or accurate response but the most statistically likely one. In addition, Polyglot may produce socially unacceptable or offensive content. We recommend having a human curator or other filtering mechanism to censor sensitive content. 

## Citation and Related Information
### BibTeX entry
If you find our work useful, please consider citing:
```bibtex
@misc{polyglot-ko,
  title = {{Polyglot-Ko: Open-Source Korean Autoregressive Language Model}},
  author = {Ko, Hyunwoong and Yang, Kichang and Ryu, Minho and Choi, Taekyoon and Yang, Seungmu and Hyun, jiwung and Park, Sungho},
  url = {https://www.github.com/eleutherai/polyglot},
  month = {9},
  year = {2022},
}
```

### Licensing
All our models are licensed under the terms of the Apache License 2.0.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### Acknowledgement

This project was made possible thanks to the computing resources from [Stability.ai](https://stability.ai), and thanks to [TUNiB](https://tunib.ai) for providing a large-scale Korean dataset for this work.
