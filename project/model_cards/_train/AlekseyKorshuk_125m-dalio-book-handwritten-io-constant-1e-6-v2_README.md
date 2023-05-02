---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
metrics:
- accuracy
model-index:
- name: 125m-dalio-book-handwritten-io-constant-1e-6-v2
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
      type: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.23359387091781458
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 125m-dalio-book-handwritten-io-constant-1e-6-v2

This model is a fine-tuned version of [facebook/opt-125m](https://huggingface.co/facebook/opt-125m) on the AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0859
- Accuracy: 0.2336
- Perplexity: 21.8880

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Perplexity |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 3.3352        | 0.01  | 1    | 3.1738          | 0.2305   | 23.8988    |
| 3.3091        | 0.03  | 2    | 3.1738          | 0.2305   | 23.8988    |
| 3.3347        | 0.04  | 3    | 3.1738          | 0.2305   | 23.8988    |
| 3.1445        | 0.05  | 4    | 3.1738          | 0.2305   | 23.8988    |
| 2.8918        | 0.07  | 5    | 3.1738          | 0.2305   | 23.8988    |
| 3.2068        | 0.08  | 6    | 3.1738          | 0.2305   | 23.8988    |
| 3.6245        | 0.09  | 7    | 3.1719          | 0.2305   | 23.8522    |
| 3.2256        | 0.11  | 8    | 3.1719          | 0.2305   | 23.8522    |
| 2.9991        | 0.12  | 9    | 3.1699          | 0.2305   | 23.8056    |
| 3.3257        | 0.13  | 10   | 3.1680          | 0.2306   | 23.7592    |
| 3.1199        | 0.15  | 11   | 3.1660          | 0.2306   | 23.7128    |
| 3.3735        | 0.16  | 12   | 3.1660          | 0.2306   | 23.7128    |
| 3.0051        | 0.17  | 13   | 3.1641          | 0.2307   | 23.6665    |
| 3.2695        | 0.19  | 14   | 3.1621          | 0.2308   | 23.6204    |
| 3.2004        | 0.2   | 15   | 3.1602          | 0.2309   | 23.5743    |
| 3.2075        | 0.21  | 16   | 3.1582          | 0.2308   | 23.5283    |
| 3.321         | 0.23  | 17   | 3.1562          | 0.2308   | 23.4824    |
| 3.4026        | 0.24  | 18   | 3.1543          | 0.2309   | 23.4366    |
| 3.0383        | 0.25  | 19   | 3.1523          | 0.2309   | 23.3908    |
| 3.166         | 0.27  | 20   | 3.1504          | 0.2309   | 23.3452    |
| 3.144         | 0.28  | 21   | 3.1484          | 0.2310   | 23.2996    |
| 3.1624        | 0.29  | 22   | 3.1484          | 0.2310   | 23.2996    |
| 3.0332        | 0.31  | 23   | 3.1465          | 0.2310   | 23.2542    |
| 3.3745        | 0.32  | 24   | 3.1445          | 0.2311   | 23.2088    |
| 3.0823        | 0.33  | 25   | 3.1426          | 0.2312   | 23.1635    |
| 3.6021        | 0.35  | 26   | 3.1406          | 0.2312   | 23.1183    |
| 3.1125        | 0.36  | 27   | 3.1387          | 0.2313   | 23.0732    |
| 3.1406        | 0.37  | 28   | 3.1387          | 0.2314   | 23.0732    |
| 3.1736        | 0.39  | 29   | 3.1367          | 0.2314   | 23.0282    |
| 3.1104        | 0.4   | 30   | 3.1348          | 0.2315   | 22.9832    |
| 3.1301        | 0.41  | 31   | 3.1328          | 0.2316   | 22.9384    |
| 3.3376        | 0.43  | 32   | 3.1309          | 0.2315   | 22.8936    |
| 3.218         | 0.44  | 33   | 3.1309          | 0.2316   | 22.8936    |
| 3.0786        | 0.45  | 34   | 3.1289          | 0.2316   | 22.8490    |
| 3.0125        | 0.47  | 35   | 3.1270          | 0.2317   | 22.8044    |
| 3.2634        | 0.48  | 36   | 3.1270          | 0.2317   | 22.8044    |
| 2.9888        | 0.49  | 37   | 3.125           | 0.2318   | 22.7599    |
| 3.1624        | 0.51  | 38   | 3.1230          | 0.2318   | 22.7155    |
| 2.9807        | 0.52  | 39   | 3.1211          | 0.2319   | 22.6712    |
| 3.446         | 0.53  | 40   | 3.1211          | 0.2319   | 22.6712    |
| 3.1338        | 0.55  | 41   | 3.1191          | 0.2320   | 22.6269    |
| 3.1841        | 0.56  | 42   | 3.1191          | 0.2320   | 22.6269    |
| 3.1079        | 0.57  | 43   | 3.1172          | 0.2320   | 22.5828    |
| 3.0918        | 0.59  | 44   | 3.1152          | 0.2321   | 22.5387    |
| 3.0302        | 0.6   | 45   | 3.1152          | 0.2322   | 22.5387    |
| 3.1123        | 0.61  | 46   | 3.1133          | 0.2323   | 22.4947    |
| 2.9985        | 0.63  | 47   | 3.1113          | 0.2324   | 22.4508    |
| 3.3816        | 0.64  | 48   | 3.1113          | 0.2324   | 22.4508    |
| 3.0813        | 0.65  | 49   | 3.1094          | 0.2324   | 22.4070    |
| 3.2024        | 0.67  | 50   | 3.1094          | 0.2325   | 22.4070    |
| 3.0178        | 0.68  | 51   | 3.1074          | 0.2325   | 22.3633    |
| 3.1646        | 0.69  | 52   | 3.1074          | 0.2326   | 22.3633    |
| 3.0046        | 0.71  | 53   | 3.1055          | 0.2327   | 22.3197    |
| 3.0266        | 0.72  | 54   | 3.1055          | 0.2327   | 22.3197    |
| 3.3857        | 0.73  | 55   | 3.1035          | 0.2327   | 22.2761    |
| 3.064         | 0.75  | 56   | 3.1035          | 0.2328   | 22.2761    |
| 3.176         | 0.76  | 57   | 3.1016          | 0.2328   | 22.2327    |
| 3.1851        | 0.77  | 58   | 3.1016          | 0.2329   | 22.2327    |
| 3.0811        | 0.79  | 59   | 3.0996          | 0.2329   | 22.1893    |
| 3.0205        | 0.8   | 60   | 3.0996          | 0.2330   | 22.1893    |
| 3.26          | 0.81  | 61   | 3.0977          | 0.2330   | 22.1460    |
| 3.2922        | 0.83  | 62   | 3.0977          | 0.2331   | 22.1460    |
| 3.5349        | 0.84  | 63   | 3.0957          | 0.2331   | 22.1028    |
| 3.3525        | 0.85  | 64   | 3.0957          | 0.2331   | 22.1028    |
| 3.135         | 0.87  | 65   | 3.0938          | 0.2331   | 22.0596    |
| 3.1707        | 0.88  | 66   | 3.0938          | 0.2332   | 22.0596    |
| 3.0127        | 0.89  | 67   | 3.0918          | 0.2332   | 22.0166    |
| 3.0952        | 0.91  | 68   | 3.0918          | 0.2332   | 22.0166    |
| 3.1023        | 0.92  | 69   | 3.0898          | 0.2334   | 21.9736    |
| 3.3821        | 0.93  | 70   | 3.0898          | 0.2334   | 21.9736    |
| 3.1118        | 0.95  | 71   | 3.0879          | 0.2334   | 21.9308    |
| 3.1143        | 0.96  | 72   | 3.0879          | 0.2335   | 21.9308    |
| 3.1118        | 0.97  | 73   | 3.0879          | 0.2335   | 21.9308    |
| 3.0596        | 0.99  | 74   | 3.0859          | 0.2336   | 21.8880    |
| 3.1033        | 1.0   | 75   | 3.0859          | 0.2336   | 21.8880    |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1