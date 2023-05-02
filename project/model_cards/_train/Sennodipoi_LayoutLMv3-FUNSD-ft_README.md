LayoutLMv3 fine-tuned on the FUNSD dataset. Code and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm).

Results obtained using seqeval in strict mode:

|              | Precision | Recall | F1-score | Variance (F1) |
|--------------|-----------|--------|----------|---------------|
| Answer       | 0.90      | 0.91   | 0.90     | 3e-5          |
| Header       | 0.61      | 0.66   | 0.63     | 4e-4          |
| Question     | 0.88      | 0.87   | 0.88     | 1e-4          |
| Micro avg    | 0.87      | 0.88   | 0.87     | 3e-5          |
| Macro avg    | 0.79      | 0.82   | 0.80     | 3e-5          |
| Weighted avg | 0.87      | 0.88   | 0.87     | 3e-5          |
