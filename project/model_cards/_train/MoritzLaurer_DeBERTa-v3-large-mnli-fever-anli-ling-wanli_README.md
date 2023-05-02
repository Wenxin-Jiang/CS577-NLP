---
language: 
- en
tags:
- text-classification
- zero-shot-classification
license: mit
metrics:
- accuracy
datasets:
- multi_nli
- anli
- fever
- lingnli
- alisawuffles/WANLI
pipeline_tag: zero-shot-classification
#- text-classification
#widget:
#- text: "I first thought that I really liked the movie, but upon second thought it was actually disappointing. [SEP] The movie was not good."

model-index:  # info: https://github.com/huggingface/hub-docs/blame/main/modelcard.md
- name: DeBERTa-v3-large-mnli-fever-anli-ling-wanli
  results:
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: multi_nli          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: MultiNLI-matched         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: validation_matched        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,912       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: multi_nli          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: MultiNLI-mismatched         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: validation_mismatched        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,908       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: anli          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: ANLI-all         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: test_r1+test_r2+test_r3        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,702       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: anli          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: ANLI-r3         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: test_r3        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,64       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: alisawuffles/WANLI          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: WANLI         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: test        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,77       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
  - task:
      type: text-classification             # Required. Example: automatic-speech-recognition
      name: Natural Language Inference             # Optional. Example: Speech Recognition
    dataset:
      type: lingnli          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: LingNLI         # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: test        # Optional. Example: test
    metrics:
      - type: accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0,87       # Required. Example: 20.90
        #name:           # Optional. Example: Test WER
        verified: false              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).



---

# DeBERTa-v3-large-mnli-fever-anli-ling-wanli
## Model description
This model was fine-tuned on the [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), Adversarial-NLI ([ANLI](https://huggingface.co/datasets/anli)), [LingNLI](https://arxiv.org/pdf/2104.07179.pdf) and [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) datasets, which comprise 885 242 NLI hypothesis-premise pairs. This model is the best performing NLI model on the Hugging Face Hub as of 06.06.22 and can be used for zero-shot classification. It significantly outperforms all other large models on the [ANLI benchmark](https://github.com/facebookresearch/anli).

The foundation model is [DeBERTa-v3-large from Microsoft](https://huggingface.co/microsoft/deberta-v3-large). DeBERTa-v3 combines several recent innovations compared to classical Masked Language Models like BERT, RoBERTa etc., see the [paper](https://arxiv.org/abs/2111.09543)


### How to use the model
#### Simple zero-shot classification pipeline
```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli")
sequence_to_classify = "Angela Merkel is a politician in Germany and leader of the CDU"
candidate_labels = ["politics", "economy", "entertainment", "environment"]
output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
print(output)
```
#### NLI use-case
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "I first thought that I liked the movie, but upon second thought it was actually disappointing."
hypothesis = "The movie was not good."

input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))  # device = "cuda:0" or "cpu"
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["entailment", "neutral", "contradiction"]
prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
print(prediction)
```

### Training data
DeBERTa-v3-large-mnli-fever-anli-ling-wanli was trained on the [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), Adversarial-NLI ([ANLI](https://huggingface.co/datasets/anli)), [LingNLI](https://arxiv.org/pdf/2104.07179.pdf) and [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) datasets, which comprise 885 242 NLI hypothesis-premise pairs. Note that [SNLI](https://huggingface.co/datasets/snli) was explicitly excluded due to quality issues with the dataset. More data does not necessarily make for better NLI models. 

### Training procedure
DeBERTa-v3-large-mnli-fever-anli-ling-wanli was trained using the Hugging Face trainer with the following hyperparameters. Note that longer training with more epochs hurt performance in my tests (overfitting).


```
training_args = TrainingArguments(
    num_train_epochs=4,              # total number of training epochs
    learning_rate=5e-06,
    per_device_train_batch_size=16,   # batch size per device during training
    gradient_accumulation_steps=2,    # doubles the effective batch_size to 32, while decreasing memory requirements
    per_device_eval_batch_size=64,    # batch size for evaluation
    warmup_ratio=0.06,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    fp16=True                        # mixed precision training
)
```

### Eval results
The model was evaluated using the test sets for MultiNLI, ANLI, LingNLI, WANLI and the dev set for Fever-NLI. The metric used is accuracy.
The model achieves state-of-the-art performance on each dataset. Surprisingly, it outperforms the previous [state-of-the-art on ANLI](https://github.com/facebookresearch/anli) (ALBERT-XXL) by 8,3%. I assume that this is because ANLI was created to fool masked language models like RoBERTa (or ALBERT), while DeBERTa-v3 uses a better pre-training objective (RTD), disentangled attention and I fine-tuned it on higher quality NLI data. 

|Datasets|mnli_test_m|mnli_test_mm|anli_test|anli_test_r3|ling_test|wanli_test|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Accuracy|0.912|0.908|0.702|0.64|0.87|0.77|
|Speed (text/sec, A100 GPU)|696.0|697.0|488.0|425.0|828.0|980.0|

## Limitations and bias
Please consult the original DeBERTa-v3 paper and literature on different NLI datasets for more information on the training data and potential biases. The model will reproduce statistical patterns in the training data. 

## Citation
If you use this model, please cite: Laurer, Moritz, Wouter van Atteveldt, Andreu Salleras Casas, and Kasper Welbers. 2022. ‘Less Annotating, More Classifying – Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT - NLI’. Preprint, June. Open Science Framework. https://osf.io/74b8k.

### Ideas for cooperation or questions?
If you have questions or ideas for cooperation, contact me at m{dot}laurer{at}vu{dot}nl or [LinkedIn](https://www.linkedin.com/in/moritz-laurer/)

### Debugging and issues
Note that DeBERTa-v3 was released on 06.12.21 and older versions of HF Transformers seem to have issues running the model (e.g. resulting in an issue with the tokenizer). Using Transformers>=4.13 might solve some issues. 