---
language: 
  - en
  - code
tags:
- code completion
- code generation
license: "apache-2.0"
---

# NLGP natural model

The NLGP natural model was introduced in the paper [Natural Language-Guided Programming](https://arxiv.org/abs/2108.05198).  The model was trained on a collection of Jupyter notebooks and can be used to synthesize Python code that addresses a natural language **intent** in a certain code **context** (see the example below). This work was carried out by a research team in Nokia Bell Labs.

**Context**
```py
import matplotlib.pyplot as plt

values = [1, 2, 3, 4]
labels = ["a", "b", "c", "d"]
```

**Intent**
```py
# plot a bar chart
```

**Prediction**
```py
plt.bar(labels, values)
plt.show()
```

## Usage

```py
import re
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

# load the model
tok = GPT2TokenizerFast.from_pretrained("Nokia/nlgp-natural")
model = GPT2LMHeadModel.from_pretrained("Nokia/nlgp-natural") 

# preprocessing functions
num_spaces = [2, 4, 6, 8, 10, 12, 14, 16, 18]
def preprocess(context, query):
    """
    Encodes context + query as a single string and 
    replaces whitespace with special tokens <|2space|>, <|4space|>, ...
    """
    input_str = f"{context}\n{query} <|endofcomment|>\n"
    indentation_symbols = {n: f"<|{n}space|>" for n in num_spaces}
    m = re.match("^[ ]+", input_str)
    if not m:
        return input_str
    leading_whitespace = m.group(0)
    N = len(leading_whitespace)
    for n in self.num_spaces:
        leading_whitespace = leading_whitespace.replace(n * " ", self.indentation_symbols[n])
    return leading_whitespace + input_str[N:]
    
detokenize_pattern = re.compile(fr"<\|(\d+)space\|>")
def postprocess(output):
    output = output.split("<|cell|>")[0]
    def insert_space(m):
        num_spaces = int(m.group(1))
        return num_spaces * " "
    return detokenize_pattern.sub(insert_space, output)

# inference
code_context = """
import matplotlib.pyplot as plt

values = [1, 2, 3, 4]
labels = ["a", "b", "c", "d"]
"""
query = "# plot a bar chart"

input_str = preprocess(code_context, query)
input_ids = tok(input_str, return_tensors="pt").input_ids

max_length = 150 # don't generate output longer than this length
total_max_length = min(1024 - input_ids.shape[-1], input_ids.shape[-1] + 150) # total = input + output

input_and_output = model.generate(
    input_ids=input_ids, 
    max_length=total_max_length,
    min_length=10,
    do_sample=False,
    num_beams=4,
    early_stopping=True,
    eos_token_id=tok.encode("<|cell|>")[0]
)

output = input_and_output[:, input_ids.shape[-1]:] # remove the tokens that correspond to the input_str
output_str = tok.decode(output[0])
postprocess(output_str)
```

## License and copyright

Copyright 2021 Nokia

Licensed under the Apache License 2.0

SPDX-License-Identifier: Apache-2.0