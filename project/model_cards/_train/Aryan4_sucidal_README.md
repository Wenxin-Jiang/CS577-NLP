---
license: afl-3.0
---
# Suicidal
This text categorization model can predict if a word sequence is suicidal (1) or not (0).

## Data
The model was trained on the [Suicide and Depression Dataset](https://www.kaggle.com/) obtained from Kaggle. The dataset was taken from Reddit and contains 232,074 data divided into two categories: suicide and non-suicide.

## Parameters
The model fine-tuning was conducted on 1 epoch, with a batch size of 6, and a learning rate of 0.00001. Due to limited computing resources and time, we were unable to scale up the number of epochs and batch size.

## Performance
Following fine-tuning on the mentioned dataset, the model generated the subsequent results:
- Accuracy: 0.9792
- Recall: 0.9788
- Precision: 0.9677
- F1 Score: 0.9732

## How to Use
Import the model from the transformers library:
```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("Aryan4/suicidal")
model = AutoModel.from_pretrained("Aryan4/suicidal")
```

## Resources
For more resources, including the source code, please refer to the GitHub repository [Aryanstha/suicidal-text-detection](https://github.com/Aryanstha/).
