LayoutLMv1 fine-tuned on the FUNSD dataset. Code and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm).

Results obtained using seqeval in strict mode:

|              | Precision | Recall | F1-score | Variance (F1) |
|--------------|-----------|--------|----------|---------------|
| ANSWER       | 0.80      | 0.78   | 0.80     | 1e-4          |
| HEADER       | 0.62      | 0.47   | 0.53     | 2e-4          |
| QUESTION     | 0.85      | 0.71   | 0.83     | 3e-5          |
| Micro avg    | 0.83      | 0.77   | 0.81     | 1e-4          |
| Macro avg    | 0.77      | 0.56   | 0.72     | 3e-5          |
| Weighted avg | 0.83      | 0.78   | 0.80     | 1e-4          |
