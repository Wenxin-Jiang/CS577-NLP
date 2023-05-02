---
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: roberta_gpt2_summarization_cnn_dailymail
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta_gpt2_summarization_cnn_dailymail

This model is a fine-tuned version of [](https://huggingface.co/) on the cnn_dailymail dataset.

## Model description
This model uses RoBerta encoder and GPT2 decoder and fine-tuned on the summarization task. It got Rouge scores as follows:

Rouge1= 35.886

Rouge2= 16.292

RougeL= 23.499
## Intended uses & limitations
To use its API:

from transformers import RobertaTokenizerFast, GPT2Tokenizer, EncoderDecoderModel

model = EncoderDecoderModel.from_pretrained("Ayham/roberta_gpt2_summarization_cnn_dailymail")

input_tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')

output_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

article = """Your Input Text"""

input_ids = input_tokenizer(article, return_tensors="pt").input_ids

output_ids = model.generate(input_ids)

print(output_tokenizer.decode(output_ids[0], skip_special_tokens=True))

More information needed

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.12.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
