---
library_name: paddlenlp
license: apache-2.0
language:
- zh
tags:
- zero-shot-classification
---

[![paddlenlp-banner](https://user-images.githubusercontent.com/1371212/175816733-8ec25eb0-9af3-4380-9218-27c154518258.png)](https://github.com/PaddlePaddle/PaddleNLP)

# PaddlePaddle/utc-large

Text classification technology is widely used in various industries such as dialogue intention recognition, bill archiving, and event detection. 
However, there are many challenges in industrial-level text classification practices, including diverse tasks, limited data availability and label transfer difficulty. 
To address these issues, UTC models text classification as a matching task between labels and text, based on the idea of Unified Semantic Matching (USM).
Thus, it can handle multiple classification tasks with a single model, reducing development and machine costs and achieving good zero/few-shot transfer performance.



USM Paper: https://arxiv.org/abs/2301.03282

PaddleNLP released UTC model for various text classification tasks which use ERNIE models as the pre-trained language models and were finetuned on a large amount of text classification data.


![UTC-diagram](https://user-images.githubusercontent.com/25607475/212268807-66181bcb-d3f9-4086-9d4a-de4d1d0933c2.png)


## Available Models

|     Model Name   |        Usage Scenarios     |       Supporting Tasks        |
| :--------------: | :------------------------- | :---------------------------- |
| `utc-large`      | A **text classification** model supports **Chinese** | Supports intention recognition, semantic matching, natural language inference, semantic analysis, etc. |


## Performance on Text Dataset

UTC tops [ZeroCLUE](https://www.cluebenchmarks.com/zeroclue.html) and [FewCLUE](https://www.cluebenchmarks.com/fewclue.html) benchmarks, as of 2023/01/12.

![UTC-benchmarks](https://s3.amazonaws.com/moonup/production/uploads/1675419368924-62d7bc8c63583ad7bf1d665a.png)



**Detailed Info:** https://github.com/PaddlePaddle/PaddleNLP/tree/develop/applications/zero_shot_text_classification
 