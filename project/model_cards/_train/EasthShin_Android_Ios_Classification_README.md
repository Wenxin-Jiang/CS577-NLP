## Bert-base-uncased for Android-Ios Question Classification

**Code**: See [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/EastHShin/Android-Ios-Classification-Workspace)
<br>
**Android-Ios-Classification DEMO**: [Ainize Endpoint](https://main-android-ios-classification-east-h-shin.endpoint.ainize.ai/)
<br>
**Demo web Code**: [Github](https://github.com/EastHShin/Android-Ios-Classification)
<br>
**Android-Ios-Classification API**: [Ainize API](https://ainize.ai/EastHShin/Android-Ios-Classification)
<br>
<br>
## Overview
**Language model**: bert-base-cased
<br>
**Language**: English
<br>
**Training data**: Question classification Android-Ios dataset from [Kaggle](https://www.kaggle.com/xhlulu/question-classification-android-or-ios)


## Usage

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_path = "EasthShin/Android_Ios_Classification"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

classifier = pipeline('text-classification', model=model_path, tokenizer=tokenizer)

question = "I bought goodnote in Appstore"

result = dict()
result[0] = classifier(question)[0]
```