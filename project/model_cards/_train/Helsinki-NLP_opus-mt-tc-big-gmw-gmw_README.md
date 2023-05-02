---
language:
- af
- de
- en
- fy
- gos
- lb
- nds
- nl

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-gmw-gmw
  results:
  - task:
      name: Translation afr-deu
      type: translation
      args: afr-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: afr deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.2
       - name: chr-F
         type: chrf
         value: 0.58718
  - task:
      name: Translation afr-eng
      type: translation
      args: afr-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: afr eng devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 55.1
       - name: chr-F
         type: chrf
         value: 0.74826
  - task:
      name: Translation afr-ltz
      type: translation
      args: afr-ltz
    dataset:
      name: flores101-devtest
      type: flores_101
      args: afr ltz devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 15.7
       - name: chr-F
         type: chrf
         value: 0.46826
  - task:
      name: Translation afr-nld
      type: translation
      args: afr-nld
    dataset:
      name: flores101-devtest
      type: flores_101
      args: afr nld devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.5
       - name: chr-F
         type: chrf
         value: 0.54441
  - task:
      name: Translation deu-afr
      type: translation
      args: deu-afr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu afr devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.4
       - name: chr-F
         type: chrf
         value: 0.57835
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu eng devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 41.8
       - name: chr-F
         type: chrf
         value: 0.66990
  - task:
      name: Translation deu-ltz
      type: translation
      args: deu-ltz
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu ltz devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.3
       - name: chr-F
         type: chrf
         value: 0.52554
  - task:
      name: Translation deu-nld
      type: translation
      args: deu-nld
    dataset:
      name: flores101-devtest
      type: flores_101
      args: deu nld devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.2
       - name: chr-F
         type: chrf
         value: 0.55710
  - task:
      name: Translation eng-afr
      type: translation
      args: eng-afr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng afr devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 40.7
       - name: chr-F
         type: chrf
         value: 0.68429
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 38.5
       - name: chr-F
         type: chrf
         value: 0.64888
  - task:
      name: Translation eng-ltz
      type: translation
      args: eng-ltz
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng ltz devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.4
       - name: chr-F
         type: chrf
         value: 0.49231
  - task:
      name: Translation eng-nld
      type: translation
      args: eng-nld
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng nld devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.8
       - name: chr-F
         type: chrf
         value: 0.57984
  - task:
      name: Translation ltz-afr
      type: translation
      args: ltz-afr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ltz afr devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.2
       - name: chr-F
         type: chrf
         value: 0.53623
  - task:
      name: Translation ltz-deu
      type: translation
      args: ltz-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ltz deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.0
       - name: chr-F
         type: chrf
         value: 0.59122
  - task:
      name: Translation ltz-eng
      type: translation
      args: ltz-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ltz eng devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.0
       - name: chr-F
         type: chrf
         value: 0.57557
  - task:
      name: Translation ltz-nld
      type: translation
      args: ltz-nld
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ltz nld devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.6
       - name: chr-F
         type: chrf
         value: 0.49312
  - task:
      name: Translation nld-afr
      type: translation
      args: nld-afr
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nld afr devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.0
       - name: chr-F
         type: chrf
         value: 0.52409
  - task:
      name: Translation nld-deu
      type: translation
      args: nld-deu
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nld deu devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.6
       - name: chr-F
         type: chrf
         value: 0.53898
  - task:
      name: Translation nld-eng
      type: translation
      args: nld-eng
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nld eng devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.7
       - name: chr-F
         type: chrf
         value: 0.58970
  - task:
      name: Translation nld-ltz
      type: translation
      args: nld-ltz
    dataset:
      name: flores101-devtest
      type: flores_101
      args: nld ltz devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 11.8
       - name: chr-F
         type: chrf
         value: 0.42637
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 39.9
       - name: chr-F
         type: chrf
         value: 0.60928
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 35.4
       - name: chr-F
         type: chrf
         value: 0.64172
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: multi30k_test_2017_flickr
      type: multi30k-2017_flickr
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 40.5
       - name: chr-F
         type: chrf
         value: 0.63154
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: multi30k_test_2017_flickr
      type: multi30k-2017_flickr
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 34.2
       - name: chr-F
         type: chrf
         value: 0.63078
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: multi30k_test_2017_mscoco
      type: multi30k-2017_mscoco
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 32.2
       - name: chr-F
         type: chrf
         value: 0.55708
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: multi30k_test_2017_mscoco
      type: multi30k-2017_mscoco
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 29.1
       - name: chr-F
         type: chrf
         value: 0.57537
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 36.9
       - name: chr-F
         type: chrf
         value: 0.59422
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 30.0
       - name: chr-F
         type: chrf
         value: 0.59597
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: news-test2008
      type: news-test2008
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 27.2
       - name: chr-F
         type: chrf
         value: 0.54601
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: news-test2008
      type: news-test2008
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 23.6
       - name: chr-F
         type: chrf
         value: 0.53149
  - task:
      name: Translation afr-deu
      type: translation
      args: afr-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: afr-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 50.4
       - name: chr-F
         type: chrf
         value: 0.68679
  - task:
      name: Translation afr-eng
      type: translation
      args: afr-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: afr-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 56.6
       - name: chr-F
         type: chrf
         value: 0.70682
  - task:
      name: Translation afr-nld
      type: translation
      args: afr-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: afr-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 55.5
       - name: chr-F
         type: chrf
         value: 0.71516
  - task:
      name: Translation deu-afr
      type: translation
      args: deu-afr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-afr
    metrics:
       - name: BLEU
         type: bleu
         value: 54.3
       - name: chr-F
         type: chrf
         value: 0.70274
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 48.6
       - name: chr-F
         type: chrf
         value: 0.66023
  - task:
      name: Translation deu-nds
      type: translation
      args: deu-nds
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-nds
    metrics:
       - name: BLEU
         type: bleu
         value: 23.2
       - name: chr-F
         type: chrf
         value: 0.48058
  - task:
      name: Translation deu-nld
      type: translation
      args: deu-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: deu-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 54.6
       - name: chr-F
         type: chrf
         value: 0.71440
  - task:
      name: Translation eng-afr
      type: translation
      args: eng-afr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-afr
    metrics:
       - name: BLEU
         type: bleu
         value: 56.5
       - name: chr-F
         type: chrf
         value: 0.71995
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 42.0
       - name: chr-F
         type: chrf
         value: 0.63103
  - task:
      name: Translation eng-fry
      type: translation
      args: eng-fry
    dataset:
      name: tatoeba-test-v2021-03-30
      type: tatoeba_mt
      args: eng-fry
    metrics:
       - name: BLEU
         type: bleu
         value: 21.3
       - name: chr-F
         type: chrf
         value: 0.38580
  - task:
      name: Translation eng-nld
      type: translation
      args: eng-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 54.5
       - name: chr-F
         type: chrf
         value: 0.71062
  - task:
      name: Translation fry-eng
      type: translation
      args: fry-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fry-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 25.1
       - name: chr-F
         type: chrf
         value: 0.40545
  - task:
      name: Translation fry-nld
      type: translation
      args: fry-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fry-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 41.7
       - name: chr-F
         type: chrf
         value: 0.55771
  - task:
      name: Translation gos-deu
      type: translation
      args: gos-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: gos-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 25.4
       - name: chr-F
         type: chrf
         value: 0.45302
  - task:
      name: Translation gos-eng
      type: translation
      args: gos-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: gos-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 24.1
       - name: chr-F
         type: chrf
         value: 0.37628
  - task:
      name: Translation gos-nld
      type: translation
      args: gos-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: gos-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 26.2
       - name: chr-F
         type: chrf
         value: 0.45777
  - task:
      name: Translation ltz-deu
      type: translation
      args: ltz-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ltz-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 21.3
       - name: chr-F
         type: chrf
         value: 0.37165
  - task:
      name: Translation ltz-eng
      type: translation
      args: ltz-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ltz-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 30.3
       - name: chr-F
         type: chrf
         value: 0.37784
  - task:
      name: Translation ltz-nld
      type: translation
      args: ltz-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ltz-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 26.7
       - name: chr-F
         type: chrf
         value: 0.32823
  - task:
      name: Translation nds-deu
      type: translation
      args: nds-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nds-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 45.4
       - name: chr-F
         type: chrf
         value: 0.64008
  - task:
      name: Translation nds-eng
      type: translation
      args: nds-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nds-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 38.3
       - name: chr-F
         type: chrf
         value: 0.55193
  - task:
      name: Translation nds-nld
      type: translation
      args: nds-nld
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nds-nld
    metrics:
       - name: BLEU
         type: bleu
         value: 50.0
       - name: chr-F
         type: chrf
         value: 0.66943
  - task:
      name: Translation nld-afr
      type: translation
      args: nld-afr
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nld-afr
    metrics:
       - name: BLEU
         type: bleu
         value: 62.3
       - name: chr-F
         type: chrf
         value: 0.76610
  - task:
      name: Translation nld-deu
      type: translation
      args: nld-deu
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nld-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 56.8
       - name: chr-F
         type: chrf
         value: 0.73162
  - task:
      name: Translation nld-eng
      type: translation
      args: nld-eng
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nld-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 60.5
       - name: chr-F
         type: chrf
         value: 0.74088
  - task:
      name: Translation nld-fry
      type: translation
      args: nld-fry
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: nld-fry
    metrics:
       - name: BLEU
         type: bleu
         value: 31.4
       - name: chr-F
         type: chrf
         value: 0.48460
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.53747
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 22.9
       - name: chr-F
         type: chrf
         value: 0.53283
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 30.6
       - name: chr-F
         type: chrf
         value: 0.58355
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 25.8
       - name: chr-F
         type: chrf
         value: 0.54885
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 26.3
       - name: chr-F
         type: chrf
         value: 0.54883
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 23.1
       - name: chr-F
         type: chrf
         value: 0.52712
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 28.5
       - name: chr-F
         type: chrf
         value: 0.56153
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 23.3
       - name: chr-F
         type: chrf
         value: 0.52662
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 31.4
       - name: chr-F
         type: chrf
         value: 0.57770
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 27.8
       - name: chr-F
         type: chrf
         value: 0.55774
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 33.2
       - name: chr-F
         type: chrf
         value: 0.59826
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 29.0
       - name: chr-F
         type: chrf
         value: 0.59301
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 33.4
       - name: chr-F
         type: chrf
         value: 0.59660
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 32.3
       - name: chr-F
         type: chrf
         value: 0.59889
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 39.8
       - name: chr-F
         type: chrf
         value: 0.64736
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 38.3
       - name: chr-F
         type: chrf
         value: 0.64427
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 35.2
       - name: chr-F
         type: chrf
         value: 0.60933
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 30.7
       - name: chr-F
         type: chrf
         value: 0.59257
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 42.6
       - name: chr-F
         type: chrf
         value: 0.66797
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 46.5
       - name: chr-F
         type: chrf
         value: 0.69605
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 39.7
       - name: chr-F
         type: chrf
         value: 0.63749
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 42.9
       - name: chr-F
         type: chrf
         value: 0.66751
  - task:
      name: Translation deu-eng
      type: translation
      args: deu-eng
    dataset:
      name: newstest2020
      type: wmt-2020-news
      args: deu-eng
    metrics:
       - name: BLEU
         type: bleu
         value: 35.0
       - name: chr-F
         type: chrf
         value: 0.61200
  - task:
      name: Translation eng-deu
      type: translation
      args: eng-deu
    dataset:
      name: newstest2020
      type: wmt-2020-news
      args: eng-deu
    metrics:
       - name: BLEU
         type: bleu
         value: 32.3
       - name: chr-F
         type: chrf
         value: 0.60411
---
# opus-mt-tc-big-gmw-gmw

## Table of Contents
- [Model Details](#model-details)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Training](#training)
- [Evaluation](#evaluation)
- [Citation Information](#citation-information)
- [Acknowledgements](#acknowledgements)

## Model Details

Neural machine translation model for translating from West Germanic languages (gmw) to West Germanic languages (gmw).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-11
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): afr deu eng enm fry gos gsw hrx ksh ltz nds nld pdc sco stq swg tpi yid
  - Target Language(s): afr ang deu eng enm fry gos ltz nds nld sco tpi yid
  - Language Pair(s): afr-deu afr-eng afr-nld deu-afr deu-eng deu-ltz deu-nds deu-nld eng-afr eng-deu eng-fry eng-nld fry-eng fry-nld gos-deu gos-eng gos-nld ltz-afr ltz-deu ltz-eng ltz-nld nds-deu nds-eng nds-nld nld-afr nld-deu nld-eng nld-fry
  - Valid Target Language Labels: >>act<< >>afr<< >>afs<< >>aig<< >>ang<< >>ang_Latn<< >>bah<< >>bar<< >>bis<< >>bjs<< >>brc<< >>bzj<< >>bzj_Latn<< >>bzk<< >>cim<< >>dcr<< >>deu<< >>djk<< >>djk_Latn<< >>drt<< >>drt_Latn<< >>dum<< >>eng<< >>enm<< >>enm_Latn<< >>fpe<< >>frk<< >>frr<< >>fry<< >>gcl<< >>gct<< >>geh<< >>gmh<< >>gml<< >>goh<< >>gos<< >>gpe<< >>gsw<< >>gul<< >>gyn<< >>hrx<< >>hrx_Latn<< >>hwc<< >>icr<< >>jam<< >>jvd<< >>kri<< >>ksh<< >>kww<< >>lim<< >>lng<< >>ltz<< >>mhn<< >>nds<< >>nld<< >>odt<< >>ofs<< >>ofs_Latn<< >>oor<< >>osx<< >>pcm<< >>pdc<< >>pdt<< >>pey<< >>pfl<< >>pih<< >>pih_Latn<< >>pis<< >>pis_Latn<< >>qlm<< >>rop<< >>sco<< >>sdz<< >>skw<< >>sli<< >>srm<< >>srm_Latn<< >>srn<< >>stl<< >>stq<< >>svc<< >>swg<< >>sxu<< >>tch<< >>tcs<< >>tgh<< >>tpi<< >>trf<< >>twd<< >>uln<< >>vel<< >>vic<< >>vls<< >>vmf<< >>wae<< >>wep<< >>wes<< >>wes_Latn<< >>wym<< >>ydd<< >>yec<< >>yid<< >>yih<< >>zea<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-11.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opusTCv20210807_transformer-big_2022-08-11.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT gmw-gmw README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmw-gmw/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>afr<<`

## Uses

This model can be used for translation and text-to-text generation.

## Risks, Limitations and Biases

**CONTENT WARNING: Readers should be aware that the model is trained on various public data sets that may contain content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).

## How to Get Started With the Model

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>nds<< Red keinen Quatsch.",
    ">>eng<< Findet ihr das nicht etwas übereilt?"
]

model_name = "pytorch-models/opus-mt-tc-big-gmw-gmw"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Kiek ok bi: Rott.
#     Aren't you in a hurry?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-gmw-gmw")
print(pipe(">>nds<< Red keinen Quatsch."))

# expected output: Kiek ok bi: Rott.
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-11.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opusTCv20210807_transformer-big_2022-08-11.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-11.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opusTCv20210807_transformer-big_2022-08-11.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-11.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opusTCv20210807_transformer-big_2022-08-11.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| afr-deu | tatoeba-test-v2021-08-07 | 0.68679 | 50.4 | 1583 | 9105 |
| afr-eng | tatoeba-test-v2021-08-07 | 0.70682 | 56.6 | 1374 | 9622 |
| afr-nld | tatoeba-test-v2021-08-07 | 0.71516 | 55.5 | 1056 | 6710 |
| deu-afr | tatoeba-test-v2021-08-07 | 0.70274 | 54.3 | 1583 | 9507 |
| deu-eng | tatoeba-test-v2021-08-07 | 0.66023 | 48.6 | 17565 | 149462 |
| deu-nds | tatoeba-test-v2021-08-07 | 0.48058 | 23.2 | 9999 | 76137 |
| deu-nld | tatoeba-test-v2021-08-07 | 0.71440 | 54.6 | 10218 | 75235 |
| deu-yid | tatoeba-test-v2021-08-07 | 9.211 | 0.4 | 853 | 5355 |
| eng-afr | tatoeba-test-v2021-08-07 | 0.71995 | 56.5 | 1374 | 10317 |
| eng-deu | tatoeba-test-v2021-08-07 | 0.63103 | 42.0 | 17565 | 151568 |
| eng-nld | tatoeba-test-v2021-08-07 | 0.71062 | 54.5 | 12696 | 91796 |
| eng-yid | tatoeba-test-v2021-08-07 | 9.624 | 0.4 | 2483 | 16395 |
| fry-eng | tatoeba-test-v2021-08-07 | 0.40545 | 25.1 | 220 | 1573 |
| fry-nld | tatoeba-test-v2021-08-07 | 0.55771 | 41.7 | 260 | 1854 |
| gos-deu | tatoeba-test-v2021-08-07 | 0.45302 | 25.4 | 207 | 1168 |
| gos-eng | tatoeba-test-v2021-08-07 | 0.37628 | 24.1 | 1154 | 5635 |
| gos-nld | tatoeba-test-v2021-08-07 | 0.45777 | 26.2 | 1852 | 9903 |
| ltz-deu | tatoeba-test-v2021-08-07 | 0.37165 | 21.3 | 347 | 2208 |
| ltz-eng | tatoeba-test-v2021-08-07 | 0.37784 | 30.3 | 293 | 1840 |
| ltz-nld | tatoeba-test-v2021-08-07 | 0.32823 | 26.7 | 292 | 1685 |
| nds-deu | tatoeba-test-v2021-08-07 | 0.64008 | 45.4 | 9999 | 74564 |
| nds-eng | tatoeba-test-v2021-08-07 | 0.55193 | 38.3 | 2500 | 17589 |
| nds-nld | tatoeba-test-v2021-08-07 | 0.66943 | 50.0 | 1657 | 11490 |
| nld-afr | tatoeba-test-v2021-08-07 | 0.76610 | 62.3 | 1056 | 6823 |
| nld-deu | tatoeba-test-v2021-08-07 | 0.73162 | 56.8 | 10218 | 74131 |
| nld-eng | tatoeba-test-v2021-08-07 | 0.74088 | 60.5 | 12696 | 89978 |
| nld-fry | tatoeba-test-v2021-08-07 | 0.48460 | 31.4 | 260 | 1857 |
| nld-nds | tatoeba-test-v2021-08-07 | 0.43779 | 19.9 | 1657 | 11711 |
| swg-deu | tatoeba-test-v2021-08-07 | 0.40348 | 16.1 | 1523 | 15632 |
| yid-deu | tatoeba-test-v2021-08-07 | 6.305 | 0.1 | 853 | 5173 |
| yid-eng | tatoeba-test-v2021-08-07 | 3.704 | 0.1 | 2483 | 15452 |
| afr-deu | flores101-devtest | 0.58718 | 30.2 | 1012 | 25094 |
| afr-eng | flores101-devtest | 0.74826 | 55.1 | 1012 | 24721 |
| afr-ltz | flores101-devtest | 0.46826 | 15.7 | 1012 | 25087 |
| afr-nld | flores101-devtest | 0.54441 | 22.5 | 1012 | 25467 |
| deu-afr | flores101-devtest | 0.57835 | 26.4 | 1012 | 25740 |
| deu-eng | flores101-devtest | 0.66990 | 41.8 | 1012 | 24721 |
| deu-ltz | flores101-devtest | 0.52554 | 20.3 | 1012 | 25087 |
| deu-nld | flores101-devtest | 0.55710 | 24.2 | 1012 | 25467 |
| eng-afr | flores101-devtest | 0.68429 | 40.7 | 1012 | 25740 |
| eng-deu | flores101-devtest | 0.64888 | 38.5 | 1012 | 25094 |
| eng-ltz | flores101-devtest | 0.49231 | 18.4 | 1012 | 25087 |
| eng-nld | flores101-devtest | 0.57984 | 26.8 | 1012 | 25467 |
| ltz-afr | flores101-devtest | 0.53623 | 23.2 | 1012 | 25740 |
| ltz-deu | flores101-devtest | 0.59122 | 30.0 | 1012 | 25094 |
| ltz-eng | flores101-devtest | 0.57557 | 31.0 | 1012 | 24721 |
| ltz-nld | flores101-devtest | 0.49312 | 18.6 | 1012 | 25467 |
| nld-afr | flores101-devtest | 0.52409 | 20.0 | 1012 | 25740 |
| nld-deu | flores101-devtest | 0.53898 | 22.6 | 1012 | 25094 |
| nld-eng | flores101-devtest | 0.58970 | 30.7 | 1012 | 24721 |
| nld-ltz | flores101-devtest | 0.42637 | 11.8 | 1012 | 25087 |
| deu-eng | multi30k_test_2016_flickr | 0.60928 | 39.9 | 1000 | 12955 |
| eng-deu | multi30k_test_2016_flickr | 0.64172 | 35.4 | 1000 | 12106 |
| deu-eng | multi30k_test_2017_flickr | 0.63154 | 40.5 | 1000 | 11374 |
| eng-deu | multi30k_test_2017_flickr | 0.63078 | 34.2 | 1000 | 10755 |
| deu-eng | multi30k_test_2017_mscoco | 0.55708 | 32.2 | 461 | 5231 |
| eng-deu | multi30k_test_2017_mscoco | 0.57537 | 29.1 | 461 | 5158 |
| deu-eng | multi30k_test_2018_flickr | 0.59422 | 36.9 | 1071 | 14689 |
| eng-deu | multi30k_test_2018_flickr | 0.59597 | 30.0 | 1071 | 13703 |
| deu-eng | newssyscomb2009 | 0.54993 | 28.2 | 502 | 11818 |
| eng-deu | newssyscomb2009 | 0.53867 | 23.2 | 502 | 11271 |
| deu-eng | news-test2008 | 0.54601 | 27.2 | 2051 | 49380 |
| eng-deu | news-test2008 | 0.53149 | 23.6 | 2051 | 47447 |
| deu-eng | newstest2009 | 0.53747 | 25.9 | 2525 | 65399 |
| eng-deu | newstest2009 | 0.53283 | 22.9 | 2525 | 62816 |
| deu-eng | newstest2010 | 0.58355 | 30.6 | 2489 | 61711 |
| eng-deu | newstest2010 | 0.54885 | 25.8 | 2489 | 61503 |
| deu-eng | newstest2011 | 0.54883 | 26.3 | 3003 | 74681 |
| eng-deu | newstest2011 | 0.52712 | 23.1 | 3003 | 72981 |
| deu-eng | newstest2012 | 0.56153 | 28.5 | 3003 | 72812 |
| eng-deu | newstest2012 | 0.52662 | 23.3 | 3003 | 72886 |
| deu-eng | newstest2013 | 0.57770 | 31.4 | 3000 | 64505 |
| eng-deu | newstest2013 | 0.55774 | 27.8 | 3000 | 63737 |
| deu-eng | newstest2014 | 0.59826 | 33.2 | 3003 | 67337 |
| eng-deu | newstest2014 | 0.59301 | 29.0 | 3003 | 62688 |
| deu-eng | newstest2015 | 0.59660 | 33.4 | 2169 | 46443 |
| eng-deu | newstest2015 | 0.59889 | 32.3 | 2169 | 44260 |
| deu-eng | newstest2016 | 0.64736 | 39.8 | 2999 | 64119 |
| eng-deu | newstest2016 | 0.64427 | 38.3 | 2999 | 62669 |
| deu-eng | newstest2017 | 0.60933 | 35.2 | 3004 | 64399 |
| eng-deu | newstest2017 | 0.59257 | 30.7 | 3004 | 61287 |
| deu-eng | newstest2018 | 0.66797 | 42.6 | 2998 | 67012 |
| eng-deu | newstest2018 | 0.69605 | 46.5 | 2998 | 64276 |
| deu-eng | newstest2019 | 0.63749 | 39.7 | 2000 | 39227 |
| eng-deu | newstest2019 | 0.66751 | 42.9 | 1997 | 48746 |
| deu-eng | newstest2020 | 0.61200 | 35.0 | 785 | 38220 |
| eng-deu | newstest2020 | 0.60411 | 32.3 | 1418 | 52383 |
| deu-eng | newstestB2020 | 0.61255 | 35.1 | 785 | 37696 |
| eng-deu | newstestB2020 | 0.59513 | 31.8 | 1418 | 53092 |

## Citation Information

* Publications: [OPUS-MT – Building open translation services for the World](https://aclanthology.org/2020.eamt-1.61/) and [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/) (Please, cite if you use this model.)

```
@inproceedings{tiedemann-thottingal-2020-opus,
    title = "{OPUS}-{MT} {--} Building open translation services for the World",
    author = {Tiedemann, J{\"o}rg  and Thottingal, Santhosh},
    booktitle = "Proceedings of the 22nd Annual Conference of the European Association for Machine Translation",
    month = nov,
    year = "2020",
    address = "Lisboa, Portugal",
    publisher = "European Association for Machine Translation",
    url = "https://aclanthology.org/2020.eamt-1.61",
    pages = "479--480",
}

@inproceedings{tiedemann-2020-tatoeba,
    title = "The Tatoeba Translation Challenge {--} Realistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.wmt-1.139",
    pages = "1174--1182",
}
```

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 8b9f0b0
* port time: Fri Aug 12 23:58:31 EEST 2022
* port machine: LM0-400-22516.local
