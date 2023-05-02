---
license: apache-2.0
---

# GPT-NEO-Model for Lean Tactics


In the project, we used an HuggingFace GPT-NEO small model and fine-tuned the tactic dataset. The Input should be of the form
```
<GOAL> Goal <PROOFSTEP>
```

The model can easily be accessed using the following code. 

```
from transformers import GPT2Tokenizer, GPTNeoForCausalLM
import torch

tokenizer = GPT2Tokenizer.from_pretrained("Saisam/gpt-neo-math-small")
model = GPTNeoForCausalLM.from_pretrained("Saisam/gpt-neo-math-small")
```

More Information can be found at https://github.com/saisurbehera/mathProof.

The current model beats the GPT-F for minif2f benchmark

Worked along with Xihao Xhang and Moya Zhu
