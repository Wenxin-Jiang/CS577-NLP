This model is fine-tuned on Medical data to perform summarization.

Data used from https://data.mendeley.com/datasets/gg58kc7zy7

Size of data ~ 10k

```python 
from transformers import pipeline
summarizer = pipeline("summarization", model="Mit1208/Med-Sum")

long_text = "The human brain is the inspiration behind neural network architecture. Human brain cells, called neurons, form a complex, highly interconnected network and send electrical signals to each other to help humans process information. Similarly, an artificial neural network is made of artificial neurons that work together to solve a problem. Artificial neurons are software modules, called nodes, and artificial neural networks are software programs or algorithms that, at their core, use computing systems to solve mathematical calculations."
result = summarizer(long_text)
print(result[0]["summary_text"])
```

Output:
```
The human brain is the inspiration behind neural network architecture. Human brain cells, called neurons, form a complex, highly interconnected network and send electrical signals to each other to help humans process information. The artificial neural network is made of artificial neurons that work together to solve a problem.
```



long_text--[https://aws.amazon.com/what-is/neural-network/]