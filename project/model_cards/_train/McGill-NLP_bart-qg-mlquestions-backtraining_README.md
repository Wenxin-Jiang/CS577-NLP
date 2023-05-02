---
license: cc-by-4.0
---
# BART-base fine-tuned on NaturalQuestions for **Question Generation**

[BART Model](https://arxiv.org/pdf/1910.13461.pdf) trained for Question Generation in an unsupervised manner using [Back-Training](https://arxiv.org/pdf/2104.08801.pdf) algorithm (Kulshreshtha et al, EMNLP 2021). The dataset used are unaligned questions and passages from [MLQuestions dataset](https://github.com/McGill-NLP/MLQuestions/tree/main/data).

## Details of Back-Training

The Back-Training algorithm was presented in [Back-Training excels Self-Training at Unsupervised Domain Adaptation
of Question Generation and Passage Retrieval](https://arxiv.org/pdf/2104.08801.pdf) by *Devang Kulshreshtha, Robert Belfer, Iulian Vlad Serban, Siva Reddy* in Here the abstract:

In this work, we introduce back-training, an alternative to self-training for unsupervised domain adaptation (UDA) from source to target domain. While self-training generates synthetic training data where natural inputs are aligned with noisy outputs, back-training results in natural outputs aligned with noisy inputs. This significantly reduces the gap between the target domain and synthetic data distribution, and reduces model overfitting to the source domain. We run UDA experiments on question generation and passage retrieval from the Natural Questions domain to machine learning and biomedical domains. We find that back-training vastly outperforms self-training by a mean improvement of 7.8 BLEU4 points on generation, and 17.6% top-20 retrieval accuracy across both domains. We further propose consistency filters to remove low-quality synthetic data before training. We also release a new domain-adaptation datasetMLQuestions containing 35K unaligned questions, 50K unaligned passages, and 3K aligned question-passage pairs.

## Model training 🏋️‍

The training script can be found [here](https://github.com/McGill-NLP/MLQuestions/blob/main/UDA-BackTraining.sh)


## Model in Action 🚀

```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("geekydevu/bart-qg-mlquestions-backtraining")
#Load the model
model = AutoModelForSeq2SeqLM.from_pretrained("geekydevu/bart-qg-mlquestions-backtraining")
```

## Citation
If you want to cite this model you can use this:

```bibtex
@inproceedings{kulshreshtha-etal-2021-back,
    title = "Back-Training excels Self-Training at Unsupervised Domain Adaptation of Question Generation and Passage Retrieval",
    author = "Kulshreshtha, Devang  and
      Belfer, Robert  and
      Serban, Iulian Vlad  and
      Reddy, Siva",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.566",
    pages = "7064--7078",
    abstract = "In this work, we introduce back-training, an alternative to self-training for unsupervised domain adaptation (UDA). While self-training generates synthetic training data where natural inputs are aligned with noisy outputs, back-training results in natural outputs aligned with noisy inputs. This significantly reduces the gap between target domain and synthetic data distribution, and reduces model overfitting to source domain. We run UDA experiments on question generation and passage retrieval from the Natural Questions domain to machine learning and biomedical domains. We find that back-training vastly outperforms self-training by a mean improvement of 7.8 BLEU-4 points on generation, and 17.6{\%} top-20 retrieval accuracy across both domains. We further propose consistency filters to remove low-quality synthetic data before training. We also release a new domain-adaptation dataset - MLQuestions containing 35K unaligned questions, 50K unaligned passages, and 3K aligned question-passage pairs.",
}
```

> Created by [Devang Kulshreshtha](https://geekydevu.netlify.app/)

> Made with <span style="color: #e25555;">&hearts;</span> in Spain
