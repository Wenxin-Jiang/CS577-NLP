---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: SGPT-5.8B-weightedmean-nli-bitfit
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
      value: 74.07462686567165
    - type: ap
      value: 37.44692407529112
    - type: f1
      value: 68.28971003916419
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
      value: 66.63811563169165
    - type: ap
      value: 78.57252079915924
    - type: f1
      value: 64.5543087846584
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
      value: 77.21889055472263
    - type: ap
      value: 25.663426367826712
    - type: f1
      value: 64.26265688503176
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
      value: 58.06209850107067
    - type: ap
      value: 14.028219107023915
    - type: f1
      value: 48.10387189660778
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
      value: 82.30920000000002
    - type: ap
      value: 76.88786578621213
    - type: f1
      value: 82.15455656065011
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
      value: 41.584
    - type: f1
      value: 41.203137944390114
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
      value: 35.288000000000004
    - type: f1
      value: 34.672995558518096
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
      value: 38.34
    - type: f1
      value: 37.608755629529455
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
      value: 37.839999999999996
    - type: f1
      value: 36.86898201563507
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
      value: 30.936000000000003
    - type: f1
      value: 30.49401738527071
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
      value: 33.75
    - type: f1
      value: 33.38338946025617
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
      value: 13.727
    - type: map_at_10
      value: 26.740000000000002
    - type: map_at_100
      value: 28.218
    - type: map_at_1000
      value: 28.246
    - type: map_at_3
      value: 21.728
    - type: map_at_5
      value: 24.371000000000002
    - type: ndcg_at_1
      value: 13.727
    - type: ndcg_at_10
      value: 35.07
    - type: ndcg_at_100
      value: 41.947
    - type: ndcg_at_1000
      value: 42.649
    - type: ndcg_at_3
      value: 24.484
    - type: ndcg_at_5
      value: 29.282999999999998
    - type: precision_at_1
      value: 13.727
    - type: precision_at_10
      value: 6.223
    - type: precision_at_100
      value: 0.9369999999999999
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 10.835
    - type: precision_at_5
      value: 8.848
    - type: recall_at_1
      value: 13.727
    - type: recall_at_10
      value: 62.233000000000004
    - type: recall_at_100
      value: 93.67
    - type: recall_at_1000
      value: 99.14699999999999
    - type: recall_at_3
      value: 32.504
    - type: recall_at_5
      value: 44.239
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
      value: 40.553923271901695
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
      value: 32.49323183712211
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
      value: 55.89811361443445
    - type: mrr
      value: 70.16235764850724
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
      value: 82.50506557805856
    - type: cos_sim_spearman
      value: 79.50000423261176
    - type: euclidean_pearson
      value: 75.76190885392926
    - type: euclidean_spearman
      value: 76.7330737163434
    - type: manhattan_pearson
      value: 75.825318036112
    - type: manhattan_spearman
      value: 76.7415076434559
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (de-en)
      config: de-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 75.49060542797494
    - type: f1
      value: 75.15379262352123
    - type: precision
      value: 74.99391092553932
    - type: recall
      value: 75.49060542797494
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (fr-en)
      config: fr-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 0.4182258419546555
    - type: f1
      value: 0.4182258419546555
    - type: precision
      value: 0.4182258419546555
    - type: recall
      value: 0.4182258419546555
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (ru-en)
      config: ru-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 0.013855213023900243
    - type: f1
      value: 0.0115460108532502
    - type: precision
      value: 0.010391409767925183
    - type: recall
      value: 0.013855213023900243
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (zh-en)
      config: zh-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 0.315955766192733
    - type: f1
      value: 0.315955766192733
    - type: precision
      value: 0.315955766192733
    - type: recall
      value: 0.315955766192733
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
      value: 81.74025974025973
    - type: f1
      value: 81.66568824876
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
      value: 33.59451202614059
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
      value: 29.128241446157165
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
      value: 26.715
    - type: map_at_10
      value: 35.007
    - type: map_at_100
      value: 36.352000000000004
    - type: map_at_1000
      value: 36.51
    - type: map_at_3
      value: 32.257999999999996
    - type: map_at_5
      value: 33.595000000000006
    - type: ndcg_at_1
      value: 33.906
    - type: ndcg_at_10
      value: 40.353
    - type: ndcg_at_100
      value: 45.562999999999995
    - type: ndcg_at_1000
      value: 48.454
    - type: ndcg_at_3
      value: 36.349
    - type: ndcg_at_5
      value: 37.856
    - type: precision_at_1
      value: 33.906
    - type: precision_at_10
      value: 7.854
    - type: precision_at_100
      value: 1.29
    - type: precision_at_1000
      value: 0.188
    - type: precision_at_3
      value: 17.549
    - type: precision_at_5
      value: 12.561
    - type: recall_at_1
      value: 26.715
    - type: recall_at_10
      value: 49.508
    - type: recall_at_100
      value: 71.76599999999999
    - type: recall_at_1000
      value: 91.118
    - type: recall_at_3
      value: 37.356
    - type: recall_at_5
      value: 41.836
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
      value: 19.663
    - type: map_at_10
      value: 27.086
    - type: map_at_100
      value: 28.066999999999997
    - type: map_at_1000
      value: 28.18
    - type: map_at_3
      value: 24.819
    - type: map_at_5
      value: 26.332
    - type: ndcg_at_1
      value: 25.732
    - type: ndcg_at_10
      value: 31.613999999999997
    - type: ndcg_at_100
      value: 35.757
    - type: ndcg_at_1000
      value: 38.21
    - type: ndcg_at_3
      value: 28.332
    - type: ndcg_at_5
      value: 30.264000000000003
    - type: precision_at_1
      value: 25.732
    - type: precision_at_10
      value: 6.038
    - type: precision_at_100
      value: 1.034
    - type: precision_at_1000
      value: 0.149
    - type: precision_at_3
      value: 13.864
    - type: precision_at_5
      value: 10.241999999999999
    - type: recall_at_1
      value: 19.663
    - type: recall_at_10
      value: 39.585
    - type: recall_at_100
      value: 57.718
    - type: recall_at_1000
      value: 74.26700000000001
    - type: recall_at_3
      value: 29.845
    - type: recall_at_5
      value: 35.105
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
      value: 30.125
    - type: map_at_10
      value: 39.824
    - type: map_at_100
      value: 40.935
    - type: map_at_1000
      value: 41.019
    - type: map_at_3
      value: 37.144
    - type: map_at_5
      value: 38.647999999999996
    - type: ndcg_at_1
      value: 34.922
    - type: ndcg_at_10
      value: 45.072
    - type: ndcg_at_100
      value: 50.046
    - type: ndcg_at_1000
      value: 51.895
    - type: ndcg_at_3
      value: 40.251
    - type: ndcg_at_5
      value: 42.581
    - type: precision_at_1
      value: 34.922
    - type: precision_at_10
      value: 7.303999999999999
    - type: precision_at_100
      value: 1.0739999999999998
    - type: precision_at_1000
      value: 0.13
    - type: precision_at_3
      value: 17.994
    - type: precision_at_5
      value: 12.475999999999999
    - type: recall_at_1
      value: 30.125
    - type: recall_at_10
      value: 57.253
    - type: recall_at_100
      value: 79.35799999999999
    - type: recall_at_1000
      value: 92.523
    - type: recall_at_3
      value: 44.088
    - type: recall_at_5
      value: 49.893
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
      value: 16.298000000000002
    - type: map_at_10
      value: 21.479
    - type: map_at_100
      value: 22.387
    - type: map_at_1000
      value: 22.483
    - type: map_at_3
      value: 19.743
    - type: map_at_5
      value: 20.444000000000003
    - type: ndcg_at_1
      value: 17.740000000000002
    - type: ndcg_at_10
      value: 24.887
    - type: ndcg_at_100
      value: 29.544999999999998
    - type: ndcg_at_1000
      value: 32.417
    - type: ndcg_at_3
      value: 21.274
    - type: ndcg_at_5
      value: 22.399
    - type: precision_at_1
      value: 17.740000000000002
    - type: precision_at_10
      value: 3.932
    - type: precision_at_100
      value: 0.666
    - type: precision_at_1000
      value: 0.094
    - type: precision_at_3
      value: 8.927
    - type: precision_at_5
      value: 6.056
    - type: recall_at_1
      value: 16.298000000000002
    - type: recall_at_10
      value: 34.031
    - type: recall_at_100
      value: 55.769000000000005
    - type: recall_at_1000
      value: 78.19500000000001
    - type: recall_at_3
      value: 23.799999999999997
    - type: recall_at_5
      value: 26.562
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
      value: 10.958
    - type: map_at_10
      value: 16.999
    - type: map_at_100
      value: 17.979
    - type: map_at_1000
      value: 18.112000000000002
    - type: map_at_3
      value: 15.010000000000002
    - type: map_at_5
      value: 16.256999999999998
    - type: ndcg_at_1
      value: 14.179
    - type: ndcg_at_10
      value: 20.985
    - type: ndcg_at_100
      value: 26.216
    - type: ndcg_at_1000
      value: 29.675
    - type: ndcg_at_3
      value: 17.28
    - type: ndcg_at_5
      value: 19.301
    - type: precision_at_1
      value: 14.179
    - type: precision_at_10
      value: 3.968
    - type: precision_at_100
      value: 0.784
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 8.541
    - type: precision_at_5
      value: 6.468
    - type: recall_at_1
      value: 10.958
    - type: recall_at_10
      value: 29.903000000000002
    - type: recall_at_100
      value: 53.413
    - type: recall_at_1000
      value: 78.74799999999999
    - type: recall_at_3
      value: 19.717000000000002
    - type: recall_at_5
      value: 24.817
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
      value: 21.217
    - type: map_at_10
      value: 29.677
    - type: map_at_100
      value: 30.928
    - type: map_at_1000
      value: 31.063000000000002
    - type: map_at_3
      value: 26.611
    - type: map_at_5
      value: 28.463
    - type: ndcg_at_1
      value: 26.083000000000002
    - type: ndcg_at_10
      value: 35.217
    - type: ndcg_at_100
      value: 40.715
    - type: ndcg_at_1000
      value: 43.559
    - type: ndcg_at_3
      value: 30.080000000000002
    - type: ndcg_at_5
      value: 32.701
    - type: precision_at_1
      value: 26.083000000000002
    - type: precision_at_10
      value: 6.622
    - type: precision_at_100
      value: 1.115
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 14.629
    - type: precision_at_5
      value: 10.837
    - type: recall_at_1
      value: 21.217
    - type: recall_at_10
      value: 47.031
    - type: recall_at_100
      value: 70.378
    - type: recall_at_1000
      value: 89.704
    - type: recall_at_3
      value: 32.427
    - type: recall_at_5
      value: 39.31
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
      value: 19.274
    - type: map_at_10
      value: 26.398
    - type: map_at_100
      value: 27.711000000000002
    - type: map_at_1000
      value: 27.833000000000002
    - type: map_at_3
      value: 24.294
    - type: map_at_5
      value: 25.385
    - type: ndcg_at_1
      value: 24.886
    - type: ndcg_at_10
      value: 30.909
    - type: ndcg_at_100
      value: 36.941
    - type: ndcg_at_1000
      value: 39.838
    - type: ndcg_at_3
      value: 27.455000000000002
    - type: ndcg_at_5
      value: 28.828
    - type: precision_at_1
      value: 24.886
    - type: precision_at_10
      value: 5.6739999999999995
    - type: precision_at_100
      value: 1.0290000000000001
    - type: precision_at_1000
      value: 0.146
    - type: precision_at_3
      value: 13.242
    - type: precision_at_5
      value: 9.292
    - type: recall_at_1
      value: 19.274
    - type: recall_at_10
      value: 39.643
    - type: recall_at_100
      value: 66.091
    - type: recall_at_1000
      value: 86.547
    - type: recall_at_3
      value: 29.602
    - type: recall_at_5
      value: 33.561
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
      value: 18.653666666666666
    - type: map_at_10
      value: 25.606666666666666
    - type: map_at_100
      value: 26.669333333333334
    - type: map_at_1000
      value: 26.795833333333334
    - type: map_at_3
      value: 23.43433333333333
    - type: map_at_5
      value: 24.609666666666666
    - type: ndcg_at_1
      value: 22.742083333333333
    - type: ndcg_at_10
      value: 29.978333333333335
    - type: ndcg_at_100
      value: 34.89808333333333
    - type: ndcg_at_1000
      value: 37.806583333333336
    - type: ndcg_at_3
      value: 26.223666666666674
    - type: ndcg_at_5
      value: 27.91033333333333
    - type: precision_at_1
      value: 22.742083333333333
    - type: precision_at_10
      value: 5.397083333333334
    - type: precision_at_100
      value: 0.9340000000000002
    - type: precision_at_1000
      value: 0.13691666666666663
    - type: precision_at_3
      value: 12.331083333333332
    - type: precision_at_5
      value: 8.805499999999999
    - type: recall_at_1
      value: 18.653666666666666
    - type: recall_at_10
      value: 39.22625000000001
    - type: recall_at_100
      value: 61.31049999999999
    - type: recall_at_1000
      value: 82.19058333333334
    - type: recall_at_3
      value: 28.517333333333333
    - type: recall_at_5
      value: 32.9565
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
      value: 16.07
    - type: map_at_10
      value: 21.509
    - type: map_at_100
      value: 22.335
    - type: map_at_1000
      value: 22.437
    - type: map_at_3
      value: 19.717000000000002
    - type: map_at_5
      value: 20.574
    - type: ndcg_at_1
      value: 18.865000000000002
    - type: ndcg_at_10
      value: 25.135999999999996
    - type: ndcg_at_100
      value: 29.483999999999998
    - type: ndcg_at_1000
      value: 32.303
    - type: ndcg_at_3
      value: 21.719
    - type: ndcg_at_5
      value: 23.039
    - type: precision_at_1
      value: 18.865000000000002
    - type: precision_at_10
      value: 4.263999999999999
    - type: precision_at_100
      value: 0.696
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 9.866999999999999
    - type: precision_at_5
      value: 6.902
    - type: recall_at_1
      value: 16.07
    - type: recall_at_10
      value: 33.661
    - type: recall_at_100
      value: 54.001999999999995
    - type: recall_at_1000
      value: 75.564
    - type: recall_at_3
      value: 23.956
    - type: recall_at_5
      value: 27.264
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
      value: 10.847
    - type: map_at_10
      value: 15.518
    - type: map_at_100
      value: 16.384
    - type: map_at_1000
      value: 16.506
    - type: map_at_3
      value: 14.093
    - type: map_at_5
      value: 14.868
    - type: ndcg_at_1
      value: 13.764999999999999
    - type: ndcg_at_10
      value: 18.766
    - type: ndcg_at_100
      value: 23.076
    - type: ndcg_at_1000
      value: 26.344
    - type: ndcg_at_3
      value: 16.150000000000002
    - type: ndcg_at_5
      value: 17.373
    - type: precision_at_1
      value: 13.764999999999999
    - type: precision_at_10
      value: 3.572
    - type: precision_at_100
      value: 0.6779999999999999
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 7.88
    - type: precision_at_5
      value: 5.712
    - type: recall_at_1
      value: 10.847
    - type: recall_at_10
      value: 25.141999999999996
    - type: recall_at_100
      value: 44.847
    - type: recall_at_1000
      value: 68.92099999999999
    - type: recall_at_3
      value: 17.721999999999998
    - type: recall_at_5
      value: 20.968999999999998
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
      value: 18.377
    - type: map_at_10
      value: 26.005
    - type: map_at_100
      value: 26.996
    - type: map_at_1000
      value: 27.116
    - type: map_at_3
      value: 23.712
    - type: map_at_5
      value: 24.859
    - type: ndcg_at_1
      value: 22.201
    - type: ndcg_at_10
      value: 30.635
    - type: ndcg_at_100
      value: 35.623
    - type: ndcg_at_1000
      value: 38.551
    - type: ndcg_at_3
      value: 26.565
    - type: ndcg_at_5
      value: 28.28
    - type: precision_at_1
      value: 22.201
    - type: precision_at_10
      value: 5.41
    - type: precision_at_100
      value: 0.88
    - type: precision_at_1000
      value: 0.125
    - type: precision_at_3
      value: 12.531
    - type: precision_at_5
      value: 8.806
    - type: recall_at_1
      value: 18.377
    - type: recall_at_10
      value: 40.908
    - type: recall_at_100
      value: 63.563
    - type: recall_at_1000
      value: 84.503
    - type: recall_at_3
      value: 29.793999999999997
    - type: recall_at_5
      value: 34.144999999999996
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
      value: 20.246
    - type: map_at_10
      value: 27.528000000000002
    - type: map_at_100
      value: 28.78
    - type: map_at_1000
      value: 29.002
    - type: map_at_3
      value: 25.226
    - type: map_at_5
      value: 26.355
    - type: ndcg_at_1
      value: 25.099
    - type: ndcg_at_10
      value: 32.421
    - type: ndcg_at_100
      value: 37.2
    - type: ndcg_at_1000
      value: 40.693
    - type: ndcg_at_3
      value: 28.768
    - type: ndcg_at_5
      value: 30.23
    - type: precision_at_1
      value: 25.099
    - type: precision_at_10
      value: 6.245
    - type: precision_at_100
      value: 1.269
    - type: precision_at_1000
      value: 0.218
    - type: precision_at_3
      value: 13.767999999999999
    - type: precision_at_5
      value: 9.881
    - type: recall_at_1
      value: 20.246
    - type: recall_at_10
      value: 41.336
    - type: recall_at_100
      value: 63.098
    - type: recall_at_1000
      value: 86.473
    - type: recall_at_3
      value: 30.069000000000003
    - type: recall_at_5
      value: 34.262
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
      value: 14.054
    - type: map_at_10
      value: 20.25
    - type: map_at_100
      value: 21.178
    - type: map_at_1000
      value: 21.288999999999998
    - type: map_at_3
      value: 18.584999999999997
    - type: map_at_5
      value: 19.536
    - type: ndcg_at_1
      value: 15.527
    - type: ndcg_at_10
      value: 23.745
    - type: ndcg_at_100
      value: 28.610999999999997
    - type: ndcg_at_1000
      value: 31.740000000000002
    - type: ndcg_at_3
      value: 20.461
    - type: ndcg_at_5
      value: 22.072
    - type: precision_at_1
      value: 15.527
    - type: precision_at_10
      value: 3.882
    - type: precision_at_100
      value: 0.6930000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 9.181000000000001
    - type: precision_at_5
      value: 6.433
    - type: recall_at_1
      value: 14.054
    - type: recall_at_10
      value: 32.714
    - type: recall_at_100
      value: 55.723
    - type: recall_at_1000
      value: 79.72399999999999
    - type: recall_at_3
      value: 23.832
    - type: recall_at_5
      value: 27.754
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
      value: 6.122
    - type: map_at_10
      value: 11.556
    - type: map_at_100
      value: 12.998000000000001
    - type: map_at_1000
      value: 13.202
    - type: map_at_3
      value: 9.657
    - type: map_at_5
      value: 10.585
    - type: ndcg_at_1
      value: 15.049000000000001
    - type: ndcg_at_10
      value: 17.574
    - type: ndcg_at_100
      value: 24.465999999999998
    - type: ndcg_at_1000
      value: 28.511999999999997
    - type: ndcg_at_3
      value: 13.931
    - type: ndcg_at_5
      value: 15.112
    - type: precision_at_1
      value: 15.049000000000001
    - type: precision_at_10
      value: 5.831
    - type: precision_at_100
      value: 1.322
    - type: precision_at_1000
      value: 0.20500000000000002
    - type: precision_at_3
      value: 10.749
    - type: precision_at_5
      value: 8.365
    - type: recall_at_1
      value: 6.122
    - type: recall_at_10
      value: 22.207
    - type: recall_at_100
      value: 47.08
    - type: recall_at_1000
      value: 70.182
    - type: recall_at_3
      value: 13.416
    - type: recall_at_5
      value: 16.672
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
      value: 4.672
    - type: map_at_10
      value: 10.534
    - type: map_at_100
      value: 14.798
    - type: map_at_1000
      value: 15.927
    - type: map_at_3
      value: 7.317
    - type: map_at_5
      value: 8.726
    - type: ndcg_at_1
      value: 36.5
    - type: ndcg_at_10
      value: 26.098
    - type: ndcg_at_100
      value: 29.215999999999998
    - type: ndcg_at_1000
      value: 36.254999999999995
    - type: ndcg_at_3
      value: 29.247
    - type: ndcg_at_5
      value: 27.692
    - type: precision_at_1
      value: 47.25
    - type: precision_at_10
      value: 22.625
    - type: precision_at_100
      value: 7.042
    - type: precision_at_1000
      value: 1.6129999999999998
    - type: precision_at_3
      value: 34.083000000000006
    - type: precision_at_5
      value: 29.5
    - type: recall_at_1
      value: 4.672
    - type: recall_at_10
      value: 15.638
    - type: recall_at_100
      value: 36.228
    - type: recall_at_1000
      value: 58.831
    - type: recall_at_3
      value: 8.578
    - type: recall_at_5
      value: 11.18
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
      value: 49.919999999999995
    - type: f1
      value: 45.37973678791632
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
      value: 25.801000000000002
    - type: map_at_10
      value: 33.941
    - type: map_at_100
      value: 34.73
    - type: map_at_1000
      value: 34.793
    - type: map_at_3
      value: 31.705
    - type: map_at_5
      value: 33.047
    - type: ndcg_at_1
      value: 27.933000000000003
    - type: ndcg_at_10
      value: 38.644
    - type: ndcg_at_100
      value: 42.594
    - type: ndcg_at_1000
      value: 44.352000000000004
    - type: ndcg_at_3
      value: 34.199
    - type: ndcg_at_5
      value: 36.573
    - type: precision_at_1
      value: 27.933000000000003
    - type: precision_at_10
      value: 5.603000000000001
    - type: precision_at_100
      value: 0.773
    - type: precision_at_1000
      value: 0.094
    - type: precision_at_3
      value: 14.171
    - type: precision_at_5
      value: 9.786999999999999
    - type: recall_at_1
      value: 25.801000000000002
    - type: recall_at_10
      value: 50.876
    - type: recall_at_100
      value: 69.253
    - type: recall_at_1000
      value: 82.907
    - type: recall_at_3
      value: 38.879000000000005
    - type: recall_at_5
      value: 44.651999999999994
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
      value: 9.142
    - type: map_at_10
      value: 13.841999999999999
    - type: map_at_100
      value: 14.960999999999999
    - type: map_at_1000
      value: 15.187000000000001
    - type: map_at_3
      value: 11.966000000000001
    - type: map_at_5
      value: 12.921
    - type: ndcg_at_1
      value: 18.364
    - type: ndcg_at_10
      value: 18.590999999999998
    - type: ndcg_at_100
      value: 24.153
    - type: ndcg_at_1000
      value: 29.104000000000003
    - type: ndcg_at_3
      value: 16.323
    - type: ndcg_at_5
      value: 17.000999999999998
    - type: precision_at_1
      value: 18.364
    - type: precision_at_10
      value: 5.216
    - type: precision_at_100
      value: 1.09
    - type: precision_at_1000
      value: 0.193
    - type: precision_at_3
      value: 10.751
    - type: precision_at_5
      value: 7.932
    - type: recall_at_1
      value: 9.142
    - type: recall_at_10
      value: 22.747
    - type: recall_at_100
      value: 44.585
    - type: recall_at_1000
      value: 75.481
    - type: recall_at_3
      value: 14.602
    - type: recall_at_5
      value: 17.957
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
      value: 18.677
    - type: map_at_10
      value: 26.616
    - type: map_at_100
      value: 27.605
    - type: map_at_1000
      value: 27.711999999999996
    - type: map_at_3
      value: 24.396
    - type: map_at_5
      value: 25.627
    - type: ndcg_at_1
      value: 37.352999999999994
    - type: ndcg_at_10
      value: 33.995
    - type: ndcg_at_100
      value: 38.423
    - type: ndcg_at_1000
      value: 40.947
    - type: ndcg_at_3
      value: 29.885
    - type: ndcg_at_5
      value: 31.874999999999996
    - type: precision_at_1
      value: 37.352999999999994
    - type: precision_at_10
      value: 7.539999999999999
    - type: precision_at_100
      value: 1.107
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_3
      value: 18.938
    - type: precision_at_5
      value: 12.943
    - type: recall_at_1
      value: 18.677
    - type: recall_at_10
      value: 37.698
    - type: recall_at_100
      value: 55.354000000000006
    - type: recall_at_1000
      value: 72.255
    - type: recall_at_3
      value: 28.406
    - type: recall_at_5
      value: 32.357
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
      value: 74.3292
    - type: ap
      value: 68.30186110189658
    - type: f1
      value: 74.20709636944783
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
      value: 6.889000000000001
    - type: map_at_10
      value: 12.321
    - type: map_at_100
      value: 13.416
    - type: map_at_1000
      value: 13.525
    - type: map_at_3
      value: 10.205
    - type: map_at_5
      value: 11.342
    - type: ndcg_at_1
      value: 7.092
    - type: ndcg_at_10
      value: 15.827
    - type: ndcg_at_100
      value: 21.72
    - type: ndcg_at_1000
      value: 24.836
    - type: ndcg_at_3
      value: 11.393
    - type: ndcg_at_5
      value: 13.462
    - type: precision_at_1
      value: 7.092
    - type: precision_at_10
      value: 2.7969999999999997
    - type: precision_at_100
      value: 0.583
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: precision_at_3
      value: 5.019
    - type: precision_at_5
      value: 4.06
    - type: recall_at_1
      value: 6.889000000000001
    - type: recall_at_10
      value: 26.791999999999998
    - type: recall_at_100
      value: 55.371
    - type: recall_at_1000
      value: 80.12899999999999
    - type: recall_at_3
      value: 14.573
    - type: recall_at_5
      value: 19.557
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
      value: 89.6374829001368
    - type: f1
      value: 89.20878379358307
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
      value: 84.54212454212454
    - type: f1
      value: 82.81080100037023
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
      value: 86.46430953969313
    - type: f1
      value: 86.00019824223267
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
      value: 81.31850923896022
    - type: f1
      value: 81.07860454762863
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
      value: 58.23234134098243
    - type: f1
      value: 56.63845098081841
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
      value: 72.28571428571429
    - type: f1
      value: 70.95796714592039
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
      value: 70.68171454628363
    - type: f1
      value: 52.57188062729139
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
      value: 60.521273598196665
    - type: f1
      value: 42.70492970339204
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
      value: 64.32288192128087
    - type: f1
      value: 45.97360620220273
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
      value: 58.67209520826808
    - type: f1
      value: 42.82844991304579
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
      value: 41.95769092864826
    - type: f1
      value: 28.914127631431263
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
      value: 55.28390596745027
    - type: f1
      value: 38.33899250561289
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
      value: 70.00336247478144
    - type: f1
      value: 68.72041942191649
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
      value: 75.0268997982515
    - type: f1
      value: 75.29844481506652
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
      value: 30.327566856300813
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
      value: 28.01650210863619
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
      value: 31.11041256752524
    - type: mrr
      value: 32.14172939750204
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
      value: 3.527
    - type: map_at_10
      value: 9.283
    - type: map_at_100
      value: 11.995000000000001
    - type: map_at_1000
      value: 13.33
    - type: map_at_3
      value: 6.223
    - type: map_at_5
      value: 7.68
    - type: ndcg_at_1
      value: 36.223
    - type: ndcg_at_10
      value: 28.255999999999997
    - type: ndcg_at_100
      value: 26.355
    - type: ndcg_at_1000
      value: 35.536
    - type: ndcg_at_3
      value: 31.962000000000003
    - type: ndcg_at_5
      value: 30.61
    - type: precision_at_1
      value: 37.771
    - type: precision_at_10
      value: 21.889
    - type: precision_at_100
      value: 7.1080000000000005
    - type: precision_at_1000
      value: 1.989
    - type: precision_at_3
      value: 30.857
    - type: precision_at_5
      value: 27.307
    - type: recall_at_1
      value: 3.527
    - type: recall_at_10
      value: 14.015
    - type: recall_at_100
      value: 28.402
    - type: recall_at_1000
      value: 59.795
    - type: recall_at_3
      value: 7.5969999999999995
    - type: recall_at_5
      value: 10.641
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
      value: 11.631
    - type: map_at_10
      value: 19.532
    - type: map_at_100
      value: 20.821
    - type: map_at_1000
      value: 20.910999999999998
    - type: map_at_3
      value: 16.597
    - type: map_at_5
      value: 18.197
    - type: ndcg_at_1
      value: 13.413
    - type: ndcg_at_10
      value: 24.628
    - type: ndcg_at_100
      value: 30.883
    - type: ndcg_at_1000
      value: 33.216
    - type: ndcg_at_3
      value: 18.697
    - type: ndcg_at_5
      value: 21.501
    - type: precision_at_1
      value: 13.413
    - type: precision_at_10
      value: 4.571
    - type: precision_at_100
      value: 0.812
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 8.845
    - type: precision_at_5
      value: 6.889000000000001
    - type: recall_at_1
      value: 11.631
    - type: recall_at_10
      value: 38.429
    - type: recall_at_100
      value: 67.009
    - type: recall_at_1000
      value: 84.796
    - type: recall_at_3
      value: 22.74
    - type: recall_at_5
      value: 29.266
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
      value: 66.64
    - type: map_at_10
      value: 80.394
    - type: map_at_100
      value: 81.099
    - type: map_at_1000
      value: 81.122
    - type: map_at_3
      value: 77.289
    - type: map_at_5
      value: 79.25999999999999
    - type: ndcg_at_1
      value: 76.85
    - type: ndcg_at_10
      value: 84.68
    - type: ndcg_at_100
      value: 86.311
    - type: ndcg_at_1000
      value: 86.49900000000001
    - type: ndcg_at_3
      value: 81.295
    - type: ndcg_at_5
      value: 83.199
    - type: precision_at_1
      value: 76.85
    - type: precision_at_10
      value: 12.928999999999998
    - type: precision_at_100
      value: 1.51
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 35.557
    - type: precision_at_5
      value: 23.576
    - type: recall_at_1
      value: 66.64
    - type: recall_at_10
      value: 93.059
    - type: recall_at_100
      value: 98.922
    - type: recall_at_1000
      value: 99.883
    - type: recall_at_3
      value: 83.49499999999999
    - type: recall_at_5
      value: 88.729
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
      value: 42.17131361041068
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
      value: 48.01815621479994
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
      value: 3.198
    - type: map_at_10
      value: 7.550999999999999
    - type: map_at_100
      value: 9.232
    - type: map_at_1000
      value: 9.51
    - type: map_at_3
      value: 5.2940000000000005
    - type: map_at_5
      value: 6.343999999999999
    - type: ndcg_at_1
      value: 15.8
    - type: ndcg_at_10
      value: 13.553999999999998
    - type: ndcg_at_100
      value: 20.776
    - type: ndcg_at_1000
      value: 26.204
    - type: ndcg_at_3
      value: 12.306000000000001
    - type: ndcg_at_5
      value: 10.952
    - type: precision_at_1
      value: 15.8
    - type: precision_at_10
      value: 7.180000000000001
    - type: precision_at_100
      value: 1.762
    - type: precision_at_1000
      value: 0.307
    - type: precision_at_3
      value: 11.333
    - type: precision_at_5
      value: 9.62
    - type: recall_at_1
      value: 3.198
    - type: recall_at_10
      value: 14.575
    - type: recall_at_100
      value: 35.758
    - type: recall_at_1000
      value: 62.317
    - type: recall_at_3
      value: 6.922000000000001
    - type: recall_at_5
      value: 9.767000000000001
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
      value: 84.5217161312271
    - type: cos_sim_spearman
      value: 79.58562467776268
    - type: euclidean_pearson
      value: 76.69364353942403
    - type: euclidean_spearman
      value: 74.68959282070473
    - type: manhattan_pearson
      value: 76.81159265133732
    - type: manhattan_spearman
      value: 74.7519444048176
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
      value: 83.70403706922605
    - type: cos_sim_spearman
      value: 74.28502198729447
    - type: euclidean_pearson
      value: 83.32719404608066
    - type: euclidean_spearman
      value: 75.92189433460788
    - type: manhattan_pearson
      value: 83.35841543005293
    - type: manhattan_spearman
      value: 75.94458615451978
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
      value: 84.94127878986795
    - type: cos_sim_spearman
      value: 85.35148434923192
    - type: euclidean_pearson
      value: 81.71127467071571
    - type: euclidean_spearman
      value: 82.88240481546771
    - type: manhattan_pearson
      value: 81.72826221967252
    - type: manhattan_spearman
      value: 82.90725064625128
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
      value: 83.1474704168523
    - type: cos_sim_spearman
      value: 79.20612995350827
    - type: euclidean_pearson
      value: 78.85993329596555
    - type: euclidean_spearman
      value: 78.91956572744715
    - type: manhattan_pearson
      value: 78.89999720522347
    - type: manhattan_spearman
      value: 78.93956842550107
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
      value: 84.81255514055894
    - type: cos_sim_spearman
      value: 85.5217140762934
    - type: euclidean_pearson
      value: 82.15024353784499
    - type: euclidean_spearman
      value: 83.04155334389833
    - type: manhattan_pearson
      value: 82.18598945053624
    - type: manhattan_spearman
      value: 83.07248357693301
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
      value: 80.63248465157822
    - type: cos_sim_spearman
      value: 82.53853238521991
    - type: euclidean_pearson
      value: 78.33936863828221
    - type: euclidean_spearman
      value: 79.16305579487414
    - type: manhattan_pearson
      value: 78.3888359870894
    - type: manhattan_spearman
      value: 79.18504473136467
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
      value: 90.09066290639687
    - type: cos_sim_spearman
      value: 90.43893699357069
    - type: euclidean_pearson
      value: 82.39520777222396
    - type: euclidean_spearman
      value: 81.23948185395952
    - type: manhattan_pearson
      value: 82.35529784653383
    - type: manhattan_spearman
      value: 81.12681522483975
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
      value: 63.52752323046846
    - type: cos_sim_spearman
      value: 63.19719780439462
    - type: euclidean_pearson
      value: 58.29085490641428
    - type: euclidean_spearman
      value: 58.975178656335046
    - type: manhattan_pearson
      value: 58.183542772416985
    - type: manhattan_spearman
      value: 59.190630462178994
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
      value: 85.45100366635687
    - type: cos_sim_spearman
      value: 85.66816193002651
    - type: euclidean_pearson
      value: 81.87976731329091
    - type: euclidean_spearman
      value: 82.01382867690964
    - type: manhattan_pearson
      value: 81.88260155706726
    - type: manhattan_spearman
      value: 82.05258597906492
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
      value: 77.53549990038017
    - type: mrr
      value: 93.37474163454556
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
      value: 31.167
    - type: map_at_10
      value: 40.778
    - type: map_at_100
      value: 42.063
    - type: map_at_1000
      value: 42.103
    - type: map_at_3
      value: 37.12
    - type: map_at_5
      value: 39.205
    - type: ndcg_at_1
      value: 33.667
    - type: ndcg_at_10
      value: 46.662
    - type: ndcg_at_100
      value: 51.995999999999995
    - type: ndcg_at_1000
      value: 53.254999999999995
    - type: ndcg_at_3
      value: 39.397999999999996
    - type: ndcg_at_5
      value: 42.934
    - type: precision_at_1
      value: 33.667
    - type: precision_at_10
      value: 7.1
    - type: precision_at_100
      value: 0.993
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_3
      value: 16.111
    - type: precision_at_5
      value: 11.600000000000001
    - type: recall_at_1
      value: 31.167
    - type: recall_at_10
      value: 63.744
    - type: recall_at_100
      value: 87.156
    - type: recall_at_1000
      value: 97.556
    - type: recall_at_3
      value: 44.0
    - type: recall_at_5
      value: 52.556000000000004
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
      value: 99.55148514851486
    - type: cos_sim_ap
      value: 80.535236573428
    - type: cos_sim_f1
      value: 75.01331912626532
    - type: cos_sim_precision
      value: 80.27366020524515
    - type: cos_sim_recall
      value: 70.39999999999999
    - type: dot_accuracy
      value: 99.04851485148515
    - type: dot_ap
      value: 28.505358821499726
    - type: dot_f1
      value: 36.36363636363637
    - type: dot_precision
      value: 37.160751565762006
    - type: dot_recall
      value: 35.6
    - type: euclidean_accuracy
      value: 99.4990099009901
    - type: euclidean_ap
      value: 74.95819047075476
    - type: euclidean_f1
      value: 71.15489874110564
    - type: euclidean_precision
      value: 78.59733978234583
    - type: euclidean_recall
      value: 65.0
    - type: manhattan_accuracy
      value: 99.50198019801981
    - type: manhattan_ap
      value: 75.02070096015086
    - type: manhattan_f1
      value: 71.20535714285712
    - type: manhattan_precision
      value: 80.55555555555556
    - type: manhattan_recall
      value: 63.800000000000004
    - type: max_accuracy
      value: 99.55148514851486
    - type: max_ap
      value: 80.535236573428
    - type: max_f1
      value: 75.01331912626532
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
      value: 54.13314692311623
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
      value: 31.115181648287145
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
      value: 44.771112666694336
    - type: mrr
      value: 45.30415764790765
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
      value: 30.849429597669374
    - type: cos_sim_spearman
      value: 30.384175038360194
    - type: dot_pearson
      value: 29.030383429536823
    - type: dot_spearman
      value: 28.03273624951732
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
      value: 0.19499999999999998
    - type: map_at_10
      value: 1.0959999999999999
    - type: map_at_100
      value: 5.726
    - type: map_at_1000
      value: 13.611999999999998
    - type: map_at_3
      value: 0.45399999999999996
    - type: map_at_5
      value: 0.67
    - type: ndcg_at_1
      value: 71.0
    - type: ndcg_at_10
      value: 55.352999999999994
    - type: ndcg_at_100
      value: 40.797
    - type: ndcg_at_1000
      value: 35.955999999999996
    - type: ndcg_at_3
      value: 63.263000000000005
    - type: ndcg_at_5
      value: 60.14000000000001
    - type: precision_at_1
      value: 78.0
    - type: precision_at_10
      value: 56.99999999999999
    - type: precision_at_100
      value: 41.199999999999996
    - type: precision_at_1000
      value: 16.154
    - type: precision_at_3
      value: 66.667
    - type: precision_at_5
      value: 62.8
    - type: recall_at_1
      value: 0.19499999999999998
    - type: recall_at_10
      value: 1.3639999999999999
    - type: recall_at_100
      value: 9.317
    - type: recall_at_1000
      value: 33.629999999999995
    - type: recall_at_3
      value: 0.49300000000000005
    - type: recall_at_5
      value: 0.756
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
      value: 1.335
    - type: map_at_10
      value: 6.293
    - type: map_at_100
      value: 10.928
    - type: map_at_1000
      value: 12.359
    - type: map_at_3
      value: 3.472
    - type: map_at_5
      value: 4.935
    - type: ndcg_at_1
      value: 19.387999999999998
    - type: ndcg_at_10
      value: 16.178
    - type: ndcg_at_100
      value: 28.149
    - type: ndcg_at_1000
      value: 39.845000000000006
    - type: ndcg_at_3
      value: 19.171
    - type: ndcg_at_5
      value: 17.864
    - type: precision_at_1
      value: 20.408
    - type: precision_at_10
      value: 14.49
    - type: precision_at_100
      value: 6.306000000000001
    - type: precision_at_1000
      value: 1.3860000000000001
    - type: precision_at_3
      value: 21.088
    - type: precision_at_5
      value: 18.367
    - type: recall_at_1
      value: 1.335
    - type: recall_at_10
      value: 10.825999999999999
    - type: recall_at_100
      value: 39.251000000000005
    - type: recall_at_1000
      value: 74.952
    - type: recall_at_3
      value: 4.9110000000000005
    - type: recall_at_5
      value: 7.312
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
      value: 69.93339999999999
    - type: ap
      value: 13.87476602492533
    - type: f1
      value: 53.867357615848555
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
      value: 62.43916242218449
    - type: f1
      value: 62.870386304954685
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
      value: 37.202082549859796
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
      value: 83.65023544137807
    - type: cos_sim_ap
      value: 65.99787692764193
    - type: cos_sim_f1
      value: 62.10650887573965
    - type: cos_sim_precision
      value: 56.30901287553648
    - type: cos_sim_recall
      value: 69.23482849604221
    - type: dot_accuracy
      value: 79.10830303391549
    - type: dot_ap
      value: 48.80109642320246
    - type: dot_f1
      value: 51.418744625967314
    - type: dot_precision
      value: 40.30253107683091
    - type: dot_recall
      value: 71.00263852242745
    - type: euclidean_accuracy
      value: 82.45812719794957
    - type: euclidean_ap
      value: 60.09969493259607
    - type: euclidean_f1
      value: 57.658573789246226
    - type: euclidean_precision
      value: 55.62913907284768
    - type: euclidean_recall
      value: 59.84168865435356
    - type: manhattan_accuracy
      value: 82.46408773916671
    - type: manhattan_ap
      value: 60.116199786815116
    - type: manhattan_f1
      value: 57.683903860160235
    - type: manhattan_precision
      value: 53.41726618705036
    - type: manhattan_recall
      value: 62.69129287598945
    - type: max_accuracy
      value: 83.65023544137807
    - type: max_ap
      value: 65.99787692764193
    - type: max_f1
      value: 62.10650887573965
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
      value: 88.34943920518494
    - type: cos_sim_ap
      value: 84.5428891020442
    - type: cos_sim_f1
      value: 77.09709933923172
    - type: cos_sim_precision
      value: 74.83150952967607
    - type: cos_sim_recall
      value: 79.50415768401602
    - type: dot_accuracy
      value: 84.53448208949432
    - type: dot_ap
      value: 73.96328242371995
    - type: dot_f1
      value: 70.00553786515299
    - type: dot_precision
      value: 63.58777665995976
    - type: dot_recall
      value: 77.86418232214352
    - type: euclidean_accuracy
      value: 86.87662514068381
    - type: euclidean_ap
      value: 81.45499631520235
    - type: euclidean_f1
      value: 73.46567109816063
    - type: euclidean_precision
      value: 69.71037533697381
    - type: euclidean_recall
      value: 77.6485987064983
    - type: manhattan_accuracy
      value: 86.88244654014825
    - type: manhattan_ap
      value: 81.47180273946366
    - type: manhattan_f1
      value: 73.44624393136418
    - type: manhattan_precision
      value: 70.80385852090032
    - type: manhattan_recall
      value: 76.29350169387126
    - type: max_accuracy
      value: 88.34943920518494
    - type: max_ap
      value: 84.5428891020442
    - type: max_f1
      value: 77.09709933923172
---

# SGPT-5.8B-weightedmean-msmarco-specb-bitfit

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to our paper: https://arxiv.org/abs/2202.08904

## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 249592 with parameters:
```
{'batch_size': 2, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
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
        "lr": 5e-05
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
  (0): Transformer({'max_seq_length': 300, 'do_lower_case': False}) with Transformer model: GPTJModel 
  (1): Pooling({'word_embedding_dimension': 4096, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': True, 'pooling_mode_lasttoken': False})
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
