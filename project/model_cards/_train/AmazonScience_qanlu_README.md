---
language: en
license: cc-by-4.0
widget:
- context: "Yes. No. I'm looking for a cheap flight to Boston."
datasets:
- atis
---

# Question Answering NLU

Question Answering NLU (QANLU) is an approach that maps the NLU task into question answering, 
leveraging pre-trained question-answering models to perform well on few-shot settings. Instead of 
training an intent classifier or a slot tagger, for example, we can ask the model intent- and 
slot-related questions in natural language: 

```
Context : Yes. No. I'm looking for a cheap flight to Boston.

Question: Is the user looking to book a flight?
Answer  : Yes

Question: Is the user asking about departure time?
Answer  : No

Question: What price is the user looking for?
Answer  : cheap

Question: Where is the user flying from?
Answer  : (empty)
```

Note the "Yes. No. " prepended in the context. Those are to allow the model to answer intent-related questions (e.g. "Is the user looking for a restaurant?").

Thus, by asking questions for each intent and slot in natural language, we can effectively construct an NLU hypothesis. For more details, please read the paper: [Language model is all you need: Natural language understanding as question answering](https://assets.amazon.science/33/ea/800419b24a09876601d8ab99bfb9/language-model-is-all-you-need-natural-language-understanding-as-question-answering.pdf).

## Model training

Instructions for how to train and evaluate a QANLU model, as well as the necessary code for ATIS are in the [Amazon Science repository](https://github.com/amazon-research/question-answering-nlu).

## Intended use and limitations

This model has been fine-tuned on ATIS (English) and is intended to demonstrate the power of this approach. For other domains or tasks, it should be further fine-tuned 
on relevant data.

## Use in transformers:

```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
  
tokenizer = AutoTokenizer.from_pretrained("AmazonScience/qanlu", use_auth_token=True)

model = AutoModelForQuestionAnswering.from_pretrained("AmazonScience/qanlu", use_auth_token=True)

qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

qa_input = {
  'context': 'Yes. No. I want a cheap flight to Boston.',
  'question': 'What is the destination?'
}

answer = qa_pipeline(qa_input)
```

## Citation
If you use this work, please cite:

```
@inproceedings{namazifar2021language,
  title={Language model is all you need: Natural language understanding as question answering},
  author={Namazifar, Mahdi and Papangelis, Alexandros and Tur, Gokhan and Hakkani-T{\"u}r, Dilek},
  booktitle={ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={7803--7807},
  year={2021},
  organization={IEEE}
}
```

## License

This library is licensed under the CC BY NC License.