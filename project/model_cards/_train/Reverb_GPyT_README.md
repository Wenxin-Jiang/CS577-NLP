---
license: apache-2.0
---

# GPyT Project
GPyT is a GPT2 model trained from scratch (not fine tuned) on Python code from Github. Overall, it was ~200GB of pure 
Python code, the current GPyT model is a mere 2 epochs through this data, so it may benefit greatly from continued training and/or fine-tuning.

Newlines are replaced by <N>

Input to the model is code, up to the context length of 1024, with newlines replaced by <N>

Here's a quick example of using this model:

```py
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("Reverb/GPyT")
model = AutoModelWithLMHead.from_pretrained("Reverb/GPyT")

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

```py
import numpy as np
import pytest

import pandas as pd<N
```
---

## The Journey
The model took 6 major steps which are:

1. Data Collection
2. Raw Data Cleaning
3. Data Preprocessing
4. Building & Training the Tokenizer
5. Testing the Model on Large Dataset
6. Deploying the Final Model on HuggingFace

#### Data Collection
The data was collected from python github repositories using web scraping techniques, It took nearly a day to gather 200GB worth of data.

#### Raw Data Cleaning
200GB of python code?? sounds ridiculous! that's why we needed to clean the downloaded repositories from any non-python files such as PDF,idx..etc

#### Data Preprocessing
I tried splitting the lines of code for each repository then merged them all under one single text file named **python_text_data.txt**

#### Building & Training the Tokenizer
For this step I have used **ByteLevelBPETokenizer** and trained it then saved the model on the desktop

#### Testing the Model on Large Dataset
After training the tokenizer on a large dataset, It was time for some tests to see how good is the model before proceeding.

---

## Considerations:

> - This model is intended for educational and research use only. Do not trust model outputs.
> - Model is highly likely to regurgitate code almost exactly as it saw it. It's up to you to determine licensing if you intend to actually use the generated code.
> - All Python code was blindly pulled from github. This means included code is both Python 2 and 3, among other more subtle differences, such as tabs being 2 spaces in some cases and 4 in others...and more non-homologous things.
> - Along with the above, this means the code generated could wind up doing or suggesting just about anything. Run the generated code at own risk...it could be anything
