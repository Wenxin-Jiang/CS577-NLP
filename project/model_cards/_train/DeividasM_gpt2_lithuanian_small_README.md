---
datasets: 
  - wikipedia
language: 
  - lt
license: apache-2.0
tags: 
  - "text-generation"
widget:
  - text: "Lietuva yra viena "
---
## Model description

![LT](LT.png)

GPT-2 model from Lithuania using Wikipedia corpus dataset based on GPT-2 small model.

This is only the first version of the model; over time model will be improved using a more extensive dataset and better data preparation.

## Training data
This model was pre-trained with 180MB of Lithuanian Wikipedia. The texts are tokenized using a byte-level version of Byte Pair Encoding (BPE).

## Training
The model was trained on wiki-corpus for 40 hours using NVIDIA Tesla P100 GPU.

### How to use

### Load model

``` 
from transformers import AutoTokenizer, TFAutoModelWithLMHead
import tensorflow as tf

tokenizer = AutoTokenizer.from_pretrained("DeividasM/gpt2_lithuanian_small")
model = TFAutoModelWithLMHead.from_pretrained("DeividasM/gpt2_lithuanian_small")

# Get sequence length max of 1024
tokenizer.model_max_length=1024 

model.eval()
```
## Generate text

``` 
text = "tekstas "
inputs = tokenizer.encode(text, return_tensors="tf")


outputs = model.generate(inputs, eos_token_id=50256, pad_token_id=50256, 
                         do_sample=True,
                         max_length=40,
                         top_k=40)
                         
print(tokenizer.decode(outputs[0]))

```
## Limitations and bias
The training data used for this model come from Lithuanian Wikipedia. We know it contains a lot of unfiltered content from the internet, which is far from neutral. As the OpenAI team themselves point out in their model card:


"Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true. Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans > unless the deployers first carry out a study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race, and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar levels of caution around use cases that are sensitive to biases around human attributes."


## Author

Lithuanian GPT-2 small was trained and evaluated by Deividas Mataciunas (https://www.linkedin.com/in/deividasmataciunas/)
