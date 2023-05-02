---

datasets:

- arxiv


widget:

- text: "summarize: We describe a system called Overton, whose main design goal is to support engineers in building, monitoring, and improving production 
machinelearning systems. Key challenges engineers face are monitoring fine-grained quality, diagnosing errors in sophisticated applications, and 
handling contradictory or incomplete supervision data. Overton automates the life cycle of model construction, deployment, and monitoring by providing a set of novel high-level, declarative abstractions. Overton's vision is to shift developers to these higher-level tasks instead of lower-level machine learning tasks. 
In fact, using Overton, engineers can build deep-learning-based applications without writing any code in frameworks like TensorFlow. For over a year, 
Overton has been used in production to support multiple applications in both near-real-time applications and back-of-house processing. 
In that time, Overton-based applications have answered billions of queries in multiple languages and processed trillions of records reducing errors 
1.7-2.9 times versus production systems."
            
license: mit
---


## Usage:
```python
abstract = """We describe a system called Overton, whose main design goal is to support engineers in building, monitoring, and improving production 
machine learning systems. Key challenges engineers face are monitoring fine-grained quality, diagnosing errors in sophisticated applications, and 
handling contradictory or incomplete supervision data. Overton automates the life cycle of model construction, deployment, and monitoring by providing a 
set of novel high-level, declarative abstractions. Overton's vision is to shift developers to these higher-level tasks instead of lower-level machine learning tasks. 
In fact, using Overton, engineers can build deep-learning-based applications without writing any code in frameworks like TensorFlow. For over a year, 
Overton has been used in production to support multiple applications in both near-real-time applications and back-of-house processing. In that time, 
Overton-based applications have answered billions of queries in multiple languages and processed trillions of records reducing errors 1.7-2.9 times versus production systems.
"""
```
### Using Transformers🤗
```python
model_name = "Suva/uptag-url-model-v2"
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
input_ids = tokenizer.encode("summarize: " + abstract, return_tensors="pt", add_special_tokens=True)
generated_ids = model.generate(input_ids=input_ids,num_beams=5,max_length=100,repetition_penalty=2.5,length_penalty=1,early_stopping=True,num_return_sequences=3)
preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in generated_ids]
print(preds)
# output
["Overton: Building, Deploying, and Monitoring Machine Learning Systems for Engineers",
 "Overton: A System for Building, Monitoring, and Improving Production Machine Learning Systems",
 "Overton: Building, Monitoring, and Improving Production Machine Learning Systems"]
 ```