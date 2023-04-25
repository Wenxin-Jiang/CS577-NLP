---
language:
- ru
tags:
- summarization
license: apache-2.0
inference:
  parameters:
    no_repeat_ngram_size: 4
    
---

# RuBertTelegramHeadlines


## Model description

Example model for [Headline generation competition](https://competitions.codalab.org/competitions/29905)

Based on [RuBERT](http://docs.deeppavlov.ai/en/master/features/models/bert.html) model

## Intended uses & limitations

#### How to use

```python
from transformers import AutoTokenizer, EncoderDecoderModel

model_name = "IlyaGusev/rubert_telegram_headlines"
tokenizer = AutoTokenizer.from_pretrained(model_name, do_lower_case=False, do_basic_tokenize=False, strip_accents=False)
model = EncoderDecoderModel.from_pretrained(model_name)

article_text = "..."

input_ids = tokenizer(
    [article_text],
    add_special_tokens=True,
    max_length=256,
    padding="max_length",
    truncation=True,
    return_tensors="pt",
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=64,
    no_repeat_ngram_size=3,
    num_beams=10,
    top_p=0.95
)[0]

headline = tokenizer.decode(output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
print(headline)
```

## Training data

- Dataset: [ru_all_split.tar.gz](https://www.dropbox.com/s/ykqk49a8avlmnaf/ru_all_split.tar.gz)

## Training procedure

```python
import random

import torch
from torch.utils.data import Dataset
from tqdm.notebook import tqdm
from transformers import BertTokenizer, EncoderDecoderModel, Trainer, TrainingArguments, logging


def convert_to_tensors(
    tokenizer,
    text,
    max_text_tokens_count,
    max_title_tokens_count = None,
    title = None
):
    inputs = tokenizer(
        text,
        add_special_tokens=True,
        max_length=max_text_tokens_count,
        padding="max_length",
        truncation=True
    )
    result = {
        "input_ids": torch.tensor(inputs["input_ids"]),
        "attention_mask": torch.tensor(inputs["attention_mask"]),
    }

    if title is not None:
        outputs = tokenizer(
            title,
            add_special_tokens=True,
            max_length=max_title_tokens_count,
            padding="max_length",
            truncation=True
        )

        decoder_input_ids = torch.tensor(outputs["input_ids"])
        decoder_attention_mask = torch.tensor(outputs["attention_mask"])
        labels = decoder_input_ids.clone()
        labels[decoder_attention_mask == 0] = -100
        result.update({
            "labels": labels,
            "decoder_input_ids": decoder_input_ids,
            "decoder_attention_mask": decoder_attention_mask
        })
    return result


class GetTitleDataset(Dataset):
    def __init__(
        self,
        original_records,
        sample_rate,
        tokenizer,
        max_text_tokens_count,
        max_title_tokens_count
    ):
        self.original_records = original_records
        self.sample_rate = sample_rate
        self.tokenizer = tokenizer
        self.max_text_tokens_count = max_text_tokens_count
        self.max_title_tokens_count = max_title_tokens_count
        self.records = []
        for record in tqdm(original_records):
            if random.random() > self.sample_rate:
                continue
            tensors = convert_to_tensors(
                tokenizer=tokenizer,
                title=record["title"],
                text=record["text"],
                max_title_tokens_count=self.max_title_tokens_count,
                max_text_tokens_count=self.max_text_tokens_count
            )
            self.records.append(tensors)

    def __len__(self):
        return len(self.records)

    def __getitem__(self, index):
        return self.records[index]


def train(
    train_records,
    val_records,
    pretrained_model_path,
    train_sample_rate=1.0,
    val_sample_rate=1.0,
    output_model_path="models",
    checkpoint=None,
    max_text_tokens_count=256,
    max_title_tokens_count=64,
    batch_size=8,
    logging_steps=1000,
    eval_steps=10000,
    save_steps=10000,
    learning_rate=0.00003,
    warmup_steps=2000,
    num_train_epochs=3
):
    logging.set_verbosity_info()
    tokenizer = BertTokenizer.from_pretrained(
        pretrained_model_path,
        do_lower_case=False,
        do_basic_tokenize=False,
        strip_accents=False
    )
    train_dataset = GetTitleDataset(
        train_records,
        train_sample_rate,
        tokenizer,
        max_text_tokens_count=max_text_tokens_count,
        max_title_tokens_count=max_title_tokens_count
    )
    val_dataset = GetTitleDataset(
        val_records,
        val_sample_rate,
        tokenizer,
        max_text_tokens_count=max_text_tokens_count,
        max_title_tokens_count=max_title_tokens_count
    )
    
    model = EncoderDecoderModel.from_encoder_decoder_pretrained(pretrained_model_path, pretrained_model_path)
    training_args = TrainingArguments(
        output_dir=output_model_path,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        do_train=True,
        do_eval=True,
        overwrite_output_dir=False,
        logging_steps=logging_steps,
        eval_steps=eval_steps,
        evaluation_strategy="steps",
        save_steps=save_steps,
        learning_rate=learning_rate,
        warmup_steps=warmup_steps,
        num_train_epochs=num_train_epochs,
        max_steps=-1,
        save_total_limit=1,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )
    trainer.train(checkpoint)
    model.save_pretrained(output_model_path)
```