### How to use
#### Requirements

Transformers require `transformers` and `sentencepiece`, both of which can be
installed using `pip`.

```sh
pip install transformers sentencepiece
```

#### Pipelines 🚀

In case you are not familiar with Transformers, you can use pipelines instead.

Note that, pipelines can't have _no answer_ for the questions.

```python
from transformers import pipeline

model_name = "SajjadAyoubi/bert-base-fa-qa"
qa_pipeline = pipeline("question-answering", model=model_name, tokenizer=model_name)

text = "سلام من سجاد ایوبی هستم ۲۰ سالمه و به پردازش زبان طبیعی علاقه دارم"
questions = ["اسمم چیه؟", "چند سالمه؟", "به چی علاقه دارم؟"]

for question in questions:
    print(qa_pipeline({"context": text, "question": question}))

>>> {'score': 0.4839823544025421, 'start': 8, 'end': 18, 'answer': 'سجاد ایوبی'}
>>> {'score': 0.3747948706150055, 'start': 24, 'end': 32, 'answer': '۲۰ سالمه'}
>>> {'score': 0.5945395827293396, 'start': 38, 'end': 55, 'answer': 'پردازش زبان طبیعی'}
```

#### Manual approach 🔥

Using the Manual approach, it is possible to have _no answer_ with even better
performance.

- PyTorch

```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from src.utils import AnswerPredictor

model_name = "SajjadAyoubi/bert-base-fa-qa"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

text = "سلام من سجاد ایوبی هستم ۲۰ سالمه و به پردازش زبان طبیعی علاقه دارم"
questions = ["اسمم چیه؟", "چند سالمه؟", "به چی علاقه دارم؟"]

# this class is from src/utils.py and you can read more about it
predictor = AnswerPredictor(model, tokenizer, device="cpu", n_best=10)
preds = predictor(questions, [text] * 3, batch_size=3)

for k, v in preds.items():
    print(v)
```

Produces an output such below:
```
100%|██████████| 1/1 [00:00<00:00,  3.56it/s]
{'score': 8.040637016296387, 'text': 'سجاد ایوبی'}
{'score': 9.901972770690918, 'text': '۲۰'}
{'score': 12.117212295532227, 'text': 'پردازش زبان طبیعی'}
```

- TensorFlow 2.X

```python
from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering
from src.utils import TFAnswerPredictor

model_name = "SajjadAyoubi/bert-base-fa-qa"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)

text = "سلام من سجاد ایوبی هستم ۲۰ سالمه و به پردازش زبان طبیعی علاقه دارم"
questions = ["اسمم چیه؟", "چند سالمه؟", "به چی علاقه دارم؟"]

# this class is from src/utils.py, you can read more about it
predictor = TFAnswerPredictor(model, tokenizer, n_best=10)
preds = predictor(questions, [text] * 3, batch_size=3)

for k, v in preds.items():
    print(v)
```

Produces an output such below:

```text
100%|██████████| 1/1 [00:00<00:00,  3.56it/s]
{'score': 8.040637016296387, 'text': 'سجاد ایوبی'}
{'score': 9.901972770690918, 'text': '۲۰'}
{'score': 12.117212295532227, 'text': 'پردازش زبان طبیعی'}
```

Or you can access the whole demonstration using [HowToUse iPython Notebook on Google Colab](https://colab.research.google.com/github/sajjjadayobi/PersianQA/blob/main/notebooks/HowToUse.ipynb)

