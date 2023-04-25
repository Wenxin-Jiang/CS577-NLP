---
library_name: lucidrains/gated-state-spaces-pytorch
license: mit
datasets:
  - c4
pipeline_tag: text-generation
tags:
  - text generation
  - pytorch
  - causal-lm
  - gated-state-space
---

# [Gated State Space](https://arxiv.org/abs/2206.13947)

This repo contains pretrain model for the gated state space paper. The model has been trained on [C4 dataset](https://huggingface.co/datasets/c4). I have used [Lucidrains' implementation](https://github.com/lucidrains/gated-state-spaces-pytorch) ([commit](https://github.com/lucidrains/gated-state-spaces-pytorch/tree/32cd036e775112cc469e94fa1165fe111393708b)) for the model. I think the main benefit of this model is the ability to scale beyond the training context length. As authors noted in the paper, they trained the model on 4k sequence length but it generalized beyond that length. I have written a **blog post on how I started the training [here](https://naxalpha.substack.com/p/devlog-experiment-a2a468-gated-state)**.

**[Wandb Report is available at this link](https://wandb.ai/naxalpha/gated-state-space/reports/Gated-State-Space-Training-v1--VmlldzozMTYzMzY3?accessToken=zy10rrpofi9k7l52aqwiej8bk0ub302rdswfkxmf8y94dt2j6z4kxbca6ar3sc52)**

## How to use this.

Since it is not based on [transformers](https://github.com/huggingface/transformers/) library, it is a bit tricky to use the model out of the box. Here are the general steps:

1. `pip install gated-state-spaces-pytorch`
2. Download the model weights from [here](https://huggingface.co/naxalpha/gated-state-space/raw/main/model.pt).
3. Download the config from [here](https://huggingface.co/naxalpha/gated-state-space/raw/main/config.json).
4. Following code to patch the original model:
```python
    model = AutoregressiveWrapper(
        GatedStateSpacesLM(
            **config
        ),
    )
    model.net.to_logits = nn.Sequential(
        nn.LayerNorm(f_emb),
        model.net.to_logits,
    )
```
5. Load the state dict: `model.load_state_dict(torch.load('model.pt'))`
6. If you want to fine-tune the model, you can freeze the embeddings:
```python
    model.net.token_emb.weight.requires_grad_(False)
    model.net.token_emb.weight.copy_(emb)

    model.net.to_logits[1].weight.requires_grad_(False)
    model.net.to_logits[1].weight.copy_(emb)
```

Training code is available in this repo. [Link to the training script](https://huggingface.co/naxalpha/gated-state-space/blob/main/app.py).

## Training Information

Here are the details of the training:

- Objective: `Alternate between simple cross entropy and GPT-2 XL distillation`
- Gradient Accumulation: `4`
- Batch Size: `8`
- Sequence Length `128`
- Learning Rate: `2e-5`
- Optimizer: `AdamW`
- Gradient Norm Clipping: `1.0`
- Hardware: `RTX 3090` on [vast.ai](vast.ai)
- Training Cost: `~20$`
- Training Time: `~3 days`
- Number of steps: `557,000`
- Tokens seen: `570 million`
- Final loss: `~3.9`

## Fine-Tuning Info:

[model2.pt](https://huggingface.co/naxalpha/gated-state-space/blob/main/) is available as fine-tuned version with longer context length.

- Objective: `Simple Cross Entropy`
- Gradient Accumulation: `4`
- Batch Size: `1`
- Sequence Length: `2048`
- Learning Rate: `5e-6`
- Embeddings: `unfrozen for fine-tuning`
- Gradient Norm Clipping: `1.0`
- Hardware: `2x3090` on vast.ai
- Extra Tricks: `Used HuggingFace Accelerate with Full Sharding without CPU offload`
