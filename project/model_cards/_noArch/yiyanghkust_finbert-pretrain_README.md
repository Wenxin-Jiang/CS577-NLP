`FinBERT` is a BERT model pre-trained on financial communication text. The purpose is to enhance financial NLP research and practice. It is trained on the following three financial communication corpus. The total corpora size is 4.9B tokens.

- Corporate Reports 10-K & 10-Q: 2.5B tokens
- Earnings Call Transcripts: 1.3B tokens
- Analyst Reports: 1.1B tokens

If you use the model in your academic work, please cite the following papers:

Huang, Allen H., Hui Wang, and Yi Yang. "FinBERT: A Large Language Model for Extracting Information from Financial Text." *Contemporary Accounting Research* (2022).

Yang, Yi, Mark Christopher Siy Uy, and Allen Huang. "Finbert: A pretrained language model for financial communications." *arXiv preprint arXiv:2006.08097* (2020).

`FinBERT` can be further fine-tuned on downstream tasks. Specifically, we have fine-tuned `FinBERT` for financial sentiment analysis, ESG classification, Forward-looking statement classification and etc. Visit [FinBERT.AI](https://finbert.ai/) for more details on these task-specific models and recent development of FinBERT.