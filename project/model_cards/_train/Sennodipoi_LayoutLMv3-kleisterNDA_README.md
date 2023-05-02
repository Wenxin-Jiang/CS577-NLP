LayoutLMv3 fine-tuned on the Kleister-NDA dataset. Code (including pre-processing) and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm).

Results obtained with seqeval in strict mode:


|                | Precision | Recall | F1-score | Variance (F1) |
|----------------|-----------|--------|----------|---------------|
| EFFECTIVE_DATE | 0.92      | 0.99   | 0.95     | 5e-5          |
| JURISDICTION   | 0.87      | 0.88   | 0.88     | 8e-6          |
| PARTY          | 0.92      | 0.99   | 0.95     | 5e-5          |
| TERM           | 1         | 1      | 1        | 0             |
| Micro avg      | 0.91      | 0.96   | 0.94     | 2e-5          |
| Macro avg      | 0.92      | 0.96   | 0.94     | 3e-7          |
| Weighted avg   | 0.91      | 0.96   | 0.94     | 2e-5          |

Since I used the same segmentation strategy of the original paper i.e. using the labels to create segments, the scores are not directly comparable with the other LayoutLM versions.