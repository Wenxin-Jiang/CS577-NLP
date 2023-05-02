---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: SGPT-2.7B-weightedmean-msmarco-specb-bitfit
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
      value: 67.56716417910448
    - type: ap
      value: 30.75574629595259
    - type: f1
      value: 61.805121301858655
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
      value: 71.439575
    - type: ap
      value: 65.91341330532453
    - type: f1
      value: 70.90561852619555
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
      value: 35.748000000000005
    - type: f1
      value: 35.48576287186347
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
      value: 25.96
    - type: map_at_10
      value: 41.619
    - type: map_at_100
      value: 42.673
    - type: map_at_1000
      value: 42.684
    - type: map_at_3
      value: 36.569
    - type: map_at_5
      value: 39.397
    - type: mrr_at_1
      value: 26.316
    - type: mrr_at_10
      value: 41.772
    - type: mrr_at_100
      value: 42.82
    - type: mrr_at_1000
      value: 42.83
    - type: mrr_at_3
      value: 36.724000000000004
    - type: mrr_at_5
      value: 39.528999999999996
    - type: ndcg_at_1
      value: 25.96
    - type: ndcg_at_10
      value: 50.491
    - type: ndcg_at_100
      value: 54.864999999999995
    - type: ndcg_at_1000
      value: 55.10699999999999
    - type: ndcg_at_3
      value: 40.053
    - type: ndcg_at_5
      value: 45.134
    - type: precision_at_1
      value: 25.96
    - type: precision_at_10
      value: 7.8950000000000005
    - type: precision_at_100
      value: 0.9780000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 16.714000000000002
    - type: precision_at_5
      value: 12.489
    - type: recall_at_1
      value: 25.96
    - type: recall_at_10
      value: 78.947
    - type: recall_at_100
      value: 97.795
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 50.141999999999996
    - type: recall_at_5
      value: 62.446999999999996
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
      value: 44.72125714642202
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
      value: 35.081451519142064
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
      value: 59.634661990392054
    - type: mrr
      value: 73.6813525040672
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
      value: 87.42754550496836
    - type: cos_sim_spearman
      value: 84.84289705838664
    - type: euclidean_pearson
      value: 85.59331970450859
    - type: euclidean_spearman
      value: 85.8525586184271
    - type: manhattan_pearson
      value: 85.41233134466698
    - type: manhattan_spearman
      value: 85.52303303767404
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
      value: 83.21753246753246
    - type: f1
      value: 83.15394543120915
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
      value: 34.41414219680629
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
      value: 30.533275862270028
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
      value: 30.808999999999997
    - type: map_at_10
      value: 40.617
    - type: map_at_100
      value: 41.894999999999996
    - type: map_at_1000
      value: 42.025
    - type: map_at_3
      value: 37.0
    - type: map_at_5
      value: 38.993
    - type: mrr_at_1
      value: 37.482
    - type: mrr_at_10
      value: 46.497
    - type: mrr_at_100
      value: 47.144000000000005
    - type: mrr_at_1000
      value: 47.189
    - type: mrr_at_3
      value: 43.705
    - type: mrr_at_5
      value: 45.193
    - type: ndcg_at_1
      value: 37.482
    - type: ndcg_at_10
      value: 46.688
    - type: ndcg_at_100
      value: 51.726000000000006
    - type: ndcg_at_1000
      value: 53.825
    - type: ndcg_at_3
      value: 41.242000000000004
    - type: ndcg_at_5
      value: 43.657000000000004
    - type: precision_at_1
      value: 37.482
    - type: precision_at_10
      value: 8.827
    - type: precision_at_100
      value: 1.393
    - type: precision_at_1000
      value: 0.186
    - type: precision_at_3
      value: 19.361
    - type: precision_at_5
      value: 14.106
    - type: recall_at_1
      value: 30.808999999999997
    - type: recall_at_10
      value: 58.47
    - type: recall_at_100
      value: 80.51899999999999
    - type: recall_at_1000
      value: 93.809
    - type: recall_at_3
      value: 42.462
    - type: recall_at_5
      value: 49.385
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
      value: 26.962000000000003
    - type: map_at_10
      value: 36.93
    - type: map_at_100
      value: 38.102000000000004
    - type: map_at_1000
      value: 38.22
    - type: map_at_3
      value: 34.065
    - type: map_at_5
      value: 35.72
    - type: mrr_at_1
      value: 33.567
    - type: mrr_at_10
      value: 42.269
    - type: mrr_at_100
      value: 42.99
    - type: mrr_at_1000
      value: 43.033
    - type: mrr_at_3
      value: 40.064
    - type: mrr_at_5
      value: 41.258
    - type: ndcg_at_1
      value: 33.567
    - type: ndcg_at_10
      value: 42.405
    - type: ndcg_at_100
      value: 46.847
    - type: ndcg_at_1000
      value: 48.951
    - type: ndcg_at_3
      value: 38.312000000000005
    - type: ndcg_at_5
      value: 40.242
    - type: precision_at_1
      value: 33.567
    - type: precision_at_10
      value: 8.032
    - type: precision_at_100
      value: 1.295
    - type: precision_at_1000
      value: 0.17600000000000002
    - type: precision_at_3
      value: 18.662
    - type: precision_at_5
      value: 13.299
    - type: recall_at_1
      value: 26.962000000000003
    - type: recall_at_10
      value: 52.489
    - type: recall_at_100
      value: 71.635
    - type: recall_at_1000
      value: 85.141
    - type: recall_at_3
      value: 40.28
    - type: recall_at_5
      value: 45.757
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
      value: 36.318
    - type: map_at_10
      value: 47.97
    - type: map_at_100
      value: 49.003
    - type: map_at_1000
      value: 49.065999999999995
    - type: map_at_3
      value: 45.031
    - type: map_at_5
      value: 46.633
    - type: mrr_at_1
      value: 41.504999999999995
    - type: mrr_at_10
      value: 51.431000000000004
    - type: mrr_at_100
      value: 52.129000000000005
    - type: mrr_at_1000
      value: 52.161
    - type: mrr_at_3
      value: 48.934
    - type: mrr_at_5
      value: 50.42
    - type: ndcg_at_1
      value: 41.504999999999995
    - type: ndcg_at_10
      value: 53.676
    - type: ndcg_at_100
      value: 57.867000000000004
    - type: ndcg_at_1000
      value: 59.166
    - type: ndcg_at_3
      value: 48.516
    - type: ndcg_at_5
      value: 50.983999999999995
    - type: precision_at_1
      value: 41.504999999999995
    - type: precision_at_10
      value: 8.608
    - type: precision_at_100
      value: 1.1560000000000001
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 21.462999999999997
    - type: precision_at_5
      value: 14.721
    - type: recall_at_1
      value: 36.318
    - type: recall_at_10
      value: 67.066
    - type: recall_at_100
      value: 85.34
    - type: recall_at_1000
      value: 94.491
    - type: recall_at_3
      value: 53.215999999999994
    - type: recall_at_5
      value: 59.214
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
      value: 22.167
    - type: map_at_10
      value: 29.543999999999997
    - type: map_at_100
      value: 30.579
    - type: map_at_1000
      value: 30.669999999999998
    - type: map_at_3
      value: 26.982
    - type: map_at_5
      value: 28.474
    - type: mrr_at_1
      value: 24.068
    - type: mrr_at_10
      value: 31.237
    - type: mrr_at_100
      value: 32.222
    - type: mrr_at_1000
      value: 32.292
    - type: mrr_at_3
      value: 28.776000000000003
    - type: mrr_at_5
      value: 30.233999999999998
    - type: ndcg_at_1
      value: 24.068
    - type: ndcg_at_10
      value: 33.973
    - type: ndcg_at_100
      value: 39.135
    - type: ndcg_at_1000
      value: 41.443999999999996
    - type: ndcg_at_3
      value: 29.018
    - type: ndcg_at_5
      value: 31.558999999999997
    - type: precision_at_1
      value: 24.068
    - type: precision_at_10
      value: 5.299
    - type: precision_at_100
      value: 0.823
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 12.166
    - type: precision_at_5
      value: 8.767999999999999
    - type: recall_at_1
      value: 22.167
    - type: recall_at_10
      value: 46.115
    - type: recall_at_100
      value: 69.867
    - type: recall_at_1000
      value: 87.234
    - type: recall_at_3
      value: 32.798
    - type: recall_at_5
      value: 38.951
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
      value: 12.033000000000001
    - type: map_at_10
      value: 19.314
    - type: map_at_100
      value: 20.562
    - type: map_at_1000
      value: 20.695
    - type: map_at_3
      value: 16.946
    - type: map_at_5
      value: 18.076999999999998
    - type: mrr_at_1
      value: 14.801
    - type: mrr_at_10
      value: 22.74
    - type: mrr_at_100
      value: 23.876
    - type: mrr_at_1000
      value: 23.949
    - type: mrr_at_3
      value: 20.211000000000002
    - type: mrr_at_5
      value: 21.573
    - type: ndcg_at_1
      value: 14.801
    - type: ndcg_at_10
      value: 24.038
    - type: ndcg_at_100
      value: 30.186
    - type: ndcg_at_1000
      value: 33.321
    - type: ndcg_at_3
      value: 19.431
    - type: ndcg_at_5
      value: 21.34
    - type: precision_at_1
      value: 14.801
    - type: precision_at_10
      value: 4.776
    - type: precision_at_100
      value: 0.897
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 9.66
    - type: precision_at_5
      value: 7.239
    - type: recall_at_1
      value: 12.033000000000001
    - type: recall_at_10
      value: 35.098
    - type: recall_at_100
      value: 62.175000000000004
    - type: recall_at_1000
      value: 84.17099999999999
    - type: recall_at_3
      value: 22.61
    - type: recall_at_5
      value: 27.278999999999996
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
      value: 26.651000000000003
    - type: map_at_10
      value: 36.901
    - type: map_at_100
      value: 38.249
    - type: map_at_1000
      value: 38.361000000000004
    - type: map_at_3
      value: 33.891
    - type: map_at_5
      value: 35.439
    - type: mrr_at_1
      value: 32.724
    - type: mrr_at_10
      value: 42.504
    - type: mrr_at_100
      value: 43.391999999999996
    - type: mrr_at_1000
      value: 43.436
    - type: mrr_at_3
      value: 39.989999999999995
    - type: mrr_at_5
      value: 41.347
    - type: ndcg_at_1
      value: 32.724
    - type: ndcg_at_10
      value: 43.007
    - type: ndcg_at_100
      value: 48.601
    - type: ndcg_at_1000
      value: 50.697
    - type: ndcg_at_3
      value: 37.99
    - type: ndcg_at_5
      value: 40.083999999999996
    - type: precision_at_1
      value: 32.724
    - type: precision_at_10
      value: 7.872999999999999
    - type: precision_at_100
      value: 1.247
    - type: precision_at_1000
      value: 0.16199999999999998
    - type: precision_at_3
      value: 18.062
    - type: precision_at_5
      value: 12.666
    - type: recall_at_1
      value: 26.651000000000003
    - type: recall_at_10
      value: 55.674
    - type: recall_at_100
      value: 78.904
    - type: recall_at_1000
      value: 92.55799999999999
    - type: recall_at_3
      value: 41.36
    - type: recall_at_5
      value: 46.983999999999995
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
      value: 22.589000000000002
    - type: map_at_10
      value: 32.244
    - type: map_at_100
      value: 33.46
    - type: map_at_1000
      value: 33.593
    - type: map_at_3
      value: 29.21
    - type: map_at_5
      value: 31.019999999999996
    - type: mrr_at_1
      value: 28.425
    - type: mrr_at_10
      value: 37.282
    - type: mrr_at_100
      value: 38.187
    - type: mrr_at_1000
      value: 38.248
    - type: mrr_at_3
      value: 34.684
    - type: mrr_at_5
      value: 36.123
    - type: ndcg_at_1
      value: 28.425
    - type: ndcg_at_10
      value: 37.942
    - type: ndcg_at_100
      value: 43.443
    - type: ndcg_at_1000
      value: 45.995999999999995
    - type: ndcg_at_3
      value: 32.873999999999995
    - type: ndcg_at_5
      value: 35.325
    - type: precision_at_1
      value: 28.425
    - type: precision_at_10
      value: 7.1
    - type: precision_at_100
      value: 1.166
    - type: precision_at_1000
      value: 0.158
    - type: precision_at_3
      value: 16.02
    - type: precision_at_5
      value: 11.644
    - type: recall_at_1
      value: 22.589000000000002
    - type: recall_at_10
      value: 50.03999999999999
    - type: recall_at_100
      value: 73.973
    - type: recall_at_1000
      value: 91.128
    - type: recall_at_3
      value: 35.882999999999996
    - type: recall_at_5
      value: 42.187999999999995
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
      value: 23.190833333333334
    - type: map_at_10
      value: 31.504916666666666
    - type: map_at_100
      value: 32.64908333333334
    - type: map_at_1000
      value: 32.77075
    - type: map_at_3
      value: 28.82575
    - type: map_at_5
      value: 30.2755
    - type: mrr_at_1
      value: 27.427499999999995
    - type: mrr_at_10
      value: 35.36483333333334
    - type: mrr_at_100
      value: 36.23441666666666
    - type: mrr_at_1000
      value: 36.297583333333336
    - type: mrr_at_3
      value: 32.97966666666667
    - type: mrr_at_5
      value: 34.294583333333335
    - type: ndcg_at_1
      value: 27.427499999999995
    - type: ndcg_at_10
      value: 36.53358333333333
    - type: ndcg_at_100
      value: 41.64508333333333
    - type: ndcg_at_1000
      value: 44.14499999999999
    - type: ndcg_at_3
      value: 31.88908333333333
    - type: ndcg_at_5
      value: 33.98433333333333
    - type: precision_at_1
      value: 27.427499999999995
    - type: precision_at_10
      value: 6.481083333333333
    - type: precision_at_100
      value: 1.0610833333333334
    - type: precision_at_1000
      value: 0.14691666666666667
    - type: precision_at_3
      value: 14.656749999999999
    - type: precision_at_5
      value: 10.493583333333332
    - type: recall_at_1
      value: 23.190833333333334
    - type: recall_at_10
      value: 47.65175
    - type: recall_at_100
      value: 70.41016666666667
    - type: recall_at_1000
      value: 87.82708333333332
    - type: recall_at_3
      value: 34.637583333333325
    - type: recall_at_5
      value: 40.05008333333333
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
      value: 20.409
    - type: map_at_10
      value: 26.794
    - type: map_at_100
      value: 27.682000000000002
    - type: map_at_1000
      value: 27.783
    - type: map_at_3
      value: 24.461
    - type: map_at_5
      value: 25.668000000000003
    - type: mrr_at_1
      value: 22.853
    - type: mrr_at_10
      value: 29.296
    - type: mrr_at_100
      value: 30.103
    - type: mrr_at_1000
      value: 30.179000000000002
    - type: mrr_at_3
      value: 27.173000000000002
    - type: mrr_at_5
      value: 28.223
    - type: ndcg_at_1
      value: 22.853
    - type: ndcg_at_10
      value: 31.007
    - type: ndcg_at_100
      value: 35.581
    - type: ndcg_at_1000
      value: 38.147
    - type: ndcg_at_3
      value: 26.590999999999998
    - type: ndcg_at_5
      value: 28.43
    - type: precision_at_1
      value: 22.853
    - type: precision_at_10
      value: 5.031
    - type: precision_at_100
      value: 0.7939999999999999
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_3
      value: 11.401
    - type: precision_at_5
      value: 8.16
    - type: recall_at_1
      value: 20.409
    - type: recall_at_10
      value: 41.766
    - type: recall_at_100
      value: 62.964
    - type: recall_at_1000
      value: 81.682
    - type: recall_at_3
      value: 29.281000000000002
    - type: recall_at_5
      value: 33.83
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
      value: 14.549000000000001
    - type: map_at_10
      value: 20.315
    - type: map_at_100
      value: 21.301000000000002
    - type: map_at_1000
      value: 21.425
    - type: map_at_3
      value: 18.132
    - type: map_at_5
      value: 19.429
    - type: mrr_at_1
      value: 17.86
    - type: mrr_at_10
      value: 23.860999999999997
    - type: mrr_at_100
      value: 24.737000000000002
    - type: mrr_at_1000
      value: 24.82
    - type: mrr_at_3
      value: 21.685
    - type: mrr_at_5
      value: 23.008
    - type: ndcg_at_1
      value: 17.86
    - type: ndcg_at_10
      value: 24.396
    - type: ndcg_at_100
      value: 29.328
    - type: ndcg_at_1000
      value: 32.486
    - type: ndcg_at_3
      value: 20.375
    - type: ndcg_at_5
      value: 22.411
    - type: precision_at_1
      value: 17.86
    - type: precision_at_10
      value: 4.47
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.125
    - type: precision_at_3
      value: 9.475
    - type: precision_at_5
      value: 7.170999999999999
    - type: recall_at_1
      value: 14.549000000000001
    - type: recall_at_10
      value: 33.365
    - type: recall_at_100
      value: 55.797
    - type: recall_at_1000
      value: 78.632
    - type: recall_at_3
      value: 22.229
    - type: recall_at_5
      value: 27.339000000000002
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
      value: 23.286
    - type: map_at_10
      value: 30.728
    - type: map_at_100
      value: 31.840000000000003
    - type: map_at_1000
      value: 31.953
    - type: map_at_3
      value: 28.302
    - type: map_at_5
      value: 29.615000000000002
    - type: mrr_at_1
      value: 27.239
    - type: mrr_at_10
      value: 34.408
    - type: mrr_at_100
      value: 35.335
    - type: mrr_at_1000
      value: 35.405
    - type: mrr_at_3
      value: 32.151999999999994
    - type: mrr_at_5
      value: 33.355000000000004
    - type: ndcg_at_1
      value: 27.239
    - type: ndcg_at_10
      value: 35.324
    - type: ndcg_at_100
      value: 40.866
    - type: ndcg_at_1000
      value: 43.584
    - type: ndcg_at_3
      value: 30.898999999999997
    - type: ndcg_at_5
      value: 32.812999999999995
    - type: precision_at_1
      value: 27.239
    - type: precision_at_10
      value: 5.896
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 13.713000000000001
    - type: precision_at_5
      value: 9.683
    - type: recall_at_1
      value: 23.286
    - type: recall_at_10
      value: 45.711
    - type: recall_at_100
      value: 70.611
    - type: recall_at_1000
      value: 90.029
    - type: recall_at_3
      value: 33.615
    - type: recall_at_5
      value: 38.41
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
      value: 23.962
    - type: map_at_10
      value: 31.942999999999998
    - type: map_at_100
      value: 33.384
    - type: map_at_1000
      value: 33.611000000000004
    - type: map_at_3
      value: 29.243000000000002
    - type: map_at_5
      value: 30.446
    - type: mrr_at_1
      value: 28.458
    - type: mrr_at_10
      value: 36.157000000000004
    - type: mrr_at_100
      value: 37.092999999999996
    - type: mrr_at_1000
      value: 37.163000000000004
    - type: mrr_at_3
      value: 33.86
    - type: mrr_at_5
      value: 35.086
    - type: ndcg_at_1
      value: 28.458
    - type: ndcg_at_10
      value: 37.201
    - type: ndcg_at_100
      value: 42.591
    - type: ndcg_at_1000
      value: 45.539
    - type: ndcg_at_3
      value: 32.889
    - type: ndcg_at_5
      value: 34.483000000000004
    - type: precision_at_1
      value: 28.458
    - type: precision_at_10
      value: 7.332
    - type: precision_at_100
      value: 1.437
    - type: precision_at_1000
      value: 0.233
    - type: precision_at_3
      value: 15.547
    - type: precision_at_5
      value: 11.146
    - type: recall_at_1
      value: 23.962
    - type: recall_at_10
      value: 46.751
    - type: recall_at_100
      value: 71.626
    - type: recall_at_1000
      value: 90.93900000000001
    - type: recall_at_3
      value: 34.138000000000005
    - type: recall_at_5
      value: 38.673
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
      value: 18.555
    - type: map_at_10
      value: 24.759
    - type: map_at_100
      value: 25.732
    - type: map_at_1000
      value: 25.846999999999998
    - type: map_at_3
      value: 22.646
    - type: map_at_5
      value: 23.791999999999998
    - type: mrr_at_1
      value: 20.148
    - type: mrr_at_10
      value: 26.695999999999998
    - type: mrr_at_100
      value: 27.605
    - type: mrr_at_1000
      value: 27.695999999999998
    - type: mrr_at_3
      value: 24.522
    - type: mrr_at_5
      value: 25.715
    - type: ndcg_at_1
      value: 20.148
    - type: ndcg_at_10
      value: 28.746
    - type: ndcg_at_100
      value: 33.57
    - type: ndcg_at_1000
      value: 36.584
    - type: ndcg_at_3
      value: 24.532
    - type: ndcg_at_5
      value: 26.484
    - type: precision_at_1
      value: 20.148
    - type: precision_at_10
      value: 4.529
    - type: precision_at_100
      value: 0.736
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_3
      value: 10.351
    - type: precision_at_5
      value: 7.32
    - type: recall_at_1
      value: 18.555
    - type: recall_at_10
      value: 39.275999999999996
    - type: recall_at_100
      value: 61.511
    - type: recall_at_1000
      value: 84.111
    - type: recall_at_3
      value: 27.778999999999996
    - type: recall_at_5
      value: 32.591
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
      value: 10.366999999999999
    - type: map_at_10
      value: 18.953999999999997
    - type: map_at_100
      value: 20.674999999999997
    - type: map_at_1000
      value: 20.868000000000002
    - type: map_at_3
      value: 15.486
    - type: map_at_5
      value: 17.347
    - type: mrr_at_1
      value: 23.257
    - type: mrr_at_10
      value: 35.419
    - type: mrr_at_100
      value: 36.361
    - type: mrr_at_1000
      value: 36.403
    - type: mrr_at_3
      value: 31.747999999999998
    - type: mrr_at_5
      value: 34.077
    - type: ndcg_at_1
      value: 23.257
    - type: ndcg_at_10
      value: 27.11
    - type: ndcg_at_100
      value: 33.981
    - type: ndcg_at_1000
      value: 37.444
    - type: ndcg_at_3
      value: 21.471999999999998
    - type: ndcg_at_5
      value: 23.769000000000002
    - type: precision_at_1
      value: 23.257
    - type: precision_at_10
      value: 8.704
    - type: precision_at_100
      value: 1.606
    - type: precision_at_1000
      value: 0.22499999999999998
    - type: precision_at_3
      value: 16.287
    - type: precision_at_5
      value: 13.068
    - type: recall_at_1
      value: 10.366999999999999
    - type: recall_at_10
      value: 33.706
    - type: recall_at_100
      value: 57.375
    - type: recall_at_1000
      value: 76.79
    - type: recall_at_3
      value: 20.18
    - type: recall_at_5
      value: 26.215
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
      value: 8.246
    - type: map_at_10
      value: 15.979
    - type: map_at_100
      value: 21.025
    - type: map_at_1000
      value: 22.189999999999998
    - type: map_at_3
      value: 11.997
    - type: map_at_5
      value: 13.697000000000001
    - type: mrr_at_1
      value: 60.75000000000001
    - type: mrr_at_10
      value: 68.70100000000001
    - type: mrr_at_100
      value: 69.1
    - type: mrr_at_1000
      value: 69.111
    - type: mrr_at_3
      value: 66.583
    - type: mrr_at_5
      value: 67.87100000000001
    - type: ndcg_at_1
      value: 49.75
    - type: ndcg_at_10
      value: 34.702
    - type: ndcg_at_100
      value: 37.607
    - type: ndcg_at_1000
      value: 44.322
    - type: ndcg_at_3
      value: 39.555
    - type: ndcg_at_5
      value: 36.684
    - type: precision_at_1
      value: 60.75000000000001
    - type: precision_at_10
      value: 26.625
    - type: precision_at_100
      value: 7.969999999999999
    - type: precision_at_1000
      value: 1.678
    - type: precision_at_3
      value: 41.833
    - type: precision_at_5
      value: 34.5
    - type: recall_at_1
      value: 8.246
    - type: recall_at_10
      value: 20.968
    - type: recall_at_100
      value: 42.065000000000005
    - type: recall_at_1000
      value: 63.671
    - type: recall_at_3
      value: 13.039000000000001
    - type: recall_at_5
      value: 16.042
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
      value: 49.214999999999996
    - type: f1
      value: 44.85952451163755
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
      value: 56.769000000000005
    - type: map_at_10
      value: 67.30199999999999
    - type: map_at_100
      value: 67.692
    - type: map_at_1000
      value: 67.712
    - type: map_at_3
      value: 65.346
    - type: map_at_5
      value: 66.574
    - type: mrr_at_1
      value: 61.370999999999995
    - type: mrr_at_10
      value: 71.875
    - type: mrr_at_100
      value: 72.195
    - type: mrr_at_1000
      value: 72.206
    - type: mrr_at_3
      value: 70.04
    - type: mrr_at_5
      value: 71.224
    - type: ndcg_at_1
      value: 61.370999999999995
    - type: ndcg_at_10
      value: 72.731
    - type: ndcg_at_100
      value: 74.468
    - type: ndcg_at_1000
      value: 74.91600000000001
    - type: ndcg_at_3
      value: 69.077
    - type: ndcg_at_5
      value: 71.111
    - type: precision_at_1
      value: 61.370999999999995
    - type: precision_at_10
      value: 9.325999999999999
    - type: precision_at_100
      value: 1.03
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_3
      value: 27.303
    - type: precision_at_5
      value: 17.525
    - type: recall_at_1
      value: 56.769000000000005
    - type: recall_at_10
      value: 85.06
    - type: recall_at_100
      value: 92.767
    - type: recall_at_1000
      value: 95.933
    - type: recall_at_3
      value: 75.131
    - type: recall_at_5
      value: 80.17
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
      value: 15.753
    - type: map_at_10
      value: 25.875999999999998
    - type: map_at_100
      value: 27.415
    - type: map_at_1000
      value: 27.590999999999998
    - type: map_at_3
      value: 22.17
    - type: map_at_5
      value: 24.236
    - type: mrr_at_1
      value: 31.019000000000002
    - type: mrr_at_10
      value: 39.977000000000004
    - type: mrr_at_100
      value: 40.788999999999994
    - type: mrr_at_1000
      value: 40.832
    - type: mrr_at_3
      value: 37.088
    - type: mrr_at_5
      value: 38.655
    - type: ndcg_at_1
      value: 31.019000000000002
    - type: ndcg_at_10
      value: 33.286
    - type: ndcg_at_100
      value: 39.528999999999996
    - type: ndcg_at_1000
      value: 42.934
    - type: ndcg_at_3
      value: 29.29
    - type: ndcg_at_5
      value: 30.615
    - type: precision_at_1
      value: 31.019000000000002
    - type: precision_at_10
      value: 9.383
    - type: precision_at_100
      value: 1.6019999999999999
    - type: precision_at_1000
      value: 0.22200000000000003
    - type: precision_at_3
      value: 19.753
    - type: precision_at_5
      value: 14.815000000000001
    - type: recall_at_1
      value: 15.753
    - type: recall_at_10
      value: 40.896
    - type: recall_at_100
      value: 64.443
    - type: recall_at_1000
      value: 85.218
    - type: recall_at_3
      value: 26.526
    - type: recall_at_5
      value: 32.452999999999996
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
      value: 32.153999999999996
    - type: map_at_10
      value: 43.651
    - type: map_at_100
      value: 44.41
    - type: map_at_1000
      value: 44.487
    - type: map_at_3
      value: 41.239
    - type: map_at_5
      value: 42.659000000000006
    - type: mrr_at_1
      value: 64.30799999999999
    - type: mrr_at_10
      value: 71.22500000000001
    - type: mrr_at_100
      value: 71.57
    - type: mrr_at_1000
      value: 71.59100000000001
    - type: mrr_at_3
      value: 69.95
    - type: mrr_at_5
      value: 70.738
    - type: ndcg_at_1
      value: 64.30799999999999
    - type: ndcg_at_10
      value: 52.835
    - type: ndcg_at_100
      value: 55.840999999999994
    - type: ndcg_at_1000
      value: 57.484
    - type: ndcg_at_3
      value: 49.014
    - type: ndcg_at_5
      value: 51.01599999999999
    - type: precision_at_1
      value: 64.30799999999999
    - type: precision_at_10
      value: 10.77
    - type: precision_at_100
      value: 1.315
    - type: precision_at_1000
      value: 0.153
    - type: precision_at_3
      value: 30.223
    - type: precision_at_5
      value: 19.716
    - type: recall_at_1
      value: 32.153999999999996
    - type: recall_at_10
      value: 53.849000000000004
    - type: recall_at_100
      value: 65.75999999999999
    - type: recall_at_1000
      value: 76.705
    - type: recall_at_3
      value: 45.334
    - type: recall_at_5
      value: 49.291000000000004
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
      value: 63.5316
    - type: ap
      value: 58.90084300359825
    - type: f1
      value: 63.35727889030892
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
      value: 20.566000000000003
    - type: map_at_10
      value: 32.229
    - type: map_at_100
      value: 33.445
    - type: map_at_1000
      value: 33.501
    - type: map_at_3
      value: 28.504
    - type: map_at_5
      value: 30.681000000000004
    - type: mrr_at_1
      value: 21.218
    - type: mrr_at_10
      value: 32.816
    - type: mrr_at_100
      value: 33.986
    - type: mrr_at_1000
      value: 34.035
    - type: mrr_at_3
      value: 29.15
    - type: mrr_at_5
      value: 31.290000000000003
    - type: ndcg_at_1
      value: 21.218
    - type: ndcg_at_10
      value: 38.832
    - type: ndcg_at_100
      value: 44.743
    - type: ndcg_at_1000
      value: 46.138
    - type: ndcg_at_3
      value: 31.232
    - type: ndcg_at_5
      value: 35.099999999999994
    - type: precision_at_1
      value: 21.218
    - type: precision_at_10
      value: 6.186
    - type: precision_at_100
      value: 0.914
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 13.314
    - type: precision_at_5
      value: 9.943
    - type: recall_at_1
      value: 20.566000000000003
    - type: recall_at_10
      value: 59.192
    - type: recall_at_100
      value: 86.626
    - type: recall_at_1000
      value: 97.283
    - type: recall_at_3
      value: 38.492
    - type: recall_at_5
      value: 47.760000000000005
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
      value: 92.56269949840402
    - type: f1
      value: 92.1020975473988
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
      value: 71.8467852257182
    - type: f1
      value: 53.652719348592015
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
      value: 69.00806993947546
    - type: f1
      value: 67.41429618885515
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
      value: 75.90114324142569
    - type: f1
      value: 76.25183590651454
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
      value: 31.350109978273395
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
      value: 28.768923695767327
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
      value: 31.716396735210754
    - type: mrr
      value: 32.88970538547634
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
      value: 5.604
    - type: map_at_10
      value: 12.379999999999999
    - type: map_at_100
      value: 15.791
    - type: map_at_1000
      value: 17.327
    - type: map_at_3
      value: 9.15
    - type: map_at_5
      value: 10.599
    - type: mrr_at_1
      value: 45.201
    - type: mrr_at_10
      value: 53.374
    - type: mrr_at_100
      value: 54.089
    - type: mrr_at_1000
      value: 54.123
    - type: mrr_at_3
      value: 51.44499999999999
    - type: mrr_at_5
      value: 52.59
    - type: ndcg_at_1
      value: 42.879
    - type: ndcg_at_10
      value: 33.891
    - type: ndcg_at_100
      value: 31.391999999999996
    - type: ndcg_at_1000
      value: 40.36
    - type: ndcg_at_3
      value: 39.076
    - type: ndcg_at_5
      value: 37.047000000000004
    - type: precision_at_1
      value: 44.582
    - type: precision_at_10
      value: 25.294
    - type: precision_at_100
      value: 8.285
    - type: precision_at_1000
      value: 2.1479999999999997
    - type: precision_at_3
      value: 36.120000000000005
    - type: precision_at_5
      value: 31.95
    - type: recall_at_1
      value: 5.604
    - type: recall_at_10
      value: 16.239
    - type: recall_at_100
      value: 32.16
    - type: recall_at_1000
      value: 64.513
    - type: recall_at_3
      value: 10.406
    - type: recall_at_5
      value: 12.684999999999999
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
      value: 25.881
    - type: map_at_10
      value: 39.501
    - type: map_at_100
      value: 40.615
    - type: map_at_1000
      value: 40.661
    - type: map_at_3
      value: 35.559000000000005
    - type: map_at_5
      value: 37.773
    - type: mrr_at_1
      value: 29.229
    - type: mrr_at_10
      value: 41.955999999999996
    - type: mrr_at_100
      value: 42.86
    - type: mrr_at_1000
      value: 42.893
    - type: mrr_at_3
      value: 38.562000000000005
    - type: mrr_at_5
      value: 40.542
    - type: ndcg_at_1
      value: 29.2
    - type: ndcg_at_10
      value: 46.703
    - type: ndcg_at_100
      value: 51.644
    - type: ndcg_at_1000
      value: 52.771
    - type: ndcg_at_3
      value: 39.141999999999996
    - type: ndcg_at_5
      value: 42.892
    - type: precision_at_1
      value: 29.2
    - type: precision_at_10
      value: 7.920000000000001
    - type: precision_at_100
      value: 1.0659999999999998
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 18.105
    - type: precision_at_5
      value: 13.036
    - type: recall_at_1
      value: 25.881
    - type: recall_at_10
      value: 66.266
    - type: recall_at_100
      value: 88.116
    - type: recall_at_1000
      value: 96.58200000000001
    - type: recall_at_3
      value: 46.526
    - type: recall_at_5
      value: 55.154
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
      value: 67.553
    - type: map_at_10
      value: 81.34
    - type: map_at_100
      value: 82.002
    - type: map_at_1000
      value: 82.027
    - type: map_at_3
      value: 78.281
    - type: map_at_5
      value: 80.149
    - type: mrr_at_1
      value: 77.72
    - type: mrr_at_10
      value: 84.733
    - type: mrr_at_100
      value: 84.878
    - type: mrr_at_1000
      value: 84.879
    - type: mrr_at_3
      value: 83.587
    - type: mrr_at_5
      value: 84.32600000000001
    - type: ndcg_at_1
      value: 77.75
    - type: ndcg_at_10
      value: 85.603
    - type: ndcg_at_100
      value: 87.069
    - type: ndcg_at_1000
      value: 87.25
    - type: ndcg_at_3
      value: 82.303
    - type: ndcg_at_5
      value: 84.03699999999999
    - type: precision_at_1
      value: 77.75
    - type: precision_at_10
      value: 13.04
    - type: precision_at_100
      value: 1.5070000000000001
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 35.903
    - type: precision_at_5
      value: 23.738
    - type: recall_at_1
      value: 67.553
    - type: recall_at_10
      value: 93.903
    - type: recall_at_100
      value: 99.062
    - type: recall_at_1000
      value: 99.935
    - type: recall_at_3
      value: 84.58099999999999
    - type: recall_at_5
      value: 89.316
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
      value: 46.46887711230235
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
      value: 54.166876298246926
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
      value: 4.053
    - type: map_at_10
      value: 9.693999999999999
    - type: map_at_100
      value: 11.387
    - type: map_at_1000
      value: 11.654
    - type: map_at_3
      value: 7.053
    - type: map_at_5
      value: 8.439
    - type: mrr_at_1
      value: 19.900000000000002
    - type: mrr_at_10
      value: 29.359
    - type: mrr_at_100
      value: 30.484
    - type: mrr_at_1000
      value: 30.553
    - type: mrr_at_3
      value: 26.200000000000003
    - type: mrr_at_5
      value: 28.115000000000002
    - type: ndcg_at_1
      value: 19.900000000000002
    - type: ndcg_at_10
      value: 16.575
    - type: ndcg_at_100
      value: 23.655
    - type: ndcg_at_1000
      value: 28.853
    - type: ndcg_at_3
      value: 15.848
    - type: ndcg_at_5
      value: 14.026
    - type: precision_at_1
      value: 19.900000000000002
    - type: precision_at_10
      value: 8.450000000000001
    - type: precision_at_100
      value: 1.872
    - type: precision_at_1000
      value: 0.313
    - type: precision_at_3
      value: 14.667
    - type: precision_at_5
      value: 12.32
    - type: recall_at_1
      value: 4.053
    - type: recall_at_10
      value: 17.169999999999998
    - type: recall_at_100
      value: 38.025
    - type: recall_at_1000
      value: 63.571999999999996
    - type: recall_at_3
      value: 8.903
    - type: recall_at_5
      value: 12.477
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
      value: 77.7548748519677
    - type: cos_sim_spearman
      value: 68.19926431966059
    - type: euclidean_pearson
      value: 71.69016204991725
    - type: euclidean_spearman
      value: 66.98099673026834
    - type: manhattan_pearson
      value: 71.62994072488664
    - type: manhattan_spearman
      value: 67.03435950744577
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
      value: 75.91051402657887
    - type: cos_sim_spearman
      value: 66.99390786191645
    - type: euclidean_pearson
      value: 71.54128036454578
    - type: euclidean_spearman
      value: 69.25605675649068
    - type: manhattan_pearson
      value: 71.60981030780171
    - type: manhattan_spearman
      value: 69.27513670128046
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
      value: 77.23835466417793
    - type: cos_sim_spearman
      value: 77.57623085766706
    - type: euclidean_pearson
      value: 77.5090992200725
    - type: euclidean_spearman
      value: 77.88601688144924
    - type: manhattan_pearson
      value: 77.39045060647423
    - type: manhattan_spearman
      value: 77.77552718279098
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
      value: 77.91692485139602
    - type: cos_sim_spearman
      value: 72.78258293483495
    - type: euclidean_pearson
      value: 74.64773017077789
    - type: euclidean_spearman
      value: 71.81662299104619
    - type: manhattan_pearson
      value: 74.71043337995533
    - type: manhattan_spearman
      value: 71.83960860845646
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
      value: 82.13422113617578
    - type: cos_sim_spearman
      value: 82.61707296911949
    - type: euclidean_pearson
      value: 81.42487480400861
    - type: euclidean_spearman
      value: 82.17970991273835
    - type: manhattan_pearson
      value: 81.41985055477845
    - type: manhattan_spearman
      value: 82.15823204362937
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
      value: 79.07989542843826
    - type: cos_sim_spearman
      value: 80.09839524406284
    - type: euclidean_pearson
      value: 76.43186028364195
    - type: euclidean_spearman
      value: 76.76720323266471
    - type: manhattan_pearson
      value: 76.4674747409161
    - type: manhattan_spearman
      value: 76.81797407068667
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
      value: 87.0420983224933
    - type: cos_sim_spearman
      value: 87.25017540413702
    - type: euclidean_pearson
      value: 84.56384596473421
    - type: euclidean_spearman
      value: 84.72557417564886
    - type: manhattan_pearson
      value: 84.7329954474549
    - type: manhattan_spearman
      value: 84.75071371008909
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
      value: 68.47031320016424
    - type: cos_sim_spearman
      value: 68.7486910762485
    - type: euclidean_pearson
      value: 71.30330985913915
    - type: euclidean_spearman
      value: 71.59666258520735
    - type: manhattan_pearson
      value: 71.4423884279027
    - type: manhattan_spearman
      value: 71.67460706861044
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
      value: 80.79514366062675
    - type: cos_sim_spearman
      value: 79.20585637461048
    - type: euclidean_pearson
      value: 78.6591557395699
    - type: euclidean_spearman
      value: 77.86455794285718
    - type: manhattan_pearson
      value: 78.67754806486865
    - type: manhattan_spearman
      value: 77.88178687200732
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
      value: 77.71580844366375
    - type: mrr
      value: 93.04215845882513
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
      value: 56.39999999999999
    - type: map_at_10
      value: 65.701
    - type: map_at_100
      value: 66.32000000000001
    - type: map_at_1000
      value: 66.34100000000001
    - type: map_at_3
      value: 62.641999999999996
    - type: map_at_5
      value: 64.342
    - type: mrr_at_1
      value: 58.667
    - type: mrr_at_10
      value: 66.45299999999999
    - type: mrr_at_100
      value: 66.967
    - type: mrr_at_1000
      value: 66.988
    - type: mrr_at_3
      value: 64.11099999999999
    - type: mrr_at_5
      value: 65.411
    - type: ndcg_at_1
      value: 58.667
    - type: ndcg_at_10
      value: 70.165
    - type: ndcg_at_100
      value: 72.938
    - type: ndcg_at_1000
      value: 73.456
    - type: ndcg_at_3
      value: 64.79
    - type: ndcg_at_5
      value: 67.28
    - type: precision_at_1
      value: 58.667
    - type: precision_at_10
      value: 9.4
    - type: precision_at_100
      value: 1.087
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 24.889
    - type: precision_at_5
      value: 16.667
    - type: recall_at_1
      value: 56.39999999999999
    - type: recall_at_10
      value: 83.122
    - type: recall_at_100
      value: 95.667
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_3
      value: 68.378
    - type: recall_at_5
      value: 74.68299999999999
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
      value: 99.76831683168317
    - type: cos_sim_ap
      value: 93.47124923047998
    - type: cos_sim_f1
      value: 88.06122448979592
    - type: cos_sim_precision
      value: 89.89583333333333
    - type: cos_sim_recall
      value: 86.3
    - type: dot_accuracy
      value: 99.57326732673268
    - type: dot_ap
      value: 84.06577868167207
    - type: dot_f1
      value: 77.82629791363416
    - type: dot_precision
      value: 75.58906691800189
    - type: dot_recall
      value: 80.2
    - type: euclidean_accuracy
      value: 99.74257425742574
    - type: euclidean_ap
      value: 92.1904681653555
    - type: euclidean_f1
      value: 86.74821610601427
    - type: euclidean_precision
      value: 88.46153846153845
    - type: euclidean_recall
      value: 85.1
    - type: manhattan_accuracy
      value: 99.74554455445545
    - type: manhattan_ap
      value: 92.4337790809948
    - type: manhattan_f1
      value: 86.86765457332653
    - type: manhattan_precision
      value: 88.81922675026124
    - type: manhattan_recall
      value: 85.0
    - type: max_accuracy
      value: 99.76831683168317
    - type: max_ap
      value: 93.47124923047998
    - type: max_f1
      value: 88.06122448979592
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
      value: 59.194098673976484
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
      value: 32.5744032578115
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
      value: 49.61186384154483
    - type: mrr
      value: 50.55424253034547
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
      value: 30.027210161713946
    - type: cos_sim_spearman
      value: 31.030178065751735
    - type: dot_pearson
      value: 30.09179785685587
    - type: dot_spearman
      value: 30.408303252207813
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
      value: 0.22300000000000003
    - type: map_at_10
      value: 1.762
    - type: map_at_100
      value: 9.984
    - type: map_at_1000
      value: 24.265
    - type: map_at_3
      value: 0.631
    - type: map_at_5
      value: 0.9950000000000001
    - type: mrr_at_1
      value: 88.0
    - type: mrr_at_10
      value: 92.833
    - type: mrr_at_100
      value: 92.833
    - type: mrr_at_1000
      value: 92.833
    - type: mrr_at_3
      value: 92.333
    - type: mrr_at_5
      value: 92.833
    - type: ndcg_at_1
      value: 83.0
    - type: ndcg_at_10
      value: 75.17
    - type: ndcg_at_100
      value: 55.432
    - type: ndcg_at_1000
      value: 49.482
    - type: ndcg_at_3
      value: 82.184
    - type: ndcg_at_5
      value: 79.712
    - type: precision_at_1
      value: 88.0
    - type: precision_at_10
      value: 78.60000000000001
    - type: precision_at_100
      value: 56.56
    - type: precision_at_1000
      value: 22.334
    - type: precision_at_3
      value: 86.667
    - type: precision_at_5
      value: 83.6
    - type: recall_at_1
      value: 0.22300000000000003
    - type: recall_at_10
      value: 1.9879999999999998
    - type: recall_at_100
      value: 13.300999999999998
    - type: recall_at_1000
      value: 46.587
    - type: recall_at_3
      value: 0.6629999999999999
    - type: recall_at_5
      value: 1.079
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
      value: 3.047
    - type: map_at_10
      value: 8.792
    - type: map_at_100
      value: 14.631
    - type: map_at_1000
      value: 16.127
    - type: map_at_3
      value: 4.673
    - type: map_at_5
      value: 5.897
    - type: mrr_at_1
      value: 38.775999999999996
    - type: mrr_at_10
      value: 49.271
    - type: mrr_at_100
      value: 50.181
    - type: mrr_at_1000
      value: 50.2
    - type: mrr_at_3
      value: 44.558
    - type: mrr_at_5
      value: 47.925000000000004
    - type: ndcg_at_1
      value: 35.714
    - type: ndcg_at_10
      value: 23.44
    - type: ndcg_at_100
      value: 35.345
    - type: ndcg_at_1000
      value: 46.495
    - type: ndcg_at_3
      value: 26.146
    - type: ndcg_at_5
      value: 24.878
    - type: precision_at_1
      value: 38.775999999999996
    - type: precision_at_10
      value: 20.816000000000003
    - type: precision_at_100
      value: 7.428999999999999
    - type: precision_at_1000
      value: 1.494
    - type: precision_at_3
      value: 25.85
    - type: precision_at_5
      value: 24.082
    - type: recall_at_1
      value: 3.047
    - type: recall_at_10
      value: 14.975
    - type: recall_at_100
      value: 45.943
    - type: recall_at_1000
      value: 80.31099999999999
    - type: recall_at_3
      value: 5.478000000000001
    - type: recall_at_5
      value: 8.294
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
      value: 68.84080000000002
    - type: ap
      value: 13.135219251019848
    - type: f1
      value: 52.849999421995506
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
      value: 56.68647425014149
    - type: f1
      value: 56.97981427365949
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
      value: 40.8911707239219
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
      value: 83.04226023722954
    - type: cos_sim_ap
      value: 63.681339908301325
    - type: cos_sim_f1
      value: 60.349184470480125
    - type: cos_sim_precision
      value: 53.437754271765655
    - type: cos_sim_recall
      value: 69.31398416886545
    - type: dot_accuracy
      value: 81.46271681468677
    - type: dot_ap
      value: 57.78072296265885
    - type: dot_f1
      value: 56.28769265132901
    - type: dot_precision
      value: 48.7993803253292
    - type: dot_recall
      value: 66.49076517150397
    - type: euclidean_accuracy
      value: 82.16606067830959
    - type: euclidean_ap
      value: 59.974530371203514
    - type: euclidean_f1
      value: 56.856023506366306
    - type: euclidean_precision
      value: 53.037916857012334
    - type: euclidean_recall
      value: 61.2664907651715
    - type: manhattan_accuracy
      value: 82.16606067830959
    - type: manhattan_ap
      value: 59.98962379571767
    - type: manhattan_f1
      value: 56.98153158451947
    - type: manhattan_precision
      value: 51.41158989598811
    - type: manhattan_recall
      value: 63.90501319261214
    - type: max_accuracy
      value: 83.04226023722954
    - type: max_ap
      value: 63.681339908301325
    - type: max_f1
      value: 60.349184470480125
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
      value: 88.56871191834517
    - type: cos_sim_ap
      value: 84.80240716354544
    - type: cos_sim_f1
      value: 77.07765285922385
    - type: cos_sim_precision
      value: 74.84947406601378
    - type: cos_sim_recall
      value: 79.44256236526024
    - type: dot_accuracy
      value: 86.00923662048356
    - type: dot_ap
      value: 78.6556459012073
    - type: dot_f1
      value: 72.7583749109052
    - type: dot_precision
      value: 67.72823779193206
    - type: dot_recall
      value: 78.59562673236834
    - type: euclidean_accuracy
      value: 87.84103698529127
    - type: euclidean_ap
      value: 83.50424424952834
    - type: euclidean_f1
      value: 75.74496544549307
    - type: euclidean_precision
      value: 73.19402556369381
    - type: euclidean_recall
      value: 78.48013550970127
    - type: manhattan_accuracy
      value: 87.9225365777933
    - type: manhattan_ap
      value: 83.49479248597825
    - type: manhattan_f1
      value: 75.67748162447101
    - type: manhattan_precision
      value: 73.06810035842294
    - type: manhattan_recall
      value: 78.48013550970127
    - type: max_accuracy
      value: 88.56871191834517
    - type: max_ap
      value: 84.80240716354544
    - type: max_f1
      value: 77.07765285922385
---

# SGPT-2.7B-weightedmean-msmarco-specb-bitfit

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to the eval folder or our paper: https://arxiv.org/abs/2202.08904

## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 124796 with parameters:
```
{'batch_size': 4, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
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
        "lr": 7.5e-05
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
  (1): Pooling({'word_embedding_dimension': 2560, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': True, 'pooling_mode_lasttoken': False})
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