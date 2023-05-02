---
tags:
- generated_from_trainer
datasets: UrukHan/wav2vec2-russian
widget:
- text: ывсем привет выныканалетоп армии и это двадцать пятый день спец операций на
    украине ет самый главной новости российские военные ракетами кинжалы калибр уничтожили
    крупную военную топливную базу украины ракетным ударом по населенному пункту под
    жетамиром уничтжены более стаукраинских военных в две тысячи двадцать втором году
model-index:
- name: t5-russian-spell
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
---
# t5-russian-spell
---
модель для исправление текста из распознаного аудио.   моя модлеь для распознования аудио https://huggingface.co/UrukHan/wav2vec2-russian и его результаты можно закидывать в эту модель. тестил на видео случайном с ютюба

<table border="0">
 <tr>
    <td><b style="font-size:30px">Output wav2vec2</b></td>
    <td><b style="font-size:30px">Output spell correcor</b></td>
 </tr>
 <tr>
    <td>ывсем привет выныканалетоп армии и это двадцать пятый день спец операций на украине ет самый главной новости российские военные ракетами кинжалы калибр уничтожили крупную военную топливную базу украины ракетным ударом по населенному пункту под жетамиром уничтжены более стаукраинских военных в две тысячи двадцать втором году</td>
    <td>Всем привет! Вы в курсе новостей от армии. И это 25 день спецопераций на Украине. Есть самые главные новости. Российские военные ракетами «Кинжалы» и «Кинжалы» калибра уничтожили крупную военную топливную базу Украины. Ракетным ударом по населенному пункту под Жетамиром уничтожены более ста украинских военных в 2022г.</td>
 </tr>
</table>


#
---
Датасеты для обучения:
UrukHan/t5-russian-spell_I   : https://huggingface.co/datasets/UrukHan/t5-russian-spell_I
UrukHan/t5-russian-spell_II  : https://huggingface.co/datasets/UrukHan/t5-russian-spell_II
UrukHan/t5-russian-spell_III : https://huggingface.co/datasets/UrukHan/t5-russian-spell_III

---

# Запуск на вывод результатов пример работы с комментариями в колабе https://colab.research.google.com/drive/1ame2va9_NflYqy4RZ07HYmQ0moJYy7w2?usp=sharing :

#
```python
# Установим библиотеку трансформеров
!pip install transformers

# Импортируем библиотеки
from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

# Зададим название выбронной модели из хаба
MODEL_NAME = 'UrukHan/t5-russian-spell'
MAX_INPUT = 256

# Загрузка модели и токенизатора
tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Входные данные (можно массив фраз или текст)
input_sequences = ['сеглдыя хорош ден', 'когд а вы прдет к нам в госи']   # или можно использовать одиночные фразы:  input_sequences = 'сеглдыя хорош ден'

task_prefix = "Spell correct: "                 # Токенизирование данных
if type(input_sequences) != list: input_sequences = [input_sequences]
encoded = tokenizer(
  [task_prefix + sequence for sequence in input_sequences],
  padding="longest",
  max_length=MAX_INPUT,
  truncation=True,
  return_tensors="pt",
)

predicts = model.generate(encoded)    # # Прогнозирование

tokenizer.batch_decode(predicts, skip_special_tokens=True)  # Декодируем данные
```
#
---
#Настроенный блокнот для запуска обучения и сохранения модели в свой репозиторий на huggingface hub:
#https://colab.research.google.com/drive/1H4IoasDqa2TEjGivVDp-4Pdpm0oxrCWd?usp=sharing
#
```python
# Установка библиотек
!pip install datasets
!apt install git-lfs
!pip install transformers
!pip install sentencepiece 
!pip install rouge_score

# Импорт библиотек
import numpy as np
from datasets import Dataset
import tensorflow as 
import nltk
from transformers import T5TokenizerFast, Seq2SeqTrainingArguments, Seq2SeqTrainer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
import torch
from transformers.optimization import Adafactor, AdafactorSchedule
from datasets import load_dataset, load_metric

# загрузка параметров
raw_datasets = load_dataset("xsum")
metric = load_metric("rouge")
nltk.download('punkt')

# Ввести свой ключ huggingface hyb
from huggingface_hub import notebook_login
notebook_login()

# Определение параметров
REPO = "t5-russian-spell"  # Введите наазвание название репозитория
MODEL_NAME = "UrukHan/t5-russian-spell" # Введите наазвание выбранной модели из хаба
MAX_INPUT = 256  # Введите максимальную длинну входных данных  в токенах (длинна входных фраз в словах (можно считать полслова токен))
MAX_OUTPUT  = 256 # Введите максимальную длинну прогнозов в токенах (можно уменьшить для задач суммризации или других задач где выход короче)
BATCH_SIZE = 8 
DATASET = 'UrukHan/t5-russian-spell_I'   # Введите наазвание название датасета

# Загрузка датасета использование других типов данных опишу ниже
data = load_dataset(DATASET)

# Загрузка модели и токенизатора
tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model.config.max_length = MAX_OUTPUT  # по умолчанию 20, поэтому во всех моделях прогнозы обрезаются выходные последовательности
# Закоментить после первого соъранения в репозиторий свой необъязательно
tokenizer.push_to_hub(repo_name) 

train = data['train']
test = data['test'].train_test_split(0.02)['test']  # Уменьшил так тестовыу. выборку чтоб не ждать долго расчет ошибок между эпохами

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model) #return_tensors="tf"

def compute_metrics(eval_pred):
  predictions, labels = eval_pred
  decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
  # Replace -100 in the labels as we can't decode them.
  labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
  decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
  
  # Rouge expects a newline after each sentence
  decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip())) for pred in decoded_preds]
  decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip())) for label in decoded_labels]
  
  result = metric.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
  # Extract a few results
  result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
  
  # Add mean generated length
  prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
  result["gen_len"] = np.mean(prediction_lens)
  
  return {k: round(v, 4) for k, v in result.items()}
  
training_args = Seq2SeqTrainingArguments(
  output_dir = REPO,
  #overwrite_output_dir=True,
  evaluation_strategy='steps',
  #learning_rate=2e-5,
  eval_steps=5000,
  save_steps=5000,
  num_train_epochs=1,
  predict_with_generate=True,
  per_device_train_batch_size=BATCH_SIZE,
  per_device_eval_batch_size=BATCH_SIZE,
  fp16=True,
  save_total_limit=2,
  #generation_max_length=256,
  #generation_num_beams=4,
  weight_decay=0.005,
  #logging_dir='logs',
  push_to_hub=True,
)

# Выберем вручную оптимизатор. Т5 в оригинальной архитектуре использует Адафактор оптимизатор
optimizer = Adafactor(
    model.parameters(),
    lr=1e-5,
    eps=(1e-30, 1e-3),
    clip_threshold=1.0,
    decay_rate=-0.8,
    beta1=None,
    weight_decay=0.0,
    relative_step=False,
    scale_parameter=False,
    warmup_init=False,
)
lr_scheduler = AdafactorSchedule(optimizer)

trainer = Seq2SeqTrainer(
  model=model,
  args=training_args,
  train_dataset = train,
  eval_dataset = test,
  optimizers = (optimizer, lr_scheduler),
  tokenizer = tokenizer,
  compute_metrics=compute_metrics
)

trainer.train()

trainer.push_to_hub()
```
#
---
# Пример конвертации массивов для данной сети
#
```python
input_data = ['удач почти отнее отвернулась', 'в хааоде проведения чемпиониавта мира дветысячивосемнандцтая лгодаа']
output_data = ['Удача почти от нее отвернулась', 'в ходе проведения чемпионата мира две тысячи восемнадцатого года']

# Токенизируем входные данные
task_prefix = "Spell correct: "
input_sequences = input_data 
encoding = tokenizer(
  [task_prefix + sequence for sequence in input_sequences],
  padding="longest",
  max_length=MAX_INPUT,
  truncation=True,
  return_tensors="pt",
)
input_ids, attention_mask = encoding.input_ids, encoding.attention_mask

# Токенизируем выходные данные
target_encoding = tokenizer(output_data, padding="longest", max_length=MAX_OUTPUT, truncation=True)
labels = target_encoding.input_ids
# replace padding token id's of the labels by -100
labels = torch.tensor(labels)
labels[labels == tokenizer.pad_token_id] = -100'''

# Конвертируем наши данные в формат dataset   

data = Dataset.from_pandas(pd.DataFrame({'input_ids': list(np.array(input_ids)), 'attention_mask': list(np.array(attention_mask)), 'labels': list(np.array(labels))}))
data = data.train_test_split(0.02)
# и получим на вход сети для нашешго trainer:   train_dataset = data['train'],  eval_dataset = data['test']