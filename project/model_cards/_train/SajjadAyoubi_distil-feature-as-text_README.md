base model: 'HooshvareLab/distilbert-fa-zwnj-base'
- trained for 2 epochs with 256 as max_length
- 3x faster than the Bert model despite having the same performance

model performance on test:
```
{'eval_loss': 0.3385954797267914,
 'eval_roc_auc': 0.9378028883850424,
 'eval_f1_score': 0.8662723907586265,
 'eval_recall': 0.8818815783774419,
 'eval_percision': 0.8512061541034324,
 'eval_runtime': 204.8524,
 'eval_samples_per_second': 229.609,
 'eval_steps_per_second': 7.176,
 'epoch': 2.0}
 ```