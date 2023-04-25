---
language:
- en
license: mit
tags:
- generated_from_trainer
- deberta-v3
datasets:
- glue
metrics:
- accuracy
model-index:
- name: ds_results
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MNLI
      type: glue
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.874593165174939
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DeBERTa v3 (small) fine-tuned on MNLI

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the GLUE MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4985
- Accuracy: 0.8746

## Model description

[DeBERTa](https://arxiv.org/abs/2006.03654) improves the BERT and RoBERTa models using disentangled attention and enhanced mask decoder. With those two improvements, DeBERTa out perform RoBERTa on a majority of NLU tasks with 80GB training data. 
Please check the [official repository](https://github.com/microsoft/DeBERTa) for more details and updates.
In [DeBERTa V3](https://arxiv.org/abs/2111.09543), we replaced the MLM objective with the RTD(Replaced Token Detection) objective introduced by ELECTRA for pre-training, as well as some innovations to be introduced in our upcoming paper. Compared to DeBERTa-V2,  our V3 version significantly improves the model performance in downstream tasks.  You can find a simple introduction about the model from the appendix A11 in our original [paper](https://arxiv.org/abs/2006.03654),  but we will provide more details in a separate write-up.
The DeBERTa V3 small model comes with 6 layers and a hidden size of 768. Its total parameter number is 143M since we use a vocabulary containing 128K tokens which introduce 98M parameters in the Embedding layer.  This model was trained using the 160GB data as DeBERTa V2.

## Intended uses & limitations

More information needed

## Training and evaluation data

The Multi-Genre Natural Language Inference Corpus is a crowdsourced collection of sentence pairs with textual entailment annotations. Given a premise sentence and a hypothesis sentence, the task is to predict whether the premise entails the hypothesis (entailment), contradicts the hypothesis (contradiction), or neither (neutral). The premise sentences are gathered from ten different sources, including transcribed speech, fiction, and government reports. The authors of the benchmark use the standard test set, for which they obtained private labels from the RTE authors, and evaluate on both the matched (in-domain) and mismatched (cross-domain) section. They also uses and recommend the SNLI corpus as 550k examples of auxiliary training data.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.7773        | 0.04  | 1000  | 0.5241          | 0.7984   |
| 0.546         | 0.08  | 2000  | 0.4629          | 0.8194   |
| 0.5032        | 0.12  | 3000  | 0.4704          | 0.8274   |
| 0.4711        | 0.16  | 4000  | 0.4383          | 0.8355   |
| 0.473         | 0.2   | 5000  | 0.4652          | 0.8305   |
| 0.4619        | 0.24  | 6000  | 0.4234          | 0.8386   |
| 0.4542        | 0.29  | 7000  | 0.4825          | 0.8349   |
| 0.4468        | 0.33  | 8000  | 0.3985          | 0.8513   |
| 0.4288        | 0.37  | 9000  | 0.4084          | 0.8493   |
| 0.4354        | 0.41  | 10000 | 0.3850          | 0.8533   |
| 0.423         | 0.45  | 11000 | 0.3855          | 0.8509   |
| 0.4167        | 0.49  | 12000 | 0.4122          | 0.8513   |
| 0.4129        | 0.53  | 13000 | 0.4009          | 0.8550   |
| 0.4135        | 0.57  | 14000 | 0.4136          | 0.8544   |
| 0.4074        | 0.61  | 15000 | 0.3869          | 0.8595   |
| 0.415         | 0.65  | 16000 | 0.3911          | 0.8517   |
| 0.4095        | 0.69  | 17000 | 0.3880          | 0.8593   |
| 0.4001        | 0.73  | 18000 | 0.3907          | 0.8587   |
| 0.4069        | 0.77  | 19000 | 0.3686          | 0.8630   |
| 0.3927        | 0.81  | 20000 | 0.4008          | 0.8593   |
| 0.3958        | 0.86  | 21000 | 0.3716          | 0.8639   |
| 0.4016        | 0.9   | 22000 | 0.3594          | 0.8679   |
| 0.3945        | 0.94  | 23000 | 0.3595          | 0.8679   |
| 0.3932        | 0.98  | 24000 | 0.3577          | 0.8645   |
| 0.345         | 1.02  | 25000 | 0.4080          | 0.8699   |
| 0.2885        | 1.06  | 26000 | 0.3919          | 0.8674   |
| 0.2858        | 1.1   | 27000 | 0.4346          | 0.8651   |
| 0.2872        | 1.14  | 28000 | 0.4105          | 0.8674   |
| 0.3002        | 1.18  | 29000 | 0.4133          | 0.8708   |
| 0.2954        | 1.22  | 30000 | 0.4062          | 0.8667   |
| 0.2912        | 1.26  | 31000 | 0.3972          | 0.8708   |
| 0.2958        | 1.3   | 32000 | 0.3713          | 0.8732   |
| 0.293         | 1.34  | 33000 | 0.3717          | 0.8715   |
| 0.3001        | 1.39  | 34000 | 0.3826          | 0.8716   |
| 0.2864        | 1.43  | 35000 | 0.4155          | 0.8694   |
| 0.2827        | 1.47  | 36000 | 0.4224          | 0.8666   |
| 0.2836        | 1.51  | 37000 | 0.3832          | 0.8744   |
| 0.2844        | 1.55  | 38000 | 0.4179          | 0.8699   |
| 0.2866        | 1.59  | 39000 | 0.3969          | 0.8681   |
| 0.2883        | 1.63  | 40000 | 0.4000          | 0.8683   |
| 0.2832        | 1.67  | 41000 | 0.3853          | 0.8688   |
| 0.2876        | 1.71  | 42000 | 0.3924          | 0.8677   |
| 0.2855        | 1.75  | 43000 | 0.4177          | 0.8719   |
| 0.2845        | 1.79  | 44000 | 0.3877          | 0.8724   |
| 0.2882        | 1.83  | 45000 | 0.3961          | 0.8713   |
| 0.2773        | 1.87  | 46000 | 0.3791          | 0.8740   |
| 0.2767        | 1.91  | 47000 | 0.3877          | 0.8779   |
| 0.2772        | 1.96  | 48000 | 0.4022          | 0.8690   |
| 0.2816        | 2.0   | 49000 | 0.3837          | 0.8732   |
| 0.2068        | 2.04  | 50000 | 0.4644          | 0.8720   |
| 0.1914        | 2.08  | 51000 | 0.4919          | 0.8744   |
| 0.2           | 2.12  | 52000 | 0.4870          | 0.8702   |
| 0.1904        | 2.16  | 53000 | 0.5038          | 0.8737   |
| 0.1915        | 2.2   | 54000 | 0.5232          | 0.8711   |
| 0.1956        | 2.24  | 55000 | 0.5192          | 0.8747   |
| 0.1911        | 2.28  | 56000 | 0.5215          | 0.8761   |
| 0.2053        | 2.32  | 57000 | 0.4604          | 0.8738   |
| 0.2008        | 2.36  | 58000 | 0.5162          | 0.8715   |
| 0.1971        | 2.4   | 59000 | 0.4886          | 0.8754   |
| 0.192         | 2.44  | 60000 | 0.4921          | 0.8725   |
| 0.1937        | 2.49  | 61000 | 0.4917          | 0.8763   |
| 0.1931        | 2.53  | 62000 | 0.4789          | 0.8778   |
| 0.1964        | 2.57  | 63000 | 0.4997          | 0.8721   |
| 0.2008        | 2.61  | 64000 | 0.4748          | 0.8756   |
| 0.1962        | 2.65  | 65000 | 0.4840          | 0.8764   |
| 0.2029        | 2.69  | 66000 | 0.4889          | 0.8767   |
| 0.1927        | 2.73  | 67000 | 0.4820          | 0.8758   |
| 0.1926        | 2.77  | 68000 | 0.4857          | 0.8762   |
| 0.1919        | 2.81  | 69000 | 0.4836          | 0.8749   |
| 0.1911        | 2.85  | 70000 | 0.4859          | 0.8742   |
| 0.1897        | 2.89  | 71000 | 0.4853          | 0.8766   |
| 0.186         | 2.93  | 72000 | 0.4946          | 0.8768   |
| 0.2011        | 2.97  | 73000 | 0.4851          | 0.8767   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
