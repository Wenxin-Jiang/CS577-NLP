---
license: bigscience-openrail-m
---

This model is part of an experiment of pre-training one very deep and another very shallow gpt2 models with similar sizes:

* https://huggingface.co/HuggingFaceM4/gpt2-deep-1b56-ratio-33
* https://huggingface.co/HuggingFaceM4/gpt2-shallow-1b32-ratio-85


Size/ratio calculations:

- shallow:

```
NHIDDEN=2048; NLAYERS=24; SEQ_LEN=2048; VOCAB_SIZE=50257; python -c "h=$NHIDDEN; l=$NLAYERS; s=$SEQ_LEN; v=$VOCAB_SIZE; print(f'Model size: {(l*(12*h**2 + 13*h) + v*h + s*h + 2*h) / 10**9 :.2f}B, ratio={int(h/l)}')"
Model size: 1.32B, ratio=85
```

- narrow:

```
NHIDDEN=1600; NLAYERS=48; SEQ_LEN=2048; VOCAB_SIZE=50257; python -c "h=$NHIDDEN; l=$NLAYERS; s=$SEQ_LEN; v=$VOCAB_SIZE; print(f'Model size: {(l*(12*h**2 + 13*h) + v*h + s*h + 2*h) / 10**9 :.2f}B, ratio={int(h/l)}')"
Model size: 1.56B, ratio=33
```

The Megatron-Deepspeed training scripts that created these can be found here:
- https://github.com/huggingface/m4/blob/text_pretraining/experiments/pretraining/text_pretraining/shallow_gpt.slurm
- https://github.com/huggingface/m4/blob/text_pretraining/experiments/pretraining/text_pretraining/narrow_gpt.slurm


The last Megatron-Deepspeed checkpoint dumps can be found here:

- https://huggingface.co/HuggingFaceM4/gpt2-shallow-1b32-ratio-85-meg-ds-checkpoint
- https://huggingface.co/HuggingFaceM4/gpt2-deep-1b56-ratio-33-meg-ds-checkpoint

Tensorboard: 
- https://huggingface.co/HuggingFaceM4/gpt2-1.35b-pile-shallow/tensorboard
- https://huggingface.co/HuggingFaceM4/gpt2-1.56b-pile-deep/tensorboard

Validate checkpoint:

```
$ python -c '\
import sys; \
mname = sys.argv[1]; \
from transformers import AutoTokenizer, AutoModelForCausalLM; \
tokenizer = AutoTokenizer.from_pretrained(mname); \
tokenizer.add_special_tokens({"pad_token": tokenizer.eos_token}); \
model = AutoModelForCausalLM.from_pretrained(mname); \
inputs = ["Hello, my dog is cute"]; \
input_tokens = tokenizer.batch_encode_plus(inputs, return_tensors="pt", padding=True)
outputs = model.generate(**input_tokens, do_sample=False); \
outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True); \
print(outputs); \
' HuggingFaceM4/gpt2-shallow-1b32-ratio-85
[...]
['Hello, my dog is cute." "I\'m gonna take him home." "I\'m gonna take']
```

