---
license: bsd-3-clause
---
# CodeGen (CodeGen-Mono 350M)

Clone of [Salesforce/codegen-350M-mono](https://huggingface.co/Salesforce/codegen-350M-mono) converted to ONNX and optimized.

## Usage

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForCausalLM

model = ORTModelForCausalLM.from_pretrained("TextCortex/codegen-350M-optimized")
tokenizer = AutoTokenizer.from_pretrained("TextCortex/codegen-350M-optimized")

text = "def hello_world():"
input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(
    input_ids,
    max_length=64,
    temperature=0.1,
    num_return_sequences=1,
    early_stopping=True,
)
out = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print(out)
```

Refer to the original model for more details.