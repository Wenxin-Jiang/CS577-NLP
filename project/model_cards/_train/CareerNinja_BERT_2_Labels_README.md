---
license: apache-2.0
---

Number of Epochs = 5 <br>
Dataset Size = 5.5 k samples [train/validation] <br>
Number of labels used = 2 <br>
Thresholding = True<br>
Thresholding value = 0.7<br>

Below is the function to aplly thresholding to output logits.


```python
  def get_prediction(text):
    encoding = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
    encoding = {k: v.to(trainer.model.device) for k,v in encoding.items()}

    outputs = model(**encoding)

    logits = outputs.logits

    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    probs = probs.detach().numpy()
    label = np.argmax(probs, axis=-1)
    if label == 1:
        if probs[1] > 0.7:
            return 1
        else:
            return 0
    else:
        return 0
```