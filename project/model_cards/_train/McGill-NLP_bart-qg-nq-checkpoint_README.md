---
license: cc-by-4.0
---
# BART-base fine-tuned on NaturalQuestions for **Question Generation**

[BART Model](https://arxiv.org/pdf/1910.13461.pdf) fine-tuned on [Google NaturalQuestions](https://ai.google.com/research/NaturalQuestions/) for **Question Generation** by treating long answer as input, and question as output.

## Details of BART

The **BART** model was presented in [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461.pdf) by *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, Luke Zettlemoyer* in Here the abstract:

We present BART, a denoising autoencoder for pretraining sequence-to-sequence models. BART is trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text. It uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and many other more recent pretraining schemes. We evaluate a number of noising approaches, finding the best performance by both randomly shuffling the order of the original sentences and using a novel in-filling scheme, where spans of text are replaced with a single mask token. BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD, achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 6 ROUGE. BART also provides a 1.1 BLEU increase over a back-translation system for machine translation, with only target language pretraining. We also report ablation experiments that replicate other pretraining schemes within the BART framework, to better measure which factors most influence end-task performance.

## Details of the downstream task (QG) - Dataset 📚 🧐

Dataset: ```NaturalQuestions``` from  Google (https://ai.google.com/research/NaturalQuestions/)

| Dataset          | Split | # samples |
| --------         | ----- | --------- |
| NaturalQuestions | train | 97650    |
| NaturalQuestions | valid  | 10850    |


## Model fine-tuning 🏋️‍

The training script can be found [here](https://github.com/McGill-NLP/MLQuestions/blob/main/QG/train.py)


## Model in Action 🚀

```python
from transformers import AutoModel, BartTokenizer
#Load the tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
#Load the model
model = AutoModelForSeq2SeqLM.from_pretrained("McGill-NLP/bart-qg-nq-checkpoint")
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
