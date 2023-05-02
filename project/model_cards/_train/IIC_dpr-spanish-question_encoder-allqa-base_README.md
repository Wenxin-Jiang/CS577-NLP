---
language:
- es
tags:
- sentence similarity  # Example: audio
- passage retrieval  # Example: automatic-speech-recognition
datasets:
- squad_es
- PlanTL-GOB-ES/SQAC
- IIC/bioasq22_es

metrics:
- eval_loss: 0.010779764448327261
- eval_accuracy: 0.9982682224158297
- eval_f1: 0.9446059155411182
- average_rank: 0.11728500598392888

model-index:
- name: dpr-spanish-question_encoder-allqa-base
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
        value: 0.010779764448327261
        name: eval_loss
      - type: accuracy
        value: 0.9982682224158297
        name: accuracy
      - type: f1
        value: 0.9446059155411182
        name: f1
      - type: avgrank
        value: 0.11728500598392888
        name: avgrank
---

[Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)-DPR is a set of tools for performing State of the Art open-domain question answering. It was initially developed by Facebook and there is an [official repository](https://github.com/facebookresearch/DPR). DPR is intended to retrieve the relevant documents to answer a given question, and is composed of 2 models, one for encoding passages and other for encoding questions. This concrete model is the one used for encoding questions.

With this and the [passage encoder model](https://huggingface.co/avacaondata/dpr-spanish-passage_encoder-allqa-base) we introduce the best passage retrievers in Spanish up to date (to the best of our knowledge), improving over the [previous model we developed](https://huggingface.co/IIC/dpr-spanish-question_encoder-squades-base), by training it for longer and with more data.

Regarding its use, this model should be used to vectorize a question that enters in a Question Answering system, and then we compare that encoding with the encodings of the database (encoded with [the passage encoder](https://huggingface.co/avacaondata/dpr-spanish-passage_encoder-squades-base)) to find the most similar documents , which then should be used for either extracting the answer or generating it.

For training the model, we used a collection of Question Answering datasets in Spanish: 
- the Spanish version of SQUAD, [SQUAD-ES](https://huggingface.co/datasets/squad_es)
- [SQAC- Spanish Question Answering Corpus](https://huggingface.co/datasets/PlanTL-GOB-ES/SQAC)
- [BioAsq22-ES](https://huggingface.co/datasets/IIC/bioasq22_es) - we translated this last one by using automatic translation with Transformers.

With this complete dataset we created positive and negative examples for the model (For more information look at [the paper](https://arxiv.org/abs/2004.04906) to understand the training process for DPR). We trained for 25 epochs with the same configuration as the paper. The [previous DPR model](https://huggingface.co/IIC/dpr-spanish-passage_encoder-squades-base) was trained for only 3 epochs with about 60% of the data.

Example of use:

```python
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer

model_str = "IIC/dpr-spanish-question_encoder-allqa-base"
tokenizer = DPRQuestionEncoderTokenizer.from_pretrained(model_str)
model = DPRQuestionEncoder.from_pretrained(model_str)

input_ids = tokenizer("¿Qué medallas ganó Usain Bolt en 2012?", return_tensors="pt")["input_ids"]
embeddings = model(input_ids).pooler_output
```

The full metrics of this model on the evaluation split of SQUADES are:

```
eval_loss: 0.010779764448327261
eval_acc: 0.9982682224158297
eval_f1: 0.9446059155411182
eval_acc_and_f1: 0.9714370689784739
eval_average_rank: 0.11728500598392888
```

And the classification report:

```
                precision    recall  f1-score   support

hard_negative     0.9991    0.9991    0.9991   1104999
     positive     0.9446    0.9446    0.9446     17547

     accuracy                         0.9983   1122546
    macro avg     0.9719    0.9719    0.9719   1122546
 weighted avg     0.9983    0.9983    0.9983   1122546

```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.