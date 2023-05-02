# Nepali Covid Tweet Classification
## This model was developed by finetuning the NepaliBERT model previously developed by me on Nepali COVID-related tweets. This dataset has about 15000 observations annotated with positive, negative, and neutral labels. NepaliBERT model was able to achieve SOTA results while finetuning this model for text classification. While training the model, the evaluation metrics obtained were:

* Training loss: 0.35592623149202174
* Validation loss: 0.6570735214928906
* F1 Score (Weighted): 0.7719232825307907



# LABELS INDICATOR
* LABEL 0 - Neutral 
* LABEL 1 - Positive
* Label 2 - Negative
## USAGE
```python
from transformers import pipeline

classifier = pipeline("text-classification", model = "Shushant/NepaliCovidTweetsClassification")
classifier("आउँदा केही दिनमा अमेरिकाले १५ लाखभन्दा बढी नेपालीलाई पुग्नेगरी कोभीड१९ खोप निशुल्क उपलब्ध गराउंदैछ।")
```