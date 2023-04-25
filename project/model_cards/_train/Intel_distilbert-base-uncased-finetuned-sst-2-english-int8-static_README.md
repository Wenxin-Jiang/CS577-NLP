---
language: en
license: apache-2.0
tags:
- text-classfication
- int8
- neural-compressor
- Intel® Neural Compressor
- PostTrainingStatic
datasets:
- sst2
model-index:
- name: distilbert-base-uncased-finetuned-sst-2-english-int8-static
  results:
  - task:
      type: sentiment-classification
      name: Sentiment Classification
    dataset:
      type: sst2
      name: Stanford Sentiment Treebank
    metrics:
    - type: accuracy
      value: 90.37
      name: accuracy
      config: accuracy
      verified: false
---

## Model Details: INT8 DistilBERT base uncased finetuned SST-2

This model is a fine-tuned DistilBERT model for the downstream task of sentiment classification, training on the [SST-2 dataset](https://huggingface.co/datasets/sst2) and quantized to INT8 (post-training static quantization) from the original FP32 model ([distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)). 
The same model is provided in two different formats: PyTorch and ONNX. 

| Model Detail | Description |
| ----------- | ----------- | 
| Model Authors - Company | Intel | 
| Date | March 29, 2022 for PyTorch model & February 3, 2023 for ONNX model | 
| Version | 1 | 
| Type | NLP DistilBERT (INT8) - Sentiment Classification (+/-) | 
| Paper or Other Resources | [https://github.com/huggingface/optimum-intel](https://github.com/huggingface/optimum-intel) | 
| License | Apache 2.0 |
| Questions or Comments | [Community Tab](https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static/discussions) and [Intel Developers Discord](https://discord.gg/rv2Gp55UJQ) |

| Intended Use | Description |
| ----------- | ----------- | 
| Primary intended uses | Inference for sentiment classification (classifying whether a statement is positive or negative) | 
| Primary intended users | Anyone | 
| Out-of-scope uses | This model is already fine-tuned and quantized to INT8. It is not suitable for further fine-tuning in this form. To fine-tune your own model, you can start with [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english). The model should not be used to intentionally create hostile or alienating environments for people. |

#### Load the PyTorch model with Optimum Intel
```python
from optimum.intel.neural_compressor import INCModelForSequenceClassification

model_id = "Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static"
int8_model = INCModelForSequenceClassification.from_pretrained(model_id)
```

#### Load the ONNX model with Optimum:
```python
from optimum.onnxruntime import ORTModelForSequenceClassification

model_id = "Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static"
int8_model = ORTModelForSequenceClassification.from_pretrained(model_id)
```

| Factors | Description | 
| ----------- | ----------- | 
| Groups | Movie reviewers from the internet | 
| Instrumentation | Text movie single-sentence reviews taken from 4 authors. More information can be found in the original paper by [Pang and Lee (2005)](https://arxiv.org/abs/cs/0506075) |
| Environment | - |
| Card Prompts | Model deployment on alternate hardware and software can change model performance |

| Metrics | Description | 
| ----------- | ----------- | 
| Model performance measures | Accuracy |
| Decision thresholds | - | 
| Approaches to uncertainty and variability | - | 

|  | PyTorch INT8 | ONNX INT8 | FP32 |
|---|---|---|---|
| **Accuracy (eval-accuracy)** |0.9037|0.9060|0.9106|
| **Model Size (MB)**  |65|80|255|

| Training and Evaluation Data | Description | 
| ----------- | ----------- | 
| Datasets | The dataset can be found here: [datasets/sst2](https://huggingface.co/datasets/sst2). There dataset has a total of 215,154 unique phrases, annotated by 3 human judges. |
| Motivation | Dataset was chosen to showcase the benefits of quantization on an NLP classification task with the [Optimum Intel](https://github.com/huggingface/optimum-intel) and [Intel® Neural Compressor](https://github.com/intel/neural-compressor)  |
| Preprocessing | The calibration dataloader is the train dataloader. The default calibration sampling size 100 isn't divisible exactly by batch size 8, so the real sampling size is 104.| 

| Quantitative Analyses | Description | 
| ----------- | ----------- | 
| Unitary results | The model was only evaluated on accuracy. There is no available comparison between evaluation factors. |
| Intersectional results | There is no available comparison between the intersection of evaluated factors.  |

| Ethical Considerations | Description | 
| ----------- | ----------- | 
| Data | The data that make up the model are movie reviews from authors on the internet. |
| Human life | The model is not intended to inform decisions central to human life or flourishing. It is an aggregated set of movie reviews from the internet. | 
| Mitigations | No additional risk mitigation strategies were considered during model development. |
| Risks and harms | The data are biased toward the particular reviewers' opinions and the judges (labelers) of the data. Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al., 2021](https://aclanthology.org/2021.acl-long.330.pdf), and [Bender et al., 2021](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)). Predictions generated by the model may include disturbing and harmful stereotypes across protected classes; identity characteristics; and sensitive, social, and occupational groups. Beyond this, the extent of the risks involved by using the model remain unknown.|
| Use cases | - | 

| Caveats and Recommendations |
| ----------- | 
| Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. There are no additional caveats or recommendations for this model. |

# BibTeX Entry and Citation Info
```
@misc{distilbert-base-uncased-finetuned-sst-2-english-int8-static
  author    = {Xin He, Yu Wenz},
  title     = {distilbert-base-uncased-finetuned-sst-2-english-int8-static},
  year      = {2022},
  url       = {https://huggingface.co/Intel/distilbert-base-uncased-finetuned-sst-2-english-int8-static},
}
```
