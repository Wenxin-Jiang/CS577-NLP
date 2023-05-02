---
language:
- ru
tags:
- summarization
- t5
datasets:
- IlyaGusev/gazeta
license:
- apache-2.0
inference:
  parameters:
    no_repeat_ngram_size: 4
widget:
- text: "Высота башни составляет 324 метра (1063 фута), примерно такая же высота, как у 81-этажного здания, и самое высокое сооружение в Париже. Его основание квадратно, размером 125 метров (410 футов) с любой стороны. Во время строительства Эйфелева башня превзошла монумент Вашингтона, став самым высоким искусственным сооружением в мире, и этот титул она удерживала в течение 41 года до завершения строительство здания Крайслер в Нью-Йорке в 1930 году. Это первое сооружение которое достигло высоты 300 метров. Из-за добавления вещательной антенны на вершине башни в 1957 году она сейчас выше здания Крайслер на 5,2 метра (17 футов). За исключением передатчиков, Эйфелева башня является второй самой высокой отдельно стоящей структурой во Франции после виадука Мийо."
  example_title: "Википедия"
- text: "С 1 сентября в России вступают в силу поправки в закон «О банкротстве» — теперь должники смогут освобождаться от непосильных обязательств во внесудебном порядке, если сумма задолженности составляет не менее 50 тыс. рублей и не превышает 500 тыс. рублей без учета штрафов, пени, процентов за просрочку платежа и прочих имущественных или финансовых санкций. У физлиц и индивидуальных предпринимателей появилась возможность пройти процедуру банкротства без участия суда и финансового управляющего — достаточно подать соответствующее заявление через МФЦ. Сумму задолженности и список всех известных заявителю кредиторов нужно предоставить самостоятельно. Если все условия соблюдены, сведения внесут в Единый федеральный реестр в течение трех рабочих дней. При этом на момент подачи заявления в отношении заявителя должно быть окончено исполнительное производство с возвращением исполнительного документа взыскателю. Это значит, что у потенциального банкрота не должно быть имущества, которое можно взыскать. Кроме того, в отношении гражданина не должно быть возбуждено другое исполнительное производство. В период всей процедуры заявитель не сможет брать займы, кредиты, выдавать поручительства, совершать иные обеспечительные сделки. Внесудебное банкротство будет длиться шесть месяцев, в течение которых также будет действовать мораторий на удовлетворение требований кредиторов, отмеченных в заявлении должника, и мораторий об уплате обязательных платежей. Кроме того, прекращается начисление неустоек и иных финансовых санкций; имущественные взыскания (кроме алиментов) также будут приостановлены. По завершению процедуры заявителя освободят от дальнейшего выполнения требований кредиторов, указанных в заявлении о признании его банкротом, а эта задолженность признается безнадежной. В прошлом месяце стало известно, что за первое полугодие 2020 года российские суды признали банкротами 42,7 тыс. граждан (в том числе индивидуальных предпринимателей) — по данным единого реестра «Федресурс», это на 47,2% больше показателя аналогичного периода 2019 года. Рост числа обанкротившихся граждан во втором квартале по сравнению с первым замедлился — такая динамика обусловлена тем, что в период ограничений с 19 марта по 11 мая суды редко рассматривали банкротные дела компаний и меньше, чем обычно, в отношении граждан, объяснял руководитель проекта «Федресурс» Алексей Юхнин. Он прогнозирует, что во втором полугодии мы увидим рост показателя, когда суды рассмотрят все дела, что не смогли ранее в режиме ограничений. По его данным, уже в июне число личных банкротств выросло до 11,5 тыс., что в два раза превышает показатель аналогичного периода 2019 года."
  example_title: "Новости"
- text: "Актуальность проблемы. Электронная информация играет все большую  роль во всех сферах жизни современного общества. В последние годы объем научно-технической текстовой информации в электронном виде возрос настолько, что возникает угроза обесценивания этой информации в связи с трудностями поиска необходимых сведений среди множества доступных текстов. Развитие информационных ресурсов Интернет многократно усугубило проблему информационной перегрузки. В этой ситуации особенно актуальными становятся методы автоматизации реферирования текстовой информации, то есть методы получения сжатого представления текстовых документов–рефератов (аннотаций). Постановка  проблемы  автоматического реферирования текста и соответственно попытки ее решения с использованием различных подходов предпринимались многими исследователями. История применения вычислительной техники для реферирования  насчитывает уже более 50 лет и связана с именами таких исследователей, как Г.П. Лун, В.Е. Берзон, И.П. Cевбо, Э.Ф. Скороходько, Д.Г. Лахути, Р.Г. Пиотровский и др. За эти годы  выработаны  многочисленные подходы к решению данной проблемы, которые достаточно четко подразделяются на два направления: автоматическое реферирование, основанное на экстрагировании из первичных документов с помощью определенных формальных признаков «наиболее информативных» фраз (фрагментов), совокупность которых образует некоторый экстракт; автоматическое реферирование, основанное на выделении из текстов с помощью специальных информационных языков наиболее существенной информации и порождении новых текстов (рефератов), содержательно обобщающих первичные  документы."
  example_title: "Научная статья"
---

# RuT5SumGazeta

## Model description

This is the model for abstractive summarization for Russian based on [rut5-base](https://huggingface.co/cointegrated/rut5-base).


## Intended uses & limitations

#### How to use

Colab: [link](https://colab.research.google.com/drive/1re5E26ZIDUpAx1gOCZkbF3hcwjozmgG0)

```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "IlyaGusev/rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

article_text = "..."

input_ids = tokenizer(
    [article_text],
    max_length=600,
    add_special_tokens=True,
    padding="max_length",
    truncation=True,
    return_tensors="pt"
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    no_repeat_ngram_size=4
)[0]

summary = tokenizer.decode(output_ids, skip_special_tokens=True)
print(summary)
```

## Training data

- Dataset: [Gazeta](https://huggingface.co/datasets/IlyaGusev/gazeta)

## Training procedure

- Training script: [train.py](https://github.com/IlyaGusev/summarus/blob/master/external/hf_scripts/train.py)
- Config: [t5_training_config.json](https://github.com/IlyaGusev/summarus/blob/master/external/hf_scripts/configs/t5_training_config.json)

## Eval results

* Train dataset: **Gazeta v1 train**
* Test dataset: **Gazeta v1 test**
* Source max_length: **600**
* Target max_length: **200**
* no_repeat_ngram_size: **4**
* num_beams: **5**

| Model                     | R-1-f | R-2-f | R-L-f | chrF | METEOR | BLEU | Avg char length |
|:--------------------------|:------|:------|:------|:-------|:-------|:-----|:-----|
| [mbart_ru_sum_gazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)       | **32.4**  | 14.3  | 28.0  | 39.7 | **26.4** | 12.1 | 371 |
| [rut5_base_sum_gazeta](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta)      | 32.2  | **14.4**  | **28.1** | **39.8** | 25.7 | **12.3** | 330 |
| [rugpt3medium_sum_gazeta](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) | 26.2 | 7.7 | 21.7 | 33.8 | 18.2 | 4.3 | 244 |

* Train dataset: **Gazeta v1 train**
* Test dataset: **Gazeta v2 test**
* Source max_length: **600**
* Target max_length: **200**
* no_repeat_ngram_size: **4**
* num_beams: **5**

| Model                     | R-1-f | R-2-f | R-L-f | chrF | METEOR | BLEU | Avg char length |
|:--------------------------|:------|:------|:------|:-------|:-------|:-----|:-----|
| [mbart_ru_sum_gazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)        | **28.7**  | **11.1**  | 24.4  | **37.3** | **22.7**  | **9.4** | 373 |
| [rut5_base_sum_gazeta](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta)      | 28.6 | **11.1** | **24.5** | 37.2 | 22.0 | **9.4** | 331 |
| [rugpt3medium_sum_gazeta](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) | 24.1 | 6.5 | 19.8 | 32.1 | 16.3 | 3.6 | 242 |

Predicting all summaries:
```python
import json
import torch
from transformers import AutoTokenizer, T5ForConditionalGeneration
from datasets import load_dataset


def gen_batch(inputs, batch_size):
    batch_start = 0
    while batch_start < len(inputs):
        yield inputs[batch_start: batch_start + batch_size]
        batch_start += batch_size


def predict(
    model_name,
    input_records,
    output_file,
    max_source_tokens_count=600,
    batch_size=8
):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
    
    predictions = []
    for batch in gen_batch(input_records, batch_size):
        texts = [r["text"] for r in batch]
        input_ids = tokenizer(
            texts,                                                                                                     
            add_special_tokens=True,
            max_length=max_source_tokens_count,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )["input_ids"].to(device)
        
        output_ids = model.generate(
            input_ids=input_ids,
            no_repeat_ngram_size=4
        )
        summaries = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        for s in summaries:
            print(s)
        predictions.extend(summaries)
    with open(output_file, "w") as w:
        for p in predictions:
            w.write(p.strip().replace("\n", " ") + "\n")

gazeta_test = load_dataset('IlyaGusev/gazeta', script_version="v1.0")["test"]
predict("IlyaGusev/rut5_base_sum_gazeta", list(gazeta_test), "t5_predictions.txt")
```

Evaluation script: [evaluate.py](https://github.com/IlyaGusev/summarus/blob/master/evaluate.py)

Flags: --language ru --tokenize-after --lower
