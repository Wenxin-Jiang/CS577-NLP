---
tags:
- question-answering
- bert
language: en
license: apache-2.0
model-index:
- name: dynamic-tinybert
  results:
  - task:
      type: question-answering
      name: question-answering
    metrics:
    - type: exact_match
      value: 81.2867
    - type: f1
      value: 88.4735
datasets:
- squad
---
## Model Details: 80% 1x4 Block Sparse BERT-Base (uncased) Fine Tuned on SQuADv1.1
This model has been fine-tuned for the NLP task of question answering, trained on the SQuAD 1.1 dataset. It is a result of fine-tuning a Prune Once For All 80% 1x4 block sparse pre-trained BERT-Base model, combined with knowledge distillation. 
> We present a new method for training sparse pre-trained Transformer language models by integrating weight pruning and model distillation. These sparse pre-trained models can be used to transfer learning for a wide range of tasks while maintaining their sparsity pattern. We show how the compressed sparse pre-trained models we trained transfer their knowledge to five different downstream natural language tasks with minimal accuracy loss. 



| Model Detail | Description |
| ----------- | ----------- | 
| Model Authors - Company | Intel | 
| Model Card Authors | Intel | 
| Date | February 27, 2022 | 
| Version | 1 | 
| Type | NLP - Question Answering | 
| Architecture | "The method consists of two steps, teacher preparation and student pruning. The sparse pre-trained model we trained is the model we use for transfer learning while maintaining its sparsity pattern. We call the method Prune Once for All since we show how to fine-tune the sparse pre-trained models for several language tasks while we prune the pre-trained model only once." [(Zafrir et al., 2021)](https://arxiv.org/abs/2111.05754) |
| Paper or Other Resources | [Paper: Zafrir et al. (2021)](https://arxiv.org/abs/2111.05754); [GitHub Repo](https://github.com/IntelLabs/Model-Compression-Research-Package/tree/main/research/prune-once-for-all) | 
| License | Apache 2.0 |
| Questions or Comments | [Community Tab](https://huggingface.co/Intel/bert-base-uncased-squadv1.1-sparse-80-1x4-block-pruneofa/discussions) and [Intel Developers Discord](https://discord.gg/rv2Gp55UJQ)|

Visualization of Prunce Once for All method from [Zafrir et al. (2021)](https://arxiv.org/abs/2111.05754). More details can be found in their paper.
![Zafrir2021_Fig1.png](https://s3.amazonaws.com/moonup/production/uploads/6297f0e30bd2f58c647abb1d/nSDP62H9NHC1FA0C429Xo.png)

| Intended Use | Description |
| ----------- | ----------- | 
| Primary intended uses | You can use the model for the NLP task of question answering: given a corpus of text, you can ask it a question about that text, and it will find the answer in the text. | 
| Primary intended users | Anyone doing question answering | 
| Out-of-scope uses |  The model should not be used to intentionally create hostile or alienating environments for people.|

### How to use

Here is how to import this model in Python:

```python
import transformers
import model_compression_research as model_comp

model = transformers.AutoModelForQuestionAnswering.from_pretrained('Intel/bert-base-uncased-squadv1.1-sparse-80-1x4-block-pruneofa')

scheduler = mcr.pruning_scheduler_factory(model, '../../examples/transformers/question-answering/config/lock_config.json')

# Train your model...

scheduler.remove_pruning()
 ```
For more code examples, refer to the [GitHub Repo](https://github.com/IntelLabs/Model-Compression-Research-Package/tree/main/research/prune-once-for-all).


### Metrics (Model Performance):
| Model                         | Model Size | SQuADv1.1 (EM/F1) | MNLI-m (Acc) | MNLI-mm (Acc) | QQP (Acc/F1) | QNLI (Acc) | SST-2 (Acc) |
|-------------------------------|:----------:|:-----------------:|:------------:|:-------------:|:------------:|:----------:|:-----------:|
| [**80% 1x4 Block Sparse BERT-Base uncased**](https://huggingface.co/Intel/bert-base-uncased-squadv1.1-sparse-80-1x4-block-pruneofa)  |   -   |    81.29/88.47    |     -    |     -     | - |    -   |    -    |
| [85% Sparse BERT-Base uncased](https://huggingface.co/Intel/bert-base-uncased-sparse-85-unstructured-pruneofa)  |   Medium   |    81.10/88.42    |     82.71    |     83.67     |  91.15/88.00 |    90.34   |    91.46    |
| [90% Sparse BERT-Base uncased](https://huggingface.co/Intel/bert-base-uncased-sparse-90-unstructured-pruneofa)  |   Medium   |    79.83/87.25    |     81.45    |     82.43     |  90.93/87.72 |    89.07   |    90.88    |
| [90% Sparse BERT-Large uncased](https://huggingface.co/Intel/bert-large-uncased-sparse-90-unstructured-pruneofa) |    Large   |    83.35/90.20    |     83.74    |     84.20     |  91.48/88.43 |    91.39   |    92.95    |
| [85% Sparse DistilBERT uncased](https://huggingface.co/Intel/distilbert-base-uncased-sparse-85-unstructured-pruneofa) |    Small   |    78.10/85.82    |     81.35    |     82.03     |  90.29/86.97 |    88.31   |    90.60    |
| [90% Sparse DistilBERT uncased](https://huggingface.co/Intel/distilbert-base-uncased-sparse-90-unstructured-pruneofa) |    Small   |    76.91/84.82    |     80.68    |     81.47     |  90.05/86.67 |    87.66   |    90.02    |

All the results are the mean of two seperate experiments with the same hyper-parameters and different seeds.

| Training and Evaluation Data | Description | 
| ----------- | ----------- | 
| Datasets | SQuAD1.1: "Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable." (https://huggingface.co/datasets/squad)|
| Motivation | To build an efficient and accurate model for the question answering task. |
| Preprocessing | "We use the English Wikipedia dataset (2500M words) for training the models on the pre-training task. We split the data into train (95%) and validation (5%) sets. Both sets are preprocessed as described in the models’ original papers ([Devlin et al., 2019](https://arxiv.org/abs/1810.04805), [Sanh et al., 2019](https://arxiv.org/abs/1910.01108)). We process the data to use the maximum sequence length allowed by the models, however, we allow shorter sequences at a probability of 0:1." Following the pre-training on Wikipedia, fine-tuning is completed on the SQuAD1.1 dataset. | 

| Ethical Considerations | Description | 
| ----------- | ----------- | 
| Data | The training data come from Wikipedia articles |
| Human life | The model is not intended to inform decisions central to human life or flourishing. It is an aggregated set of labelled Wikipedia articles. | 
| Mitigations | No additional risk mitigation strategies were considered during model development. |
| Risks and harms | Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al., 2021](https://aclanthology.org/2021.acl-long.330.pdf), and [Bender et al., 2021](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)). Predictions generated by the model may include disturbing and harmful stereotypes across protected classes; identity characteristics; and sensitive, social, and occupational groups. Beyond this, the extent of the risks involved by using the model remain unknown.|
| Use cases | - | 

| Caveats and Recommendations |
| ----------- | 
| Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. There are no additional caveats or recommendations for this model. |

### BibTeX entry and citation info
```bibtex
@article{zafrir2021prune,
  title={Prune Once for All: Sparse Pre-Trained Language Models},
  author={Zafrir, Ofir and Larey, Ariel and Boudoukh, Guy and Shen, Haihao and Wasserblat, Moshe},
  journal={arXiv preprint arXiv:2111.05754},
  year={2021}
}
```