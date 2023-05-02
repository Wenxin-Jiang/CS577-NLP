---
license: mit
---

# PyAutoCode: GPT-2 based Python auto-code.

PyAutoCode is a cut-down python autosuggestion built on **GPT-2** *(motivation: GPyT)* model. This baby model *(trained only up to 3 epochs)* is not **"fine-tuned"** yet therefore, I highly recommend not to use it in a production environment or incorporate PyAutoCode in any of your projects. It has been trained on **112GB** of Python data sourced from the best crowdsource platform ever -- **GitHub**.

*NOTE: Increased training and fine tuning would be highly appreciated and I firmly believe that it would improve the ability of PyAutoCode significantly.*

## Some Model Features

- Built on *GPT-2*
- Tokenized with *ByteLevelBPETokenizer*
- Data Sourced from *GitHub (almost 5 consecutive days of latest Python repositories)*
- Makes use of *GPTLMHeadModel* and *DataCollatorForLanguageModelling* for training
- Newline characters are custom coded as `<N>`

## Get a Glimpse of the Model

You can make use of the **Inference API** of huggingface *(present on the right sidebar)* to load the model and check the result. Just enter any code snippet as input. Something like:

```sh
for i in range(
```

## Usage

You can use my model too!. Here's a quick tour of how you can achieve this:

Install transformers
```sh
$ pip install transformers
```

Call the API and get it to work!
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("P0intMaN/PyAutoCode")

model = AutoModelForCausalLM.from_pretrained("P0intMaN/PyAutoCode")

# input: single line or multi-line. Highly recommended to use doc-strings.
inp = """import pandas"""

format_inp = inp.replace('\n', "<N>")
tokenize_inp = tokenizer.encode(format_inp, return_tensors='pt')
result = model.generate(tokenize_inp)

decode_result = tokenizer.decode(result[0])
format_result = decode_result.replace('<N>', "\n")

# printing the result
print(format_result)
```

Upon successful execution, the above should probably produce *(your results may vary when this model is fine-tuned)*
```sh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

```
## Credits
##### *Developed as a part of a university project by [Pratheek U](https://www.github.com/P0intMaN) and [Sourav Singh](https://github.com/Sourav11902312lpu)*