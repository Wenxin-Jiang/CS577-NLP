---
license: apache-2.0
tags:
- generated_from_trainer
datasets: Sakonii/nepalitext-language-model-dataset
widget:
- text: नेपाल र भारतबीच
  example_title: Example 1
- text: प्रधानमन्त्री
  example_title: Example 2
- text: 'दस वर्ष लामो '
  example_title: Example 3
- text: 'जापानमा आज '
  example_title: Example 4
- text: नेपालका धेरैजसो चाडपर्वहरूमध्ये,
  example_title: Example 5
model-index:
- name: distilgpt2-nepali
  results: []
---

# distilgpt2-nepali

This model is pre-trained on [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) dataset consisting of over 13 million Nepali text sequences using a Causal language modeling (CLM) objective. Our approach trains a Sentence Piece Model (SPM) for text tokenization similar to [XLM-ROBERTa](https://arxiv.org/abs/1911.02116) and trains [distilgpt2](https://huggingface.co/distilgpt2) for language modeling.

It achieves the following results on the evaluation set:

| Training Loss | Validation Loss | Perplexity
|:-------------:|:---------------:|:----------:|
| 3.3968        | 3.2705          | 26.3245

## Model description

Refer to original [distilgpt2](https://huggingface.co/distilgpt2)

## Intended uses & limitations

This raw model can be used for Nepali text generation and intends to be fine-tuned on Nepali language focused downstream task. 
The language model being trained on a data with texts grouped to a block size of 512, it handles text sequence up to 512 tokens and may not perform satisfactorily on shorter sequences.

## Usage

This model can be used directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility:

```python
>>> from transformers import pipeline, set_seed
>>> set_seed(42)
>>> generator = pipeline('text-generation', model='Sakonii/distilgpt2-nepali')
>>> generator("नेपालका धेरैजसो चाडपर्वहरूमध्ये,", max_length=30, num_return_sequences=5)

Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
[{'generated_text': 'नेपालका धेरैजसो चाडपर्वहरूमध्ये, तिहार र छठपर्व विशेष रूपमा मनाइने भएकाले नेपाली मौलिक पर्व पनि हो । हिन्दू धर्म र संस्कृतिक... काठमाडौं ।'},
 {'generated_text': 'नेपालका धेरैजसो चाडपर्वहरूमध्ये, तिहारको मुख्य दिन आज साँझ अस्ताउँदो सूर्यलाई अर्घ्य दिइएको छ । वैदिक विधि...विस्तृतमा पढ्नुस् काठमाडौं । नेपाल चिकित्सक संघका'},
 {'generated_text': 'नेपालका धेरैजसो चाडपर्वहरूमध्ये, चाडपर्व, विवाह,... नेपाली काँग्रेसका प्रवक्ता विश्वप्रकाश शर्माले पार्टीभित्र आन्तरिक झगडा हुने निश्चित भएको र गुटबन्दीका कारण चुनावमा हार बेहोर्नु'},
 {'generated_text': 'नेपालका धेरैजसो चाडपर्वहरूमध्ये, दशैं नेपालीहरूको मौलिक पर्वका रूपमा मनाउँछन् । नेपालीहरूको दोस्रो महान् पर्व तिहार हो । तिहारले दाजुभाइ तथा दिदीबहिनीहरूको बीचमा प्रगाढ सम्बन्ध स्थापित'},
 {'generated_text': 'नेपालका धेरैजसो चाडपर्वहरूमध्ये, माघे संक्रान्ति र माघे संक्रान्तिमा माघे संक्रान्तिमा मात्र नभएर फागुन महिनाभर नै विशेष महत्व रहने गरेको छ । काठमाडौं ।'}]
```

Here is how we can use the model to get the features of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('Sakonii/distilgpt2-nepali')
model = AutoModelForCausalLM.from_pretrained('Sakonii/distilgpt2-nepali')

# prepare input
text = "चाहिएको text यता राख्नु होला।"
encoded_input = tokenizer(text, return_tensors='pt')

# forward pass
output = model(**encoded_input)
```

## Training data

This model is trained on [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) language modeling dataset which combines the datasets: [OSCAR](https://huggingface.co/datasets/oscar) , [cc100](https://huggingface.co/datasets/cc100) and a set of scraped Nepali articles on Wikipedia.
As for training the language model, the texts are tokenized using Sentence Piece Model (SPM), a vocabulary size of 24,576 and texts are are grouped to a block of 512 tokens.

## Training procedure

The model is trained with the same configuration as the original [distilgpt2](https://huggingface.co/distilgpt2); but with 512 tokens per instance, 12 instances per batch, and around 188.8K training steps.


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Perplexity |
|:-------------:|:-----:|:------:|:---------------:|:----------:|
| 3.7645        | 1.0   | 94395  | 3.6291          | 37.6789    |
| 3.5857        | 2.0   | 188790 | 3.4442          | 31.3182    |
| 3.505         | 3.0   | 283185 | 3.3749          | 29.2214    |
| 3.4688        | 4.0   | 377580 | 3.3439          | 28.3294    |
| 3.3968        | 5.0   | 471975 | 3.2705          | 26.3245    |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 2.0.0
- Tokenizers 0.11.6
