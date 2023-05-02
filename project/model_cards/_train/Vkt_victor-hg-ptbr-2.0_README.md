---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: victor-hg-ptbr-2.0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# victor-hg-ptbr-2.0

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0240
- Wer: 0.0219

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.4069        | 0.21  | 400   | 1.1372          | 0.9140 |
| 0.8079        | 0.43  | 800   | 0.5822          | 0.5339 |
| 0.5821        | 0.64  | 1200  | 0.4226          | 0.4177 |
| 0.5159        | 0.86  | 1600  | 0.4074          | 0.3970 |
| 0.4484        | 1.07  | 2000  | 0.3144          | 0.3220 |
| 0.3937        | 1.29  | 2400  | 0.3160          | 0.3264 |
| 0.3911        | 1.5   | 2800  | 0.2863          | 0.2956 |
| 0.3761        | 1.71  | 3200  | 0.3029          | 0.3128 |
| 0.3722        | 1.93  | 3600  | 0.2771          | 0.2933 |
| 0.3193        | 2.14  | 4000  | 0.2603          | 0.2795 |
| 0.3013        | 2.36  | 4400  | 0.2682          | 0.2703 |
| 0.3039        | 2.57  | 4800  | 0.2630          | 0.2618 |
| 0.3133        | 2.79  | 5200  | 0.2578          | 0.2629 |
| 0.3173        | 3.0   | 5600  | 0.2640          | 0.2746 |
| 0.2521        | 3.22  | 6000  | 0.2797          | 0.2662 |
| 0.2654        | 3.43  | 6400  | 0.2762          | 0.2640 |
| 0.2586        | 3.64  | 6800  | 0.2642          | 0.2596 |
| 0.265         | 3.86  | 7200  | 0.2656          | 0.2794 |
| 0.2432        | 4.07  | 7600  | 0.2459          | 0.2497 |
| 0.226         | 4.29  | 8000  | 0.2533          | 0.2509 |
| 0.2385        | 4.5   | 8400  | 0.2332          | 0.2394 |
| 0.2332        | 4.72  | 8800  | 0.2500          | 0.2569 |
| 0.2358        | 4.93  | 9200  | 0.2384          | 0.2489 |
| 0.2169        | 5.14  | 9600  | 0.2410          | 0.2380 |
| 0.2038        | 5.36  | 10000 | 0.2426          | 0.2333 |
| 0.2109        | 5.57  | 10400 | 0.2480          | 0.2473 |
| 0.2147        | 5.79  | 10800 | 0.2341          | 0.2272 |
| 0.2153        | 6.0   | 11200 | 0.2402          | 0.2424 |
| 0.186         | 6.22  | 11600 | 0.2560          | 0.2489 |
| 0.1854        | 6.43  | 12000 | 0.2444          | 0.2402 |
| 0.1915        | 6.65  | 12400 | 0.2720          | 0.2531 |
| 0.1929        | 6.86  | 12800 | 0.2516          | 0.2342 |
| 0.1842        | 7.07  | 13200 | 0.2480          | 0.2304 |
| 0.1682        | 7.29  | 13600 | 0.2393          | 0.2276 |
| 0.1753        | 7.5   | 14000 | 0.2514          | 0.2263 |
| 0.1798        | 7.72  | 14400 | 0.2191          | 0.2178 |
| 0.1736        | 7.93  | 14800 | 0.2351          | 0.2197 |
| 0.1668        | 8.15  | 15200 | 0.2315          | 0.2194 |
| 0.1545        | 8.36  | 15600 | 0.2291          | 0.2079 |
| 0.1508        | 8.57  | 16000 | 0.2351          | 0.2134 |
| 0.1662        | 8.79  | 16400 | 0.2298          | 0.2197 |
| 0.1621        | 9.0   | 16800 | 0.2314          | 0.2219 |
| 0.1416        | 9.22  | 17200 | 0.2306          | 0.2192 |
| 0.1455        | 9.43  | 17600 | 0.2466          | 0.2184 |
| 0.1522        | 9.65  | 18000 | 0.2392          | 0.2255 |
| 0.1434        | 9.86  | 18400 | 0.2464          | 0.2208 |
| 0.1362        | 10.08 | 18800 | 0.2351          | 0.2095 |
| 0.127         | 10.29 | 19200 | 0.2373          | 0.2110 |
| 0.133         | 10.5  | 19600 | 0.2269          | 0.2031 |
| 0.1308        | 10.72 | 20000 | 0.2400          | 0.2096 |
| 0.1331        | 10.93 | 20400 | 0.2243          | 0.2083 |
| 0.125         | 11.15 | 20800 | 0.2334          | 0.2063 |
| 0.1236        | 11.36 | 21200 | 0.2195          | 0.2044 |
| 0.1263        | 11.58 | 21600 | 0.2263          | 0.2050 |
| 0.1235        | 11.79 | 22000 | 0.2217          | 0.2087 |
| 0.1301        | 12.0  | 22400 | 0.2332          | 0.2094 |
| 0.1123        | 12.22 | 22800 | 0.2195          | 0.2068 |
| 0.117         | 12.43 | 23200 | 0.2266          | 0.2110 |
| 0.1156        | 12.65 | 23600 | 0.2469          | 0.2063 |
| 0.1117        | 12.86 | 24000 | 0.2379          | 0.2035 |
| 0.1124        | 13.08 | 24400 | 0.2156          | 0.1963 |
| 0.106         | 13.29 | 24800 | 0.2310          | 0.1988 |
| 0.1066        | 13.5  | 25200 | 0.2334          | 0.1950 |
| 0.1069        | 13.72 | 25600 | 0.2230          | 0.2011 |
| 0.1089        | 13.93 | 26000 | 0.2233          | 0.2003 |
| 0.0977        | 14.15 | 26400 | 0.2273          | 0.1895 |
| 0.0972        | 14.36 | 26800 | 0.2265          | 0.1887 |
| 0.1005        | 14.58 | 27200 | 0.2196          | 0.1934 |
| 0.1058        | 14.79 | 27600 | 0.2213          | 0.1870 |
| 0.1027        | 15.01 | 28000 | 0.2361          | 0.1916 |
| 0.0886        | 15.22 | 28400 | 0.2275          | 0.1815 |
| 0.0885        | 15.43 | 28800 | 0.2230          | 0.1891 |
| 0.0911        | 15.65 | 29200 | 0.2237          | 0.1989 |
| 0.0923        | 15.86 | 29600 | 0.2200          | 0.1857 |
| 0.0868        | 16.08 | 30000 | 0.2248          | 0.1875 |
| 0.0812        | 16.29 | 30400 | 0.2240          | 0.1874 |
| 0.0829        | 16.51 | 30800 | 0.2198          | 0.1814 |
| 0.0832        | 16.72 | 31200 | 0.2328          | 0.1892 |
| 0.0822        | 16.93 | 31600 | 0.2283          | 0.1862 |
| 0.0828        | 17.15 | 32000 | 0.2283          | 0.1806 |
| 0.0791        | 17.36 | 32400 | 0.2197          | 0.1787 |
| 0.0801        | 17.58 | 32800 | 0.2249          | 0.1815 |
| 0.0804        | 17.79 | 33200 | 0.2304          | 0.1789 |
| 0.0833        | 18.01 | 33600 | 0.2235          | 0.1832 |
| 0.0762        | 18.22 | 34000 | 0.2358          | 0.1784 |
| 0.0688        | 18.44 | 34400 | 0.2183          | 0.1758 |
| 0.0751        | 18.65 | 34800 | 0.2169          | 0.1805 |
| 0.0729        | 18.86 | 35200 | 0.2296          | 0.1770 |
| 0.0681        | 19.08 | 35600 | 0.2380          | 0.1770 |
| 0.067         | 19.29 | 36000 | 0.2153          | 0.1777 |
| 0.0669        | 19.51 | 36400 | 0.2260          | 0.1742 |
| 0.0824        | 19.72 | 36800 | 0.0289          | 0.0310 |
| 0.0857        | 19.94 | 37200 | 0.0289          | 0.0322 |
| 0.0799        | 20.15 | 37600 | 0.0264          | 0.0298 |
| 0.0767        | 20.36 | 38000 | 0.0273          | 0.0318 |
| 0.079         | 20.58 | 38400 | 0.0274          | 0.0320 |
| 0.0791        | 20.79 | 38800 | 0.0279          | 0.0318 |
| 0.0805        | 21.01 | 39200 | 0.0285          | 0.0330 |
| 0.0622        | 21.22 | 39600 | 0.0263          | 0.0306 |
| 0.0622        | 21.44 | 40000 | 0.0290          | 0.0318 |
| 0.0672        | 21.65 | 40400 | 0.0278          | 0.0330 |
| 0.0706        | 21.86 | 40800 | 0.0270          | 0.0297 |
| 0.0619        | 22.08 | 41200 | 0.0288          | 0.0328 |
| 0.0633        | 22.29 | 41600 | 0.0256          | 0.0303 |
| 0.0618        | 22.51 | 42000 | 0.0263          | 0.0299 |
| 0.0576        | 22.72 | 42400 | 0.0273          | 0.0301 |
| 0.0583        | 22.94 | 42800 | 0.0282          | 0.0297 |
| 0.0565        | 23.15 | 43200 | 0.0256          | 0.0280 |
| 0.0557        | 23.37 | 43600 | 0.0268          | 0.0280 |
| 0.0548        | 23.58 | 44000 | 0.0266          | 0.0291 |
| 0.056         | 23.79 | 44400 | 0.0264          | 0.0290 |
| 0.0546        | 24.01 | 44800 | 0.0273          | 0.0284 |
| 0.0496        | 24.22 | 45200 | 0.0261          | 0.0279 |
| 0.0512        | 24.44 | 45600 | 0.0256          | 0.0281 |
| 0.0482        | 24.65 | 46000 | 0.0264          | 0.0285 |
| 0.0503        | 24.87 | 46400 | 0.0256          | 0.0268 |
| 0.0471        | 25.08 | 46800 | 0.0270          | 0.0282 |
| 0.0453        | 25.29 | 47200 | 0.0255          | 0.0267 |
| 0.0431        | 25.51 | 47600 | 0.0251          | 0.0264 |
| 0.0464        | 25.72 | 48000 | 0.0262          | 0.0261 |
| 0.0431        | 25.94 | 48400 | 0.0257          | 0.0265 |
| 0.0405        | 26.15 | 48800 | 0.0260          | 0.0251 |
| 0.0406        | 26.37 | 49200 | 0.0246          | 0.0250 |
| 0.0397        | 26.58 | 49600 | 0.0252          | 0.0254 |
| 0.0403        | 26.8  | 50000 | 0.0250          | 0.0256 |
| 0.0385        | 27.01 | 50400 | 0.0254          | 0.0241 |
| 0.0398        | 27.22 | 50800 | 0.0255          | 0.0242 |
| 0.0363        | 27.44 | 51200 | 0.0250          | 0.0236 |
| 0.0372        | 27.65 | 51600 | 0.0247          | 0.0232 |
| 0.0362        | 27.87 | 52000 | 0.0240          | 0.0226 |
| 0.0367        | 28.08 | 52400 | 0.0246          | 0.0224 |
| 0.0347        | 28.3  | 52800 | 0.0247          | 0.0229 |
| 0.0348        | 28.51 | 53200 | 0.0241          | 0.0229 |
| 0.0331        | 28.72 | 53600 | 0.0242          | 0.0224 |
| 0.0339        | 28.94 | 54000 | 0.0241          | 0.0220 |
| 0.0336        | 29.15 | 54400 | 0.0244          | 0.0221 |
| 0.0336        | 29.37 | 54800 | 0.0243          | 0.0215 |
| 0.0349        | 29.58 | 55200 | 0.0239          | 0.0217 |
| 0.0308        | 29.8  | 55600 | 0.0240          | 0.0219 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.8.1+cu111
- Datasets 2.2.1
- Tokenizers 0.12.1