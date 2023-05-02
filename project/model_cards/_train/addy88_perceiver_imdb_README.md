### How to use
Here is how to use this model in PyTorch:
```python
from transformers import PerceiverTokenizer, PerceiverForMaskedLM
tokenizer = PerceiverTokenizer.from_pretrained("addy88/perceiver_imdb")
model = PerceiverForMaskedLM.from_pretrained("addy88/perceiver_imdb")
text = "This is an incomplete sentence where some words are missing."
# prepare input
encoding = tokenizer(text, padding="max_length", return_tensors="pt")
# mask " missing.". Note that the model performs much better if the masked span starts with a space.
encoding.input_ids[0, 52:61] = tokenizer.mask_token_id
inputs, input_mask = encoding.input_ids.to(device), encoding.attention_mask.to(device)
# forward pass
outputs = model(inputs=inputs, attention_mask=input_mask)
logits = outputs.logits
masked_tokens_predictions = logits[0, 51:61].argmax(dim=-1)
print(tokenizer.decode(masked_tokens_predictions))
>>> should print " missing."
```