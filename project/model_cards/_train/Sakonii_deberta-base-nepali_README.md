---
license: mit
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
- name: de-berta-base-base-nepali
  results: []
---

# deberta-base-nepali

This model is pre-trained on [nepalitext](https://huggingface.co/datasets/Sakonii/nepalitext-language-model-dataset) dataset consisting of over 13 million Nepali text sequences using a masked language modeling (MLM) objective. Our approach trains a Sentence Piece Model (SPM) for text tokenization similar to [XLM-ROBERTa](https://arxiv.org/abs/1911.02116) and trains [DeBERTa](https://arxiv.org/abs/2006.03654) for language modeling. Find more details in [this paper](https://aclanthology.org/2022.sigul-1.14/).

It achieves the following results on the evaluation set:

mlm probability|evaluation loss|evaluation perplexity
--:|----:|-----:|
20%|1.860|6.424|

## Model description

Refer to original [microsoft/deberta-base](https://huggingface.co/microsoft/deberta-base)

## Intended uses & limitations

This backbone model intends to be fine-tuned on Nepali language focused downstream task such as sequence classification, token classification or question answering. 
The language model being trained on a data with texts grouped to a block size of 512, it handles text sequence up to 512 tokens and may not perform satisfactorily on shorter sequences.

## Usage

This model can be used directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Sakonii/deberta-base-nepali')
>>> unmasker("मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, <mask>, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।")

[{'score': 0.10054448992013931,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, वातावरण, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 790,
  'token_str': 'वातावरण'},
 {'score': 0.05399947986006737,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, स्वास्थ्य, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 231,
  'token_str': 'स्वास्थ्य'},
 {'score': 0.045006219297647476,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, जल, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 1313,
  'token_str': 'जल'},
 {'score': 0.04032573476433754,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, पर्यावरण, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 13156,
  'token_str': 'पर्यावरण'},
 {'score': 0.026729246601462364,
  'sequence': 'मानविय गतिविधिले प्रातृतिक पर्यावरन प्रनालीलाई अपरिमेय क्षति पु्र्याएको छ। परिवर्तनशिल जलवायुले खाध, सुरक्षा, संचार, जमिन, मौसमलगायतलाई असंख्य तरिकाले प्रभावित छ।',
  'token': 3996,
  'token_str': 'संचार'}]
  ```

Here is how we can use the model to get the features of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained('Sakonii/deberta-base-nepali')
model = AutoModelForMaskedLM.from_pretrained('Sakonii/deberta-base-nepali')

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
The model is trained with the same configuration as the original [microsoft/deberta-base](https://huggingface.co/microsoft/deberta-base); 512 tokens per instance, 6 instances per batch, and around 188.8K training steps (per epoch).


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Perplexity |
|:-------------:|:-----:|:------:|:---------------:|:----------:|
| 2.5454        | 1.0   | 188789 | 2.4273          | 11.3283    |
| 2.2592        | 2.0   | 377578 | 2.1448          | 8.5403     |
| 2.1171        | 3.0   | 566367 | 2.0030          | 7.4113     |
| 2.0227        | 4.0   | 755156 | 1.9133          | 6.7754     |
| 1.9375        | 5.0   | 943945 | 1.8600          | 6.4237     |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 2.0.0
- Tokenizers 0.11.6
