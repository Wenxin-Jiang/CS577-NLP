---
language: en
thumbnail:
license: mit
inference: false
tags:
- question-answering
datasets:
- squad_v2
metrics:
- squad_v2
---

## bert-large-uncased-wwm-squadv2-optimized-f16

This is an optimized model using [madlag/bert-large-uncased-wwm-squadv2-x2.63-f82.6-d16-hybrid-v1](https://huggingface.co/madlag/bert-large-uncased-wwm-squadv2-x2.63-f82.6-d16-hybrid-v1) as the base model which was created using the [nn_pruning](https://github.com/huggingface/nn_pruning) python library. This is a pruned model of [madlag/bert-large-uncased-whole-word-masking-finetuned-squadv2](https://huggingface.co/madlag/bert-large-uncased-whole-word-masking-finetuned-squadv2)

Feel free to read our blog about how we optimized this model [(link)](https://tryolabs.com/blog/2022/11/24/transformer-based-model-for-faster-inference)

Our final optimized model weighs **579 MB**, has an inference speed of **18.184 ms** on a Tesla T4 and has a performance of **82.68%** best F1. Below there is a comparison for each base model:

| Model  | Weight | Throughput on Tesla T4 | Best F1 |
| -------- | ----- | --------- | --------- |
| [madlag/bert-large-uncased-whole-word-masking-finetuned-squadv2](https://huggingface.co/madlag/bert-large-uncased-whole-word-masking-finetuned-squadv2) | 1275 MB | 140.529 ms | 86.08% |
| [madlag/bert-large-uncased-wwm-squadv2-x2.63-f82.6-d16-hybrid-v1](https://huggingface.co/madlag/bert-large-uncased-wwm-squadv2-x2.63-f82.6-d16-hybrid-v1) | 1085 MB | 90.801 ms | 82.67% |
| Our optimized model | 579 MB | 18.184 ms | 82.68% |

You can test the inference of those models on [tryolabs/transformers-optimization space](https://huggingface.co/spaces/tryolabs/transformers-optimization)

## Example Usage

```python
import torch
from huggingface_hub import hf_hub_download
from onnxruntime import InferenceSession
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

MAX_SEQUENCE_LENGTH = 512

# Download the model
model= hf_hub_download(
    repo_id="tryolabs/bert-large-uncased-wwm-squadv2-optimized-f16", filename="model.onnx"
)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("tryolabs/bert-large-uncased-wwm-squadv2-optimized-f16")

question = "Who worked a little bit harder?"
context = "The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day."

# Generate an input
inputs = dict(
    tokenizer(
        question, context, return_tensors="np", max_length=MAX_SEQUENCE_LENGTH
    )
)

# Create session
sess = InferenceSession(
    model, providers=["CPUExecutionProvider"]
)

# Run predictions
output = sess.run(None, input_feed=inputs)

answer_start_scores, answer_end_scores = torch.tensor(output[0]), torch.tensor(
    output[1]
)

# Post process predictions
input_ids = inputs["input_ids"].tolist()[0]
answer_start = torch.argmax(answer_start_scores)
answer_end = torch.argmax(answer_end_scores) + 1
answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
)

# Output prediction
print("Answer", answer)
```


