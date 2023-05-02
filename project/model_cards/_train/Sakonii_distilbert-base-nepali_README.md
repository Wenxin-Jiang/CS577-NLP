---
license: apache-2.0
tags:
- generated_from_trainer
datasets: Sakonii/nepalitext-language-model-dataset
mask_token: <mask>
widget:
- text: मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ।
    परिवर्तनशिल जलवायुले खाध, सुरक्षा, <mask>, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित
    छ।
  example_title: Example 1
- text: अचेल विद्यालय र कलेजहरूले स्मारिका कत्तिको प्रकाशन गर्छन्, यकिन छैन । केही
    वर्षपहिलेसम्म गाउँसहरका सानाठूला <mask> संस्थाहरूमा पुग्दा शिक्षक वा कर्मचारीले
    संस्थाबाट प्रकाशित पत्रिका, स्मारिका र पुस्तक कोसेलीका रूपमा थमाउँथे ।
  example_title: Example 2
- text: जलविद्युत् विकासको ११० वर्षको इतिहास बनाएको नेपालमा हाल सरकारी र निजी क्षेत्रबाट
    गरी करिब २ हजार मेगावाट <mask> उत्पादन भइरहेको छ ।
  example_title: Example 3
model-index:
- name: distilbert-base-nepali
  results: []
---

# distilbert-base-nepali

This model is pre-trained on [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) dataset consisting of over 13 million Nepali text sequences using a masked language modeling (MLM) objective. Our approach trains a Sentence Piece Model (SPM) for text tokenization similar to [XLM-ROBERTa](https://arxiv.org/abs/1911.02116) and trains [distilbert model](https://arxiv.org/abs/1910.01108) for language modeling. Find more details in [this paper](https://aclanthology.org/2022.sigul-1.14/).

It achieves the following results on the evaluation set:

mlm probability|evaluation loss|evaluation perplexity
--:|----:|-----:|
15%|2.349|10.479|
20%|2.605|13.351|

## Model description

Refer to original [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)

## Intended uses & limitations

This backbone model intends to be fine-tuned on Nepali language focused downstream task such as sequence classification, token classification or question answering. 
The language model being trained on a data with texts grouped to a block size of 512, it handles text sequence up to 512 tokens and may not perform satisfactorily on shorter sequences.

## Usage

This model can be used directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Sakonii/distilbert-base-nepali')
>>> unmasker("मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, <mask>, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।")

[{'score': 0.04128897562623024,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, मौसम, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 2605,
  'token_str': 'मौसम'},
 {'score': 0.04100276157259941,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, प्रकृति, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 2792,
  'token_str': 'प्रकृति'},
 {'score': 0.026525357738137245,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, पानी, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 387,
  'token_str': 'पानी'},
 {'score': 0.02340106852352619,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, जल, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 1313,
  'token_str': 'जल'},
 {'score': 0.02055591531097889,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, वातावरण, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 790,
  'token_str': 'वातावरण'}]
```

Here is how we can use the model to get the features of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained('Sakonii/distilbert-base-nepali')
model = AutoModelForMaskedLM.from_pretrained('Sakonii/distilbert-base-nepali')

# prepare input
text = "चाहिएको text यता राख्नु होला।"
encoded_input = tokenizer(text, return_tensors='pt')

# forward pass
output = model(**encoded_input)
```

## Training data

This model is trained on [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) language modeling dataset which combines the datasets: [OSCAR](https://huggingface.co/datasets/oscar) , [cc100](https://huggingface.co/datasets/cc100) and a set of scraped Nepali articles on Wikipedia.
As for training the language model, the texts in the training set are grouped to a block of 512 tokens.

## Tokenization

A Sentence Piece Model (SPM) is trained on a subset of [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) dataset for text tokenization. The tokenizer trained with vocab-size=24576, min-frequency=4, limit-alphabet=1000 and model-max-length=512.

## Training procedure

The model is trained with the same configuration as the original [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased); 512 tokens per instance, 28 instances per batch, and around 35.7K training steps.

### Training hyperparameters

The following hyperparameters were used for training of the final epoch: [ Refer to the *Training results* table below for varying hyperparameters every epoch ]
- learning_rate: 5e-05
- train_batch_size: 28
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

The model is trained for 4 epochs with varying hyperparameters:

| Training Loss | Epoch | MLM Probability | Train Batch Size | Step  | Validation Loss | Perplexity |
|:-------------:|:-----:|:---------------:|:----------------:|:-----:|:---------------:|:----------:|
| 3.4477        | 1.0   | 15              | 26               | 38864 | 3.3067          | 27.2949    |
| 2.9451        | 2.0   | 15              | 28               | 35715 | 2.8238          | 16.8407    |
| 2.866         | 3.0   | 20              | 28               | 35715 | 2.7431          | 15.5351    |
| 2.7287        | 4.0   | 20              | 28               | 35715 | 2.6053          | 13.5353    |
| 2.6412        | 5.0   | 20              | 28               | 35715 | 2.5161          | 12.3802    |

Final model evaluated with MLM Probability of 15%:

| Training Loss | Epoch | MLM Probability | Train Batch Size | Step  | Validation Loss | Perplexity |
|:-------------:|:-----:|:---------------:|:----------------:|:-----:|:---------------:|:----------:|
| -             | -     | 15              | -                | -     | 2.3494          | 10.4791    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.9.1
- Datasets 1.18.3
- Tokenizers 0.10.3
