LayoutLMv2 fine-tuned on the FUNSD dataset. Code and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm).

Results obtained with seqeval in strict mode:

|              | Precision | Recall | F1-score | Variance (F1) |
|--------------|-----------|--------|----------|---------------|
| ANSWER       | 0.82      | 0.83   | 0.82     | 4e-4          |
| HEADER       | 0.65      | 0.58   | 0.62     | 9e-4          |
| QUESTION     | 0.87      | 0.83   | 0.85     | 3e-5          |
| Micro avg    | 0.84      | 0.82   | 0.82     | 1e-4          |
| Macro avg    | 0.79      | 0.75   | 0.76     | 4e-4          |
| Weighted avg | 0.84      | 0.82   | 0.82     | 1e-4          |
