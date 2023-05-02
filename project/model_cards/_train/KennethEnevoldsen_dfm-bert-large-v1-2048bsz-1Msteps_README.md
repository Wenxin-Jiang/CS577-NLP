---
license: cc-by-4.0
metrics:
- accuracy
model-index:
- name: dfm-encoder-large-v1
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
    datasets:
    - netarkivet_text_v1
    - danews_v1
    - hopetwitter_v1
    - DDSC/dagw_reddit_filtered_v1.0.0
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7328012831797821
language:
- da
tags:
- bert
- pytorch
- large
- danish
- mlm
---

# dfm-encoder-large-v1
This model is trained as a part of the Danish Foundation Models project.

## Training procedure

This model is a fine-tuned version of [NbAiLab/nb-bert-large](https://huggingface.co/NbAiLab/nb-bert-large) on the dcc_v1.1.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3175
- Accuracy: 0.7328

<details>
    <summary> Training Hyperparameters </summary>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 2048
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-06
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10000
- training_steps: 100000
- mixed_precision_training: Native AMP

</details>



<details>
    <summary> Training Results </summary>


### Training results

| Training Loss | Epoch | Step   | Accuracy | Validation Loss |
|:-------------:|:-----:|:------:|:--------:|:---------------:|
| 1.4239        | 0.02  | 2000   | 0.6481   | 1.9361          |
| 1.299         | 0.04  | 4000   | 0.6646   | 1.8073          |
| 1.2008        | 0.06  | 6000   | 0.6766   | 1.7281          |
| 1.193         | 0.08  | 8000   | 0.6770   | 1.6885          |
| 1.138         | 0.1   | 10000  | 0.6803   | 1.6729          |
| 1.1401        | 0.12  | 12000  | 0.6729   | 1.7227          |
| 4.1932        | 0.14  | 14000  | 0.3016   | 4.5455          |
| 2.3732        | 0.16  | 16000  | 0.5607   | 2.3964          |
| 1.2114        | 0.18  | 18000  | 0.6667   | 1.7638          |
| 1.1482        | 0.2   | 20000  | 0.6576   | 1.7839          |
| 1.0815        | 0.22  | 22000  | 0.6862   | 1.6308          |
| 1.085         | 0.24  | 24000  | 0.6837   | 1.6383          |
| 1.0788        | 0.26  | 26000  | 0.6812   | 1.6585          |
| 1.0389        | 0.28  | 28000  | 0.6861   | 1.5927          |
| 1.0283        | 0.3   | 30000  | 0.6937   | 1.5779          |
| 1.0145        | 0.32  | 32000  | 0.6967   | 1.5439          |
| 1.0023        | 0.34  | 34000  | 0.6980   | 1.5237          |
| 0.9976        | 0.36  | 36000  | 0.6962   | 1.5692          |
| 1.019         | 0.38  | 38000  | 0.6970   | 1.5460          |
| 1.0137        | 0.4   | 40000  | 0.6967   | 1.5564          |
| 1.0067        | 0.42  | 42000  | 0.7008   | 1.5176          |
| 0.992         | 0.44  | 44000  | 0.7060   | 1.4806          |
| 0.9796        | 0.46  | 46000  | 0.7026   | 1.5085          |
| 0.976         | 0.48  | 48000  | 0.7092   | 1.4705          |
| 0.9571        | 0.5   | 50000  | 0.7052   | 1.4895          |
| 0.9723        | 0.52  | 52000  | 0.7135   | 1.4516          |
| 0.9581        | 0.54  | 54000  | 0.7145   | 1.4343          |
| 0.9511        | 0.56  | 56000  | 0.7124   | 1.4334          |
| 0.9608        | 0.58  | 58000  | 0.7151   | 1.4268          |
| 0.9588        | 0.6   | 60000  | 0.7127   | 1.4471          |
| 0.9473        | 0.62  | 62000  | 0.7202   | 1.4037          |
| 0.9266        | 0.64  | 64000  | 0.7158   | 1.4225          |
| 0.925         | 0.66  | 66000  | 0.7208   | 1.3940          |
| 0.9242        | 0.68  | 68000  | 0.7189   | 1.4090          |
| 0.9141        | 0.7   | 70000  | 0.7229   | 1.3831          |
| 0.8884        | 0.72  | 72000  | 1.3738   | 0.7233          |
| 0.9145        | 0.74  | 74000  | 1.3478   | 0.7275          |
| 0.8741        | 0.76  | 76000  | 1.3691   | 0.7255          |
| 0.8752        | 0.78  | 78000  | 1.3530   | 0.7276          |
| 0.8634        | 0.8   | 80000  | 1.3428   | 0.7272          |
| 0.8882        | 0.82  | 82000  | 1.3490   | 0.7270          |
| 0.8872        | 0.84  | 84000  | 1.3458   | 0.7296          |
| 0.892         | 0.86  | 86000  | 1.3382   | 0.7279          |
| 0.9002        | 0.88  | 88000  | 1.3091   | 0.7341          |
| 0.8805        | 0.9   | 90000  | 1.3209   | 0.7310          |
| 0.8944        | 0.92  | 92000  | 1.3133   | 0.7332          |
| 0.8605        | 0.94  | 94000  | 1.3404   | 0.7311          |
| 0.879         | 0.96  | 96000  | 1.2890   | 0.7356          |
| 0.871         | 0.98  | 98000  | 1.2954   | 0.7352          |
| 0.8676        | 1.0   | 100000 | 1.2935   | 0.7369          |



</details>


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.5.3.dev0
- Tokenizers 0.12.1

# Model Card

Following [1], the following constitutes a model for this model.

---

*Organization developing the Model*: The Danish Foundation Models project

*Model Creation Date*: June 2022

*Model Type*: Transformer encoder model [2]; BERT [3]

*Feedback on the Model*: For feedback on the model please use the [community forum](https://huggingface.co/chcaa/dfm-bert-base-v1/discussions). 

*Training logs and performance metrics*: Check out this Weight and biases [Dashboard](https://wandb.ai/chcaa/danish-foundation-models/reports/dfm-bert-base-v1--VmlldzoyODkwMzc2).


## Intended Uses

*Primary Intended Uses*: 

The primary intended use case of this model is the reproduction and validation of dataset quality. The intended use cases for future iterations of this model are the application in industry and research for Danish natural language tasks.

*Primary Intended Users*:

Future iterations of the model are intended for NLP practitioners dealing with Danish text documents.

*Out-of-Scope Uses*:

Use of the model for profiling in a way which is inconsiderate of the potential harm it might cause, such as racial profiling.

## Factors

*Card prompts - Relevant Factors*:

Relevant factors include which language is used. Our model is trained on a Danish 
text corpus and is intended to compare the training data.

*Card prompts - Evaluation Factors*:

Future iterations of this model should include a validation of biases pertaining to gender, race, and religious and social groups.

## Metrics

*Performance Metrics*:

Our model is evaluated on the following performance metrics:

- Pseudo perplexity, following [4], across eight distinct domains, including Danish dialects, books, legal, social media (Reddit, Twitter), spontaneous speech, news and Wikipedia.
- The Danish subsection of Scandeval [5].

To see the performance metrics, check out this Weight and biases [Dashboard](https://wandb.ai/chcaa/danish-foundation-models/reports/dfm-bert-base-v1--VmlldzoyODkwMzc2).

*Decision Threshold*: 

N/A

*Approaches to Uncertainty and Variability*: 

Due to the cost of training the model is only pre-trained once, but the ScandEval fine-tunes ten times to obtain a reasonable estimate of model performance.

## Evaluation Data

*Datasets*:

The ScandEval's Danish benchmark includes:

- Named entity recognition on DaNE [7,8].
- Part-of-speech tagging and dependency on DDT [8].
- Sentiment classification on AngryTweets [9], TwitterSent [9], Europarl [9], LCC [10]
- Hate speech classification on DKHate [11].

*Motivation*:

The ScandEval benchmark is the most comprehensive benchmark for Danish. Pseudo perplexity was analysed to examine the model's ability to model certain language domains.

## Training Data

For our training data, we sample from HopeTwitter, DaNews, [DAGW](DDSC/dagw_reddit_filtered_v1.0.0) and Netarkivet Text (NAT) with the probabilites; 0.10, 0.10, 0.10, 0.70. For more information on the training and datasets, see the respective datasheets on the Danish foundation models [GitHub page](https://github.com/centre-for-humanities-computing/danish-foundation-models).


*Pre-processing*:

Input documents are tokenized using the tokenizer of the Danish BERT by BotXO [12], which uses a BPE with a vocabulary size of ~30,000 and NFKC normalization. 

## Ethical Considerations

*Data*: The is sources from News, DAGW, Twitter, and Netarkivet Text (NAT) and might thus contain hate-speech, sexually explicit content and otherwise harmful content.

*Mitigations*: We considered removing sexually explicit content by filtering web domians using a DNS or using google safe-search. However, examining the filtering domains these were also found to include news media pertaining to a specific demographic (e.g. Dagens.dk) and educational sites pertaining to sexual education. We also examined the use of word-based filters, but found that might influence certain demographic groups disproportionally.

*Risk and Harms*: As Netarkivet Text cover such a wide array of the Danish internet it undoubtably contains personal information. To avoid model memorization of this information we have deduplicated the data such that the model does not learn this information.

# References:

- [1] Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model Cards for Model Reporting. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220–229. https://doi.org/10.1145/3287560.3287596
- [2] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention Is All You Need. ArXiv:1706.03762 [Cs]. http://arxiv.org/abs/1706.03762
- [3] Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. ArXiv:1810.04805 [Cs]. http://arxiv.org/abs/1810.04805
- [4] Salazar, J., Liang, D., Nguyen, T. Q., & Kirchhoff, K. (2020). Masked Language Model Scoring. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2699–2712. https://doi.org/10.18653/v1/2020.acl-main.240
- [6] Nielsen, D. S. (2021). ScandEval: Evaluation of language models on mono- or multilingual Scandinavian language tasks. GitHub. Note: Https://Github.Com/Saattrupdan/ScandEval.
- [7] Hvingelby, R., Pauli, A. B., Barrett, M., Rosted, C., Lidegaard, L. M., & Søgaard, A. (2020). DaNE: A named entity resource for danish. Proceedings of the 12th Language Resources and Evaluation Conference, 4597–4604.
- [8] Kromann, M. T. (2003). The Danish Dependency Treebank and the DTAG Treebank Tool. https://research.cbs.dk/en/publications/the-danish-dependency-treebank-and-the-dtag-treebank-tool
- [9] Alexandrainst/danlp. (2022). Alexandra Institute. https://github.com/alexandrainst/danlp/blob/a1e9fa70fc5a3ae7ff78877062da3a8a8da80758/docs/docs/datasets.md (Original work published 2019)
- [10] Nielsen, F. Å. (2022). Lcc-sentiment. https://github.com/fnielsen/lcc-sentiment (Original work published 2016)
- [11] Sigurbergsson, G. I., & Derczynski, L. (2020). Offensive Language and Hate Speech Detection for Danish. Proceedings of the 12th Language Resources and Evaluation Conference, 3498–3508. https://aclanthology.org/2020.lrec-1.430
- [12] Møllerhøj, J. D. (2019, December 5). Danish BERT model: BotXO has trained the most advanced BERT model. BotXO. https://www.botxo.ai/blog/danish-bert-model/