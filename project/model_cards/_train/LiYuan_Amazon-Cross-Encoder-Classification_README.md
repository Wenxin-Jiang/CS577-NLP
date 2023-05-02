---
license: afl-3.0
---

There are two types of Cross-Encoder models. One is the Cross-Encoder Regression model that we fine-tuned and mentioned in the previous section. Next, we have the Cross-Encoder Classification model. These two models are introduced in the same paper https://doi.org/10.48550/arxiv.1908.10084 

Both models resolve the issue that the BERT model is too time-consuming and resource-consuming to train in pairwised sentences. These two model weights are initialized as the BERT and RoBERTa networks. We only need to fine-tune them, spending much less time to yield a comparable or even better sentence embedding. The below figure \ref{figure:5} shows the architecture of Cross-Encoder Classification.

![](1.png) 

Then we evaluated the model performance on the 2,000 held-out test set. We also got a test accuracy **46.05%** that is almost identical to the best validation accuracy, suggesting a good generalization model. 