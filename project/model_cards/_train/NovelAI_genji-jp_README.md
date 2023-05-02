---
language:
- ja
- en
tags:
- pytorch
- causal-lm
license: apache-2.0

---

# Genji-JP 6B

Please check our blog post for more details, samples, evaluations and more:
[Blogpost](https://blog.novelai.net/data-efficient-language-transfer-with-gpt-j-45daedaaf35a)

## Model Description

Genji-JP 6B is a model finetuned on our Japanese storytelling dataset based on EleutherAI's GPT-J 6B model. This particular model is trained on Japanese web novels.

| Hyperparameter    | Value  | 
|-------------------|--------|
| n_parameters      | 6,053,381,344 |
| n_layers          | 28*    |
| d_model           | 4,096  |
| d_ff              | 16,384 |
| n_heads           | 16     |
| d_head            | 256    |
| n_ctx             | 2,048  |
| n_vocab           | 50,400 (same tokenizer as GPT-2/3)  |
| position encoding | [Rotary position encodings (RoPE)](https://arxiv.org/abs/2104.09864) |
| RoPE dimensions   | [64](https://github.com/kingoflolz/mesh-transformer-jax/blob/f2aa66e0925de6593dcbb70e72399b97b4130482/mesh_transformer/layers.py#L223) |

`*` each layer consists of one feedforward block and one self attention block

The model consists of 28 layers with a model dimension of 4096, and a feedforward dimension of 16384. The model
dimension is split into 16 heads, each with a dimension of 256. Rotary position encodings (RoPE) was applied to 64
dimensions of each head. The model is trained with a tokenization vocabulary of 50257, using the same set of BPEs as
GPT-2/GPT-3.

## Training data

GPT-J 6B was pretrained on the [Pile](pile.eleuther.ai), a large scale curated dataset created by EleutherAI for the purpose of training this model. After the pre-training, it's finetuned on our Japanese storytelling dataset. Check our blog post for more details.

### How to use

```
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("NovelAI/genji-jp", torch_dtype=torch.float16, low_cpu_mem_usage=True).eval().cuda()
text = '''あらすじ：あなたは異世界に転生してしまいました。勇者となって、仲間を作り、異世界を冒険しよう！
***
転生すると、ある能力を手に入れていた。それは、'''

tokens = tokenizer(text, return_tensors="pt").input_ids
generated_tokens = model.generate(tokens.long().cuda(), use_cache=True, do_sample=True, temperature=1, top_p=0.9, repetition_penalty=1.125, min_length=1, max_length=len(tokens[0]) + 400, pad_token_id=tokenizer.eos_token_id)
last_tokens = generated_tokens[0]
generated_text = tokenizer.decode(last_tokens).replace("�", "")
print("Generation:\n" + generated_text)
```
When run, produces output like this:
```
Generation:
あらすじ：あなたは異世界に転生してしまいました。勇者となって、仲間を作り、異世界を冒険しよう！
***
転生すると、ある能力を手に入れていた。それは、『予知』だ。過去から未来のことを、誰も知らない出来事も含めて見通すことが出来る。
悪魔の欠片と呼ばれる小さな結晶を取り込んで、使役することが出来る。人を惹きつけ、堕落させる。何より、俺は男なんて居なかったし、女に興味もない。……そんなクズの片棒を担ぎ上げる奴が多くなると思うと、ちょっと苦しい。
だが、一部の人間には協力者を得ることが出来る。目立たない街にある寺の中で、常に家に引きこもっている老人。そんなヤツの魂をコントロールすることが出来るのだ。便利な能力だ。しかし、裏切り者は大勢いる。気を抜けば、狂う。だから注意が必要だ。
――「やってやるよ」
　アーロンは不敵に笑った。この
```

## Acknowledgements

This project was possible because of the compute provided by the
[TPU Research Cloud](https://sites.research.google/trc/)

Thanks [EleutherAI](https://eleuther.ai/) for pretraining the GPT-J 6B model.

Thanks to everyone who contributed to this project!

- [Finetune](https://github.com/finetuneanon)
- [Aero](https://github.com/AeroScripts)
- [Kurumuz](https://github.com/kurumuz)