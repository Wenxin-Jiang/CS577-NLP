---
widget:
- text: "Paytm’s Revenue Growth Trajectory To Remain Strong In Q1: Goldman Sachs"
- text: "Nifty ends above 16,900, Sensex gains 1,041 pts led by IT, metal, realty"
- text: "Amazon reports BLOWOUT earnings, beating revenue estimates and raising Q3 guidance"
- text: "Company went through great loss due to lawsuit in Q1"
---

## What is Roberta-Earning-Call-Transcript-Classification Model?

Roberta-Earning-Call-Transcript-Classification is a Multi-Label Classification Model trained with Annotated earning call transcript data. Roberta-base model was fine-tuned to train on earning call transcript data. This model could be very helpful in finding Negative, Positive, Litigious, Constraining and Uncertain thing in the sentence. This could be really helpful in analyzing Profit warning of a company.

## What is RoBERTa

RoBERTa builds on BERT’s language masking strategy and modifies key hyperparameters in BERT, including removing BERT’s next-sentence pretraining objective, and training with much larger mini-batches and learning rates. RoBERTa was also trained on an order of magnitude more data than BERT, for a longer amount of time. This allows RoBERTa representations to generalize even better to downstream tasks compared to BERT.

## What is Earning Call Transcript?

An earnings call is a teleconference, or webcast, in which a public company discusses the financial results of a reporting period. The name comes from earnings per share, the bottom line number in the income statement divided by the number of shares outstanding.

Example of Earning call Transcipt: https://www.fool.com/earnings/call-transcripts/2022/04/29/apple-aapl-q2-2022-earnings-call-transcript

Scraped 10 years of earning call transcript data for 10 companies like Apple, google, microsoft, Nvidia, Amazon, Intel, Cisco etc. Annotate the data in various categories of sentences like Negative, Positive, Litigious, Constraining and Uncertainty

And then used Loughran-McDonald sentiment lexicon and Use FinancialPhraseBank [Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. Journal of the Association for Information Science and Technology, 65(4), 782-796.] for data annotation.

## Hyperparameters

| Parameter         |      |
| ----------------- | :---: |
| Learning rate     | 1e-5 |
| Epochs            |  12 |
| Max Seq Length    | 240 |
| Batch size        |  128 |

## Results

Best Result of `Micro F1` - 82.8%

## Usage
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("NLPScholars/Roberta-Earning-Call-Transcript-Classification")
model = AutoModelForSequenceClassification.from_pretrained("NLPScholars/Roberta-Earning-Call-Transcript-Classification")
```

# Contributors 

* Sumit Ranjan- sumit.ranjan819@gmail.com,

* Aanchal Varma- aanchalvarma511@gmail.com,

* Akshul Mittal- akshull.mittal@gmail.com 
