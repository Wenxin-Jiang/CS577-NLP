---
language:
- ru

widget:
- text: "Цель одна - истребление как можно больше славянских народов. На очереди поляки, они тоже славяне, их тоже на утилизировать. Это Цель НАТО. Ну и заодно разрушение экономики ЕС, ну и Китай дот кучи под плинтус загнать."
- text: "Дочке 15, книг не читает, вся жизнь (вне школы) в телефоне на кровати. Любознательности ноль. Куда-то поехать в новое место, узнать что-то, найти интересные курсы - вообще не про нее. Учеба все хуже, багажа знаний уже нет, списывает и выкручивается в течение четверти, как контрольная или что-то посерьезнее, где не списать - на 2-3. При любой возможности не ходит в школу (голова болит, можно сегодня не пойду. а потом пятница, что на один день ходить...)"
- "Ребёнок учится в 8 классе. По алгебре одни тройки. Но это точно 2. Просто учитель не будет ставить в четверти 2. Она гуманитарий. Алгебра никак не идёт. Репетитор сейчас занимается, понимает только лёгкие темы. Я боюсь, что провалит ОГЭ. Там пересдать можно? А если опять 2,это второй год?"
---
# eva_ru_forum_headlines

## Model Description
The model was trained on forum topics names and first posts (100 - 150 words). It generates short headlines (3 - 5 words) in the opposite to headlines from models trained on newspaper articles.

"I do not know how to title this post" can be a valid headline.
"What would you do in my place?" is one of the most popular headline.

### Usage
```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "Kateryna/eva_ru_forum_headlines"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

text = "Я влюбилась в одного парня. Каждый раз, когда он меня видит, он плюется и переходит на другую сторону улицы. Как вы думаете, он меня любит?"

input_ids = tokenizer(
    [text],
    max_length=150,
    add_special_tokens=True,
    padding="max_length",
    truncation=True,
    return_tensors="pt"
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=25,
    num_beams=4,
    repetition_penalty=5.0,
    no_repeat_ngram_size=4
)[0]

headline = tokenizer.decode(output_ids, skip_special_tokens=True)

print(headline)
```
### Training and Validation

Training dataset: https://huggingface.co/datasets/Kateryna/eva_ru_forum_headlines

From all available posts and topics names I selected only posts and abstractive topic names e.g. the topic name does not match exactly anything in the correspondent post.

The base model is cointegrated/rut5-base

Training parameters:
- max_source_tokens_count = 150
- max_target_tokens_count = 25
- learning_rate = 0.0007
- num_train_epochs = 3
- batch_size = 8
- gradient_accumulation_steps = 96

ROUGE and BLUE scores were not very helpful to choose a best model. 

I manually estimated ~100 results in each candidate model.

1. The less gradient_accumulation_steps the more abstractive headlines but they becomes less and less related to the correspondent posts. The worse model with gradient_accumulation_steps = 1 had all headlines abstractive but random.
2. The source for the model is real short texts created by ordinary persons without any editing. In many cases, the forum posts are not connected sentences and it is not clear what the author wanted to say or discuss. Sometimes there is a contradiction in the text and only the real topic name reveals what this all about. Naturally the model fails to produce a good headline in such cases.

https://github.com/KaterynaD/eva.ru/tree/main/Code/Notebooks/9.%20Headlines



