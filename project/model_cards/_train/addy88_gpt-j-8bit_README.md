This Model is 8bit Version of EleutherAI/gpt-j-6B. It is converted by Facebook's bitsandbytes library. The original GPT-J takes 22+ GB memory for float32 parameters alone, and that's before you account for gradients & optimizer. So for finetuning on single GPU This model is converted into 8bit.

Here's how to run it: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KNf5siQdM7ILQM-pHsP6gNVPKl1SJdU1)
__The [original GPT-J](https://huggingface.co/EleutherAI/gpt-j-6B/tree/main)__ takes 22+ GB memory for float32 parameters alone, and that's before you account for gradients & optimizer. Even if you cast everything to 16-bit, it will still not fit onto most single-GPU setups short of A6000 and A100. You can inference it [on TPU](https://colab.research.google.com/github/kingoflolz/mesh-transformer-jax/blob/master/colab_demo.ipynb) or CPUs, but fine-tuning is way more expensive.
Here, we apply several techniques to make GPT-J usable and fine-tunable on a single GPU with ~11 GB memory:
- large weight tensors are quantized using dynamic 8-bit quantization and de-quantized just-in-time for multiplication
- using gradient checkpoints to store one only activation per layer: using dramatically less memory at the cost of 30% slower training
- scalable fine-tuning with [LoRA](https://arxiv.org/abs/2106.09685) and [8-bit Adam](https://arxiv.org/abs/2110.02861)
In other words, all of the large weight-matrices are frozen in 8-bit, and you only train small adapters and optionally 1d tensors (layernorm scales, biases).
![img](https://i.imgur.com/n4XXo1x.png)
__Does 8-bit affect model quality?__ Technically yes, but the effect is negligible in practice. [This notebook measures wikitext test perplexity](https://colab.research.google.com/drive/1FxGeYQyE7cx9VNCBC4gUyRVZGORW7c6g) and it is nigh indistinguishable from the original GPT-J. Quantized model is even slightly better, but that is not statistically significant.
Our code differs from other 8-bit methods in that we use **8-bit only for storage, and all computations are performed in float16 or float32**. As a result, we can take advantage of nonlinear quantization that fits to each individual weight distribution. Such nonlinear quantization does not accelerate inference, but it allows for much smaller error.
__What about performance?__ Both checkpointing and de-quantization has some overhead, but it's surprisingly manageable. Depending on GPU and batch size, the quantized model is 1-10% slower than the original model on top of using gradient checkpoints (which is 30% overhead). In short, this is because block-wise quantization from bitsandbytes is really fast on GPU.
### How should I fine-tune the model?
We recommend starting with the original hyperparameters from [the LoRA paper](https://arxiv.org/pdf/2106.09685.pdf).
On top of that, there is one more trick to consider: the overhead from de-quantizing weights does not depend on batch size.
As a result, the larger batch size you can fit, the more efficient you will train.
### Can I use this technique with other models?
The model was converted using [this notebook](https://colab.research.google.com/drive/1rwxh0XRdVi8VEbTx97l9xXr4JbRhZaq5#scrollTo=CX3VHn-J1Zer). It can be adapted to work with other model types. However, please bear in mind that some models replace Linear and Embedding with custom alternatives that require their own BNBWhateverWithAdapters.
