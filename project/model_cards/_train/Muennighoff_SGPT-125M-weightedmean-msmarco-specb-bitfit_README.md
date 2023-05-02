---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: SGPT-125M-weightedmean-msmarco-specb-bitfit
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: 2d8a100785abf0ae21420d2a55b0c56e3e1ea996
    metrics:
    - type: accuracy
      value: 61.23880597014926
    - type: ap
      value: 25.854431650388644
    - type: f1
      value: 55.751862762818604
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (de)
      config: de
      split: test
      revision: 2d8a100785abf0ae21420d2a55b0c56e3e1ea996
    metrics:
    - type: accuracy
      value: 56.88436830835117
    - type: ap
      value: 72.67279104379772
    - type: f1
      value: 54.449840243786404
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en-ext)
      config: en-ext
      split: test
      revision: 2d8a100785abf0ae21420d2a55b0c56e3e1ea996
    metrics:
    - type: accuracy
      value: 58.27586206896551
    - type: ap
      value: 14.067357642500387
    - type: f1
      value: 48.172318518691334
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (ja)
      config: ja
      split: test
      revision: 2d8a100785abf0ae21420d2a55b0c56e3e1ea996
    metrics:
    - type: accuracy
      value: 54.64668094218415
    - type: ap
      value: 11.776694555054965
    - type: f1
      value: 44.526622834078765
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: 80714f8dcf8cefc218ef4f8c5a966dd83f75a0e1
    metrics:
    - type: accuracy
      value: 65.401225
    - type: ap
      value: 60.22809958678552
    - type: f1
      value: 65.0251824898292
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 31.165999999999993
    - type: f1
      value: 30.908870050167437
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (de)
      config: de
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 24.79
    - type: f1
      value: 24.5833598854121
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (es)
      config: es
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 26.643999999999995
    - type: f1
      value: 26.39012792213563
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (fr)
      config: fr
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 26.386000000000003
    - type: f1
      value: 26.276867791454873
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (ja)
      config: ja
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 22.078000000000003
    - type: f1
      value: 21.797960290226843
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: c379a6705fec24a2493fa68e011692605f44e119
    metrics:
    - type: accuracy
      value: 24.274
    - type: f1
      value: 23.887054434822627
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: 5b3e3697907184a9b77a3c99ee9ea1a9cbb1e4e3
    metrics:
    - type: map_at_1
      value: 22.404
    - type: map_at_10
      value: 36.845
    - type: map_at_100
      value: 37.945
    - type: map_at_1000
      value: 37.966
    - type: map_at_3
      value: 31.78
    - type: map_at_5
      value: 34.608
    - type: mrr_at_1
      value: 22.902
    - type: mrr_at_10
      value: 37.034
    - type: mrr_at_100
      value: 38.134
    - type: mrr_at_1000
      value: 38.155
    - type: mrr_at_3
      value: 31.935000000000002
    - type: mrr_at_5
      value: 34.812
    - type: ndcg_at_1
      value: 22.404
    - type: ndcg_at_10
      value: 45.425
    - type: ndcg_at_100
      value: 50.354
    - type: ndcg_at_1000
      value: 50.873999999999995
    - type: ndcg_at_3
      value: 34.97
    - type: ndcg_at_5
      value: 40.081
    - type: precision_at_1
      value: 22.404
    - type: precision_at_10
      value: 7.303999999999999
    - type: precision_at_100
      value: 0.951
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 14.746
    - type: precision_at_5
      value: 11.337
    - type: recall_at_1
      value: 22.404
    - type: recall_at_10
      value: 73.044
    - type: recall_at_100
      value: 95.092
    - type: recall_at_1000
      value: 99.075
    - type: recall_at_3
      value: 44.239
    - type: recall_at_5
      value: 56.686
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: 0bbdb47bcbe3a90093699aefeed338a0f28a7ee8
    metrics:
    - type: v_measure
      value: 39.70858340673288
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: b73bd54100e5abfa6e3a23dcafb46fe4d2438dc3
    metrics:
    - type: v_measure
      value: 28.242847713721048
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 4d853f94cd57d85ec13805aeeac3ae3e5eb4c49c
    metrics:
    - type: map
      value: 55.83700395192393
    - type: mrr
      value: 70.3891307215407
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: 9ee918f184421b6bd48b78f6c714d86546106103
    metrics:
    - type: cos_sim_pearson
      value: 79.25366801756223
    - type: cos_sim_spearman
      value: 75.20954502580506
    - type: euclidean_pearson
      value: 78.79900722991617
    - type: euclidean_spearman
      value: 77.79996549607588
    - type: manhattan_pearson
      value: 78.18408109480399
    - type: manhattan_spearman
      value: 76.85958262303106
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 44fa15921b4c889113cc5df03dd4901b49161ab7
    metrics:
    - type: accuracy
      value: 77.70454545454545
    - type: f1
      value: 77.6929000113803
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 11d0121201d1f1f280e8cc8f3d98fb9c4d9f9c55
    metrics:
    - type: v_measure
      value: 33.63260395543984
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: c0fab014e1bcb8d3a5e31b2088972a1e01547dc1
    metrics:
    - type: v_measure
      value: 27.038042665369925
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 22.139
    - type: map_at_10
      value: 28.839
    - type: map_at_100
      value: 30.023
    - type: map_at_1000
      value: 30.153000000000002
    - type: map_at_3
      value: 26.521
    - type: map_at_5
      value: 27.775
    - type: mrr_at_1
      value: 26.466
    - type: mrr_at_10
      value: 33.495000000000005
    - type: mrr_at_100
      value: 34.416999999999994
    - type: mrr_at_1000
      value: 34.485
    - type: mrr_at_3
      value: 31.402
    - type: mrr_at_5
      value: 32.496
    - type: ndcg_at_1
      value: 26.466
    - type: ndcg_at_10
      value: 33.372
    - type: ndcg_at_100
      value: 38.7
    - type: ndcg_at_1000
      value: 41.696
    - type: ndcg_at_3
      value: 29.443
    - type: ndcg_at_5
      value: 31.121
    - type: precision_at_1
      value: 26.466
    - type: precision_at_10
      value: 6.037
    - type: precision_at_100
      value: 1.0670000000000002
    - type: precision_at_1000
      value: 0.16199999999999998
    - type: precision_at_3
      value: 13.782
    - type: precision_at_5
      value: 9.757
    - type: recall_at_1
      value: 22.139
    - type: recall_at_10
      value: 42.39
    - type: recall_at_100
      value: 65.427
    - type: recall_at_1000
      value: 86.04899999999999
    - type: recall_at_3
      value: 31.127
    - type: recall_at_5
      value: 35.717999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 20.652
    - type: map_at_10
      value: 27.558
    - type: map_at_100
      value: 28.473
    - type: map_at_1000
      value: 28.577
    - type: map_at_3
      value: 25.402
    - type: map_at_5
      value: 26.68
    - type: mrr_at_1
      value: 25.223000000000003
    - type: mrr_at_10
      value: 31.966
    - type: mrr_at_100
      value: 32.664
    - type: mrr_at_1000
      value: 32.724
    - type: mrr_at_3
      value: 30.074
    - type: mrr_at_5
      value: 31.249
    - type: ndcg_at_1
      value: 25.223000000000003
    - type: ndcg_at_10
      value: 31.694
    - type: ndcg_at_100
      value: 35.662
    - type: ndcg_at_1000
      value: 38.092
    - type: ndcg_at_3
      value: 28.294000000000004
    - type: ndcg_at_5
      value: 30.049
    - type: precision_at_1
      value: 25.223000000000003
    - type: precision_at_10
      value: 5.777
    - type: precision_at_100
      value: 0.9730000000000001
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: precision_at_3
      value: 13.397
    - type: precision_at_5
      value: 9.605
    - type: recall_at_1
      value: 20.652
    - type: recall_at_10
      value: 39.367999999999995
    - type: recall_at_100
      value: 56.485
    - type: recall_at_1000
      value: 73.292
    - type: recall_at_3
      value: 29.830000000000002
    - type: recall_at_5
      value: 34.43
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 25.180000000000003
    - type: map_at_10
      value: 34.579
    - type: map_at_100
      value: 35.589999999999996
    - type: map_at_1000
      value: 35.68
    - type: map_at_3
      value: 31.735999999999997
    - type: map_at_5
      value: 33.479
    - type: mrr_at_1
      value: 29.467
    - type: mrr_at_10
      value: 37.967
    - type: mrr_at_100
      value: 38.800000000000004
    - type: mrr_at_1000
      value: 38.858
    - type: mrr_at_3
      value: 35.465
    - type: mrr_at_5
      value: 37.057
    - type: ndcg_at_1
      value: 29.467
    - type: ndcg_at_10
      value: 39.796
    - type: ndcg_at_100
      value: 44.531
    - type: ndcg_at_1000
      value: 46.666000000000004
    - type: ndcg_at_3
      value: 34.676
    - type: ndcg_at_5
      value: 37.468
    - type: precision_at_1
      value: 29.467
    - type: precision_at_10
      value: 6.601999999999999
    - type: precision_at_100
      value: 0.9900000000000001
    - type: precision_at_1000
      value: 0.124
    - type: precision_at_3
      value: 15.568999999999999
    - type: precision_at_5
      value: 11.172
    - type: recall_at_1
      value: 25.180000000000003
    - type: recall_at_10
      value: 52.269
    - type: recall_at_100
      value: 73.574
    - type: recall_at_1000
      value: 89.141
    - type: recall_at_3
      value: 38.522
    - type: recall_at_5
      value: 45.323
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 16.303
    - type: map_at_10
      value: 21.629
    - type: map_at_100
      value: 22.387999999999998
    - type: map_at_1000
      value: 22.489
    - type: map_at_3
      value: 19.608
    - type: map_at_5
      value: 20.774
    - type: mrr_at_1
      value: 17.740000000000002
    - type: mrr_at_10
      value: 23.214000000000002
    - type: mrr_at_100
      value: 23.97
    - type: mrr_at_1000
      value: 24.054000000000002
    - type: mrr_at_3
      value: 21.243000000000002
    - type: mrr_at_5
      value: 22.322
    - type: ndcg_at_1
      value: 17.740000000000002
    - type: ndcg_at_10
      value: 25.113000000000003
    - type: ndcg_at_100
      value: 29.287999999999997
    - type: ndcg_at_1000
      value: 32.204
    - type: ndcg_at_3
      value: 21.111
    - type: ndcg_at_5
      value: 23.061999999999998
    - type: precision_at_1
      value: 17.740000000000002
    - type: precision_at_10
      value: 3.955
    - type: precision_at_100
      value: 0.644
    - type: precision_at_1000
      value: 0.093
    - type: precision_at_3
      value: 8.851
    - type: precision_at_5
      value: 6.418
    - type: recall_at_1
      value: 16.303
    - type: recall_at_10
      value: 34.487
    - type: recall_at_100
      value: 54.413999999999994
    - type: recall_at_1000
      value: 77.158
    - type: recall_at_3
      value: 23.733
    - type: recall_at_5
      value: 28.381
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 10.133000000000001
    - type: map_at_10
      value: 15.665999999999999
    - type: map_at_100
      value: 16.592000000000002
    - type: map_at_1000
      value: 16.733999999999998
    - type: map_at_3
      value: 13.625000000000002
    - type: map_at_5
      value: 14.721
    - type: mrr_at_1
      value: 12.562000000000001
    - type: mrr_at_10
      value: 18.487000000000002
    - type: mrr_at_100
      value: 19.391
    - type: mrr_at_1000
      value: 19.487
    - type: mrr_at_3
      value: 16.418
    - type: mrr_at_5
      value: 17.599999999999998
    - type: ndcg_at_1
      value: 12.562000000000001
    - type: ndcg_at_10
      value: 19.43
    - type: ndcg_at_100
      value: 24.546
    - type: ndcg_at_1000
      value: 28.193
    - type: ndcg_at_3
      value: 15.509999999999998
    - type: ndcg_at_5
      value: 17.322000000000003
    - type: precision_at_1
      value: 12.562000000000001
    - type: precision_at_10
      value: 3.794
    - type: precision_at_100
      value: 0.74
    - type: precision_at_1000
      value: 0.122
    - type: precision_at_3
      value: 7.546
    - type: precision_at_5
      value: 5.721
    - type: recall_at_1
      value: 10.133000000000001
    - type: recall_at_10
      value: 28.261999999999997
    - type: recall_at_100
      value: 51.742999999999995
    - type: recall_at_1000
      value: 78.075
    - type: recall_at_3
      value: 17.634
    - type: recall_at_5
      value: 22.128999999999998
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 19.991999999999997
    - type: map_at_10
      value: 27.346999999999998
    - type: map_at_100
      value: 28.582
    - type: map_at_1000
      value: 28.716
    - type: map_at_3
      value: 24.907
    - type: map_at_5
      value: 26.1
    - type: mrr_at_1
      value: 23.773
    - type: mrr_at_10
      value: 31.647
    - type: mrr_at_100
      value: 32.639
    - type: mrr_at_1000
      value: 32.706
    - type: mrr_at_3
      value: 29.195
    - type: mrr_at_5
      value: 30.484
    - type: ndcg_at_1
      value: 23.773
    - type: ndcg_at_10
      value: 32.322
    - type: ndcg_at_100
      value: 37.996
    - type: ndcg_at_1000
      value: 40.819
    - type: ndcg_at_3
      value: 27.876
    - type: ndcg_at_5
      value: 29.664
    - type: precision_at_1
      value: 23.773
    - type: precision_at_10
      value: 5.976999999999999
    - type: precision_at_100
      value: 1.055
    - type: precision_at_1000
      value: 0.15
    - type: precision_at_3
      value: 13.122
    - type: precision_at_5
      value: 9.451
    - type: recall_at_1
      value: 19.991999999999997
    - type: recall_at_10
      value: 43.106
    - type: recall_at_100
      value: 67.264
    - type: recall_at_1000
      value: 86.386
    - type: recall_at_3
      value: 30.392000000000003
    - type: recall_at_5
      value: 34.910999999999994
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 17.896
    - type: map_at_10
      value: 24.644
    - type: map_at_100
      value: 25.790000000000003
    - type: map_at_1000
      value: 25.913999999999998
    - type: map_at_3
      value: 22.694
    - type: map_at_5
      value: 23.69
    - type: mrr_at_1
      value: 21.346999999999998
    - type: mrr_at_10
      value: 28.594
    - type: mrr_at_100
      value: 29.543999999999997
    - type: mrr_at_1000
      value: 29.621
    - type: mrr_at_3
      value: 26.807
    - type: mrr_at_5
      value: 27.669
    - type: ndcg_at_1
      value: 21.346999999999998
    - type: ndcg_at_10
      value: 28.833
    - type: ndcg_at_100
      value: 34.272000000000006
    - type: ndcg_at_1000
      value: 37.355
    - type: ndcg_at_3
      value: 25.373
    - type: ndcg_at_5
      value: 26.756
    - type: precision_at_1
      value: 21.346999999999998
    - type: precision_at_10
      value: 5.2170000000000005
    - type: precision_at_100
      value: 0.954
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 11.948
    - type: precision_at_5
      value: 8.425
    - type: recall_at_1
      value: 17.896
    - type: recall_at_10
      value: 37.291000000000004
    - type: recall_at_100
      value: 61.138000000000005
    - type: recall_at_1000
      value: 83.212
    - type: recall_at_3
      value: 27.705999999999996
    - type: recall_at_5
      value: 31.234
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 17.195166666666665
    - type: map_at_10
      value: 23.329083333333333
    - type: map_at_100
      value: 24.30308333333333
    - type: map_at_1000
      value: 24.422416666666667
    - type: map_at_3
      value: 21.327416666666664
    - type: map_at_5
      value: 22.419999999999998
    - type: mrr_at_1
      value: 19.999916666666667
    - type: mrr_at_10
      value: 26.390166666666666
    - type: mrr_at_100
      value: 27.230999999999998
    - type: mrr_at_1000
      value: 27.308333333333334
    - type: mrr_at_3
      value: 24.4675
    - type: mrr_at_5
      value: 25.541083333333336
    - type: ndcg_at_1
      value: 19.999916666666667
    - type: ndcg_at_10
      value: 27.248666666666665
    - type: ndcg_at_100
      value: 32.00258333333334
    - type: ndcg_at_1000
      value: 34.9465
    - type: ndcg_at_3
      value: 23.58566666666667
    - type: ndcg_at_5
      value: 25.26341666666666
    - type: precision_at_1
      value: 19.999916666666667
    - type: precision_at_10
      value: 4.772166666666666
    - type: precision_at_100
      value: 0.847
    - type: precision_at_1000
      value: 0.12741666666666668
    - type: precision_at_3
      value: 10.756166666666669
    - type: precision_at_5
      value: 7.725416666666667
    - type: recall_at_1
      value: 17.195166666666665
    - type: recall_at_10
      value: 35.99083333333334
    - type: recall_at_100
      value: 57.467999999999996
    - type: recall_at_1000
      value: 78.82366666666667
    - type: recall_at_3
      value: 25.898499999999995
    - type: recall_at_5
      value: 30.084333333333333
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 16.779
    - type: map_at_10
      value: 21.557000000000002
    - type: map_at_100
      value: 22.338
    - type: map_at_1000
      value: 22.421
    - type: map_at_3
      value: 19.939
    - type: map_at_5
      value: 20.903
    - type: mrr_at_1
      value: 18.404999999999998
    - type: mrr_at_10
      value: 23.435
    - type: mrr_at_100
      value: 24.179000000000002
    - type: mrr_at_1000
      value: 24.25
    - type: mrr_at_3
      value: 21.907
    - type: mrr_at_5
      value: 22.781000000000002
    - type: ndcg_at_1
      value: 18.404999999999998
    - type: ndcg_at_10
      value: 24.515
    - type: ndcg_at_100
      value: 28.721000000000004
    - type: ndcg_at_1000
      value: 31.259999999999998
    - type: ndcg_at_3
      value: 21.508
    - type: ndcg_at_5
      value: 23.01
    - type: precision_at_1
      value: 18.404999999999998
    - type: precision_at_10
      value: 3.834
    - type: precision_at_100
      value: 0.641
    - type: precision_at_1000
      value: 0.093
    - type: precision_at_3
      value: 9.151
    - type: precision_at_5
      value: 6.503
    - type: recall_at_1
      value: 16.779
    - type: recall_at_10
      value: 31.730000000000004
    - type: recall_at_100
      value: 51.673
    - type: recall_at_1000
      value: 71.17599999999999
    - type: recall_at_3
      value: 23.518
    - type: recall_at_5
      value: 27.230999999999998
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 9.279
    - type: map_at_10
      value: 13.822000000000001
    - type: map_at_100
      value: 14.533
    - type: map_at_1000
      value: 14.649999999999999
    - type: map_at_3
      value: 12.396
    - type: map_at_5
      value: 13.214
    - type: mrr_at_1
      value: 11.149000000000001
    - type: mrr_at_10
      value: 16.139
    - type: mrr_at_100
      value: 16.872
    - type: mrr_at_1000
      value: 16.964000000000002
    - type: mrr_at_3
      value: 14.613000000000001
    - type: mrr_at_5
      value: 15.486
    - type: ndcg_at_1
      value: 11.149000000000001
    - type: ndcg_at_10
      value: 16.82
    - type: ndcg_at_100
      value: 20.73
    - type: ndcg_at_1000
      value: 23.894000000000002
    - type: ndcg_at_3
      value: 14.11
    - type: ndcg_at_5
      value: 15.404000000000002
    - type: precision_at_1
      value: 11.149000000000001
    - type: precision_at_10
      value: 3.063
    - type: precision_at_100
      value: 0.587
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 6.699
    - type: precision_at_5
      value: 4.928
    - type: recall_at_1
      value: 9.279
    - type: recall_at_10
      value: 23.745
    - type: recall_at_100
      value: 41.873
    - type: recall_at_1000
      value: 64.982
    - type: recall_at_3
      value: 16.152
    - type: recall_at_5
      value: 19.409000000000002
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 16.36
    - type: map_at_10
      value: 21.927
    - type: map_at_100
      value: 22.889
    - type: map_at_1000
      value: 22.994
    - type: map_at_3
      value: 20.433
    - type: map_at_5
      value: 21.337
    - type: mrr_at_1
      value: 18.75
    - type: mrr_at_10
      value: 24.859
    - type: mrr_at_100
      value: 25.746999999999996
    - type: mrr_at_1000
      value: 25.829
    - type: mrr_at_3
      value: 23.383000000000003
    - type: mrr_at_5
      value: 24.297
    - type: ndcg_at_1
      value: 18.75
    - type: ndcg_at_10
      value: 25.372
    - type: ndcg_at_100
      value: 30.342999999999996
    - type: ndcg_at_1000
      value: 33.286
    - type: ndcg_at_3
      value: 22.627
    - type: ndcg_at_5
      value: 24.04
    - type: precision_at_1
      value: 18.75
    - type: precision_at_10
      value: 4.1419999999999995
    - type: precision_at_100
      value: 0.738
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 10.261000000000001
    - type: precision_at_5
      value: 7.164
    - type: recall_at_1
      value: 16.36
    - type: recall_at_10
      value: 32.949
    - type: recall_at_100
      value: 55.552
    - type: recall_at_1000
      value: 77.09899999999999
    - type: recall_at_3
      value: 25.538
    - type: recall_at_5
      value: 29.008
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 17.39
    - type: map_at_10
      value: 23.058
    - type: map_at_100
      value: 24.445
    - type: map_at_1000
      value: 24.637999999999998
    - type: map_at_3
      value: 21.037
    - type: map_at_5
      value: 21.966
    - type: mrr_at_1
      value: 19.96
    - type: mrr_at_10
      value: 26.301000000000002
    - type: mrr_at_100
      value: 27.297
    - type: mrr_at_1000
      value: 27.375
    - type: mrr_at_3
      value: 24.340999999999998
    - type: mrr_at_5
      value: 25.339
    - type: ndcg_at_1
      value: 19.96
    - type: ndcg_at_10
      value: 27.249000000000002
    - type: ndcg_at_100
      value: 32.997
    - type: ndcg_at_1000
      value: 36.359
    - type: ndcg_at_3
      value: 23.519000000000002
    - type: ndcg_at_5
      value: 24.915000000000003
    - type: precision_at_1
      value: 19.96
    - type: precision_at_10
      value: 5.356000000000001
    - type: precision_at_100
      value: 1.198
    - type: precision_at_1000
      value: 0.20400000000000001
    - type: precision_at_3
      value: 10.738
    - type: precision_at_5
      value: 7.904999999999999
    - type: recall_at_1
      value: 17.39
    - type: recall_at_10
      value: 35.254999999999995
    - type: recall_at_100
      value: 61.351
    - type: recall_at_1000
      value: 84.395
    - type: recall_at_3
      value: 25.194
    - type: recall_at_5
      value: 28.546
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: 2b9f5791698b5be7bc5e10535c8690f20043c3db
    metrics:
    - type: map_at_1
      value: 14.238999999999999
    - type: map_at_10
      value: 19.323
    - type: map_at_100
      value: 19.994
    - type: map_at_1000
      value: 20.102999999999998
    - type: map_at_3
      value: 17.631
    - type: map_at_5
      value: 18.401
    - type: mrr_at_1
      value: 15.157000000000002
    - type: mrr_at_10
      value: 20.578
    - type: mrr_at_100
      value: 21.252
    - type: mrr_at_1000
      value: 21.346999999999998
    - type: mrr_at_3
      value: 18.762
    - type: mrr_at_5
      value: 19.713
    - type: ndcg_at_1
      value: 15.157000000000002
    - type: ndcg_at_10
      value: 22.468
    - type: ndcg_at_100
      value: 26.245
    - type: ndcg_at_1000
      value: 29.534
    - type: ndcg_at_3
      value: 18.981
    - type: ndcg_at_5
      value: 20.349999999999998
    - type: precision_at_1
      value: 15.157000000000002
    - type: precision_at_10
      value: 3.512
    - type: precision_at_100
      value: 0.577
    - type: precision_at_1000
      value: 0.091
    - type: precision_at_3
      value: 8.01
    - type: precision_at_5
      value: 5.656
    - type: recall_at_1
      value: 14.238999999999999
    - type: recall_at_10
      value: 31.038
    - type: recall_at_100
      value: 49.122
    - type: recall_at_1000
      value: 74.919
    - type: recall_at_3
      value: 21.436
    - type: recall_at_5
      value: 24.692
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: 392b78eb68c07badcd7c2cd8f39af108375dfcce
    metrics:
    - type: map_at_1
      value: 8.828
    - type: map_at_10
      value: 14.982000000000001
    - type: map_at_100
      value: 16.495
    - type: map_at_1000
      value: 16.658
    - type: map_at_3
      value: 12.366000000000001
    - type: map_at_5
      value: 13.655000000000001
    - type: mrr_at_1
      value: 19.088
    - type: mrr_at_10
      value: 29.29
    - type: mrr_at_100
      value: 30.291
    - type: mrr_at_1000
      value: 30.342000000000002
    - type: mrr_at_3
      value: 25.907000000000004
    - type: mrr_at_5
      value: 27.840999999999998
    - type: ndcg_at_1
      value: 19.088
    - type: ndcg_at_10
      value: 21.858
    - type: ndcg_at_100
      value: 28.323999999999998
    - type: ndcg_at_1000
      value: 31.561
    - type: ndcg_at_3
      value: 17.175
    - type: ndcg_at_5
      value: 18.869
    - type: precision_at_1
      value: 19.088
    - type: precision_at_10
      value: 6.9190000000000005
    - type: precision_at_100
      value: 1.376
    - type: precision_at_1000
      value: 0.197
    - type: precision_at_3
      value: 12.703999999999999
    - type: precision_at_5
      value: 9.993
    - type: recall_at_1
      value: 8.828
    - type: recall_at_10
      value: 27.381
    - type: recall_at_100
      value: 50.0
    - type: recall_at_1000
      value: 68.355
    - type: recall_at_3
      value: 16.118
    - type: recall_at_5
      value: 20.587
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: f097057d03ed98220bc7309ddb10b71a54d667d6
    metrics:
    - type: map_at_1
      value: 5.586
    - type: map_at_10
      value: 10.040000000000001
    - type: map_at_100
      value: 12.55
    - type: map_at_1000
      value: 13.123999999999999
    - type: map_at_3
      value: 7.75
    - type: map_at_5
      value: 8.835999999999999
    - type: mrr_at_1
      value: 42.25
    - type: mrr_at_10
      value: 51.205999999999996
    - type: mrr_at_100
      value: 51.818
    - type: mrr_at_1000
      value: 51.855
    - type: mrr_at_3
      value: 48.875
    - type: mrr_at_5
      value: 50.488
    - type: ndcg_at_1
      value: 32.25
    - type: ndcg_at_10
      value: 22.718
    - type: ndcg_at_100
      value: 24.359
    - type: ndcg_at_1000
      value: 29.232000000000003
    - type: ndcg_at_3
      value: 25.974000000000004
    - type: ndcg_at_5
      value: 24.291999999999998
    - type: precision_at_1
      value: 42.25
    - type: precision_at_10
      value: 17.75
    - type: precision_at_100
      value: 5.032
    - type: precision_at_1000
      value: 1.117
    - type: precision_at_3
      value: 28.833
    - type: precision_at_5
      value: 24.25
    - type: recall_at_1
      value: 5.586
    - type: recall_at_10
      value: 14.16
    - type: recall_at_100
      value: 28.051
    - type: recall_at_1000
      value: 45.157000000000004
    - type: recall_at_3
      value: 8.758000000000001
    - type: recall_at_5
      value: 10.975999999999999
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 829147f8f75a25f005913200eb5ed41fae320aa1
    metrics:
    - type: accuracy
      value: 39.075
    - type: f1
      value: 35.01420354708222
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: 1429cf27e393599b8b359b9b72c666f96b2525f9
    metrics:
    - type: map_at_1
      value: 43.519999999999996
    - type: map_at_10
      value: 54.368
    - type: map_at_100
      value: 54.918
    - type: map_at_1000
      value: 54.942
    - type: map_at_3
      value: 51.712
    - type: map_at_5
      value: 53.33599999999999
    - type: mrr_at_1
      value: 46.955000000000005
    - type: mrr_at_10
      value: 58.219
    - type: mrr_at_100
      value: 58.73500000000001
    - type: mrr_at_1000
      value: 58.753
    - type: mrr_at_3
      value: 55.518
    - type: mrr_at_5
      value: 57.191
    - type: ndcg_at_1
      value: 46.955000000000005
    - type: ndcg_at_10
      value: 60.45
    - type: ndcg_at_100
      value: 63.047
    - type: ndcg_at_1000
      value: 63.712999999999994
    - type: ndcg_at_3
      value: 55.233
    - type: ndcg_at_5
      value: 58.072
    - type: precision_at_1
      value: 46.955000000000005
    - type: precision_at_10
      value: 8.267
    - type: precision_at_100
      value: 0.962
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 22.326999999999998
    - type: precision_at_5
      value: 14.940999999999999
    - type: recall_at_1
      value: 43.519999999999996
    - type: recall_at_10
      value: 75.632
    - type: recall_at_100
      value: 87.41600000000001
    - type: recall_at_1000
      value: 92.557
    - type: recall_at_3
      value: 61.597
    - type: recall_at_5
      value: 68.518
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: 41b686a7f28c59bcaaa5791efd47c67c8ebe28be
    metrics:
    - type: map_at_1
      value: 9.549000000000001
    - type: map_at_10
      value: 15.762
    - type: map_at_100
      value: 17.142
    - type: map_at_1000
      value: 17.329
    - type: map_at_3
      value: 13.575000000000001
    - type: map_at_5
      value: 14.754000000000001
    - type: mrr_at_1
      value: 19.753
    - type: mrr_at_10
      value: 26.568
    - type: mrr_at_100
      value: 27.606
    - type: mrr_at_1000
      value: 27.68
    - type: mrr_at_3
      value: 24.203
    - type: mrr_at_5
      value: 25.668999999999997
    - type: ndcg_at_1
      value: 19.753
    - type: ndcg_at_10
      value: 21.118000000000002
    - type: ndcg_at_100
      value: 27.308
    - type: ndcg_at_1000
      value: 31.304
    - type: ndcg_at_3
      value: 18.319
    - type: ndcg_at_5
      value: 19.414
    - type: precision_at_1
      value: 19.753
    - type: precision_at_10
      value: 6.08
    - type: precision_at_100
      value: 1.204
    - type: precision_at_1000
      value: 0.192
    - type: precision_at_3
      value: 12.191
    - type: precision_at_5
      value: 9.383
    - type: recall_at_1
      value: 9.549000000000001
    - type: recall_at_10
      value: 26.131
    - type: recall_at_100
      value: 50.544999999999995
    - type: recall_at_1000
      value: 74.968
    - type: recall_at_3
      value: 16.951
    - type: recall_at_5
      value: 20.95
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: 766870b35a1b9ca65e67a0d1913899973551fc6c
    metrics:
    - type: map_at_1
      value: 25.544
    - type: map_at_10
      value: 32.62
    - type: map_at_100
      value: 33.275
    - type: map_at_1000
      value: 33.344
    - type: map_at_3
      value: 30.851
    - type: map_at_5
      value: 31.868999999999996
    - type: mrr_at_1
      value: 51.087
    - type: mrr_at_10
      value: 57.704
    - type: mrr_at_100
      value: 58.175
    - type: mrr_at_1000
      value: 58.207
    - type: mrr_at_3
      value: 56.106
    - type: mrr_at_5
      value: 57.074000000000005
    - type: ndcg_at_1
      value: 51.087
    - type: ndcg_at_10
      value: 40.876000000000005
    - type: ndcg_at_100
      value: 43.762
    - type: ndcg_at_1000
      value: 45.423
    - type: ndcg_at_3
      value: 37.65
    - type: ndcg_at_5
      value: 39.305
    - type: precision_at_1
      value: 51.087
    - type: precision_at_10
      value: 8.304
    - type: precision_at_100
      value: 1.059
    - type: precision_at_1000
      value: 0.128
    - type: precision_at_3
      value: 22.875999999999998
    - type: precision_at_5
      value: 15.033
    - type: recall_at_1
      value: 25.544
    - type: recall_at_10
      value: 41.519
    - type: recall_at_100
      value: 52.957
    - type: recall_at_1000
      value: 64.132
    - type: recall_at_3
      value: 34.315
    - type: recall_at_5
      value: 37.583
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 8d743909f834c38949e8323a8a6ce8721ea6c7f4
    metrics:
    - type: accuracy
      value: 58.6696
    - type: ap
      value: 55.3644880984279
    - type: f1
      value: 58.07942097405652
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: validation
      revision: e6838a846e2408f22cf5cc337ebc83e0bcf77849
    metrics:
    - type: map_at_1
      value: 14.442
    - type: map_at_10
      value: 22.932
    - type: map_at_100
      value: 24.132
    - type: map_at_1000
      value: 24.213
    - type: map_at_3
      value: 20.002
    - type: map_at_5
      value: 21.636
    - type: mrr_at_1
      value: 14.841999999999999
    - type: mrr_at_10
      value: 23.416
    - type: mrr_at_100
      value: 24.593999999999998
    - type: mrr_at_1000
      value: 24.669
    - type: mrr_at_3
      value: 20.494
    - type: mrr_at_5
      value: 22.14
    - type: ndcg_at_1
      value: 14.841999999999999
    - type: ndcg_at_10
      value: 27.975
    - type: ndcg_at_100
      value: 34.143
    - type: ndcg_at_1000
      value: 36.370000000000005
    - type: ndcg_at_3
      value: 21.944
    - type: ndcg_at_5
      value: 24.881
    - type: precision_at_1
      value: 14.841999999999999
    - type: precision_at_10
      value: 4.537
    - type: precision_at_100
      value: 0.767
    - type: precision_at_1000
      value: 0.096
    - type: precision_at_3
      value: 9.322
    - type: precision_at_5
      value: 7.074
    - type: recall_at_1
      value: 14.442
    - type: recall_at_10
      value: 43.557
    - type: recall_at_100
      value: 72.904
    - type: recall_at_1000
      value: 90.40700000000001
    - type: recall_at_3
      value: 27.088
    - type: recall_at_5
      value: 34.144000000000005
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 86.95622435020519
    - type: f1
      value: 86.58363130708494
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (de)
      config: de
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 62.73034657650043
    - type: f1
      value: 60.78623915840713
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (es)
      config: es
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 67.54503002001334
    - type: f1
      value: 65.34879794116112
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (fr)
      config: fr
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 65.35233322893829
    - type: f1
      value: 62.994001882446646
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (hi)
      config: hi
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 45.37110075295806
    - type: f1
      value: 44.26285860740745
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (th)
      config: th
      split: test
      revision: a7e2a951126a26fc8c6a69f835f33a346ba259e3
    metrics:
    - type: accuracy
      value: 55.276672694394215
    - type: f1
      value: 53.28388179869587
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 62.25262197902417
    - type: f1
      value: 43.44084037148853
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (de)
      config: de
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 49.56043956043956
    - type: f1
      value: 32.86333673498598
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (es)
      config: es
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 49.93995997331555
    - type: f1
      value: 34.726671876888126
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (fr)
      config: fr
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 46.32947071719386
    - type: f1
      value: 32.325273615982795
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (hi)
      config: hi
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 32.208676945141626
    - type: f1
      value: 21.32185122815139
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (th)
      config: th
      split: test
      revision: 6299947a7777084cc2d4b64235bf7190381ce755
    metrics:
    - type: accuracy
      value: 43.627486437613015
    - type: f1
      value: 27.04872922347508
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (af)
      config: af
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 40.548083389374575
    - type: f1
      value: 39.490307545239716
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (am)
      config: am
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 24.18291862811029
    - type: f1
      value: 23.437620034727473
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ar)
      config: ar
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 30.134498991257562
    - type: f1
      value: 28.787175191531283
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (az)
      config: az
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 35.88433086751849
    - type: f1
      value: 36.264500398782126
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (bn)
      config: bn
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 29.17283120376597
    - type: f1
      value: 27.8101616531901
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (cy)
      config: cy
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 41.788836583725626
    - type: f1
      value: 39.71413181054801
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (da)
      config: da
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 44.176193678547406
    - type: f1
      value: 42.192499826552286
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (de)
      config: de
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.07464694014795
    - type: f1
      value: 39.44188259183162
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (el)
      config: el
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 36.254203093476804
    - type: f1
      value: 34.46592715936761
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 61.40887693342301
    - type: f1
      value: 59.79854802683996
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (es)
      config: es
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.679892400807
    - type: f1
      value: 42.04801248338172
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fa)
      config: fa
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 35.59179556153329
    - type: f1
      value: 34.045862930486166
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fi)
      config: fi
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 40.036987222595826
    - type: f1
      value: 38.117703439362785
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fr)
      config: fr
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 43.43981170141224
    - type: f1
      value: 42.7084388987865
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (he)
      config: he
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 31.593813046402154
    - type: f1
      value: 29.98550522450782
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hi)
      config: hi
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 27.044384667114997
    - type: f1
      value: 27.313059184832667
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hu)
      config: hu
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 38.453261600538
    - type: f1
      value: 37.309189326110435
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hy)
      config: hy
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 27.979152656355076
    - type: f1
      value: 27.430939684346445
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (id)
      config: id
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 43.97108271687963
    - type: f1
      value: 43.40585705688761
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (is)
      config: is
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 40.302622730329524
    - type: f1
      value: 39.108052180520744
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (it)
      config: it
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 45.474108944182916
    - type: f1
      value: 45.85950328241134
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ja)
      config: ja
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 45.60860793544048
    - type: f1
      value: 43.94920708216737
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (jv)
      config: jv
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 38.668459986550104
    - type: f1
      value: 37.6990034018859
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ka)
      config: ka
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 25.6523201075992
    - type: f1
      value: 25.279084273189582
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (km)
      config: km
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 28.295225285810353
    - type: f1
      value: 26.645825638771548
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (kn)
      config: kn
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 23.480161398789505
    - type: f1
      value: 22.275241866506732
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ko)
      config: ko
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 36.55682582380632
    - type: f1
      value: 36.004753171063605
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (lv)
      config: lv
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 41.84936112979153
    - type: f1
      value: 41.38932672359119
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ml)
      config: ml
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 24.90921318090114
    - type: f1
      value: 23.968687483768807
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (mn)
      config: mn
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 29.86213853396099
    - type: f1
      value: 29.977152075255407
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ms)
      config: ms
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.42098184263618
    - type: f1
      value: 41.50877432664628
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (my)
      config: my
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 25.131136516476126
    - type: f1
      value: 23.938932214086776
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nb)
      config: nb
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 39.81506388702084
    - type: f1
      value: 38.809586587791664
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nl)
      config: nl
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 43.62138533960995
    - type: f1
      value: 42.01386842914633
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pl)
      config: pl
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.19569603227976
    - type: f1
      value: 40.00556559825827
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pt)
      config: pt
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 45.20847343644923
    - type: f1
      value: 44.24115005029051
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ro)
      config: ro
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 41.80901143241426
    - type: f1
      value: 40.474074848670085
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ru)
      config: ru
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 35.96839273705447
    - type: f1
      value: 35.095456843621
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sl)
      config: sl
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 40.60524546065905
    - type: f1
      value: 39.302383051500136
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sq)
      config: sq
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.75722932078009
    - type: f1
      value: 41.53763931497389
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sv)
      config: sv
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.347007397444514
    - type: f1
      value: 41.04366017948627
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sw)
      config: sw
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 41.12306657700067
    - type: f1
      value: 39.712940473289024
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ta)
      config: ta
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 24.603227975790183
    - type: f1
      value: 23.969236788828606
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (te)
      config: te
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 25.03698722259583
    - type: f1
      value: 24.37196123281459
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (th)
      config: th
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 35.40013449899126
    - type: f1
      value: 35.063600413688036
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tl)
      config: tl
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 41.19031607262945
    - type: f1
      value: 40.240432304273014
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tr)
      config: tr
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 36.405514458641555
    - type: f1
      value: 36.03844992856558
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ur)
      config: ur
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 25.934767989240076
    - type: f1
      value: 25.2074457023531
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (vi)
      config: vi
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 38.79959650302622
    - type: f1
      value: 37.160233794673125
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 46.244115669132476
    - type: f1
      value: 44.367480561291906
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 072a486a144adf7f4479a4a0dddb2152e161e1ea
    metrics:
    - type: accuracy
      value: 42.30665770006724
    - type: f1
      value: 41.9642223283514
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (af)
      config: af
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 43.2481506388702
    - type: f1
      value: 40.924230769590785
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (am)
      config: am
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 25.30262273032952
    - type: f1
      value: 24.937105830264066
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ar)
      config: ar
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 32.07128446536651
    - type: f1
      value: 31.80245816594883
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (az)
      config: az
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 36.681237390719566
    - type: f1
      value: 36.37219042508338
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (bn)
      config: bn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 29.56624075319435
    - type: f1
      value: 28.386042056362758
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (cy)
      config: cy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.1049092131809
    - type: f1
      value: 38.926150886991294
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (da)
      config: da
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 45.44384667114997
    - type: f1
      value: 42.578252395460005
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (de)
      config: de
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 43.211163416274374
    - type: f1
      value: 41.04465858304789
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (el)
      config: el
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 36.503026227303295
    - type: f1
      value: 34.49785095312759
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.73772696704773
    - type: f1
      value: 69.21759502909043
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (es)
      config: es
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 44.078681909885674
    - type: f1
      value: 43.05914426901129
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fa)
      config: fa
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 32.61264290517821
    - type: f1
      value: 32.02463177462754
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fi)
      config: fi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 40.35642232683255
    - type: f1
      value: 38.13642481807678
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fr)
      config: fr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 45.06724949562878
    - type: f1
      value: 43.19827608343738
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (he)
      config: he
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 32.178883658372555
    - type: f1
      value: 29.979761884698775
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hi)
      config: hi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 26.903160726294555
    - type: f1
      value: 25.833010434083363
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hu)
      config: hu
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 40.379959650302624
    - type: f1
      value: 37.93134355292882
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hy)
      config: hy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 28.375924680564896
    - type: f1
      value: 26.96255693013172
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (id)
      config: id
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 44.361129791526565
    - type: f1
      value: 43.54445012295126
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (is)
      config: is
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 39.290517821116346
    - type: f1
      value: 37.26982052174147
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (it)
      config: it
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 46.4694014794889
    - type: f1
      value: 44.060986162841566
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ja)
      config: ja
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 46.25756556825824
    - type: f1
      value: 45.625139456758816
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (jv)
      config: jv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 41.12642905178212
    - type: f1
      value: 39.54392378396527
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ka)
      config: ka
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 24.72763954270343
    - type: f1
      value: 23.337743140804484
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (km)
      config: km
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 29.741089441829182
    - type: f1
      value: 27.570876190083748
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (kn)
      config: kn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 23.850033624747816
    - type: f1
      value: 22.86733484540032
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ko)
      config: ko
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 36.56691324815064
    - type: f1
      value: 35.504081677134565
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (lv)
      config: lv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 40.928043039677206
    - type: f1
      value: 39.108589131211254
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ml)
      config: ml
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 25.527908540685946
    - type: f1
      value: 25.333391622280477
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (mn)
      config: mn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 29.105581708137183
    - type: f1
      value: 28.478235012692814
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ms)
      config: ms
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 43.78614660390047
    - type: f1
      value: 41.9640143926267
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (my)
      config: my
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 27.269670477471415
    - type: f1
      value: 26.228386764141852
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nb)
      config: nb
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 39.018157363819775
    - type: f1
      value: 37.641949339321854
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nl)
      config: nl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 45.35978480161399
    - type: f1
      value: 42.6851176096831
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pl)
      config: pl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 41.89307330195023
    - type: f1
      value: 40.888710642615024
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pt)
      config: pt
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 45.901143241425686
    - type: f1
      value: 44.496942353920545
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ro)
      config: ro
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 44.11566913248151
    - type: f1
      value: 41.953945105870616
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ru)
      config: ru
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 32.76395427034297
    - type: f1
      value: 31.436372571600934
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sl)
      config: sl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 40.504371217215876
    - type: f1
      value: 39.322752749628165
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sq)
      config: sq
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.51849361129792
    - type: f1
      value: 41.4139297118463
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sv)
      config: sv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.293207800941495
    - type: f1
      value: 40.50409536806683
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sw)
      config: sw
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.9993275050437
    - type: f1
      value: 41.045416224973266
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ta)
      config: ta
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 28.32548755884331
    - type: f1
      value: 27.276841995561867
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (te)
      config: te
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 26.593813046402154
    - type: f1
      value: 25.483878616197586
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (th)
      config: th
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 36.788836583725626
    - type: f1
      value: 34.603932909177686
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tl)
      config: tl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.5689307330195
    - type: f1
      value: 40.924469309079825
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tr)
      config: tr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 37.09482178883658
    - type: f1
      value: 37.949628822857164
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ur)
      config: ur
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 28.836583725622063
    - type: f1
      value: 27.806558655512344
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (vi)
      config: vi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 37.357094821788834
    - type: f1
      value: 37.507918961038165
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 49.37794216543375
    - type: f1
      value: 47.20421153697707
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 44.42165433759248
    - type: f1
      value: 44.34741861198931
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: dcefc037ef84348e49b0d29109e891c01067226b
    metrics:
    - type: v_measure
      value: 31.374938993074252
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 3cd0e71dfbe09d4de0f9e5ecba43e7ce280959dc
    metrics:
    - type: v_measure
      value: 26.871455379644093
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 30.402396942935333
    - type: mrr
      value: 31.42600938803256
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: 7eb63cc0c1eb59324d709ebed25fcab851fa7610
    metrics:
    - type: map_at_1
      value: 3.7740000000000005
    - type: map_at_10
      value: 7.614999999999999
    - type: map_at_100
      value: 9.574
    - type: map_at_1000
      value: 10.711
    - type: map_at_3
      value: 5.7540000000000004
    - type: map_at_5
      value: 6.6659999999999995
    - type: mrr_at_1
      value: 33.127
    - type: mrr_at_10
      value: 40.351
    - type: mrr_at_100
      value: 41.144
    - type: mrr_at_1000
      value: 41.202
    - type: mrr_at_3
      value: 38.029
    - type: mrr_at_5
      value: 39.190000000000005
    - type: ndcg_at_1
      value: 31.579
    - type: ndcg_at_10
      value: 22.792
    - type: ndcg_at_100
      value: 21.698999999999998
    - type: ndcg_at_1000
      value: 30.892999999999997
    - type: ndcg_at_3
      value: 26.828999999999997
    - type: ndcg_at_5
      value: 25.119000000000003
    - type: precision_at_1
      value: 33.127
    - type: precision_at_10
      value: 16.718
    - type: precision_at_100
      value: 5.7090000000000005
    - type: precision_at_1000
      value: 1.836
    - type: precision_at_3
      value: 24.768
    - type: precision_at_5
      value: 21.3
    - type: recall_at_1
      value: 3.7740000000000005
    - type: recall_at_10
      value: 10.302999999999999
    - type: recall_at_100
      value: 23.013
    - type: recall_at_1000
      value: 54.864999999999995
    - type: recall_at_3
      value: 6.554
    - type: recall_at_5
      value: 8.087
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: 6062aefc120bfe8ece5897809fb2e53bfe0d128c
    metrics:
    - type: map_at_1
      value: 15.620999999999999
    - type: map_at_10
      value: 24.519
    - type: map_at_100
      value: 25.586
    - type: map_at_1000
      value: 25.662000000000003
    - type: map_at_3
      value: 21.619
    - type: map_at_5
      value: 23.232
    - type: mrr_at_1
      value: 17.497
    - type: mrr_at_10
      value: 26.301000000000002
    - type: mrr_at_100
      value: 27.235
    - type: mrr_at_1000
      value: 27.297
    - type: mrr_at_3
      value: 23.561
    - type: mrr_at_5
      value: 25.111
    - type: ndcg_at_1
      value: 17.497
    - type: ndcg_at_10
      value: 29.725
    - type: ndcg_at_100
      value: 34.824
    - type: ndcg_at_1000
      value: 36.907000000000004
    - type: ndcg_at_3
      value: 23.946
    - type: ndcg_at_5
      value: 26.739
    - type: precision_at_1
      value: 17.497
    - type: precision_at_10
      value: 5.2170000000000005
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 11.114
    - type: precision_at_5
      value: 8.285
    - type: recall_at_1
      value: 15.620999999999999
    - type: recall_at_10
      value: 43.999
    - type: recall_at_100
      value: 67.183
    - type: recall_at_1000
      value: 83.174
    - type: recall_at_3
      value: 28.720000000000002
    - type: recall_at_5
      value: 35.154
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: 6205996560df11e3a3da9ab4f926788fc30a7db4
    metrics:
    - type: map_at_1
      value: 54.717000000000006
    - type: map_at_10
      value: 67.514
    - type: map_at_100
      value: 68.484
    - type: map_at_1000
      value: 68.523
    - type: map_at_3
      value: 64.169
    - type: map_at_5
      value: 66.054
    - type: mrr_at_1
      value: 62.46000000000001
    - type: mrr_at_10
      value: 71.503
    - type: mrr_at_100
      value: 71.91499999999999
    - type: mrr_at_1000
      value: 71.923
    - type: mrr_at_3
      value: 69.46799999999999
    - type: mrr_at_5
      value: 70.677
    - type: ndcg_at_1
      value: 62.480000000000004
    - type: ndcg_at_10
      value: 72.98
    - type: ndcg_at_100
      value: 76.023
    - type: ndcg_at_1000
      value: 76.512
    - type: ndcg_at_3
      value: 68.138
    - type: ndcg_at_5
      value: 70.458
    - type: precision_at_1
      value: 62.480000000000004
    - type: precision_at_10
      value: 11.373
    - type: precision_at_100
      value: 1.437
    - type: precision_at_1000
      value: 0.154
    - type: precision_at_3
      value: 29.622999999999998
    - type: precision_at_5
      value: 19.918
    - type: recall_at_1
      value: 54.717000000000006
    - type: recall_at_10
      value: 84.745
    - type: recall_at_100
      value: 96.528
    - type: recall_at_1000
      value: 99.39
    - type: recall_at_3
      value: 71.60600000000001
    - type: recall_at_5
      value: 77.511
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: b2805658ae38990172679479369a78b86de8c390
    metrics:
    - type: v_measure
      value: 40.23390747226228
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
    metrics:
    - type: v_measure
      value: 49.090518272935626
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: 5c59ef3e437a0a9651c8fe6fde943e7dce59fba5
    metrics:
    - type: map_at_1
      value: 3.028
    - type: map_at_10
      value: 6.968000000000001
    - type: map_at_100
      value: 8.200000000000001
    - type: map_at_1000
      value: 8.432
    - type: map_at_3
      value: 5.3069999999999995
    - type: map_at_5
      value: 6.099
    - type: mrr_at_1
      value: 14.799999999999999
    - type: mrr_at_10
      value: 22.425
    - type: mrr_at_100
      value: 23.577
    - type: mrr_at_1000
      value: 23.669999999999998
    - type: mrr_at_3
      value: 20.233
    - type: mrr_at_5
      value: 21.318
    - type: ndcg_at_1
      value: 14.799999999999999
    - type: ndcg_at_10
      value: 12.206
    - type: ndcg_at_100
      value: 17.799
    - type: ndcg_at_1000
      value: 22.891000000000002
    - type: ndcg_at_3
      value: 12.128
    - type: ndcg_at_5
      value: 10.212
    - type: precision_at_1
      value: 14.799999999999999
    - type: precision_at_10
      value: 6.17
    - type: precision_at_100
      value: 1.428
    - type: precision_at_1000
      value: 0.266
    - type: precision_at_3
      value: 11.333
    - type: precision_at_5
      value: 8.74
    - type: recall_at_1
      value: 3.028
    - type: recall_at_10
      value: 12.522
    - type: recall_at_100
      value: 28.975
    - type: recall_at_1000
      value: 54.038
    - type: recall_at_3
      value: 6.912999999999999
    - type: recall_at_5
      value: 8.883000000000001
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
    metrics:
    - type: cos_sim_pearson
      value: 76.62983928119752
    - type: cos_sim_spearman
      value: 65.92910683118656
    - type: euclidean_pearson
      value: 71.10290039690963
    - type: euclidean_spearman
      value: 64.80076622426652
    - type: manhattan_pearson
      value: 70.8944726230188
    - type: manhattan_spearman
      value: 64.75082576033986
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: fdf84275bb8ce4b49c971d02e84dd1abc677a50f
    metrics:
    - type: cos_sim_pearson
      value: 74.42679147085553
    - type: cos_sim_spearman
      value: 66.52980061546658
    - type: euclidean_pearson
      value: 74.87039477408763
    - type: euclidean_spearman
      value: 70.63397666902786
    - type: manhattan_pearson
      value: 74.97015137513088
    - type: manhattan_spearman
      value: 70.75951355434326
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 1591bfcbe8c69d4bf7fe2a16e2451017832cafb9
    metrics:
    - type: cos_sim_pearson
      value: 75.62472426599543
    - type: cos_sim_spearman
      value: 76.1662886374236
    - type: euclidean_pearson
      value: 76.3297128081315
    - type: euclidean_spearman
      value: 77.19385151966563
    - type: manhattan_pearson
      value: 76.50363291423257
    - type: manhattan_spearman
      value: 77.37081896355399
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: e2125984e7df8b7871f6ae9949cf6b6795e7c54b
    metrics:
    - type: cos_sim_pearson
      value: 74.48227705407035
    - type: cos_sim_spearman
      value: 69.04572664009687
    - type: euclidean_pearson
      value: 71.76138185714849
    - type: euclidean_spearman
      value: 68.93415452043307
    - type: manhattan_pearson
      value: 71.68010915543306
    - type: manhattan_spearman
      value: 68.99176321262806
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: 1cd7298cac12a96a373b6a2f18738bb3e739a9b6
    metrics:
    - type: cos_sim_pearson
      value: 78.1566527175902
    - type: cos_sim_spearman
      value: 79.23677712825851
    - type: euclidean_pearson
      value: 76.29138438696417
    - type: euclidean_spearman
      value: 77.20108266215374
    - type: manhattan_pearson
      value: 76.27464935799118
    - type: manhattan_spearman
      value: 77.15286174478099
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 360a0b2dff98700d09e634a01e1cc1624d3e42cd
    metrics:
    - type: cos_sim_pearson
      value: 75.068454465977
    - type: cos_sim_spearman
      value: 76.06792422441929
    - type: euclidean_pearson
      value: 70.64605440627699
    - type: euclidean_spearman
      value: 70.21776051117844
    - type: manhattan_pearson
      value: 70.32479295054918
    - type: manhattan_spearman
      value: 69.89782458638528
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ko-ko)
      config: ko-ko
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 39.43327289939437
    - type: cos_sim_spearman
      value: 52.386010275505654
    - type: euclidean_pearson
      value: 46.40999904885745
    - type: euclidean_spearman
      value: 51.00333465175934
    - type: manhattan_pearson
      value: 46.55753533133655
    - type: manhattan_spearman
      value: 51.07550440519388
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ar-ar)
      config: ar-ar
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 55.54431928210687
    - type: cos_sim_spearman
      value: 55.61674586076298
    - type: euclidean_pearson
      value: 58.07442713714088
    - type: euclidean_spearman
      value: 55.74066216931719
    - type: manhattan_pearson
      value: 57.84021675638542
    - type: manhattan_spearman
      value: 55.20365812536853
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-ar)
      config: en-ar
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 11.378463868809098
    - type: cos_sim_spearman
      value: 8.209569244801065
    - type: euclidean_pearson
      value: 1.07041700730406
    - type: euclidean_spearman
      value: 2.2052197108931892
    - type: manhattan_pearson
      value: 0.7671300251104268
    - type: manhattan_spearman
      value: 3.430645020535567
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-de)
      config: en-de
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 32.71403560929013
    - type: cos_sim_spearman
      value: 30.18181775929109
    - type: euclidean_pearson
      value: 25.57368595910298
    - type: euclidean_spearman
      value: 23.316649115731376
    - type: manhattan_pearson
      value: 24.144200325329614
    - type: manhattan_spearman
      value: 21.64621546338457
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 83.36340470799158
    - type: cos_sim_spearman
      value: 84.95398260629699
    - type: euclidean_pearson
      value: 80.69876969911644
    - type: euclidean_spearman
      value: 80.97451731130427
    - type: manhattan_pearson
      value: 80.65869354146945
    - type: manhattan_spearman
      value: 80.8540858718528
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-tr)
      config: en-tr
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 1.9200044163754912
    - type: cos_sim_spearman
      value: 1.0393399782021342
    - type: euclidean_pearson
      value: 1.1376003191297994
    - type: euclidean_spearman
      value: 1.8947106671763914
    - type: manhattan_pearson
      value: 3.8362564474484335
    - type: manhattan_spearman
      value: 4.242750882792888
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-en)
      config: es-en
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 26.561262451099577
    - type: cos_sim_spearman
      value: 28.776666666659906
    - type: euclidean_pearson
      value: 14.640410196999088
    - type: euclidean_spearman
      value: 16.10557011701786
    - type: manhattan_pearson
      value: 15.019405495911272
    - type: manhattan_spearman
      value: 15.37192083104197
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-es)
      config: es-es
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 69.7544202001433
    - type: cos_sim_spearman
      value: 71.88444295144646
    - type: euclidean_pearson
      value: 73.84934185952773
    - type: euclidean_spearman
      value: 73.26911108021089
    - type: manhattan_pearson
      value: 74.04354196954574
    - type: manhattan_spearman
      value: 73.37650787943872
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (fr-en)
      config: fr-en
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 27.70511842301491
    - type: cos_sim_spearman
      value: 26.339466714066447
    - type: euclidean_pearson
      value: 9.323158236506385
    - type: euclidean_spearman
      value: 7.32083231520273
    - type: manhattan_pearson
      value: 7.807399527573071
    - type: manhattan_spearman
      value: 5.525546663067113
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (it-en)
      config: it-en
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 24.226521799447692
    - type: cos_sim_spearman
      value: 20.72992940458968
    - type: euclidean_pearson
      value: 6.753378617205011
    - type: euclidean_spearman
      value: 6.281654679029505
    - type: manhattan_pearson
      value: 7.087180250449323
    - type: manhattan_spearman
      value: 6.41611659259516
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (nl-en)
      config: nl-en
      split: test
      revision: 9fc37e8c632af1c87a3d23e685d49552a02582a0
    metrics:
    - type: cos_sim_pearson
      value: 29.131412364061234
    - type: cos_sim_spearman
      value: 25.053429612793547
    - type: euclidean_pearson
      value: 10.657141303962
    - type: euclidean_spearman
      value: 9.712124819778452
    - type: manhattan_pearson
      value: 12.481782693315688
    - type: manhattan_spearman
      value: 11.287958480905973
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 64.04750650962879
    - type: cos_sim_spearman
      value: 65.66183708171826
    - type: euclidean_pearson
      value: 66.90887604405887
    - type: euclidean_spearman
      value: 66.89814072484552
    - type: manhattan_pearson
      value: 67.31627110509089
    - type: manhattan_spearman
      value: 67.01048176165322
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de)
      config: de
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 19.26519187000913
    - type: cos_sim_spearman
      value: 21.987647321429005
    - type: euclidean_pearson
      value: 17.850618752342946
    - type: euclidean_spearman
      value: 22.86669392885474
    - type: manhattan_pearson
      value: 18.16183594260708
    - type: manhattan_spearman
      value: 23.637510352837907
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es)
      config: es
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 34.221261828226936
    - type: cos_sim_spearman
      value: 49.811823238907664
    - type: euclidean_pearson
      value: 44.50394399762147
    - type: euclidean_spearman
      value: 50.959184495072876
    - type: manhattan_pearson
      value: 45.83191034038624
    - type: manhattan_spearman
      value: 50.190409866117946
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl)
      config: pl
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 3.620381732096531
    - type: cos_sim_spearman
      value: 23.30843951799194
    - type: euclidean_pearson
      value: 0.965453312113125
    - type: euclidean_spearman
      value: 24.235967620790316
    - type: manhattan_pearson
      value: 1.4408922275701606
    - type: manhattan_spearman
      value: 25.161920137046096
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (tr)
      config: tr
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 16.69489628726267
    - type: cos_sim_spearman
      value: 34.66348380997687
    - type: euclidean_pearson
      value: 29.415825529188606
    - type: euclidean_spearman
      value: 38.33011033170646
    - type: manhattan_pearson
      value: 31.23273195263394
    - type: manhattan_spearman
      value: 39.10055785755795
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ar)
      config: ar
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 9.134927430889528
    - type: cos_sim_spearman
      value: 28.18922448944151
    - type: euclidean_pearson
      value: 19.86814169549051
    - type: euclidean_spearman
      value: 27.519588644948627
    - type: manhattan_pearson
      value: 21.80949221238945
    - type: manhattan_spearman
      value: 28.25217200494078
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ru)
      config: ru
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 3.6386482942352085
    - type: cos_sim_spearman
      value: 9.068119621940966
    - type: euclidean_pearson
      value: 0.8123129118737714
    - type: euclidean_spearman
      value: 9.173672890166147
    - type: manhattan_pearson
      value: 0.754518899822658
    - type: manhattan_spearman
      value: 8.431719541986524
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 2.972091574908432
    - type: cos_sim_spearman
      value: 25.48511383289232
    - type: euclidean_pearson
      value: 12.751569670148918
    - type: euclidean_spearman
      value: 24.940721642439286
    - type: manhattan_pearson
      value: 14.310238482989826
    - type: manhattan_spearman
      value: 24.69821216148647
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 54.4745185734135
    - type: cos_sim_spearman
      value: 67.66493409568727
    - type: euclidean_pearson
      value: 60.13580336797049
    - type: euclidean_spearman
      value: 66.12319300814538
    - type: manhattan_pearson
      value: 60.816210368708155
    - type: manhattan_spearman
      value: 65.70010026716766
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-en)
      config: de-en
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 49.37865412588201
    - type: cos_sim_spearman
      value: 53.07135629778897
    - type: euclidean_pearson
      value: 49.29201416711091
    - type: euclidean_spearman
      value: 50.54523702399645
    - type: manhattan_pearson
      value: 51.265764141268534
    - type: manhattan_spearman
      value: 51.979086403193605
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-en)
      config: es-en
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 44.925652392562135
    - type: cos_sim_spearman
      value: 49.51253904767726
    - type: euclidean_pearson
      value: 48.79346518897415
    - type: euclidean_spearman
      value: 51.47957870101565
    - type: manhattan_pearson
      value: 49.51314553898044
    - type: manhattan_spearman
      value: 51.895207893189166
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (it)
      config: it
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 45.241690321111875
    - type: cos_sim_spearman
      value: 48.24795739512037
    - type: euclidean_pearson
      value: 49.22719494399897
    - type: euclidean_spearman
      value: 49.64102442042809
    - type: manhattan_pearson
      value: 49.497887732970256
    - type: manhattan_spearman
      value: 49.940515338096304
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl-en)
      config: pl-en
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 36.42138324083909
    - type: cos_sim_spearman
      value: 36.79867489417801
    - type: euclidean_pearson
      value: 27.760612942610084
    - type: euclidean_spearman
      value: 29.140966500287625
    - type: manhattan_pearson
      value: 28.456674031350115
    - type: manhattan_spearman
      value: 27.46356370924497
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh-en)
      config: zh-en
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 26.55350664089358
    - type: cos_sim_spearman
      value: 28.681707196975008
    - type: euclidean_pearson
      value: 12.613577889195138
    - type: euclidean_spearman
      value: 13.589493311702933
    - type: manhattan_pearson
      value: 11.640157427420958
    - type: manhattan_spearman
      value: 10.345223941212415
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-it)
      config: es-it
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 38.54682179114309
    - type: cos_sim_spearman
      value: 45.782560880405704
    - type: euclidean_pearson
      value: 46.496857002368486
    - type: euclidean_spearman
      value: 48.21270426410012
    - type: manhattan_pearson
      value: 46.871839119374044
    - type: manhattan_spearman
      value: 47.556987773851525
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-fr)
      config: de-fr
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 35.12956772546032
    - type: cos_sim_spearman
      value: 32.96920218281008
    - type: euclidean_pearson
      value: 34.23140384382136
    - type: euclidean_spearman
      value: 32.19303153191447
    - type: manhattan_pearson
      value: 34.189468276600635
    - type: manhattan_spearman
      value: 34.887065709732376
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-pl)
      config: de-pl
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 30.507667380509634
    - type: cos_sim_spearman
      value: 20.447284723752716
    - type: euclidean_pearson
      value: 29.662041381794474
    - type: euclidean_spearman
      value: 20.939990379746757
    - type: manhattan_pearson
      value: 32.5112080506328
    - type: manhattan_spearman
      value: 23.773047901712495
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr-pl)
      config: fr-pl
      split: test
      revision: 2de6ce8c1921b71a755b262c6b57fef195dd7906
    metrics:
    - type: cos_sim_pearson
      value: 71.10820459712156
    - type: cos_sim_spearman
      value: 61.97797868009122
    - type: euclidean_pearson
      value: 60.30910689156633
    - type: euclidean_spearman
      value: 61.97797868009122
    - type: manhattan_pearson
      value: 66.3405176964038
    - type: manhattan_spearman
      value: 61.97797868009122
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: 8913289635987208e6e7c72789e4be2fe94b6abd
    metrics:
    - type: cos_sim_pearson
      value: 76.53032504460737
    - type: cos_sim_spearman
      value: 75.33716094627373
    - type: euclidean_pearson
      value: 69.64662673290599
    - type: euclidean_spearman
      value: 67.30188896368857
    - type: manhattan_pearson
      value: 69.45096082050807
    - type: manhattan_spearman
      value: 67.0718727259371
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: 56a6d0140cf6356659e2a7c1413286a774468d44
    metrics:
    - type: map
      value: 71.33941904192648
    - type: mrr
      value: 89.73766429648782
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: a75ae049398addde9b70f6b268875f5cbce99089
    metrics:
    - type: map_at_1
      value: 43.333
    - type: map_at_10
      value: 52.364
    - type: map_at_100
      value: 53.184
    - type: map_at_1000
      value: 53.234
    - type: map_at_3
      value: 49.832
    - type: map_at_5
      value: 51.244
    - type: mrr_at_1
      value: 45.333
    - type: mrr_at_10
      value: 53.455
    - type: mrr_at_100
      value: 54.191
    - type: mrr_at_1000
      value: 54.235
    - type: mrr_at_3
      value: 51.556000000000004
    - type: mrr_at_5
      value: 52.622
    - type: ndcg_at_1
      value: 45.333
    - type: ndcg_at_10
      value: 56.899
    - type: ndcg_at_100
      value: 60.702
    - type: ndcg_at_1000
      value: 62.046
    - type: ndcg_at_3
      value: 52.451
    - type: ndcg_at_5
      value: 54.534000000000006
    - type: precision_at_1
      value: 45.333
    - type: precision_at_10
      value: 7.8
    - type: precision_at_100
      value: 0.987
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_3
      value: 20.778
    - type: precision_at_5
      value: 13.866999999999999
    - type: recall_at_1
      value: 43.333
    - type: recall_at_10
      value: 69.69999999999999
    - type: recall_at_100
      value: 86.9
    - type: recall_at_1000
      value: 97.6
    - type: recall_at_3
      value: 57.81699999999999
    - type: recall_at_5
      value: 62.827999999999996
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: 5a8256d0dff9c4bd3be3ba3e67e4e70173f802ea
    metrics:
    - type: cos_sim_accuracy
      value: 99.7
    - type: cos_sim_ap
      value: 89.88577913120001
    - type: cos_sim_f1
      value: 84.62694041061593
    - type: cos_sim_precision
      value: 84.7542627883651
    - type: cos_sim_recall
      value: 84.5
    - type: dot_accuracy
      value: 99.24752475247524
    - type: dot_ap
      value: 56.81855467290009
    - type: dot_f1
      value: 56.084126189283936
    - type: dot_precision
      value: 56.16850551654965
    - type: dot_recall
      value: 56.00000000000001
    - type: euclidean_accuracy
      value: 99.7059405940594
    - type: euclidean_ap
      value: 90.12451226491524
    - type: euclidean_f1
      value: 84.44211629125196
    - type: euclidean_precision
      value: 88.66886688668868
    - type: euclidean_recall
      value: 80.60000000000001
    - type: manhattan_accuracy
      value: 99.7128712871287
    - type: manhattan_ap
      value: 90.67590584183216
    - type: manhattan_f1
      value: 84.85436893203884
    - type: manhattan_precision
      value: 82.45283018867924
    - type: manhattan_recall
      value: 87.4
    - type: max_accuracy
      value: 99.7128712871287
    - type: max_ap
      value: 90.67590584183216
    - type: max_f1
      value: 84.85436893203884
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 70a89468f6dccacc6aa2b12a6eac54e74328f235
    metrics:
    - type: v_measure
      value: 52.74481093815175
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: d88009ab563dd0b16cfaf4436abaf97fa3550cf0
    metrics:
    - type: v_measure
      value: 32.65999453562101
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: ef807ea29a75ec4f91b50fd4191cb4ee4589a9f9
    metrics:
    - type: map
      value: 44.74498464555465
    - type: mrr
      value: 45.333879764026825
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: 8753c2788d36c01fc6f05d03fe3f7268d63f9122
    metrics:
    - type: cos_sim_pearson
      value: 29,603788751645216
    - type: cos_sim_spearman
      value: 29.705103354786033
    - type: dot_pearson
      value: 28.07425338095399
    - type: dot_spearman
      value: 26.841406359135367
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: 2c8041b2c07a79b6f7ba8fe6acc72e5d9f92d217
    metrics:
    - type: map_at_1
      value: 0.241
    - type: map_at_10
      value: 1.672
    - type: map_at_100
      value: 7.858999999999999
    - type: map_at_1000
      value: 17.616
    - type: map_at_3
      value: 0.631
    - type: map_at_5
      value: 0.968
    - type: mrr_at_1
      value: 90.0
    - type: mrr_at_10
      value: 92.952
    - type: mrr_at_100
      value: 93.036
    - type: mrr_at_1000
      value: 93.036
    - type: mrr_at_3
      value: 92.667
    - type: mrr_at_5
      value: 92.667
    - type: ndcg_at_1
      value: 83.0
    - type: ndcg_at_10
      value: 70.30199999999999
    - type: ndcg_at_100
      value: 48.149
    - type: ndcg_at_1000
      value: 40.709
    - type: ndcg_at_3
      value: 79.173
    - type: ndcg_at_5
      value: 75.347
    - type: precision_at_1
      value: 90.0
    - type: precision_at_10
      value: 72.6
    - type: precision_at_100
      value: 48.46
    - type: precision_at_1000
      value: 18.093999999999998
    - type: precision_at_3
      value: 84.0
    - type: precision_at_5
      value: 78.8
    - type: recall_at_1
      value: 0.241
    - type: recall_at_10
      value: 1.814
    - type: recall_at_100
      value: 11.141
    - type: recall_at_1000
      value: 37.708999999999996
    - type: recall_at_3
      value: 0.647
    - type: recall_at_5
      value: 1.015
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: 527b7d77e16e343303e68cb6af11d6e18b9f7b3b
    metrics:
    - type: map_at_1
      value: 2.782
    - type: map_at_10
      value: 9.06
    - type: map_at_100
      value: 14.571000000000002
    - type: map_at_1000
      value: 16.006999999999998
    - type: map_at_3
      value: 5.037
    - type: map_at_5
      value: 6.63
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 48.243
    - type: mrr_at_100
      value: 49.065
    - type: mrr_at_1000
      value: 49.065
    - type: mrr_at_3
      value: 44.897999999999996
    - type: mrr_at_5
      value: 46.428999999999995
    - type: ndcg_at_1
      value: 31.633
    - type: ndcg_at_10
      value: 22.972
    - type: ndcg_at_100
      value: 34.777
    - type: ndcg_at_1000
      value: 45.639
    - type: ndcg_at_3
      value: 26.398
    - type: ndcg_at_5
      value: 24.418
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 19.796
    - type: precision_at_100
      value: 7.224
    - type: precision_at_1000
      value: 1.4449999999999998
    - type: precision_at_3
      value: 26.531
    - type: precision_at_5
      value: 23.265
    - type: recall_at_1
      value: 2.782
    - type: recall_at_10
      value: 14.841
    - type: recall_at_100
      value: 44.86
    - type: recall_at_1000
      value: 78.227
    - type: recall_at_3
      value: 5.959
    - type: recall_at_5
      value: 8.969000000000001
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
    metrics:
    - type: accuracy
      value: 62.657999999999994
    - type: ap
      value: 10.96353161716344
    - type: f1
      value: 48.294226423442645
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: 62146448f05be9e52a36b8ee9936447ea787eede
    metrics:
    - type: accuracy
      value: 52.40803621958121
    - type: f1
      value: 52.61009636022186
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 091a54f9a36281ce7d6590ec8c75dd485e7e01d4
    metrics:
    - type: v_measure
      value: 32.12697126747911
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 80.69976753889253
    - type: cos_sim_ap
      value: 54.74680676121268
    - type: cos_sim_f1
      value: 53.18923998590391
    - type: cos_sim_precision
      value: 47.93563413084904
    - type: cos_sim_recall
      value: 59.73614775725594
    - type: dot_accuracy
      value: 79.3348036001669
    - type: dot_ap
      value: 48.46902128933627
    - type: dot_f1
      value: 50.480109739369006
    - type: dot_precision
      value: 42.06084051345173
    - type: dot_recall
      value: 63.113456464379944
    - type: euclidean_accuracy
      value: 79.78780473266973
    - type: euclidean_ap
      value: 50.258327255164815
    - type: euclidean_f1
      value: 49.655838666827684
    - type: euclidean_precision
      value: 45.78044978846582
    - type: euclidean_recall
      value: 54.24802110817942
    - type: manhattan_accuracy
      value: 79.76992310901831
    - type: manhattan_ap
      value: 49.89892485714363
    - type: manhattan_f1
      value: 49.330433787341185
    - type: manhattan_precision
      value: 43.56175459874672
    - type: manhattan_recall
      value: 56.86015831134564
    - type: max_accuracy
      value: 80.69976753889253
    - type: max_ap
      value: 54.74680676121268
    - type: max_f1
      value: 53.18923998590391
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 86.90573213800597
    - type: cos_sim_ap
      value: 81.05760818661524
    - type: cos_sim_f1
      value: 73.64688856729379
    - type: cos_sim_precision
      value: 69.46491946491946
    - type: cos_sim_recall
      value: 78.3646442870342
    - type: dot_accuracy
      value: 83.80680715644041
    - type: dot_ap
      value: 72.49774005947461
    - type: dot_f1
      value: 68.68460650173216
    - type: dot_precision
      value: 62.954647507858105
    - type: dot_recall
      value: 75.56205728364644
    - type: euclidean_accuracy
      value: 85.97430822369697
    - type: euclidean_ap
      value: 78.86101740829326
    - type: euclidean_f1
      value: 71.07960824663695
    - type: euclidean_precision
      value: 70.36897306270279
    - type: euclidean_recall
      value: 71.8047428395442
    - type: manhattan_accuracy
      value: 85.94132029339853
    - type: manhattan_ap
      value: 78.77876711171923
    - type: manhattan_f1
      value: 71.07869075515912
    - type: manhattan_precision
      value: 69.80697847067557
    - type: manhattan_recall
      value: 72.39759778256852
    - type: max_accuracy
      value: 86.90573213800597
    - type: max_ap
      value: 81.05760818661524
    - type: max_f1
      value: 73.64688856729379
---

# SGPT-125M-weightedmean-msmarco-specb-bitfit

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to the eval folder or our paper: https://arxiv.org/abs/2202.08904


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 15600 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 10,
    "evaluation_steps": 0,
    "evaluator": "NoneType",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 0.0002
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 1000,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 300, 'do_lower_case': False}) with Transformer model: GPTNeoModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': True, 'pooling_mode_lasttoken': False})
)
```

## Citing & Authors

```bibtex
@article{muennighoff2022sgpt,
  title={SGPT: GPT Sentence Embeddings for Semantic Search},
  author={Muennighoff, Niklas},
  journal={arXiv preprint arXiv:2202.08904},
  year={2022}
}
```
