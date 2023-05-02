---
language: en
widget:
- text: "I got a rash from taking acetaminophen"
tags:
- sagemaker
- bert-base-uncased
- text classification
license: apache-2.0
datasets:
- adecorpusv2
model-index:
- name: BERT-ade_corpus
  results:
  - task: 
      name: Text Classification
      type: text-classification
    dataset:
      name: "ade_corpus_v2Ade_corpus_v2_classification" 
      type: ade_corpus
    metrics:
       - name: Validation Accuracy
         type: accuracy
         value: 92.98
       - name: Validation F1
         type: f1
         value: 82.73
  
---

## bert-base-uncased
This model was trained using Amazon SageMaker and the new Hugging Face Deep Learning container.

- Problem type: Text Classification(adverse drug effects detection).

## Hyperparameters
```json
{
    "do_eval": true,
    "do_train": true,
    "fp16": true,
    "load_best_model_at_end": true,
    "model_name": "bert-base-uncased",
    "num_train_epochs": 10,
    "per_device_eval_batch_size": 16,
    "per_device_train_batch_size": 16,
    "learning_rate":5e-5

}
```
## Validation Metrics
| key | value |
| --- | ----- |
| eval_accuracy  | 0.9298021697511167 |
| eval_auc | 0.8902672664394546 |
| eval_f1 | 0.827315541601256 |
| eval_loss | 0.17835010588169098 |
| eval_recall | 0.8234375 |
| eval_precision | 0.831230283911672 |

## Usage
You can use cURL to access this model:
```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I got a rash from taking acetaminophen"}' https://api-inference.huggingface.co/models/Jorgeutd/bert-base-uncased-ade-Ade-corpus-v2
```


"""