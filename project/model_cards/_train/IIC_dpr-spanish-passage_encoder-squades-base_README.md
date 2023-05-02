---
language:
- es
tags:
- sentence similarity  # Example: audio
- passage retrieval  # Example: automatic-speech-recognition
datasets:
- squad_es
metrics:
- eval_loss: 0.08608942725107592
- eval_accuracy: 0.9925325215819639
- eval_f1: 0.8805402320715237
- average_rank: 0.27430093209054596

model-index:
- name: dpr-spanish-passage_encoder-squades-base
  results:
  - task: 
      type: text similarity  # Required. Example: automatic-speech-recognition
      name: text similarity  # Optional. Example: Speech Recognition
    dataset:
      type: squad_es  # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: squad_es  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: loss
        value: 0.08608942725107592
        name: eval_loss
      - type: accuracy
        value: 0.99
        name: accuracy
      - type: f1
        value: 0.88
        name: f1
      - type: avgrank
        value: 0.2743
        name: avgrank
---

[Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) is a set of tools for performing state of the art open-domain question answering. It was initially developed by Facebook and there is an [official repository](https://github.com/facebookresearch/DPR). DPR is intended to retrieve the relevant documents to answer a given question, and is composed of 2 models, one for encoding passages and other for encoding questions. This concrete model is the one used for encoding passages. 

Regarding its use, this model should be used to vectorize the documents in the database of a question answering system in Spanish. Then, when a new question enters, [the question encoder should be used](https://huggingface.co/avacaondata/dpr-spanish-question_encoder-squades-base) to encode it, and then we compare that encoding with the encodings of the database to find the most similar documents, which then should be used for either extracting the answer or generating it.

For training the model, we used the spanish version of SQUAD, [SQUAD-ES](https://huggingface.co/datasets/squad_es), with which we created positive and negative examples for the model. 

Example of use:

```python
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer

model_str = "avacaondata/dpr-spanish-passage_encoder-squades-base"
tokenizer = DPRContextEncoderTokenizer.from_pretrained(model_str)
model = DPRContextEncoder.from_pretrained(model_str)

input_ids = tokenizer("Usain Bolt ganó varias medallas de oro en las Olimpiadas del año 2012", return_tensors="pt")["input_ids"]
embeddings = model(input_ids).pooler_output
```

The full metrics of this model on the evaluation split of SQUADES are:

```
evalloss: 0.08608942725107592
acc: 0.9925325215819639
f1: 0.8805402320715237
acc_and_f1: 0.9365363768267438
average_rank: 0.27430093209054596
```

And the classification report:

```
                precision   recall    f1-score   support

hard_negative     0.9961    0.9961    0.9961    325878
     positive     0.8805    0.8805    0.8805     10514

     accuracy                         0.9925    336392
    macro avg     0.9383    0.9383    0.9383    336392
 weighted avg     0.9925    0.9925    0.9925    336392

```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.