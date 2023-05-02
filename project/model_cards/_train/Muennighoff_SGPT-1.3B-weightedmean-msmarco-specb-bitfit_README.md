---
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: SGPT-1.3B-weightedmean-msmarco-specb-bitfit
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
      value: 65.20895522388061
    - type: ap
      value: 29.59212705444778
    - type: f1
      value: 59.97099864321921
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
      value: 73.20565
    - type: ap
      value: 67.36680643550963
    - type: f1
      value: 72.90420520325125
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
      value: 34.955999999999996
    - type: f1
      value: 34.719324437696955
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
      value: 26.101999999999997
    - type: map_at_10
      value: 40.958
    - type: map_at_100
      value: 42.033
    - type: map_at_1000
      value: 42.042
    - type: map_at_3
      value: 36.332
    - type: map_at_5
      value: 38.608
    - type: mrr_at_1
      value: 26.387
    - type: mrr_at_10
      value: 41.051
    - type: mrr_at_100
      value: 42.118
    - type: mrr_at_1000
      value: 42.126999999999995
    - type: mrr_at_3
      value: 36.415
    - type: mrr_at_5
      value: 38.72
    - type: ndcg_at_1
      value: 26.101999999999997
    - type: ndcg_at_10
      value: 49.68
    - type: ndcg_at_100
      value: 54.257999999999996
    - type: ndcg_at_1000
      value: 54.486000000000004
    - type: ndcg_at_3
      value: 39.864
    - type: ndcg_at_5
      value: 43.980000000000004
    - type: precision_at_1
      value: 26.101999999999997
    - type: precision_at_10
      value: 7.781000000000001
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 16.714000000000002
    - type: precision_at_5
      value: 12.034
    - type: recall_at_1
      value: 26.101999999999997
    - type: recall_at_10
      value: 77.809
    - type: recall_at_100
      value: 97.866
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 50.141999999999996
    - type: recall_at_5
      value: 60.171
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
      value: 43.384194916953774
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
      value: 33.70962633433912
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
      value: 58.133058996870076
    - type: mrr
      value: 72.10922041946972
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
      value: 86.62153841660047
    - type: cos_sim_spearman
      value: 83.01514456843276
    - type: euclidean_pearson
      value: 86.00431518427241
    - type: euclidean_spearman
      value: 83.85552516285783
    - type: manhattan_pearson
      value: 85.83025803351181
    - type: manhattan_spearman
      value: 83.86636878343106
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
      value: 82.05844155844156
    - type: f1
      value: 82.0185837884764
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
      value: 35.05918333141837
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
      value: 30.71055028830579
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
      value: 26.519
    - type: map_at_10
      value: 35.634
    - type: map_at_100
      value: 36.961
    - type: map_at_1000
      value: 37.088
    - type: map_at_3
      value: 32.254
    - type: map_at_5
      value: 34.22
    - type: mrr_at_1
      value: 32.332
    - type: mrr_at_10
      value: 41.168
    - type: mrr_at_100
      value: 41.977
    - type: mrr_at_1000
      value: 42.028999999999996
    - type: mrr_at_3
      value: 38.196999999999996
    - type: mrr_at_5
      value: 40.036
    - type: ndcg_at_1
      value: 32.332
    - type: ndcg_at_10
      value: 41.471000000000004
    - type: ndcg_at_100
      value: 46.955999999999996
    - type: ndcg_at_1000
      value: 49.262
    - type: ndcg_at_3
      value: 35.937999999999995
    - type: ndcg_at_5
      value: 38.702999999999996
    - type: precision_at_1
      value: 32.332
    - type: precision_at_10
      value: 7.7829999999999995
    - type: precision_at_100
      value: 1.29
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 16.834
    - type: precision_at_5
      value: 12.418
    - type: recall_at_1
      value: 26.519
    - type: recall_at_10
      value: 53.190000000000005
    - type: recall_at_100
      value: 76.56500000000001
    - type: recall_at_1000
      value: 91.47800000000001
    - type: recall_at_3
      value: 38.034
    - type: recall_at_5
      value: 45.245999999999995
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
      value: 25.356
    - type: map_at_10
      value: 34.596
    - type: map_at_100
      value: 35.714
    - type: map_at_1000
      value: 35.839999999999996
    - type: map_at_3
      value: 32.073
    - type: map_at_5
      value: 33.475
    - type: mrr_at_1
      value: 31.274
    - type: mrr_at_10
      value: 39.592
    - type: mrr_at_100
      value: 40.284
    - type: mrr_at_1000
      value: 40.339999999999996
    - type: mrr_at_3
      value: 37.378
    - type: mrr_at_5
      value: 38.658
    - type: ndcg_at_1
      value: 31.274
    - type: ndcg_at_10
      value: 39.766
    - type: ndcg_at_100
      value: 44.028
    - type: ndcg_at_1000
      value: 46.445
    - type: ndcg_at_3
      value: 35.934
    - type: ndcg_at_5
      value: 37.751000000000005
    - type: precision_at_1
      value: 31.274
    - type: precision_at_10
      value: 7.452
    - type: precision_at_100
      value: 1.217
    - type: precision_at_1000
      value: 0.16999999999999998
    - type: precision_at_3
      value: 17.431
    - type: precision_at_5
      value: 12.306000000000001
    - type: recall_at_1
      value: 25.356
    - type: recall_at_10
      value: 49.344
    - type: recall_at_100
      value: 67.497
    - type: recall_at_1000
      value: 83.372
    - type: recall_at_3
      value: 38.227
    - type: recall_at_5
      value: 43.187999999999995
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
      value: 32.759
    - type: map_at_10
      value: 43.937
    - type: map_at_100
      value: 45.004
    - type: map_at_1000
      value: 45.07
    - type: map_at_3
      value: 40.805
    - type: map_at_5
      value: 42.497
    - type: mrr_at_1
      value: 37.367
    - type: mrr_at_10
      value: 47.237
    - type: mrr_at_100
      value: 47.973
    - type: mrr_at_1000
      value: 48.010999999999996
    - type: mrr_at_3
      value: 44.65
    - type: mrr_at_5
      value: 46.050999999999995
    - type: ndcg_at_1
      value: 37.367
    - type: ndcg_at_10
      value: 49.659
    - type: ndcg_at_100
      value: 54.069
    - type: ndcg_at_1000
      value: 55.552
    - type: ndcg_at_3
      value: 44.169000000000004
    - type: ndcg_at_5
      value: 46.726
    - type: precision_at_1
      value: 37.367
    - type: precision_at_10
      value: 8.163
    - type: precision_at_100
      value: 1.133
    - type: precision_at_1000
      value: 0.131
    - type: precision_at_3
      value: 19.707
    - type: precision_at_5
      value: 13.718
    - type: recall_at_1
      value: 32.759
    - type: recall_at_10
      value: 63.341
    - type: recall_at_100
      value: 82.502
    - type: recall_at_1000
      value: 93.259
    - type: recall_at_3
      value: 48.796
    - type: recall_at_5
      value: 54.921
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
      value: 18.962
    - type: map_at_10
      value: 25.863000000000003
    - type: map_at_100
      value: 26.817999999999998
    - type: map_at_1000
      value: 26.918
    - type: map_at_3
      value: 23.043
    - type: map_at_5
      value: 24.599
    - type: mrr_at_1
      value: 20.452
    - type: mrr_at_10
      value: 27.301
    - type: mrr_at_100
      value: 28.233000000000004
    - type: mrr_at_1000
      value: 28.310000000000002
    - type: mrr_at_3
      value: 24.539
    - type: mrr_at_5
      value: 26.108999999999998
    - type: ndcg_at_1
      value: 20.452
    - type: ndcg_at_10
      value: 30.354999999999997
    - type: ndcg_at_100
      value: 35.336
    - type: ndcg_at_1000
      value: 37.927
    - type: ndcg_at_3
      value: 24.705
    - type: ndcg_at_5
      value: 27.42
    - type: precision_at_1
      value: 20.452
    - type: precision_at_10
      value: 4.949
    - type: precision_at_100
      value: 0.7799999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 10.358
    - type: precision_at_5
      value: 7.774
    - type: recall_at_1
      value: 18.962
    - type: recall_at_10
      value: 43.056
    - type: recall_at_100
      value: 66.27300000000001
    - type: recall_at_1000
      value: 85.96000000000001
    - type: recall_at_3
      value: 27.776
    - type: recall_at_5
      value: 34.287
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
      value: 11.24
    - type: map_at_10
      value: 18.503
    - type: map_at_100
      value: 19.553
    - type: map_at_1000
      value: 19.689999999999998
    - type: map_at_3
      value: 16.150000000000002
    - type: map_at_5
      value: 17.254
    - type: mrr_at_1
      value: 13.806
    - type: mrr_at_10
      value: 21.939
    - type: mrr_at_100
      value: 22.827
    - type: mrr_at_1000
      value: 22.911
    - type: mrr_at_3
      value: 19.32
    - type: mrr_at_5
      value: 20.558
    - type: ndcg_at_1
      value: 13.806
    - type: ndcg_at_10
      value: 23.383000000000003
    - type: ndcg_at_100
      value: 28.834
    - type: ndcg_at_1000
      value: 32.175
    - type: ndcg_at_3
      value: 18.651999999999997
    - type: ndcg_at_5
      value: 20.505000000000003
    - type: precision_at_1
      value: 13.806
    - type: precision_at_10
      value: 4.714
    - type: precision_at_100
      value: 0.864
    - type: precision_at_1000
      value: 0.13
    - type: precision_at_3
      value: 9.328
    - type: precision_at_5
      value: 6.841
    - type: recall_at_1
      value: 11.24
    - type: recall_at_10
      value: 34.854
    - type: recall_at_100
      value: 59.50299999999999
    - type: recall_at_1000
      value: 83.25
    - type: recall_at_3
      value: 22.02
    - type: recall_at_5
      value: 26.715
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
      value: 23.012
    - type: map_at_10
      value: 33.048
    - type: map_at_100
      value: 34.371
    - type: map_at_1000
      value: 34.489
    - type: map_at_3
      value: 29.942999999999998
    - type: map_at_5
      value: 31.602000000000004
    - type: mrr_at_1
      value: 28.104000000000003
    - type: mrr_at_10
      value: 37.99
    - type: mrr_at_100
      value: 38.836
    - type: mrr_at_1000
      value: 38.891
    - type: mrr_at_3
      value: 35.226
    - type: mrr_at_5
      value: 36.693999999999996
    - type: ndcg_at_1
      value: 28.104000000000003
    - type: ndcg_at_10
      value: 39.037
    - type: ndcg_at_100
      value: 44.643
    - type: ndcg_at_1000
      value: 46.939
    - type: ndcg_at_3
      value: 33.784
    - type: ndcg_at_5
      value: 36.126000000000005
    - type: precision_at_1
      value: 28.104000000000003
    - type: precision_at_10
      value: 7.2669999999999995
    - type: precision_at_100
      value: 1.193
    - type: precision_at_1000
      value: 0.159
    - type: precision_at_3
      value: 16.298000000000002
    - type: precision_at_5
      value: 11.684
    - type: recall_at_1
      value: 23.012
    - type: recall_at_10
      value: 52.054
    - type: recall_at_100
      value: 75.622
    - type: recall_at_1000
      value: 90.675
    - type: recall_at_3
      value: 37.282
    - type: recall_at_5
      value: 43.307
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
      value: 21.624
    - type: map_at_10
      value: 30.209999999999997
    - type: map_at_100
      value: 31.52
    - type: map_at_1000
      value: 31.625999999999998
    - type: map_at_3
      value: 26.951000000000004
    - type: map_at_5
      value: 28.938999999999997
    - type: mrr_at_1
      value: 26.941
    - type: mrr_at_10
      value: 35.13
    - type: mrr_at_100
      value: 36.15
    - type: mrr_at_1000
      value: 36.204
    - type: mrr_at_3
      value: 32.42
    - type: mrr_at_5
      value: 34.155
    - type: ndcg_at_1
      value: 26.941
    - type: ndcg_at_10
      value: 35.726
    - type: ndcg_at_100
      value: 41.725
    - type: ndcg_at_1000
      value: 44.105
    - type: ndcg_at_3
      value: 30.184
    - type: ndcg_at_5
      value: 33.176
    - type: precision_at_1
      value: 26.941
    - type: precision_at_10
      value: 6.654999999999999
    - type: precision_at_100
      value: 1.1520000000000001
    - type: precision_at_1000
      value: 0.152
    - type: precision_at_3
      value: 14.346
    - type: precision_at_5
      value: 10.868
    - type: recall_at_1
      value: 21.624
    - type: recall_at_10
      value: 47.359
    - type: recall_at_100
      value: 73.436
    - type: recall_at_1000
      value: 89.988
    - type: recall_at_3
      value: 32.34
    - type: recall_at_5
      value: 39.856
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
      value: 20.67566666666667
    - type: map_at_10
      value: 28.479333333333333
    - type: map_at_100
      value: 29.612249999999996
    - type: map_at_1000
      value: 29.731166666666663
    - type: map_at_3
      value: 25.884
    - type: map_at_5
      value: 27.298916666666667
    - type: mrr_at_1
      value: 24.402583333333332
    - type: mrr_at_10
      value: 32.07041666666667
    - type: mrr_at_100
      value: 32.95841666666667
    - type: mrr_at_1000
      value: 33.025416666666665
    - type: mrr_at_3
      value: 29.677749999999996
    - type: mrr_at_5
      value: 31.02391666666667
    - type: ndcg_at_1
      value: 24.402583333333332
    - type: ndcg_at_10
      value: 33.326166666666666
    - type: ndcg_at_100
      value: 38.51566666666667
    - type: ndcg_at_1000
      value: 41.13791666666667
    - type: ndcg_at_3
      value: 28.687749999999994
    - type: ndcg_at_5
      value: 30.84766666666667
    - type: precision_at_1
      value: 24.402583333333332
    - type: precision_at_10
      value: 5.943749999999999
    - type: precision_at_100
      value: 1.0098333333333334
    - type: precision_at_1000
      value: 0.14183333333333334
    - type: precision_at_3
      value: 13.211500000000001
    - type: precision_at_5
      value: 9.548416666666668
    - type: recall_at_1
      value: 20.67566666666667
    - type: recall_at_10
      value: 44.245583333333336
    - type: recall_at_100
      value: 67.31116666666667
    - type: recall_at_1000
      value: 85.87841666666665
    - type: recall_at_3
      value: 31.49258333333333
    - type: recall_at_5
      value: 36.93241666666667
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
      value: 18.34
    - type: map_at_10
      value: 23.988
    - type: map_at_100
      value: 24.895
    - type: map_at_1000
      value: 24.992
    - type: map_at_3
      value: 21.831
    - type: map_at_5
      value: 23.0
    - type: mrr_at_1
      value: 20.399
    - type: mrr_at_10
      value: 26.186
    - type: mrr_at_100
      value: 27.017999999999997
    - type: mrr_at_1000
      value: 27.090999999999998
    - type: mrr_at_3
      value: 24.08
    - type: mrr_at_5
      value: 25.230000000000004
    - type: ndcg_at_1
      value: 20.399
    - type: ndcg_at_10
      value: 27.799000000000003
    - type: ndcg_at_100
      value: 32.579
    - type: ndcg_at_1000
      value: 35.209
    - type: ndcg_at_3
      value: 23.684
    - type: ndcg_at_5
      value: 25.521
    - type: precision_at_1
      value: 20.399
    - type: precision_at_10
      value: 4.585999999999999
    - type: precision_at_100
      value: 0.755
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 10.276
    - type: precision_at_5
      value: 7.362
    - type: recall_at_1
      value: 18.34
    - type: recall_at_10
      value: 37.456
    - type: recall_at_100
      value: 59.86
    - type: recall_at_1000
      value: 79.703
    - type: recall_at_3
      value: 26.163999999999998
    - type: recall_at_5
      value: 30.652
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
      value: 12.327
    - type: map_at_10
      value: 17.572
    - type: map_at_100
      value: 18.534
    - type: map_at_1000
      value: 18.653
    - type: map_at_3
      value: 15.703
    - type: map_at_5
      value: 16.752
    - type: mrr_at_1
      value: 15.038000000000002
    - type: mrr_at_10
      value: 20.726
    - type: mrr_at_100
      value: 21.61
    - type: mrr_at_1000
      value: 21.695
    - type: mrr_at_3
      value: 18.829
    - type: mrr_at_5
      value: 19.885
    - type: ndcg_at_1
      value: 15.038000000000002
    - type: ndcg_at_10
      value: 21.241
    - type: ndcg_at_100
      value: 26.179000000000002
    - type: ndcg_at_1000
      value: 29.316
    - type: ndcg_at_3
      value: 17.762
    - type: ndcg_at_5
      value: 19.413
    - type: precision_at_1
      value: 15.038000000000002
    - type: precision_at_10
      value: 3.8920000000000003
    - type: precision_at_100
      value: 0.75
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 8.351
    - type: precision_at_5
      value: 6.187
    - type: recall_at_1
      value: 12.327
    - type: recall_at_10
      value: 29.342000000000002
    - type: recall_at_100
      value: 51.854
    - type: recall_at_1000
      value: 74.648
    - type: recall_at_3
      value: 19.596
    - type: recall_at_5
      value: 23.899
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
      value: 20.594
    - type: map_at_10
      value: 27.878999999999998
    - type: map_at_100
      value: 28.926000000000002
    - type: map_at_1000
      value: 29.041
    - type: map_at_3
      value: 25.668999999999997
    - type: map_at_5
      value: 26.773999999999997
    - type: mrr_at_1
      value: 23.694000000000003
    - type: mrr_at_10
      value: 31.335
    - type: mrr_at_100
      value: 32.218
    - type: mrr_at_1000
      value: 32.298
    - type: mrr_at_3
      value: 29.26
    - type: mrr_at_5
      value: 30.328
    - type: ndcg_at_1
      value: 23.694000000000003
    - type: ndcg_at_10
      value: 32.456
    - type: ndcg_at_100
      value: 37.667
    - type: ndcg_at_1000
      value: 40.571
    - type: ndcg_at_3
      value: 28.283
    - type: ndcg_at_5
      value: 29.986
    - type: precision_at_1
      value: 23.694000000000003
    - type: precision_at_10
      value: 5.448
    - type: precision_at_100
      value: 0.9119999999999999
    - type: precision_at_1000
      value: 0.127
    - type: precision_at_3
      value: 12.717999999999998
    - type: precision_at_5
      value: 8.843
    - type: recall_at_1
      value: 20.594
    - type: recall_at_10
      value: 43.004999999999995
    - type: recall_at_100
      value: 66.228
    - type: recall_at_1000
      value: 87.17099999999999
    - type: recall_at_3
      value: 31.554
    - type: recall_at_5
      value: 35.838
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
      value: 20.855999999999998
    - type: map_at_10
      value: 28.372000000000003
    - type: map_at_100
      value: 29.87
    - type: map_at_1000
      value: 30.075000000000003
    - type: map_at_3
      value: 26.054
    - type: map_at_5
      value: 27.128999999999998
    - type: mrr_at_1
      value: 25.494
    - type: mrr_at_10
      value: 32.735
    - type: mrr_at_100
      value: 33.794000000000004
    - type: mrr_at_1000
      value: 33.85
    - type: mrr_at_3
      value: 30.731
    - type: mrr_at_5
      value: 31.897
    - type: ndcg_at_1
      value: 25.494
    - type: ndcg_at_10
      value: 33.385
    - type: ndcg_at_100
      value: 39.436
    - type: ndcg_at_1000
      value: 42.313
    - type: ndcg_at_3
      value: 29.612
    - type: ndcg_at_5
      value: 31.186999999999998
    - type: precision_at_1
      value: 25.494
    - type: precision_at_10
      value: 6.422999999999999
    - type: precision_at_100
      value: 1.383
    - type: precision_at_1000
      value: 0.22399999999999998
    - type: precision_at_3
      value: 13.834
    - type: precision_at_5
      value: 10.0
    - type: recall_at_1
      value: 20.855999999999998
    - type: recall_at_10
      value: 42.678
    - type: recall_at_100
      value: 70.224
    - type: recall_at_1000
      value: 89.369
    - type: recall_at_3
      value: 31.957
    - type: recall_at_5
      value: 36.026
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
      value: 16.519000000000002
    - type: map_at_10
      value: 22.15
    - type: map_at_100
      value: 23.180999999999997
    - type: map_at_1000
      value: 23.291999999999998
    - type: map_at_3
      value: 20.132
    - type: map_at_5
      value: 21.346
    - type: mrr_at_1
      value: 17.93
    - type: mrr_at_10
      value: 23.506
    - type: mrr_at_100
      value: 24.581
    - type: mrr_at_1000
      value: 24.675
    - type: mrr_at_3
      value: 21.503
    - type: mrr_at_5
      value: 22.686
    - type: ndcg_at_1
      value: 17.93
    - type: ndcg_at_10
      value: 25.636
    - type: ndcg_at_100
      value: 30.736
    - type: ndcg_at_1000
      value: 33.841
    - type: ndcg_at_3
      value: 21.546000000000003
    - type: ndcg_at_5
      value: 23.658
    - type: precision_at_1
      value: 17.93
    - type: precision_at_10
      value: 3.993
    - type: precision_at_100
      value: 0.6890000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 9.057
    - type: precision_at_5
      value: 6.58
    - type: recall_at_1
      value: 16.519000000000002
    - type: recall_at_10
      value: 35.268
    - type: recall_at_100
      value: 58.17
    - type: recall_at_1000
      value: 81.66799999999999
    - type: recall_at_3
      value: 24.165
    - type: recall_at_5
      value: 29.254
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
      value: 10.363
    - type: map_at_10
      value: 18.301000000000002
    - type: map_at_100
      value: 20.019000000000002
    - type: map_at_1000
      value: 20.207
    - type: map_at_3
      value: 14.877
    - type: map_at_5
      value: 16.544
    - type: mrr_at_1
      value: 22.866
    - type: mrr_at_10
      value: 34.935
    - type: mrr_at_100
      value: 35.802
    - type: mrr_at_1000
      value: 35.839999999999996
    - type: mrr_at_3
      value: 30.965999999999998
    - type: mrr_at_5
      value: 33.204
    - type: ndcg_at_1
      value: 22.866
    - type: ndcg_at_10
      value: 26.595000000000002
    - type: ndcg_at_100
      value: 33.513999999999996
    - type: ndcg_at_1000
      value: 36.872
    - type: ndcg_at_3
      value: 20.666999999999998
    - type: ndcg_at_5
      value: 22.728
    - type: precision_at_1
      value: 22.866
    - type: precision_at_10
      value: 8.632
    - type: precision_at_100
      value: 1.6119999999999999
    - type: precision_at_1000
      value: 0.22399999999999998
    - type: precision_at_3
      value: 15.504999999999999
    - type: precision_at_5
      value: 12.404
    - type: recall_at_1
      value: 10.363
    - type: recall_at_10
      value: 33.494
    - type: recall_at_100
      value: 57.593
    - type: recall_at_1000
      value: 76.342
    - type: recall_at_3
      value: 19.157
    - type: recall_at_5
      value: 24.637999999999998
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
      value: 7.436
    - type: map_at_10
      value: 14.760000000000002
    - type: map_at_100
      value: 19.206
    - type: map_at_1000
      value: 20.267
    - type: map_at_3
      value: 10.894
    - type: map_at_5
      value: 12.828999999999999
    - type: mrr_at_1
      value: 54.25
    - type: mrr_at_10
      value: 63.769
    - type: mrr_at_100
      value: 64.193
    - type: mrr_at_1000
      value: 64.211
    - type: mrr_at_3
      value: 61.458
    - type: mrr_at_5
      value: 63.096
    - type: ndcg_at_1
      value: 42.875
    - type: ndcg_at_10
      value: 31.507
    - type: ndcg_at_100
      value: 34.559
    - type: ndcg_at_1000
      value: 41.246
    - type: ndcg_at_3
      value: 35.058
    - type: ndcg_at_5
      value: 33.396
    - type: precision_at_1
      value: 54.25
    - type: precision_at_10
      value: 24.45
    - type: precision_at_100
      value: 7.383000000000001
    - type: precision_at_1000
      value: 1.582
    - type: precision_at_3
      value: 38.083
    - type: precision_at_5
      value: 32.6
    - type: recall_at_1
      value: 7.436
    - type: recall_at_10
      value: 19.862
    - type: recall_at_100
      value: 38.981
    - type: recall_at_1000
      value: 61.038000000000004
    - type: recall_at_3
      value: 11.949
    - type: recall_at_5
      value: 15.562000000000001
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
      value: 46.39
    - type: f1
      value: 42.26424885856703
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
      value: 50.916
    - type: map_at_10
      value: 62.258
    - type: map_at_100
      value: 62.741
    - type: map_at_1000
      value: 62.763000000000005
    - type: map_at_3
      value: 60.01800000000001
    - type: map_at_5
      value: 61.419999999999995
    - type: mrr_at_1
      value: 54.964999999999996
    - type: mrr_at_10
      value: 66.554
    - type: mrr_at_100
      value: 66.96600000000001
    - type: mrr_at_1000
      value: 66.97800000000001
    - type: mrr_at_3
      value: 64.414
    - type: mrr_at_5
      value: 65.77
    - type: ndcg_at_1
      value: 54.964999999999996
    - type: ndcg_at_10
      value: 68.12
    - type: ndcg_at_100
      value: 70.282
    - type: ndcg_at_1000
      value: 70.788
    - type: ndcg_at_3
      value: 63.861999999999995
    - type: ndcg_at_5
      value: 66.216
    - type: precision_at_1
      value: 54.964999999999996
    - type: precision_at_10
      value: 8.998000000000001
    - type: precision_at_100
      value: 1.016
    - type: precision_at_1000
      value: 0.107
    - type: precision_at_3
      value: 25.618000000000002
    - type: precision_at_5
      value: 16.676
    - type: recall_at_1
      value: 50.916
    - type: recall_at_10
      value: 82.04
    - type: recall_at_100
      value: 91.689
    - type: recall_at_1000
      value: 95.34899999999999
    - type: recall_at_3
      value: 70.512
    - type: recall_at_5
      value: 76.29899999999999
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
      value: 13.568
    - type: map_at_10
      value: 23.264000000000003
    - type: map_at_100
      value: 24.823999999999998
    - type: map_at_1000
      value: 25.013999999999996
    - type: map_at_3
      value: 19.724
    - type: map_at_5
      value: 21.772
    - type: mrr_at_1
      value: 27.315
    - type: mrr_at_10
      value: 35.935
    - type: mrr_at_100
      value: 36.929
    - type: mrr_at_1000
      value: 36.985
    - type: mrr_at_3
      value: 33.591
    - type: mrr_at_5
      value: 34.848
    - type: ndcg_at_1
      value: 27.315
    - type: ndcg_at_10
      value: 29.988
    - type: ndcg_at_100
      value: 36.41
    - type: ndcg_at_1000
      value: 40.184999999999995
    - type: ndcg_at_3
      value: 26.342
    - type: ndcg_at_5
      value: 27.68
    - type: precision_at_1
      value: 27.315
    - type: precision_at_10
      value: 8.565000000000001
    - type: precision_at_100
      value: 1.508
    - type: precision_at_1000
      value: 0.219
    - type: precision_at_3
      value: 17.849999999999998
    - type: precision_at_5
      value: 13.672999999999998
    - type: recall_at_1
      value: 13.568
    - type: recall_at_10
      value: 37.133
    - type: recall_at_100
      value: 61.475
    - type: recall_at_1000
      value: 84.372
    - type: recall_at_3
      value: 24.112000000000002
    - type: recall_at_5
      value: 29.507
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
      value: 30.878
    - type: map_at_10
      value: 40.868
    - type: map_at_100
      value: 41.693999999999996
    - type: map_at_1000
      value: 41.775
    - type: map_at_3
      value: 38.56
    - type: map_at_5
      value: 39.947
    - type: mrr_at_1
      value: 61.756
    - type: mrr_at_10
      value: 68.265
    - type: mrr_at_100
      value: 68.671
    - type: mrr_at_1000
      value: 68.694
    - type: mrr_at_3
      value: 66.78399999999999
    - type: mrr_at_5
      value: 67.704
    - type: ndcg_at_1
      value: 61.756
    - type: ndcg_at_10
      value: 49.931
    - type: ndcg_at_100
      value: 53.179
    - type: ndcg_at_1000
      value: 54.94799999999999
    - type: ndcg_at_3
      value: 46.103
    - type: ndcg_at_5
      value: 48.147
    - type: precision_at_1
      value: 61.756
    - type: precision_at_10
      value: 10.163
    - type: precision_at_100
      value: 1.2710000000000001
    - type: precision_at_1000
      value: 0.151
    - type: precision_at_3
      value: 28.179
    - type: precision_at_5
      value: 18.528
    - type: recall_at_1
      value: 30.878
    - type: recall_at_10
      value: 50.817
    - type: recall_at_100
      value: 63.544999999999995
    - type: recall_at_1000
      value: 75.361
    - type: recall_at_3
      value: 42.269
    - type: recall_at_5
      value: 46.32
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
      value: 64.04799999999999
    - type: ap
      value: 59.185251455339284
    - type: f1
      value: 63.947123181349255
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
      value: 18.9
    - type: map_at_10
      value: 29.748
    - type: map_at_100
      value: 30.976
    - type: map_at_1000
      value: 31.041
    - type: map_at_3
      value: 26.112999999999996
    - type: map_at_5
      value: 28.197
    - type: mrr_at_1
      value: 19.413
    - type: mrr_at_10
      value: 30.322
    - type: mrr_at_100
      value: 31.497000000000003
    - type: mrr_at_1000
      value: 31.555
    - type: mrr_at_3
      value: 26.729000000000003
    - type: mrr_at_5
      value: 28.788999999999998
    - type: ndcg_at_1
      value: 19.413
    - type: ndcg_at_10
      value: 36.048
    - type: ndcg_at_100
      value: 42.152
    - type: ndcg_at_1000
      value: 43.772
    - type: ndcg_at_3
      value: 28.642
    - type: ndcg_at_5
      value: 32.358
    - type: precision_at_1
      value: 19.413
    - type: precision_at_10
      value: 5.785
    - type: precision_at_100
      value: 0.8869999999999999
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 12.192
    - type: precision_at_5
      value: 9.189
    - type: recall_at_1
      value: 18.9
    - type: recall_at_10
      value: 55.457
    - type: recall_at_100
      value: 84.09100000000001
    - type: recall_at_1000
      value: 96.482
    - type: recall_at_3
      value: 35.359
    - type: recall_at_5
      value: 44.275
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
      value: 92.07706338349293
    - type: f1
      value: 91.56680443236652
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
      value: 71.18559051527589
    - type: f1
      value: 52.42887061726789
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
      value: 68.64828513786148
    - type: f1
      value: 66.54281381596097
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
      value: 76.04236718224612
    - type: f1
      value: 75.89170458655639
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
      value: 32.0840369055247
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
      value: 29.448729560244537
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
      value: 31.340856463122375
    - type: mrr
      value: 32.398547669840916
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
      value: 5.526
    - type: map_at_10
      value: 11.745
    - type: map_at_100
      value: 14.831
    - type: map_at_1000
      value: 16.235
    - type: map_at_3
      value: 8.716
    - type: map_at_5
      value: 10.101
    - type: mrr_at_1
      value: 43.653
    - type: mrr_at_10
      value: 51.06699999999999
    - type: mrr_at_100
      value: 51.881
    - type: mrr_at_1000
      value: 51.912000000000006
    - type: mrr_at_3
      value: 49.02
    - type: mrr_at_5
      value: 50.288999999999994
    - type: ndcg_at_1
      value: 41.949999999999996
    - type: ndcg_at_10
      value: 32.083
    - type: ndcg_at_100
      value: 30.049999999999997
    - type: ndcg_at_1000
      value: 38.661
    - type: ndcg_at_3
      value: 37.940000000000005
    - type: ndcg_at_5
      value: 35.455999999999996
    - type: precision_at_1
      value: 43.344
    - type: precision_at_10
      value: 23.437
    - type: precision_at_100
      value: 7.829999999999999
    - type: precision_at_1000
      value: 2.053
    - type: precision_at_3
      value: 35.501
    - type: precision_at_5
      value: 30.464000000000002
    - type: recall_at_1
      value: 5.526
    - type: recall_at_10
      value: 15.445999999999998
    - type: recall_at_100
      value: 31.179000000000002
    - type: recall_at_1000
      value: 61.578
    - type: recall_at_3
      value: 9.71
    - type: recall_at_5
      value: 12.026
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
      value: 23.467
    - type: map_at_10
      value: 36.041000000000004
    - type: map_at_100
      value: 37.268
    - type: map_at_1000
      value: 37.322
    - type: map_at_3
      value: 32.09
    - type: map_at_5
      value: 34.414
    - type: mrr_at_1
      value: 26.738
    - type: mrr_at_10
      value: 38.665
    - type: mrr_at_100
      value: 39.64
    - type: mrr_at_1000
      value: 39.681
    - type: mrr_at_3
      value: 35.207
    - type: mrr_at_5
      value: 37.31
    - type: ndcg_at_1
      value: 26.709
    - type: ndcg_at_10
      value: 42.942
    - type: ndcg_at_100
      value: 48.296
    - type: ndcg_at_1000
      value: 49.651
    - type: ndcg_at_3
      value: 35.413
    - type: ndcg_at_5
      value: 39.367999999999995
    - type: precision_at_1
      value: 26.709
    - type: precision_at_10
      value: 7.306
    - type: precision_at_100
      value: 1.0290000000000001
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 16.348
    - type: precision_at_5
      value: 12.068
    - type: recall_at_1
      value: 23.467
    - type: recall_at_10
      value: 61.492999999999995
    - type: recall_at_100
      value: 85.01100000000001
    - type: recall_at_1000
      value: 95.261
    - type: recall_at_3
      value: 41.952
    - type: recall_at_5
      value: 51.105999999999995
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
      value: 67.51700000000001
    - type: map_at_10
      value: 81.054
    - type: map_at_100
      value: 81.727
    - type: map_at_1000
      value: 81.75200000000001
    - type: map_at_3
      value: 78.018
    - type: map_at_5
      value: 79.879
    - type: mrr_at_1
      value: 77.52
    - type: mrr_at_10
      value: 84.429
    - type: mrr_at_100
      value: 84.58200000000001
    - type: mrr_at_1000
      value: 84.584
    - type: mrr_at_3
      value: 83.268
    - type: mrr_at_5
      value: 84.013
    - type: ndcg_at_1
      value: 77.53
    - type: ndcg_at_10
      value: 85.277
    - type: ndcg_at_100
      value: 86.80499999999999
    - type: ndcg_at_1000
      value: 87.01
    - type: ndcg_at_3
      value: 81.975
    - type: ndcg_at_5
      value: 83.723
    - type: precision_at_1
      value: 77.53
    - type: precision_at_10
      value: 12.961
    - type: precision_at_100
      value: 1.502
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 35.713
    - type: precision_at_5
      value: 23.574
    - type: recall_at_1
      value: 67.51700000000001
    - type: recall_at_10
      value: 93.486
    - type: recall_at_100
      value: 98.9
    - type: recall_at_1000
      value: 99.92999999999999
    - type: recall_at_3
      value: 84.17999999999999
    - type: recall_at_5
      value: 88.97500000000001
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
      value: 48.225994608749915
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
      value: 53.17635557157765
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
      value: 3.988
    - type: map_at_10
      value: 9.4
    - type: map_at_100
      value: 10.968
    - type: map_at_1000
      value: 11.257
    - type: map_at_3
      value: 7.123
    - type: map_at_5
      value: 8.221
    - type: mrr_at_1
      value: 19.7
    - type: mrr_at_10
      value: 29.098000000000003
    - type: mrr_at_100
      value: 30.247
    - type: mrr_at_1000
      value: 30.318
    - type: mrr_at_3
      value: 26.55
    - type: mrr_at_5
      value: 27.915
    - type: ndcg_at_1
      value: 19.7
    - type: ndcg_at_10
      value: 16.176
    - type: ndcg_at_100
      value: 22.931
    - type: ndcg_at_1000
      value: 28.301
    - type: ndcg_at_3
      value: 16.142
    - type: ndcg_at_5
      value: 13.633999999999999
    - type: precision_at_1
      value: 19.7
    - type: precision_at_10
      value: 8.18
    - type: precision_at_100
      value: 1.8010000000000002
    - type: precision_at_1000
      value: 0.309
    - type: precision_at_3
      value: 15.1
    - type: precision_at_5
      value: 11.74
    - type: recall_at_1
      value: 3.988
    - type: recall_at_10
      value: 16.625
    - type: recall_at_100
      value: 36.61
    - type: recall_at_1000
      value: 62.805
    - type: recall_at_3
      value: 9.168
    - type: recall_at_5
      value: 11.902
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
      value: 77.29330379162072
    - type: cos_sim_spearman
      value: 67.22953551111448
    - type: euclidean_pearson
      value: 71.44682700059415
    - type: euclidean_spearman
      value: 66.33178012153247
    - type: manhattan_pearson
      value: 71.46941734657887
    - type: manhattan_spearman
      value: 66.43234359835814
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
      value: 75.40943196466576
    - type: cos_sim_spearman
      value: 66.59241013465915
    - type: euclidean_pearson
      value: 71.32500540796616
    - type: euclidean_spearman
      value: 67.86667467202591
    - type: manhattan_pearson
      value: 71.48209832089134
    - type: manhattan_spearman
      value: 67.94511626964879
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
      value: 77.08302398877518
    - type: cos_sim_spearman
      value: 77.33151317062642
    - type: euclidean_pearson
      value: 76.77020279715008
    - type: euclidean_spearman
      value: 77.13893776083225
    - type: manhattan_pearson
      value: 76.76732290707477
    - type: manhattan_spearman
      value: 77.14500877396631
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
      value: 77.46886184932168
    - type: cos_sim_spearman
      value: 71.82815265534886
    - type: euclidean_pearson
      value: 75.19783284299076
    - type: euclidean_spearman
      value: 71.36479611710412
    - type: manhattan_pearson
      value: 75.30375233959337
    - type: manhattan_spearman
      value: 71.46280266488021
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
      value: 80.093017609484
    - type: cos_sim_spearman
      value: 80.65931167868882
    - type: euclidean_pearson
      value: 80.36786337117047
    - type: euclidean_spearman
      value: 81.30521389642827
    - type: manhattan_pearson
      value: 80.37922433220973
    - type: manhattan_spearman
      value: 81.30496664496285
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
      value: 77.98998347238742
    - type: cos_sim_spearman
      value: 78.91151365939403
    - type: euclidean_pearson
      value: 76.40510899217841
    - type: euclidean_spearman
      value: 76.8551459824213
    - type: manhattan_pearson
      value: 76.3986079603294
    - type: manhattan_spearman
      value: 76.8848053254288
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
      value: 85.63510653472044
    - type: cos_sim_spearman
      value: 86.98674844768605
    - type: euclidean_pearson
      value: 85.205080538809
    - type: euclidean_spearman
      value: 85.53630494151886
    - type: manhattan_pearson
      value: 85.48612469885626
    - type: manhattan_spearman
      value: 85.81741413931921
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
      value: 66.7257987615171
    - type: cos_sim_spearman
      value: 67.30387805090024
    - type: euclidean_pearson
      value: 69.46877227885867
    - type: euclidean_spearman
      value: 69.33161798704344
    - type: manhattan_pearson
      value: 69.82773311626424
    - type: manhattan_spearman
      value: 69.57199940498796
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
      value: 79.37322139418472
    - type: cos_sim_spearman
      value: 77.5887175717799
    - type: euclidean_pearson
      value: 78.23006410562164
    - type: euclidean_spearman
      value: 77.18470385673044
    - type: manhattan_pearson
      value: 78.40868369362455
    - type: manhattan_spearman
      value: 77.36675823897656
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
      value: 77.21233007730808
    - type: mrr
      value: 93.0502386139641
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
      value: 54.567
    - type: map_at_10
      value: 63.653000000000006
    - type: map_at_100
      value: 64.282
    - type: map_at_1000
      value: 64.31099999999999
    - type: map_at_3
      value: 60.478
    - type: map_at_5
      value: 62.322
    - type: mrr_at_1
      value: 56.99999999999999
    - type: mrr_at_10
      value: 64.759
    - type: mrr_at_100
      value: 65.274
    - type: mrr_at_1000
      value: 65.301
    - type: mrr_at_3
      value: 62.333000000000006
    - type: mrr_at_5
      value: 63.817
    - type: ndcg_at_1
      value: 56.99999999999999
    - type: ndcg_at_10
      value: 68.28699999999999
    - type: ndcg_at_100
      value: 70.98400000000001
    - type: ndcg_at_1000
      value: 71.695
    - type: ndcg_at_3
      value: 62.656
    - type: ndcg_at_5
      value: 65.523
    - type: precision_at_1
      value: 56.99999999999999
    - type: precision_at_10
      value: 9.232999999999999
    - type: precision_at_100
      value: 1.0630000000000002
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 24.221999999999998
    - type: precision_at_5
      value: 16.333000000000002
    - type: recall_at_1
      value: 54.567
    - type: recall_at_10
      value: 81.45599999999999
    - type: recall_at_100
      value: 93.5
    - type: recall_at_1000
      value: 99.0
    - type: recall_at_3
      value: 66.228
    - type: recall_at_5
      value: 73.489
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
      value: 99.74455445544554
    - type: cos_sim_ap
      value: 92.57836032673468
    - type: cos_sim_f1
      value: 87.0471464019851
    - type: cos_sim_precision
      value: 86.4039408866995
    - type: cos_sim_recall
      value: 87.7
    - type: dot_accuracy
      value: 99.56039603960396
    - type: dot_ap
      value: 82.47233353407186
    - type: dot_f1
      value: 76.78207739307537
    - type: dot_precision
      value: 78.21576763485477
    - type: dot_recall
      value: 75.4
    - type: euclidean_accuracy
      value: 99.73069306930694
    - type: euclidean_ap
      value: 91.70507666665775
    - type: euclidean_f1
      value: 86.26262626262626
    - type: euclidean_precision
      value: 87.14285714285714
    - type: euclidean_recall
      value: 85.39999999999999
    - type: manhattan_accuracy
      value: 99.73861386138614
    - type: manhattan_ap
      value: 91.96809459281754
    - type: manhattan_f1
      value: 86.6
    - type: manhattan_precision
      value: 86.6
    - type: manhattan_recall
      value: 86.6
    - type: max_accuracy
      value: 99.74455445544554
    - type: max_ap
      value: 92.57836032673468
    - type: max_f1
      value: 87.0471464019851
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
      value: 60.85593925770172
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
      value: 32.356772998237496
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
      value: 49.320607035290735
    - type: mrr
      value: 50.09196481622952
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
      value: 31.17573968015504
    - type: cos_sim_spearman
      value: 30.43371643155132
    - type: dot_pearson
      value: 30.164319483092744
    - type: dot_spearman
      value: 29.207082242868754
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
      value: 0.22100000000000003
    - type: map_at_10
      value: 1.7229999999999999
    - type: map_at_100
      value: 9.195
    - type: map_at_1000
      value: 21.999
    - type: map_at_3
      value: 0.6479999999999999
    - type: map_at_5
      value: 0.964
    - type: mrr_at_1
      value: 86.0
    - type: mrr_at_10
      value: 90.667
    - type: mrr_at_100
      value: 90.858
    - type: mrr_at_1000
      value: 90.858
    - type: mrr_at_3
      value: 90.667
    - type: mrr_at_5
      value: 90.667
    - type: ndcg_at_1
      value: 82.0
    - type: ndcg_at_10
      value: 72.98
    - type: ndcg_at_100
      value: 52.868
    - type: ndcg_at_1000
      value: 46.541
    - type: ndcg_at_3
      value: 80.39699999999999
    - type: ndcg_at_5
      value: 76.303
    - type: precision_at_1
      value: 86.0
    - type: precision_at_10
      value: 75.8
    - type: precision_at_100
      value: 53.5
    - type: precision_at_1000
      value: 20.946
    - type: precision_at_3
      value: 85.333
    - type: precision_at_5
      value: 79.2
    - type: recall_at_1
      value: 0.22100000000000003
    - type: recall_at_10
      value: 1.9109999999999998
    - type: recall_at_100
      value: 12.437
    - type: recall_at_1000
      value: 43.606
    - type: recall_at_3
      value: 0.681
    - type: recall_at_5
      value: 1.023
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
      value: 2.5
    - type: map_at_10
      value: 9.568999999999999
    - type: map_at_100
      value: 15.653
    - type: map_at_1000
      value: 17.188
    - type: map_at_3
      value: 5.335999999999999
    - type: map_at_5
      value: 6.522
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 49.184
    - type: mrr_at_100
      value: 50.512
    - type: mrr_at_1000
      value: 50.512
    - type: mrr_at_3
      value: 46.259
    - type: mrr_at_5
      value: 48.299
    - type: ndcg_at_1
      value: 30.612000000000002
    - type: ndcg_at_10
      value: 24.45
    - type: ndcg_at_100
      value: 35.870999999999995
    - type: ndcg_at_1000
      value: 47.272999999999996
    - type: ndcg_at_3
      value: 28.528
    - type: ndcg_at_5
      value: 25.768
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 21.429000000000002
    - type: precision_at_100
      value: 7.265000000000001
    - type: precision_at_1000
      value: 1.504
    - type: precision_at_3
      value: 29.252
    - type: precision_at_5
      value: 24.898
    - type: recall_at_1
      value: 2.5
    - type: recall_at_10
      value: 15.844
    - type: recall_at_100
      value: 45.469
    - type: recall_at_1000
      value: 81.148
    - type: recall_at_3
      value: 6.496
    - type: recall_at_5
      value: 8.790000000000001
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
      value: 68.7272
    - type: ap
      value: 13.156450706152686
    - type: f1
      value: 52.814703437064395
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
      value: 55.6677985285795
    - type: f1
      value: 55.9373937514999
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
      value: 40.05809562275603
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
      value: 82.76807534124099
    - type: cos_sim_ap
      value: 62.37052608803734
    - type: cos_sim_f1
      value: 59.077414934916646
    - type: cos_sim_precision
      value: 52.07326892109501
    - type: cos_sim_recall
      value: 68.25857519788919
    - type: dot_accuracy
      value: 80.56267509089825
    - type: dot_ap
      value: 54.75349561321037
    - type: dot_f1
      value: 54.75483794372552
    - type: dot_precision
      value: 49.77336499028707
    - type: dot_recall
      value: 60.844327176781
    - type: euclidean_accuracy
      value: 82.476008821601
    - type: euclidean_ap
      value: 61.17417554210511
    - type: euclidean_f1
      value: 57.80318696022382
    - type: euclidean_precision
      value: 53.622207176709544
    - type: euclidean_recall
      value: 62.69129287598945
    - type: manhattan_accuracy
      value: 82.48792990403528
    - type: manhattan_ap
      value: 61.044816292966544
    - type: manhattan_f1
      value: 58.03033951360462
    - type: manhattan_precision
      value: 53.36581045172719
    - type: manhattan_recall
      value: 63.58839050131926
    - type: max_accuracy
      value: 82.76807534124099
    - type: max_ap
      value: 62.37052608803734
    - type: max_f1
      value: 59.077414934916646
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
      value: 87.97881010594946
    - type: cos_sim_ap
      value: 83.78748636891035
    - type: cos_sim_f1
      value: 75.94113995691386
    - type: cos_sim_precision
      value: 72.22029307590805
    - type: cos_sim_recall
      value: 80.06621496766245
    - type: dot_accuracy
      value: 85.69294058291614
    - type: dot_ap
      value: 78.15363722278026
    - type: dot_f1
      value: 72.08894926888564
    - type: dot_precision
      value: 67.28959487419075
    - type: dot_recall
      value: 77.62550046196489
    - type: euclidean_accuracy
      value: 87.73625179493149
    - type: euclidean_ap
      value: 83.19012184470559
    - type: euclidean_f1
      value: 75.5148064623461
    - type: euclidean_precision
      value: 72.63352535381551
    - type: euclidean_recall
      value: 78.6341238065907
    - type: manhattan_accuracy
      value: 87.74013272790779
    - type: manhattan_ap
      value: 83.23305405113403
    - type: manhattan_f1
      value: 75.63960775639607
    - type: manhattan_precision
      value: 72.563304569246
    - type: manhattan_recall
      value: 78.9882968894364
    - type: max_accuracy
      value: 87.97881010594946
    - type: max_ap
      value: 83.78748636891035
    - type: max_f1
      value: 75.94113995691386
---

# SGPT-1.3B-weightedmean-msmarco-specb-bitfit

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to the eval folder or our paper: https://arxiv.org/abs/2202.08904

## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 62398 with parameters:
```
{'batch_size': 8, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
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
  (1): Pooling({'word_embedding_dimension': 2048, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': True, 'pooling_mode_lasttoken': False})
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
