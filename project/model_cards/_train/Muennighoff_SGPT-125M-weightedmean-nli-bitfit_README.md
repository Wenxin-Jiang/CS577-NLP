---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: SGPT-125M-weightedmean-nli-bitfit
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
      value: 65.88059701492537
    - type: ap
      value: 28.685493163579785
    - type: f1
      value: 59.79951005816335
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
      value: 59.07922912205568
    - type: ap
      value: 73.91887421019034
    - type: f1
      value: 56.6316368658711
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
      value: 64.91754122938531
    - type: ap
      value: 16.360681214864226
    - type: f1
      value: 53.126592061523766
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
      value: 56.423982869378996
    - type: ap
      value: 12.143003571907899
    - type: f1
      value: 45.76363777987471
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
      value: 74.938225
    - type: ap
      value: 69.58187110320567
    - type: f1
      value: 74.72744058439321
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
      value: 35.098
    - type: f1
      value: 34.73265651435726
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
      value: 24.516
    - type: f1
      value: 24.21748200448397
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
      value: 29.097999999999995
    - type: f1
      value: 28.620040162757093
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
      value: 27.395999999999997
    - type: f1
      value: 27.146888644986284
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
      value: 21.724
    - type: f1
      value: 21.37230564276654
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
      value: 23.976
    - type: f1
      value: 23.741137981755482
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
      value: 13.442000000000002
    - type: map_at_10
      value: 24.275
    - type: map_at_100
      value: 25.588
    - type: map_at_1000
      value: 25.659
    - type: map_at_3
      value: 20.092
    - type: map_at_5
      value: 22.439999999999998
    - type: ndcg_at_1
      value: 13.442000000000002
    - type: ndcg_at_10
      value: 31.04
    - type: ndcg_at_100
      value: 37.529
    - type: ndcg_at_1000
      value: 39.348
    - type: ndcg_at_3
      value: 22.342000000000002
    - type: ndcg_at_5
      value: 26.595999999999997
    - type: precision_at_1
      value: 13.442000000000002
    - type: precision_at_10
      value: 5.299
    - type: precision_at_100
      value: 0.836
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 9.625
    - type: precision_at_5
      value: 7.852
    - type: recall_at_1
      value: 13.442000000000002
    - type: recall_at_10
      value: 52.986999999999995
    - type: recall_at_100
      value: 83.64200000000001
    - type: recall_at_1000
      value: 97.795
    - type: recall_at_3
      value: 28.876
    - type: recall_at_5
      value: 39.26
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
      value: 34.742482477870766
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
      value: 24.67870651472156
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
      value: 52.63439984994702
    - type: mrr
      value: 65.75704612408214
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
      value: 72.78000135012542
    - type: cos_sim_spearman
      value: 70.92812216947605
    - type: euclidean_pearson
      value: 77.1169214949292
    - type: euclidean_spearman
      value: 77.10175681583313
    - type: manhattan_pearson
      value: 76.84527031837595
    - type: manhattan_spearman
      value: 77.0704308008438
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
      value: 1.0960334029227559
    - type: f1
      value: 1.0925539318023658
    - type: precision
      value: 1.0908141962421711
    - type: recall
      value: 1.0960334029227559
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
      value: 0.02201188641866608
    - type: f1
      value: 0.02201188641866608
    - type: precision
      value: 0.02201188641866608
    - type: recall
      value: 0.02201188641866608
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
      value: 0.0
    - type: f1
      value: 0.0
    - type: precision
      value: 0.0
    - type: recall
      value: 0.0
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
      value: 0.0
    - type: f1
      value: 0.0
    - type: precision
      value: 0.0
    - type: recall
      value: 0.0
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
      value: 74.67857142857142
    - type: f1
      value: 74.61743413995573
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
      value: 28.93427045246491
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
      value: 23.080939123955474
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
      value: 18.221999999999998
    - type: map_at_10
      value: 24.506
    - type: map_at_100
      value: 25.611
    - type: map_at_1000
      value: 25.758
    - type: map_at_3
      value: 22.264999999999997
    - type: map_at_5
      value: 23.698
    - type: ndcg_at_1
      value: 23.033
    - type: ndcg_at_10
      value: 28.719
    - type: ndcg_at_100
      value: 33.748
    - type: ndcg_at_1000
      value: 37.056
    - type: ndcg_at_3
      value: 25.240000000000002
    - type: ndcg_at_5
      value: 27.12
    - type: precision_at_1
      value: 23.033
    - type: precision_at_10
      value: 5.408
    - type: precision_at_100
      value: 1.004
    - type: precision_at_1000
      value: 0.158
    - type: precision_at_3
      value: 11.874
    - type: precision_at_5
      value: 8.927
    - type: recall_at_1
      value: 18.221999999999998
    - type: recall_at_10
      value: 36.355
    - type: recall_at_100
      value: 58.724
    - type: recall_at_1000
      value: 81.33500000000001
    - type: recall_at_3
      value: 26.334000000000003
    - type: recall_at_5
      value: 31.4
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
      value: 12.058
    - type: map_at_10
      value: 16.051000000000002
    - type: map_at_100
      value: 16.772000000000002
    - type: map_at_1000
      value: 16.871
    - type: map_at_3
      value: 14.78
    - type: map_at_5
      value: 15.5
    - type: ndcg_at_1
      value: 15.35
    - type: ndcg_at_10
      value: 18.804000000000002
    - type: ndcg_at_100
      value: 22.346
    - type: ndcg_at_1000
      value: 25.007
    - type: ndcg_at_3
      value: 16.768
    - type: ndcg_at_5
      value: 17.692
    - type: precision_at_1
      value: 15.35
    - type: precision_at_10
      value: 3.51
    - type: precision_at_100
      value: 0.664
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 7.983
    - type: precision_at_5
      value: 5.656
    - type: recall_at_1
      value: 12.058
    - type: recall_at_10
      value: 23.644000000000002
    - type: recall_at_100
      value: 39.76
    - type: recall_at_1000
      value: 58.56
    - type: recall_at_3
      value: 17.541999999999998
    - type: recall_at_5
      value: 20.232
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
      value: 21.183
    - type: map_at_10
      value: 28.9
    - type: map_at_100
      value: 29.858
    - type: map_at_1000
      value: 29.953999999999997
    - type: map_at_3
      value: 26.58
    - type: map_at_5
      value: 27.912
    - type: ndcg_at_1
      value: 24.765
    - type: ndcg_at_10
      value: 33.339999999999996
    - type: ndcg_at_100
      value: 37.997
    - type: ndcg_at_1000
      value: 40.416000000000004
    - type: ndcg_at_3
      value: 29.044999999999998
    - type: ndcg_at_5
      value: 31.121
    - type: precision_at_1
      value: 24.765
    - type: precision_at_10
      value: 5.599
    - type: precision_at_100
      value: 0.8699999999999999
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 13.270999999999999
    - type: precision_at_5
      value: 9.367
    - type: recall_at_1
      value: 21.183
    - type: recall_at_10
      value: 43.875
    - type: recall_at_100
      value: 65.005
    - type: recall_at_1000
      value: 83.017
    - type: recall_at_3
      value: 32.232
    - type: recall_at_5
      value: 37.308
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
      value: 11.350999999999999
    - type: map_at_10
      value: 14.953
    - type: map_at_100
      value: 15.623000000000001
    - type: map_at_1000
      value: 15.716
    - type: map_at_3
      value: 13.603000000000002
    - type: map_at_5
      value: 14.343
    - type: ndcg_at_1
      value: 12.429
    - type: ndcg_at_10
      value: 17.319000000000003
    - type: ndcg_at_100
      value: 20.990000000000002
    - type: ndcg_at_1000
      value: 23.899
    - type: ndcg_at_3
      value: 14.605
    - type: ndcg_at_5
      value: 15.89
    - type: precision_at_1
      value: 12.429
    - type: precision_at_10
      value: 2.701
    - type: precision_at_100
      value: 0.48700000000000004
    - type: precision_at_1000
      value: 0.078
    - type: precision_at_3
      value: 6.026
    - type: precision_at_5
      value: 4.3839999999999995
    - type: recall_at_1
      value: 11.350999999999999
    - type: recall_at_10
      value: 23.536
    - type: recall_at_100
      value: 40.942
    - type: recall_at_1000
      value: 64.05
    - type: recall_at_3
      value: 16.195
    - type: recall_at_5
      value: 19.264
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
      value: 8.08
    - type: map_at_10
      value: 11.691
    - type: map_at_100
      value: 12.312
    - type: map_at_1000
      value: 12.439
    - type: map_at_3
      value: 10.344000000000001
    - type: map_at_5
      value: 10.996
    - type: ndcg_at_1
      value: 10.697
    - type: ndcg_at_10
      value: 14.48
    - type: ndcg_at_100
      value: 18.160999999999998
    - type: ndcg_at_1000
      value: 21.886
    - type: ndcg_at_3
      value: 11.872
    - type: ndcg_at_5
      value: 12.834000000000001
    - type: precision_at_1
      value: 10.697
    - type: precision_at_10
      value: 2.811
    - type: precision_at_100
      value: 0.551
    - type: precision_at_1000
      value: 0.10200000000000001
    - type: precision_at_3
      value: 5.804
    - type: precision_at_5
      value: 4.154
    - type: recall_at_1
      value: 8.08
    - type: recall_at_10
      value: 20.235
    - type: recall_at_100
      value: 37.525999999999996
    - type: recall_at_1000
      value: 65.106
    - type: recall_at_3
      value: 12.803999999999998
    - type: recall_at_5
      value: 15.498999999999999
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
      value: 13.908999999999999
    - type: map_at_10
      value: 19.256
    - type: map_at_100
      value: 20.286
    - type: map_at_1000
      value: 20.429
    - type: map_at_3
      value: 17.399
    - type: map_at_5
      value: 18.398999999999997
    - type: ndcg_at_1
      value: 17.421
    - type: ndcg_at_10
      value: 23.105999999999998
    - type: ndcg_at_100
      value: 28.128999999999998
    - type: ndcg_at_1000
      value: 31.480999999999998
    - type: ndcg_at_3
      value: 19.789
    - type: ndcg_at_5
      value: 21.237000000000002
    - type: precision_at_1
      value: 17.421
    - type: precision_at_10
      value: 4.331
    - type: precision_at_100
      value: 0.839
    - type: precision_at_1000
      value: 0.131
    - type: precision_at_3
      value: 9.4
    - type: precision_at_5
      value: 6.776
    - type: recall_at_1
      value: 13.908999999999999
    - type: recall_at_10
      value: 31.086999999999996
    - type: recall_at_100
      value: 52.946000000000005
    - type: recall_at_1000
      value: 76.546
    - type: recall_at_3
      value: 21.351
    - type: recall_at_5
      value: 25.264999999999997
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
      value: 12.598
    - type: map_at_10
      value: 17.304
    - type: map_at_100
      value: 18.209
    - type: map_at_1000
      value: 18.328
    - type: map_at_3
      value: 15.784
    - type: map_at_5
      value: 16.669999999999998
    - type: ndcg_at_1
      value: 15.867999999999999
    - type: ndcg_at_10
      value: 20.623
    - type: ndcg_at_100
      value: 25.093
    - type: ndcg_at_1000
      value: 28.498
    - type: ndcg_at_3
      value: 17.912
    - type: ndcg_at_5
      value: 19.198
    - type: precision_at_1
      value: 15.867999999999999
    - type: precision_at_10
      value: 3.7670000000000003
    - type: precision_at_100
      value: 0.716
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 8.638
    - type: precision_at_5
      value: 6.21
    - type: recall_at_1
      value: 12.598
    - type: recall_at_10
      value: 27.144000000000002
    - type: recall_at_100
      value: 46.817
    - type: recall_at_1000
      value: 71.86099999999999
    - type: recall_at_3
      value: 19.231
    - type: recall_at_5
      value: 22.716
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
      value: 12.738416666666666
    - type: map_at_10
      value: 17.235916666666668
    - type: map_at_100
      value: 18.063333333333333
    - type: map_at_1000
      value: 18.18433333333333
    - type: map_at_3
      value: 15.74775
    - type: map_at_5
      value: 16.57825
    - type: ndcg_at_1
      value: 15.487416666666665
    - type: ndcg_at_10
      value: 20.290166666666668
    - type: ndcg_at_100
      value: 24.41291666666666
    - type: ndcg_at_1000
      value: 27.586333333333336
    - type: ndcg_at_3
      value: 17.622083333333332
    - type: ndcg_at_5
      value: 18.859916666666667
    - type: precision_at_1
      value: 15.487416666666665
    - type: precision_at_10
      value: 3.6226666666666665
    - type: precision_at_100
      value: 0.6820833333333334
    - type: precision_at_1000
      value: 0.11216666666666666
    - type: precision_at_3
      value: 8.163749999999999
    - type: precision_at_5
      value: 5.865416666666667
    - type: recall_at_1
      value: 12.738416666666666
    - type: recall_at_10
      value: 26.599416666666663
    - type: recall_at_100
      value: 45.41258333333334
    - type: recall_at_1000
      value: 68.7565
    - type: recall_at_3
      value: 19.008166666666668
    - type: recall_at_5
      value: 22.24991666666667
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
      value: 12.307
    - type: map_at_10
      value: 15.440000000000001
    - type: map_at_100
      value: 16.033
    - type: map_at_1000
      value: 16.14
    - type: map_at_3
      value: 14.393
    - type: map_at_5
      value: 14.856
    - type: ndcg_at_1
      value: 14.571000000000002
    - type: ndcg_at_10
      value: 17.685000000000002
    - type: ndcg_at_100
      value: 20.882
    - type: ndcg_at_1000
      value: 23.888
    - type: ndcg_at_3
      value: 15.739
    - type: ndcg_at_5
      value: 16.391
    - type: precision_at_1
      value: 14.571000000000002
    - type: precision_at_10
      value: 2.883
    - type: precision_at_100
      value: 0.49100000000000005
    - type: precision_at_1000
      value: 0.08
    - type: precision_at_3
      value: 7.0040000000000004
    - type: precision_at_5
      value: 4.693
    - type: recall_at_1
      value: 12.307
    - type: recall_at_10
      value: 22.566
    - type: recall_at_100
      value: 37.469
    - type: recall_at_1000
      value: 60.550000000000004
    - type: recall_at_3
      value: 16.742
    - type: recall_at_5
      value: 18.634
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
      value: 6.496
    - type: map_at_10
      value: 9.243
    - type: map_at_100
      value: 9.841
    - type: map_at_1000
      value: 9.946000000000002
    - type: map_at_3
      value: 8.395
    - type: map_at_5
      value: 8.872
    - type: ndcg_at_1
      value: 8.224
    - type: ndcg_at_10
      value: 11.24
    - type: ndcg_at_100
      value: 14.524999999999999
    - type: ndcg_at_1000
      value: 17.686
    - type: ndcg_at_3
      value: 9.617
    - type: ndcg_at_5
      value: 10.37
    - type: precision_at_1
      value: 8.224
    - type: precision_at_10
      value: 2.0820000000000003
    - type: precision_at_100
      value: 0.443
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: precision_at_3
      value: 4.623
    - type: precision_at_5
      value: 3.331
    - type: recall_at_1
      value: 6.496
    - type: recall_at_10
      value: 15.310000000000002
    - type: recall_at_100
      value: 30.680000000000003
    - type: recall_at_1000
      value: 54.335
    - type: recall_at_3
      value: 10.691
    - type: recall_at_5
      value: 12.687999999999999
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
      value: 13.843
    - type: map_at_10
      value: 17.496000000000002
    - type: map_at_100
      value: 18.304000000000002
    - type: map_at_1000
      value: 18.426000000000002
    - type: map_at_3
      value: 16.225
    - type: map_at_5
      value: 16.830000000000002
    - type: ndcg_at_1
      value: 16.698
    - type: ndcg_at_10
      value: 20.301
    - type: ndcg_at_100
      value: 24.523
    - type: ndcg_at_1000
      value: 27.784
    - type: ndcg_at_3
      value: 17.822
    - type: ndcg_at_5
      value: 18.794
    - type: precision_at_1
      value: 16.698
    - type: precision_at_10
      value: 3.3579999999999997
    - type: precision_at_100
      value: 0.618
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 7.898
    - type: precision_at_5
      value: 5.428999999999999
    - type: recall_at_1
      value: 13.843
    - type: recall_at_10
      value: 25.887999999999998
    - type: recall_at_100
      value: 45.028
    - type: recall_at_1000
      value: 68.991
    - type: recall_at_3
      value: 18.851000000000003
    - type: recall_at_5
      value: 21.462
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
      value: 13.757
    - type: map_at_10
      value: 19.27
    - type: map_at_100
      value: 20.461
    - type: map_at_1000
      value: 20.641000000000002
    - type: map_at_3
      value: 17.865000000000002
    - type: map_at_5
      value: 18.618000000000002
    - type: ndcg_at_1
      value: 16.996
    - type: ndcg_at_10
      value: 22.774
    - type: ndcg_at_100
      value: 27.675
    - type: ndcg_at_1000
      value: 31.145
    - type: ndcg_at_3
      value: 20.691000000000003
    - type: ndcg_at_5
      value: 21.741
    - type: precision_at_1
      value: 16.996
    - type: precision_at_10
      value: 4.545
    - type: precision_at_100
      value: 1.036
    - type: precision_at_1000
      value: 0.185
    - type: precision_at_3
      value: 10.145
    - type: precision_at_5
      value: 7.391
    - type: recall_at_1
      value: 13.757
    - type: recall_at_10
      value: 28.233999999999998
    - type: recall_at_100
      value: 51.05499999999999
    - type: recall_at_1000
      value: 75.35300000000001
    - type: recall_at_3
      value: 21.794
    - type: recall_at_5
      value: 24.614
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
      value: 9.057
    - type: map_at_10
      value: 12.720999999999998
    - type: map_at_100
      value: 13.450000000000001
    - type: map_at_1000
      value: 13.564000000000002
    - type: map_at_3
      value: 11.34
    - type: map_at_5
      value: 12.245000000000001
    - type: ndcg_at_1
      value: 9.797
    - type: ndcg_at_10
      value: 15.091
    - type: ndcg_at_100
      value: 18.886
    - type: ndcg_at_1000
      value: 22.29
    - type: ndcg_at_3
      value: 12.365
    - type: ndcg_at_5
      value: 13.931
    - type: precision_at_1
      value: 9.797
    - type: precision_at_10
      value: 2.477
    - type: precision_at_100
      value: 0.466
    - type: precision_at_1000
      value: 0.082
    - type: precision_at_3
      value: 5.299
    - type: precision_at_5
      value: 4.067
    - type: recall_at_1
      value: 9.057
    - type: recall_at_10
      value: 21.319
    - type: recall_at_100
      value: 38.999
    - type: recall_at_1000
      value: 65.374
    - type: recall_at_3
      value: 14.331
    - type: recall_at_5
      value: 17.916999999999998
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
      value: 3.714
    - type: map_at_10
      value: 6.926
    - type: map_at_100
      value: 7.879
    - type: map_at_1000
      value: 8.032
    - type: map_at_3
      value: 5.504
    - type: map_at_5
      value: 6.357
    - type: ndcg_at_1
      value: 8.86
    - type: ndcg_at_10
      value: 11.007
    - type: ndcg_at_100
      value: 16.154
    - type: ndcg_at_1000
      value: 19.668
    - type: ndcg_at_3
      value: 8.103
    - type: ndcg_at_5
      value: 9.456000000000001
    - type: precision_at_1
      value: 8.86
    - type: precision_at_10
      value: 3.7199999999999998
    - type: precision_at_100
      value: 0.9169999999999999
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 6.254
    - type: precision_at_5
      value: 5.380999999999999
    - type: recall_at_1
      value: 3.714
    - type: recall_at_10
      value: 14.382
    - type: recall_at_100
      value: 33.166000000000004
    - type: recall_at_1000
      value: 53.444
    - type: recall_at_3
      value: 7.523000000000001
    - type: recall_at_5
      value: 10.91
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
      value: 1.764
    - type: map_at_10
      value: 3.8600000000000003
    - type: map_at_100
      value: 5.457
    - type: map_at_1000
      value: 5.938000000000001
    - type: map_at_3
      value: 2.667
    - type: map_at_5
      value: 3.2199999999999998
    - type: ndcg_at_1
      value: 14.000000000000002
    - type: ndcg_at_10
      value: 10.868
    - type: ndcg_at_100
      value: 12.866
    - type: ndcg_at_1000
      value: 17.43
    - type: ndcg_at_3
      value: 11.943
    - type: ndcg_at_5
      value: 11.66
    - type: precision_at_1
      value: 19.25
    - type: precision_at_10
      value: 10.274999999999999
    - type: precision_at_100
      value: 3.527
    - type: precision_at_1000
      value: 0.9119999999999999
    - type: precision_at_3
      value: 14.917
    - type: precision_at_5
      value: 13.5
    - type: recall_at_1
      value: 1.764
    - type: recall_at_10
      value: 6.609
    - type: recall_at_100
      value: 17.616
    - type: recall_at_1000
      value: 33.085
    - type: recall_at_3
      value: 3.115
    - type: recall_at_5
      value: 4.605
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
      value: 42.225
    - type: f1
      value: 37.563516542112104
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
      value: 11.497
    - type: map_at_10
      value: 15.744
    - type: map_at_100
      value: 16.3
    - type: map_at_1000
      value: 16.365
    - type: map_at_3
      value: 14.44
    - type: map_at_5
      value: 15.18
    - type: ndcg_at_1
      value: 12.346
    - type: ndcg_at_10
      value: 18.398999999999997
    - type: ndcg_at_100
      value: 21.399
    - type: ndcg_at_1000
      value: 23.442
    - type: ndcg_at_3
      value: 15.695
    - type: ndcg_at_5
      value: 17.027
    - type: precision_at_1
      value: 12.346
    - type: precision_at_10
      value: 2.798
    - type: precision_at_100
      value: 0.445
    - type: precision_at_1000
      value: 0.063
    - type: precision_at_3
      value: 6.586
    - type: precision_at_5
      value: 4.665
    - type: recall_at_1
      value: 11.497
    - type: recall_at_10
      value: 25.636
    - type: recall_at_100
      value: 39.894
    - type: recall_at_1000
      value: 56.181000000000004
    - type: recall_at_3
      value: 18.273
    - type: recall_at_5
      value: 21.474
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
      value: 3.637
    - type: map_at_10
      value: 6.084
    - type: map_at_100
      value: 6.9190000000000005
    - type: map_at_1000
      value: 7.1080000000000005
    - type: map_at_3
      value: 5.071
    - type: map_at_5
      value: 5.5649999999999995
    - type: ndcg_at_1
      value: 7.407
    - type: ndcg_at_10
      value: 8.94
    - type: ndcg_at_100
      value: 13.594999999999999
    - type: ndcg_at_1000
      value: 18.29
    - type: ndcg_at_3
      value: 7.393
    - type: ndcg_at_5
      value: 7.854
    - type: precision_at_1
      value: 7.407
    - type: precision_at_10
      value: 2.778
    - type: precision_at_100
      value: 0.75
    - type: precision_at_1000
      value: 0.154
    - type: precision_at_3
      value: 5.144
    - type: precision_at_5
      value: 3.981
    - type: recall_at_1
      value: 3.637
    - type: recall_at_10
      value: 11.821
    - type: recall_at_100
      value: 30.18
    - type: recall_at_1000
      value: 60.207
    - type: recall_at_3
      value: 6.839
    - type: recall_at_5
      value: 8.649
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
      value: 9.676
    - type: map_at_10
      value: 13.350999999999999
    - type: map_at_100
      value: 13.919
    - type: map_at_1000
      value: 14.01
    - type: map_at_3
      value: 12.223
    - type: map_at_5
      value: 12.812000000000001
    - type: ndcg_at_1
      value: 19.352
    - type: ndcg_at_10
      value: 17.727
    - type: ndcg_at_100
      value: 20.837
    - type: ndcg_at_1000
      value: 23.412
    - type: ndcg_at_3
      value: 15.317
    - type: ndcg_at_5
      value: 16.436
    - type: precision_at_1
      value: 19.352
    - type: precision_at_10
      value: 3.993
    - type: precision_at_100
      value: 0.651
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 9.669
    - type: precision_at_5
      value: 6.69
    - type: recall_at_1
      value: 9.676
    - type: recall_at_10
      value: 19.966
    - type: recall_at_100
      value: 32.573
    - type: recall_at_1000
      value: 49.905
    - type: recall_at_3
      value: 14.504
    - type: recall_at_5
      value: 16.725
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
      value: 62.895999999999994
    - type: ap
      value: 58.47769349850157
    - type: f1
      value: 62.67885149592086
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
      value: 2.88
    - type: map_at_10
      value: 4.914000000000001
    - type: map_at_100
      value: 5.459
    - type: map_at_1000
      value: 5.538
    - type: map_at_3
      value: 4.087
    - type: map_at_5
      value: 4.518
    - type: ndcg_at_1
      value: 2.937
    - type: ndcg_at_10
      value: 6.273
    - type: ndcg_at_100
      value: 9.426
    - type: ndcg_at_1000
      value: 12.033000000000001
    - type: ndcg_at_3
      value: 4.513
    - type: ndcg_at_5
      value: 5.292
    - type: precision_at_1
      value: 2.937
    - type: precision_at_10
      value: 1.089
    - type: precision_at_100
      value: 0.27699999999999997
    - type: precision_at_1000
      value: 0.051000000000000004
    - type: precision_at_3
      value: 1.9290000000000003
    - type: precision_at_5
      value: 1.547
    - type: recall_at_1
      value: 2.88
    - type: recall_at_10
      value: 10.578
    - type: recall_at_100
      value: 26.267000000000003
    - type: recall_at_1000
      value: 47.589999999999996
    - type: recall_at_3
      value: 5.673
    - type: recall_at_5
      value: 7.545
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
      value: 81.51846785225717
    - type: f1
      value: 81.648869152345
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
      value: 60.37475345167653
    - type: f1
      value: 58.452649375517026
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
      value: 67.36824549699799
    - type: f1
      value: 65.35927434998516
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
      value: 63.12871907297212
    - type: f1
      value: 61.37620329272278
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
      value: 47.04553603442094
    - type: f1
      value: 46.20389912644561
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
      value: 52.282097649186255
    - type: f1
      value: 50.75489206473579
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
      value: 58.2421340629275
    - type: f1
      value: 40.11696046622642
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
      value: 45.069033530571986
    - type: f1
      value: 30.468468273374967
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
      value: 48.80920613742495
    - type: f1
      value: 32.65985375400447
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
      value: 44.337613529595984
    - type: f1
      value: 29.302047435606436
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
      value: 34.198637504481894
    - type: f1
      value: 22.063706032248408
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
      value: 43.11030741410488
    - type: f1
      value: 26.92408933648504
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
      value: 37.79421654337593
    - type: f1
      value: 36.81580701507746
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
      value: 23.722259583053127
    - type: f1
      value: 23.235269695764273
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
      value: 29.64021519838601
    - type: f1
      value: 28.273175327650137
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
      value: 39.4754539340955
    - type: f1
      value: 39.25997361415121
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
      value: 26.550100874243444
    - type: f1
      value: 25.607924873522975
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
      value: 38.78278412911904
    - type: f1
      value: 37.64180582626517
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
      value: 43.557498318762605
    - type: f1
      value: 41.35305173800667
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
      value: 40.39340954942838
    - type: f1
      value: 38.33393219528934
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
      value: 37.28648285137861
    - type: f1
      value: 36.64005906680284
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
      value: 58.080026899798256
    - type: f1
      value: 56.49243881660991
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
      value: 41.176866173503704
    - type: f1
      value: 40.66779962225799
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
      value: 36.422326832548755
    - type: f1
      value: 34.6441738042885
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
      value: 38.75588433086752
    - type: f1
      value: 37.26725894668694
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
      value: 43.67182246133153
    - type: f1
      value: 42.351846624566605
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
      value: 31.980497646267658
    - type: f1
      value: 30.557928872809008
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
      value: 28.039677202420982
    - type: f1
      value: 28.428418145508306
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
      value: 38.13718897108272
    - type: f1
      value: 37.057406988196874
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
      value: 26.05245460659045
    - type: f1
      value: 25.25483953344816
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
      value: 41.156691324815064
    - type: f1
      value: 40.83715033247605
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
      value: 38.62811028917284
    - type: f1
      value: 37.67691901246032
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
      value: 44.0383322125084
    - type: f1
      value: 43.77259010877456
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
      value: 46.20712844653666
    - type: f1
      value: 44.66632875940824
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
      value: 37.60591795561533
    - type: f1
      value: 36.581071742378015
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
      value: 24.47209145931405
    - type: f1
      value: 24.238209697895606
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
      value: 26.23739071956961
    - type: f1
      value: 25.378783150845052
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
      value: 17.831203765971754
    - type: f1
      value: 17.275078420466343
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
      value: 37.266308002689975
    - type: f1
      value: 36.92473791708214
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
      value: 40.93140551445864
    - type: f1
      value: 40.825227889641965
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
      value: 17.88500336247478
    - type: f1
      value: 17.621569082971817
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
      value: 32.975790181573636
    - type: f1
      value: 33.402014633349665
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
      value: 40.91123066577001
    - type: f1
      value: 40.09538559124075
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
      value: 17.834566240753194
    - type: f1
      value: 17.006381849454314
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
      value: 39.47881640887693
    - type: f1
      value: 37.819934317839305
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
      value: 41.76193678547412
    - type: f1
      value: 40.281991759509694
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
      value: 42.61936785474109
    - type: f1
      value: 40.83673914649905
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
      value: 44.54270342972427
    - type: f1
      value: 43.45243164278448
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
      value: 39.96973772696705
    - type: f1
      value: 38.74209466530094
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
      value: 37.461331540013454
    - type: f1
      value: 36.91132021821187
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
      value: 38.28850033624748
    - type: f1
      value: 37.37259394049676
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
      value: 40.95494283792872
    - type: f1
      value: 39.767707902869084
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
      value: 41.85272360457296
    - type: f1
      value: 40.42848260365438
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
      value: 38.328850033624754
    - type: f1
      value: 36.90334596675622
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
      value: 19.031607262945528
    - type: f1
      value: 18.66510306325761
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
      value: 19.38466711499664
    - type: f1
      value: 19.186399376652535
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
      value: 34.088769334229994
    - type: f1
      value: 34.20383086009429
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
      value: 40.285810356422324
    - type: f1
      value: 39.361500249640414
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
      value: 38.860121049092136
    - type: f1
      value: 37.81916859627235
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
      value: 27.834566240753194
    - type: f1
      value: 26.898389386106487
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
      value: 38.70544720914593
    - type: f1
      value: 38.280026442024415
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
      value: 45.78009414929387
    - type: f1
      value: 44.21526778674136
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
      value: 42.32010759919301
    - type: f1
      value: 42.25772977490916
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
      value: 40.24546065904506
    - type: f1
      value: 38.79924050989544
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
      value: 25.68930733019502
    - type: f1
      value: 25.488166279162712
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
      value: 32.39744451916611
    - type: f1
      value: 31.863029579075775
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
      value: 40.53127101546738
    - type: f1
      value: 39.707079033948936
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
      value: 27.23268325487559
    - type: f1
      value: 26.443653281858793
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
      value: 38.69872225958305
    - type: f1
      value: 36.55930387892567
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
      value: 44.75453934095494
    - type: f1
      value: 42.87356484024154
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
      value: 41.355077336919976
    - type: f1
      value: 39.82365179458047
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
      value: 38.43981170141224
    - type: f1
      value: 37.02538368296387
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
      value: 66.33826496301278
    - type: f1
      value: 65.89634765029932
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
      value: 44.17955615332885
    - type: f1
      value: 43.10228811620319
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
      value: 34.82851378614661
    - type: f1
      value: 33.95952441502803
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
      value: 40.561533288500335
    - type: f1
      value: 38.04939011733627
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
      value: 45.917955615332886
    - type: f1
      value: 44.65741971572902
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
      value: 32.08473436449227
    - type: f1
      value: 29.53932929808133
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
      value: 28.369199731002016
    - type: f1
      value: 27.52902837981212
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
      value: 39.49226630800269
    - type: f1
      value: 37.3272340470504
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
      value: 25.904505716207133
    - type: f1
      value: 24.547396574853444
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
      value: 40.95830531271016
    - type: f1
      value: 40.177843177422226
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
      value: 38.564223268325485
    - type: f1
      value: 37.35307758495248
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
      value: 46.58708809683928
    - type: f1
      value: 44.103900526804985
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
      value: 46.24747814391393
    - type: f1
      value: 45.4107101796664
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
      value: 39.6570275722932
    - type: f1
      value: 38.82737576832412
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
      value: 25.279085406859448
    - type: f1
      value: 23.662661686788493
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
      value: 28.97108271687962
    - type: f1
      value: 27.195758324189246
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
      value: 19.27370544720915
    - type: f1
      value: 18.694271924323637
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
      value: 35.729657027572294
    - type: f1
      value: 34.38287006177308
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
      value: 39.57296570275723
    - type: f1
      value: 38.074945140886925
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
      value: 19.895763281775388
    - type: f1
      value: 20.00931364846829
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
      value: 32.431069266980494
    - type: f1
      value: 31.395958664782576
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
      value: 42.32347007397445
    - type: f1
      value: 40.81374026314701
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
      value: 20.864156018829856
    - type: f1
      value: 20.409870408935436
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
      value: 40.47074646940148
    - type: f1
      value: 39.19044149415904
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
      value: 43.591123066577
    - type: f1
      value: 41.43420363064241
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
      value: 41.876260928043045
    - type: f1
      value: 41.192117676667614
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
      value: 46.30800268997983
    - type: f1
      value: 45.25536730126799
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
      value: 42.525218560860786
    - type: f1
      value: 41.02418109296485
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
      value: 35.94821788836584
    - type: f1
      value: 35.08598314806566
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
      value: 38.69199731002017
    - type: f1
      value: 37.68119408674127
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
      value: 40.474108944182916
    - type: f1
      value: 39.480530387013594
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
      value: 41.523201075991935
    - type: f1
      value: 40.20097996024383
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
      value: 39.54942837928716
    - type: f1
      value: 38.185561243338064
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
      value: 22.8782784129119
    - type: f1
      value: 22.239467186721456
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
      value: 20.51445864156019
    - type: f1
      value: 19.999047885530217
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
      value: 34.92602555480834
    - type: f1
      value: 33.24016717215723
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
      value: 40.74983187626093
    - type: f1
      value: 39.30274328728882
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
      value: 39.06859448554136
    - type: f1
      value: 39.21542039662971
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
      value: 29.747814391392062
    - type: f1
      value: 28.261836892220447
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
      value: 38.02286482851379
    - type: f1
      value: 37.8742438608697
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
      value: 48.550773369199725
    - type: f1
      value: 46.7399625882649
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
      value: 45.17821116341628
    - type: f1
      value: 44.84809741811729
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
      value: 28.301902023313875
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
      value: 24.932123582259287
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
      value: 29.269341041468326
    - type: mrr
      value: 30.132140876875717
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
      value: 1.2269999999999999
    - type: map_at_10
      value: 3.081
    - type: map_at_100
      value: 4.104
    - type: map_at_1000
      value: 4.989
    - type: map_at_3
      value: 2.221
    - type: map_at_5
      value: 2.535
    - type: ndcg_at_1
      value: 15.015
    - type: ndcg_at_10
      value: 11.805
    - type: ndcg_at_100
      value: 12.452
    - type: ndcg_at_1000
      value: 22.284000000000002
    - type: ndcg_at_3
      value: 13.257
    - type: ndcg_at_5
      value: 12.199
    - type: precision_at_1
      value: 16.409000000000002
    - type: precision_at_10
      value: 9.102
    - type: precision_at_100
      value: 3.678
    - type: precision_at_1000
      value: 1.609
    - type: precision_at_3
      value: 12.797
    - type: precision_at_5
      value: 10.464
    - type: recall_at_1
      value: 1.2269999999999999
    - type: recall_at_10
      value: 5.838
    - type: recall_at_100
      value: 15.716
    - type: recall_at_1000
      value: 48.837
    - type: recall_at_3
      value: 2.828
    - type: recall_at_5
      value: 3.697
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
      value: 3.515
    - type: map_at_10
      value: 5.884
    - type: map_at_100
      value: 6.510000000000001
    - type: map_at_1000
      value: 6.598999999999999
    - type: map_at_3
      value: 4.8919999999999995
    - type: map_at_5
      value: 5.391
    - type: ndcg_at_1
      value: 4.056
    - type: ndcg_at_10
      value: 7.6259999999999994
    - type: ndcg_at_100
      value: 11.08
    - type: ndcg_at_1000
      value: 13.793
    - type: ndcg_at_3
      value: 5.537
    - type: ndcg_at_5
      value: 6.45
    - type: precision_at_1
      value: 4.056
    - type: precision_at_10
      value: 1.4569999999999999
    - type: precision_at_100
      value: 0.347
    - type: precision_at_1000
      value: 0.061
    - type: precision_at_3
      value: 2.6069999999999998
    - type: precision_at_5
      value: 2.086
    - type: recall_at_1
      value: 3.515
    - type: recall_at_10
      value: 12.312
    - type: recall_at_100
      value: 28.713
    - type: recall_at_1000
      value: 50.027
    - type: recall_at_3
      value: 6.701
    - type: recall_at_5
      value: 8.816
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
      value: 61.697
    - type: map_at_10
      value: 74.20400000000001
    - type: map_at_100
      value: 75.023
    - type: map_at_1000
      value: 75.059
    - type: map_at_3
      value: 71.265
    - type: map_at_5
      value: 73.001
    - type: ndcg_at_1
      value: 70.95
    - type: ndcg_at_10
      value: 78.96
    - type: ndcg_at_100
      value: 81.26
    - type: ndcg_at_1000
      value: 81.679
    - type: ndcg_at_3
      value: 75.246
    - type: ndcg_at_5
      value: 77.092
    - type: precision_at_1
      value: 70.95
    - type: precision_at_10
      value: 11.998000000000001
    - type: precision_at_100
      value: 1.451
    - type: precision_at_1000
      value: 0.154
    - type: precision_at_3
      value: 32.629999999999995
    - type: precision_at_5
      value: 21.573999999999998
    - type: recall_at_1
      value: 61.697
    - type: recall_at_10
      value: 88.23299999999999
    - type: recall_at_100
      value: 96.961
    - type: recall_at_1000
      value: 99.401
    - type: recall_at_3
      value: 77.689
    - type: recall_at_5
      value: 82.745
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
      value: 33.75741018380938
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
      value: 41.00799910099266
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
      value: 1.72
    - type: map_at_10
      value: 3.8240000000000003
    - type: map_at_100
      value: 4.727
    - type: map_at_1000
      value: 4.932
    - type: map_at_3
      value: 2.867
    - type: map_at_5
      value: 3.3230000000000004
    - type: ndcg_at_1
      value: 8.5
    - type: ndcg_at_10
      value: 7.133000000000001
    - type: ndcg_at_100
      value: 11.911
    - type: ndcg_at_1000
      value: 16.962
    - type: ndcg_at_3
      value: 6.763
    - type: ndcg_at_5
      value: 5.832
    - type: precision_at_1
      value: 8.5
    - type: precision_at_10
      value: 3.6799999999999997
    - type: precision_at_100
      value: 1.0670000000000002
    - type: precision_at_1000
      value: 0.22999999999999998
    - type: precision_at_3
      value: 6.2330000000000005
    - type: precision_at_5
      value: 5.0200000000000005
    - type: recall_at_1
      value: 1.72
    - type: recall_at_10
      value: 7.487000000000001
    - type: recall_at_100
      value: 21.683
    - type: recall_at_1000
      value: 46.688
    - type: recall_at_3
      value: 3.798
    - type: recall_at_5
      value: 5.113
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
      value: 80.96286245858941
    - type: cos_sim_spearman
      value: 74.57093488947429
    - type: euclidean_pearson
      value: 75.50377970259402
    - type: euclidean_spearman
      value: 71.7498004622999
    - type: manhattan_pearson
      value: 75.3256836091382
    - type: manhattan_spearman
      value: 71.80676733410375
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
      value: 80.20938796088339
    - type: cos_sim_spearman
      value: 69.16914010333394
    - type: euclidean_pearson
      value: 79.33415250097545
    - type: euclidean_spearman
      value: 71.46707320292745
    - type: manhattan_pearson
      value: 79.73669837981976
    - type: manhattan_spearman
      value: 71.87919511134902
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
      value: 76.401935081936
    - type: cos_sim_spearman
      value: 77.23446219694267
    - type: euclidean_pearson
      value: 74.61017160439877
    - type: euclidean_spearman
      value: 75.85871531365609
    - type: manhattan_pearson
      value: 74.83034779539724
    - type: manhattan_spearman
      value: 75.95948993588429
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
      value: 75.35551963935667
    - type: cos_sim_spearman
      value: 70.98892671568665
    - type: euclidean_pearson
      value: 73.24467338564628
    - type: euclidean_spearman
      value: 71.97533151639425
    - type: manhattan_pearson
      value: 73.2776559359938
    - type: manhattan_spearman
      value: 72.2221421456084
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
      value: 79.05293131911803
    - type: cos_sim_spearman
      value: 79.7379478259805
    - type: euclidean_pearson
      value: 78.17016171851057
    - type: euclidean_spearman
      value: 78.76038607583105
    - type: manhattan_pearson
      value: 78.4994607532332
    - type: manhattan_spearman
      value: 79.13026720132872
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
      value: 76.04750373932828
    - type: cos_sim_spearman
      value: 77.93230986462234
    - type: euclidean_pearson
      value: 75.8320302521164
    - type: euclidean_spearman
      value: 76.83154481579385
    - type: manhattan_pearson
      value: 75.98713517720608
    - type: manhattan_spearman
      value: 76.95479705521507
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
      value: 43.0464619152799
    - type: cos_sim_spearman
      value: 45.65606588928089
    - type: euclidean_pearson
      value: 45.69437788355499
    - type: euclidean_spearman
      value: 45.08552742346606
    - type: manhattan_pearson
      value: 45.87166698903681
    - type: manhattan_spearman
      value: 45.155963016434164
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
      value: 53.27469278912148
    - type: cos_sim_spearman
      value: 54.16113207623789
    - type: euclidean_pearson
      value: 55.97026429327157
    - type: euclidean_spearman
      value: 54.71320909074608
    - type: manhattan_pearson
      value: 56.12511774278802
    - type: manhattan_spearman
      value: 55.22875659158676
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
      value: 1.5482997790039945
    - type: cos_sim_spearman
      value: 1.7208386347363582
    - type: euclidean_pearson
      value: 6.727915670345885
    - type: euclidean_spearman
      value: 6.112826908474543
    - type: manhattan_pearson
      value: 4.94386093060865
    - type: manhattan_spearman
      value: 5.018174110623732
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
      value: 27.5420218362265
    - type: cos_sim_spearman
      value: 25.483838431031007
    - type: euclidean_pearson
      value: 6.268684143856358
    - type: euclidean_spearman
      value: 5.877961421091679
    - type: manhattan_pearson
      value: 2.667237739227861
    - type: manhattan_spearman
      value: 2.5683839956554775
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
      value: 85.32029757646663
    - type: cos_sim_spearman
      value: 87.32720847297225
    - type: euclidean_pearson
      value: 81.12594485791254
    - type: euclidean_spearman
      value: 81.1531079489332
    - type: manhattan_pearson
      value: 81.32899414704019
    - type: manhattan_spearman
      value: 81.3897040261192
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
      value: 4.37162299241808
    - type: cos_sim_spearman
      value: 2.0879072561774543
    - type: euclidean_pearson
      value: 3.0725243785454595
    - type: euclidean_spearman
      value: 5.3721339279483535
    - type: manhattan_pearson
      value: 4.867795293367359
    - type: manhattan_spearman
      value: 7.9397069840018775
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
      value: 20.306030448858603
    - type: cos_sim_spearman
      value: 21.93220782551375
    - type: euclidean_pearson
      value: 3.878631934602361
    - type: euclidean_spearman
      value: 5.171796902725965
    - type: manhattan_pearson
      value: 7.13020644036815
    - type: manhattan_spearman
      value: 7.707315591498748
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
      value: 66.81873207478459
    - type: cos_sim_spearman
      value: 67.80273445636502
    - type: euclidean_pearson
      value: 70.60654682977268
    - type: euclidean_spearman
      value: 69.4566208379486
    - type: manhattan_pearson
      value: 70.9548461896642
    - type: manhattan_spearman
      value: 69.78323323058773
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
      value: 21.366487281202602
    - type: cos_sim_spearman
      value: 18.90627528698481
    - type: euclidean_pearson
      value: 2.3390998579461995
    - type: euclidean_spearman
      value: 4.151213674012541
    - type: manhattan_pearson
      value: 2.234831868844863
    - type: manhattan_spearman
      value: 4.555291328501442
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
      value: 20.73153177251085
    - type: cos_sim_spearman
      value: 16.3855949033176
    - type: euclidean_pearson
      value: 8.734648741714238
    - type: euclidean_spearman
      value: 10.75672244732182
    - type: manhattan_pearson
      value: 7.536654126608877
    - type: manhattan_spearman
      value: 8.330065460047296
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
      value: 26.618435024084253
    - type: cos_sim_spearman
      value: 23.488974089577816
    - type: euclidean_pearson
      value: 3.1310350304707866
    - type: euclidean_spearman
      value: 3.1242598481634665
    - type: manhattan_pearson
      value: 1.1096752982707008
    - type: manhattan_spearman
      value: 1.4591693078765848
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
      value: 59.17638344661753
    - type: cos_sim_spearman
      value: 59.636760071130865
    - type: euclidean_pearson
      value: 56.68753290255448
    - type: euclidean_spearman
      value: 57.613280258574484
    - type: manhattan_pearson
      value: 56.92312052723706
    - type: manhattan_spearman
      value: 57.76774918418505
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
      value: 10.322254716987457
    - type: cos_sim_spearman
      value: 11.0033092996862
    - type: euclidean_pearson
      value: 6.006926471684402
    - type: euclidean_spearman
      value: 10.972140246688376
    - type: manhattan_pearson
      value: 5.933298751861177
    - type: manhattan_spearman
      value: 11.030111585680233
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
      value: 43.38031880545056
    - type: cos_sim_spearman
      value: 43.05358201410913
    - type: euclidean_pearson
      value: 42.72327196362553
    - type: euclidean_spearman
      value: 42.55163899944477
    - type: manhattan_pearson
      value: 44.01557499780587
    - type: manhattan_spearman
      value: 43.12473221615855
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
      value: 4.291290504363136
    - type: cos_sim_spearman
      value: 14.912727487893479
    - type: euclidean_pearson
      value: 3.2855132112394485
    - type: euclidean_spearman
      value: 16.575204463951025
    - type: manhattan_pearson
      value: 3.2398776723465814
    - type: manhattan_spearman
      value: 16.841985772913855
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
      value: 4.102739498555817
    - type: cos_sim_spearman
      value: 3.818238576547375
    - type: euclidean_pearson
      value: 2.3181033496453556
    - type: euclidean_spearman
      value: 5.1826811802703565
    - type: manhattan_pearson
      value: 4.8006179265256455
    - type: manhattan_spearman
      value: 6.738401400306252
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
      value: 2.38765395226737
    - type: cos_sim_spearman
      value: 5.173899391162327
    - type: euclidean_pearson
      value: 3.0710263954769825
    - type: euclidean_spearman
      value: 5.04922290903982
    - type: manhattan_pearson
      value: 3.7826314109861703
    - type: manhattan_spearman
      value: 5.042238232170212
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
      value: 7.6735490672676345
    - type: cos_sim_spearman
      value: 3.3631215256878892
    - type: euclidean_pearson
      value: 4.64331702652217
    - type: euclidean_spearman
      value: 3.6129205171334324
    - type: manhattan_pearson
      value: 4.011231736076196
    - type: manhattan_spearman
      value: 3.233959766173701
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
      value: 0.06167614416104335
    - type: cos_sim_spearman
      value: 6.521685391703255
    - type: euclidean_pearson
      value: 4.884572579069032
    - type: euclidean_spearman
      value: 5.59058032900239
    - type: manhattan_pearson
      value: 6.139838096573897
    - type: manhattan_spearman
      value: 5.0060884837066215
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
      value: 53.19490347682836
    - type: cos_sim_spearman
      value: 54.56055727079527
    - type: euclidean_pearson
      value: 52.55574442039842
    - type: euclidean_spearman
      value: 52.94640154371587
    - type: manhattan_pearson
      value: 53.275993040454196
    - type: manhattan_spearman
      value: 53.174561503510155
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
      value: 51.151158530122146
    - type: cos_sim_spearman
      value: 53.926925081736655
    - type: euclidean_pearson
      value: 44.55629287737235
    - type: euclidean_spearman
      value: 46.222372143731384
    - type: manhattan_pearson
      value: 42.831322151459005
    - type: manhattan_spearman
      value: 45.70991764985799
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
      value: 30.36194885126792
    - type: cos_sim_spearman
      value: 32.739632941633836
    - type: euclidean_pearson
      value: 29.83135800843496
    - type: euclidean_spearman
      value: 31.114406001326923
    - type: manhattan_pearson
      value: 31.264502938148286
    - type: manhattan_spearman
      value: 33.3112040753475
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
      value: 35.23883630335275
    - type: cos_sim_spearman
      value: 33.67797082086704
    - type: euclidean_pearson
      value: 34.878640693874544
    - type: euclidean_spearman
      value: 33.525189235133496
    - type: manhattan_pearson
      value: 34.22761246389947
    - type: manhattan_spearman
      value: 32.713218497609176
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
      value: 19.809302548119547
    - type: cos_sim_spearman
      value: 20.540370202115497
    - type: euclidean_pearson
      value: 23.006803962133016
    - type: euclidean_spearman
      value: 22.96270653079511
    - type: manhattan_pearson
      value: 25.40168317585851
    - type: manhattan_spearman
      value: 25.421508137540865
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
      value: 20.393500955410488
    - type: cos_sim_spearman
      value: 26.705713693011603
    - type: euclidean_pearson
      value: 18.168376767724585
    - type: euclidean_spearman
      value: 19.260826601517245
    - type: manhattan_pearson
      value: 18.302619990671527
    - type: manhattan_spearman
      value: 19.4691037846159
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
      value: 36.58919983075148
    - type: cos_sim_spearman
      value: 35.989722099974045
    - type: euclidean_pearson
      value: 41.045112547574206
    - type: euclidean_spearman
      value: 39.322301680629835
    - type: manhattan_pearson
      value: 41.36802503205308
    - type: manhattan_spearman
      value: 40.76270030293609
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
      value: 26.350936227950083
    - type: cos_sim_spearman
      value: 25.108218032460343
    - type: euclidean_pearson
      value: 28.61681094744849
    - type: euclidean_spearman
      value: 27.350990203943592
    - type: manhattan_pearson
      value: 30.527977072984513
    - type: manhattan_spearman
      value: 26.403339990640813
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
      value: 20.056269198600322
    - type: cos_sim_spearman
      value: 20.939990379746757
    - type: euclidean_pearson
      value: 18.942765438962198
    - type: euclidean_spearman
      value: 21.709842967237446
    - type: manhattan_pearson
      value: 23.643909798655123
    - type: manhattan_spearman
      value: 23.58828328071473
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
      value: 19.563740271419395
    - type: cos_sim_spearman
      value: 5.634361698190111
    - type: euclidean_pearson
      value: 16.833522619239474
    - type: euclidean_spearman
      value: 16.903085094570333
    - type: manhattan_pearson
      value: 5.805392712660814
    - type: manhattan_spearman
      value: 16.903085094570333
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
      value: 80.00905671833966
    - type: cos_sim_spearman
      value: 79.54269211027272
    - type: euclidean_pearson
      value: 79.51954544247441
    - type: euclidean_spearman
      value: 78.93670303434288
    - type: manhattan_pearson
      value: 79.47610653340678
    - type: manhattan_spearman
      value: 79.07344156719613
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
      value: 68.35710819755543
    - type: mrr
      value: 88.05442832403617
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
      value: 21.556
    - type: map_at_10
      value: 27.982000000000003
    - type: map_at_100
      value: 28.937
    - type: map_at_1000
      value: 29.058
    - type: map_at_3
      value: 25.644
    - type: map_at_5
      value: 26.996
    - type: ndcg_at_1
      value: 23.333000000000002
    - type: ndcg_at_10
      value: 31.787
    - type: ndcg_at_100
      value: 36.647999999999996
    - type: ndcg_at_1000
      value: 39.936
    - type: ndcg_at_3
      value: 27.299
    - type: ndcg_at_5
      value: 29.659000000000002
    - type: precision_at_1
      value: 23.333000000000002
    - type: precision_at_10
      value: 4.867
    - type: precision_at_100
      value: 0.743
    - type: precision_at_1000
      value: 0.10200000000000001
    - type: precision_at_3
      value: 11.333
    - type: precision_at_5
      value: 8.133
    - type: recall_at_1
      value: 21.556
    - type: recall_at_10
      value: 42.333
    - type: recall_at_100
      value: 65.706
    - type: recall_at_1000
      value: 91.489
    - type: recall_at_3
      value: 30.361
    - type: recall_at_5
      value: 36.222
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
      value: 99.49306930693069
    - type: cos_sim_ap
      value: 77.7308550291728
    - type: cos_sim_f1
      value: 71.78978681209718
    - type: cos_sim_precision
      value: 71.1897738446411
    - type: cos_sim_recall
      value: 72.39999999999999
    - type: dot_accuracy
      value: 99.08118811881188
    - type: dot_ap
      value: 30.267748833368234
    - type: dot_f1
      value: 34.335201222618444
    - type: dot_precision
      value: 34.994807892004154
    - type: dot_recall
      value: 33.7
    - type: euclidean_accuracy
      value: 99.51683168316832
    - type: euclidean_ap
      value: 78.64498778235628
    - type: euclidean_f1
      value: 73.09149972929075
    - type: euclidean_precision
      value: 79.69303423848878
    - type: euclidean_recall
      value: 67.5
    - type: manhattan_accuracy
      value: 99.53168316831683
    - type: manhattan_ap
      value: 79.45274878693958
    - type: manhattan_f1
      value: 74.19863373620599
    - type: manhattan_precision
      value: 78.18383167220377
    - type: manhattan_recall
      value: 70.6
    - type: max_accuracy
      value: 99.53168316831683
    - type: max_ap
      value: 79.45274878693958
    - type: max_f1
      value: 74.19863373620599
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
      value: 44.59127540530939
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
      value: 28.230204578753636
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
      value: 39.96520488022785
    - type: mrr
      value: 40.189248047703934
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
      value: 30.56303767714449
    - type: cos_sim_spearman
      value: 30.256847004390487
    - type: dot_pearson
      value: 29.453520030995005
    - type: dot_spearman
      value: 29.561732550926777
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
      value: 0.11299999999999999
    - type: map_at_10
      value: 0.733
    - type: map_at_100
      value: 3.313
    - type: map_at_1000
      value: 7.355
    - type: map_at_3
      value: 0.28200000000000003
    - type: map_at_5
      value: 0.414
    - type: ndcg_at_1
      value: 42.0
    - type: ndcg_at_10
      value: 39.31
    - type: ndcg_at_100
      value: 26.904
    - type: ndcg_at_1000
      value: 23.778
    - type: ndcg_at_3
      value: 42.775999999999996
    - type: ndcg_at_5
      value: 41.554
    - type: precision_at_1
      value: 48.0
    - type: precision_at_10
      value: 43.0
    - type: precision_at_100
      value: 27.08
    - type: precision_at_1000
      value: 11.014
    - type: precision_at_3
      value: 48.0
    - type: precision_at_5
      value: 45.6
    - type: recall_at_1
      value: 0.11299999999999999
    - type: recall_at_10
      value: 0.976
    - type: recall_at_100
      value: 5.888
    - type: recall_at_1000
      value: 22.634999999999998
    - type: recall_at_3
      value: 0.329
    - type: recall_at_5
      value: 0.518
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
      value: 0.645
    - type: map_at_10
      value: 4.1160000000000005
    - type: map_at_100
      value: 7.527
    - type: map_at_1000
      value: 8.677999999999999
    - type: map_at_3
      value: 1.6019999999999999
    - type: map_at_5
      value: 2.6
    - type: ndcg_at_1
      value: 10.204
    - type: ndcg_at_10
      value: 12.27
    - type: ndcg_at_100
      value: 22.461000000000002
    - type: ndcg_at_1000
      value: 33.543
    - type: ndcg_at_3
      value: 9.982000000000001
    - type: ndcg_at_5
      value: 11.498
    - type: precision_at_1
      value: 10.204
    - type: precision_at_10
      value: 12.245000000000001
    - type: precision_at_100
      value: 5.286
    - type: precision_at_1000
      value: 1.2630000000000001
    - type: precision_at_3
      value: 10.884
    - type: precision_at_5
      value: 13.061
    - type: recall_at_1
      value: 0.645
    - type: recall_at_10
      value: 8.996
    - type: recall_at_100
      value: 33.666000000000004
    - type: recall_at_1000
      value: 67.704
    - type: recall_at_3
      value: 2.504
    - type: recall_at_5
      value: 4.95
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
      value: 62.7862
    - type: ap
      value: 10.958454618347831
    - type: f1
      value: 48.37243417046763
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
      value: 54.821731748726656
    - type: f1
      value: 55.14729314789282
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
      value: 28.24295128553035
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
      value: 81.5640460153782
    - type: cos_sim_ap
      value: 57.094095366921536
    - type: cos_sim_f1
      value: 55.29607083563918
    - type: cos_sim_precision
      value: 47.62631077216397
    - type: cos_sim_recall
      value: 65.91029023746702
    - type: dot_accuracy
      value: 78.81623651427549
    - type: dot_ap
      value: 47.42989400382077
    - type: dot_f1
      value: 51.25944584382871
    - type: dot_precision
      value: 42.55838271174625
    - type: dot_recall
      value: 64.43271767810026
    - type: euclidean_accuracy
      value: 80.29445073612685
    - type: euclidean_ap
      value: 53.42012231336148
    - type: euclidean_f1
      value: 51.867783563504645
    - type: euclidean_precision
      value: 45.4203013481364
    - type: euclidean_recall
      value: 60.4485488126649
    - type: manhattan_accuracy
      value: 80.2884901949097
    - type: manhattan_ap
      value: 53.43205271323232
    - type: manhattan_f1
      value: 52.014165559982295
    - type: manhattan_precision
      value: 44.796035074342356
    - type: manhattan_recall
      value: 62.00527704485488
    - type: max_accuracy
      value: 81.5640460153782
    - type: max_ap
      value: 57.094095366921536
    - type: max_f1
      value: 55.29607083563918
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
      value: 86.63018589668955
    - type: cos_sim_ap
      value: 80.51063771262909
    - type: cos_sim_f1
      value: 72.70810586950793
    - type: cos_sim_precision
      value: 71.14123627790467
    - type: cos_sim_recall
      value: 74.3455497382199
    - type: dot_accuracy
      value: 82.41743315092948
    - type: dot_ap
      value: 69.2393381283664
    - type: dot_f1
      value: 65.61346624814597
    - type: dot_precision
      value: 59.43260638630257
    - type: dot_recall
      value: 73.22913458577148
    - type: euclidean_accuracy
      value: 86.49435324251951
    - type: euclidean_ap
      value: 80.28100477250926
    - type: euclidean_f1
      value: 72.58242344489099
    - type: euclidean_precision
      value: 67.44662568576906
    - type: euclidean_recall
      value: 78.56482907299045
    - type: manhattan_accuracy
      value: 86.59525749990297
    - type: manhattan_ap
      value: 80.37850832566262
    - type: manhattan_f1
      value: 72.59435321233073
    - type: manhattan_precision
      value: 68.19350473612991
    - type: manhattan_recall
      value: 77.60240221743148
    - type: max_accuracy
      value: 86.63018589668955
    - type: max_ap
      value: 80.51063771262909
    - type: max_f1
      value: 72.70810586950793
---

# SGPT-125M-weightedmean-nli-bitfit

## Usage

For usage instructions, refer to our codebase: https://github.com/Muennighoff/sgpt 

## Evaluation Results

For eval results, refer to the eval folder or our paper: https://arxiv.org/abs/2202.08904

## Training
The model was trained with the parameters:

**DataLoader**:

`sentence_transformers.datasets.NoDuplicatesDataLoader.NoDuplicatesDataLoader` of length 8807 with parameters:
```
{'batch_size': 64}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 1,
    "evaluation_steps": 880,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 0.0002
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 881,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 75, 'do_lower_case': False}) with Transformer model: GPTNeoModel 
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
