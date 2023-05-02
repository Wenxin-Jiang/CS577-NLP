LayoutLMv2 fine-tuned on the Kleister-NDA dataset. Code (including pre-processing) and results are available at the official GitHub repository of my [Master Degree thesis ](https://github.com/AleRosae/thesis-layoutlm).

Results obtained with seqeval in strict mode:

|                    |   Precision  |   Recall  |   F1-Score  |   Variance (F1)  |
|--------------------|--------------|-----------|-------------|------------------|
|   EFFECTIVE _DATE  | 0.69         | 0.77      | 0.72        | 4e-4             |
|   JURISDICTION     | 0.90         | 0.87      | 0.88        | 1e-4             |
|   PARTY            | 0.73         | 0.87      | 0.79        | 8e-5             |
|   TERM             | 0.76         | 0.63      | 0.68        | 2e-3             |
|   Micro avg        | 0.76         | 0.85      | 0.80        | 1e-4             |
|   Macro avg        | 0.76         | 0.78      | 0.77        | 4e-4             |
|   Weighted avg     | 0.77         | 0.85      | 0.80        | 1e-4             |

