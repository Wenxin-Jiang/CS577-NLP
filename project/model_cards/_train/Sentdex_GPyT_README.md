---
language: code
license: mit
tags:
- Code
- GPyT
- code generator
---


GPyT is a GPT2 model trained from scratch (not fine tuned) on Python code from Github. Overall, it was ~80GB of pure Python code, the current GPyT model is a mere 2 epochs through this data, so it may benefit greatly from continued training and/or fine-tuning.

Newlines are replaced by `<N>`

Input to the model is code, up to the context length of 1024, with newlines replaced by `<N>`

Here's a quick example of using this model:

```py
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("Sentdex/GPyT")
model = AutoModelWithLMHead.from_pretrained("Sentdex/GPyT")

# copy and paste some code in here
inp = """import"""

newlinechar = "<N>"
converted = inp.replace("\n", newlinechar)
tokenized = tokenizer.encode(converted, return_tensors='pt')
resp = model.generate(tokenized)

decoded = tokenizer.decode(resp[0])
reformatted = decoded.replace("<N>","\n")

print(reformatted)
```

Should produce:

```
import numpy as np
import pytest

import pandas as pd<N
```


This model does a ton more than just imports, however. For a bunch of examples and a better understanding of the model's capabilities: 
https://pythonprogramming.net/GPT-python-code-transformer-model-GPyT/




Considerations: 

1. This model is intended for educational and research use only. Do not trust model outputs.
2. Model is highly likely to regurgitate code almost exactly as it saw it. It's up to you to determine licensing if you intend to actually use the generated code.
3. All Python code was blindly pulled from github. This means included code is both Python 2 and 3, among other more subtle differences, such as tabs being 2 spaces in some cases and 4 in others...and more non-homologous things.
4. Along with the above, this means the code generated could wind up doing or suggesting just about anything. Run the generated code at own risk...it could be *anything*



