---
language: en
license: mit
datasets:
- acl-14-short-data
- semeval14
- semeval15
- semeval16
tags:
- gcn
- bert
- senticgcn
- text-classification
inference: false
model-index:
- name: SenticGCN
  results:
  - task:
      type: text-classification
      name: Sentic-GCN
    dataset:
      name: SemEval14-Laptop (Sentic-GCN)
      type: semeval14
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9436
    - name: F1 
      type: f1
      value: 0.9443
  - task:
      type: text-classification
      name: Sentic-GCN
    dataset:
      name: SemEval14-Restaurant (Sentic-GCN)
      type: semeval14
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9455
    - name: F1 
      type: f1
      value: 0.9199
  - task:
      type: text-classification
      name: Sentic-GCN
    dataset:
      name: SemEval15-Restaurant (Sentic-GCN)
      type: semeval15
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9675
    - name: F1 
      type: f1
      value: 0.9355
  - task:
      type: text-classification
      name: Sentic-GCN
    dataset:
      name: SemEval16-Restaurant (Sentic-GCN)
      type: semeval16
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9922
    - name: F1 
      type: f1
      value: 0.9915
      
- name: SenticGCNBert
  results:
  - task:
      type: text-classification
      name: Sentic-GCN Bert
    dataset:
      name: SemEval14-Laptop (Sentic-GCN Bert)
      type: semeval14
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9922
    - name: F1 
      type: f1
      value: 0.9915
  - task:
      type: text-classification
      name: Sentic-GCN Bert
    dataset:
      name: SemEval14-Restaurant (Sentic-GCN Bert)
      type: semeval14
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9739
    - name: F1 
      type: f1
      value: 0.9653
  - task:
      type: text-classification
      name: Sentic-GCN Bert
    dataset:
      name: SemEval15-Restaurant (Sentic-GCN Bert)
      type: semeval15
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9917
    - name: F1 
      type: f1
      value: 0.9878
  - task:
      type: text-classification
      name: Sentic-GCN Bert
    dataset:
      name: SemEval16-Restaurant (Sentic-GCN Bert)
      type: semeval16
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9937
    - name: F1 
      type: f1
      value: 0.9879
---

# Aspect-Based Sentiment Analysis
You can **test the model** at [aspect-based-sentiment-analysis](https://huggingface.co/spaces/aisingapore/aspect-based-sentiment-analysis).<br />
If you want to find out more information, please contact us at sg-nlp@aisingapore.org.


## Table of Contents
- [Model Details](#model-details)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Training](#training)
- [Model Parameters](#parameters)

## Model Details
**Model Name:** Sentic-GCN
- **Description:** This is a neural network that utilises LSTM and GCN to detect the sentiment polarities of different aspects in the same sentence. The models used corresponds to the associated models described in the paper.
- **Paper:** Aspect-based sentiment analysis via affective knowledge enhanced graph convolutional networks, 2021: 107643.
- **Author(s):** Bin Liang, Hang Su, Lin Gui, Erik Cambria, Ruifeng Xu. (2021).
- **URL:** https://github.com/BinLiang-NLP/Sentic-GCN 

# How to Get Started With the Model

## Install Python package
SGnlp is an initiative by AI Singapore's NLP Hub. They aim to bridge the gap between research and industry, promote translational research, and encourage adoption of NLP techniques in the industry. <br><br> Various NLP models, other than aspect sentiment analysis are available in the python package. You can try them out at [NLP Hub - Demo](https://sgnlp.aisingapore.net/).

```python
pip install sgnlp

```

## Examples
For more full code guide (such as SenticGCN), please refer to this [documentation](https://sgnlp.aisingapore.net/docs/model/senticgcn.html). <br> Alternatively, you can also try out the [demo](https://huggingface.co/spaces/aisingapore/aspect-based-sentiment-analysis) for SenticGCN-Bert.

Example of SenticGCN-Bert model (with embedding):
```python
from sgnlp.models.sentic_gcn import(
    SenticGCNBertConfig,
    SenticGCNBertModel,
    SenticGCNBertEmbeddingConfig,
    SenticGCNBertEmbeddingModel,
    SenticGCNBertTokenizer,
    SenticGCNBertPreprocessor,
    SenticGCNBertPostprocessor
)

tokenizer = SenticGCNBertTokenizer.from_pretrained("bert-base-uncased")

# Load Model
config  = SenticGCNBertConfig.from_pretrained("./senticgcn_bert/config.json")
model   = SenticGCNBertModel.from_pretrained("./senticgcn_bert/pytorch_model.bin",config=config)

# Load Embedding Model
embed_config    = SenticGCNBertEmbeddingConfig.from_pretrained("bert-base-uncased")
embed_model     = SenticGCNBertEmbeddingModel.from_pretrained("bert-base-uncased", config=embed_config)

preprocessor = SenticGCNBertPreprocessor(
    tokenizer=tokenizer, embedding_model=embed_model,
    senticnet="./senticgcn_bert/senticnet.pickle",
    device="cpu")

postprocessor = SenticGCNBertPostprocessor()

inputs = [
    {  # Single word aspect
        "aspects": ["service"],
        "sentence": "To sum it up : service varies from good to mediorce , \
        depending on which waiter you get ; generally it is just average ok .",
    },
    {  # Single-word, multiple aspects
        "aspects": ["service", "decor"],
        "sentence": "Everything is always cooked to perfection , the service \
        is excellent, the decor cool and understated.",
    },
    {  # Multi-word aspect
        "aspects": ["grilled chicken", "chicken"],
        "sentence": "the only chicken i moderately enjoyed was their grilled chicken \
        special with edamame puree .",
    },
]

processed_inputs, processed_indices = preprocessor(inputs)
raw_outputs = model(processed_indices)

post_outputs = postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)

print(post_outputs[0])
# {'sentence': ['To', 'sum', 'it', 'up', ':', 'service', 'varies', 'from', 'good', 'to', 'mediorce', ',', 'depending', 'on', 'which'
#               'waiter', 'you', 'get', ';', 'generally', 'it', 'is', 'just', 'average', 'ok', '.'],
#  'aspects': [[5]],
#  'labels': [0]}

print(post_outputs[1])
# {'sentence': ['Everything', 'is', 'always', 'cooked', 'to', 'perfection', ',', 'the', 'service',
#               'is', 'excellent,', 'the', 'decor', 'cool', 'and', 'understated.'],
#  'aspects': [[8], [12]],
#  'labels': [1, 1]}

print(post_outputs[2])
# {'sentence': ['the', 'only', 'chicken', 'i', 'moderately', 'enjoyed', 'was', 'their', 'grilled',
#               'chicken', 'special', 'with', 'edamame', 'puree', '.'],
#  'aspects': [[8, 9], [2], [9]],
#  'labels': [1, 1, 1]}


```


# Training
The training datasets can be retrieved from the following Sentic-GCN([github](https://github.com/BinLiang-NLP/Sentic-GCN/tree/main/datasets)).

#### Training Results - For Sentic-GCN
- **Training Time:** ~10mins for ~35 epochs (early stopped)
- **Datasets:** SemEval14-Laptop/ SemEval14-Restaurant/ SemEval15-Restaurant/ SemEval16-Restaurant

#### Training Results - For Sentic-GCN Bert
- **Training Time:** ~1 hr for ~40 epochs (early stopped)
- **Datasets:** SemEval14-Laptop/ SemEval14-Restaurant/ SemEval15-Restaurant/ SemEval16-Restaurant

# Model Parameters
- **Model Weights:** [senticgcn](https://huggingface.co/aisingapore/SenticGCN/blob/main/senticgcn/pytorch_model.bin) | [senticgcn-bert](https://huggingface.co/aisingapore/SenticGCN/blob/main/senticgcn_bert/pytorch_model.bin)
- **Model Config:** [senticgcn](https://huggingface.co/aisingapore/SenticGCN/blob/main/senticgcn/config.json) | [senticgcn-bert](https://huggingface.co/aisingapore/SenticGCN/blob/main/senticgcn_bert/config.json)
- **Model Inputs:** Aspect (word), sentence containing the aspect
- **Model Outputs:** Sentiment of aspect, -1 (negative), 0 (neutral), 1 (postive)
- **Model Inference Info:**  1 sec on Intel(R) i7 Quad-Core @ 1.7GHz.



