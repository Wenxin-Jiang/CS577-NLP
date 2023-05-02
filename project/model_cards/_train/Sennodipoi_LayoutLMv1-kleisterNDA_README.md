LayoutLMv1 fine-tuned on the Kleister-NDA dataset. Code (including pre-processing) and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm)

Results obtained with seqeval in strict mode:

|                          | Precision | Recall| F1-score | Variance (F1) |
|--------------------------|--------------------|-----------------|-------------------|------------------------|
| EFFECTIVE\_DATE | 0.87               | 0.51            | 0.64              | 2e-6                   |
| JURISDICTION   | 0.75               | 0.84            | 0.80              | 4e-7                   |
| PARTY           | 0.84               | 0.71            | 0.77              | 9e-6                   |
| TERM            | 0.69               | 0.51            | 0.58              | 1e-3                   |
| Micro avg       | 0.81               | 0.72            | 0.77              | 2e-6                   |
| Macro avg       | 0.79               | 0.65            | 0.70              | 9e-5                   |
| Weighted avg    | 0.82               | 0.73            | 0.76              | 3e-6                   |
