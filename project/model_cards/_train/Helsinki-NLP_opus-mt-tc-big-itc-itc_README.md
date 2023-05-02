---
language:
- ast
- ca
- es
- fr
- gl
- it
- lad
- oc
- pms
- pt
- ro

tags:
- translation
- opus-mt-tc

license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-itc-itc
  results:
  - task:
      name: Translation ast-cat
      type: translation
      args: ast-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.8
       - name: chr-F
         type: chrf
         value: 0.57870
  - task:
      name: Translation ast-fra
      type: translation
      args: ast-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.1
       - name: chr-F
         type: chrf
         value: 0.56761
  - task:
      name: Translation ast-glg
      type: translation
      args: ast-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.9
       - name: chr-F
         type: chrf
         value: 0.55161
  - task:
      name: Translation ast-ita
      type: translation
      args: ast-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.1
       - name: chr-F
         type: chrf
         value: 0.51764
  - task:
      name: Translation ast-oci
      type: translation
      args: ast-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.6
       - name: chr-F
         type: chrf
         value: 0.49545
  - task:
      name: Translation ast-por
      type: translation
      args: ast-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 31.5
       - name: chr-F
         type: chrf
         value: 0.57347
  - task:
      name: Translation ast-ron
      type: translation
      args: ast-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.8
       - name: chr-F
         type: chrf
         value: 0.52317
  - task:
      name: Translation ast-spa
      type: translation
      args: ast-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ast spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.2
       - name: chr-F
         type: chrf
         value: 0.49741
  - task:
      name: Translation cat-ast
      type: translation
      args: cat-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.7
       - name: chr-F
         type: chrf
         value: 0.56754
  - task:
      name: Translation cat-fra
      type: translation
      args: cat-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 38.4
       - name: chr-F
         type: chrf
         value: 0.63368
  - task:
      name: Translation cat-glg
      type: translation
      args: cat-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.2
       - name: chr-F
         type: chrf
         value: 0.59596
  - task:
      name: Translation cat-ita
      type: translation
      args: cat-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.3
       - name: chr-F
         type: chrf
         value: 0.55886
  - task:
      name: Translation cat-oci
      type: translation
      args: cat-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.6
       - name: chr-F
         type: chrf
         value: 0.54285
  - task:
      name: Translation cat-por
      type: translation
      args: cat-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 37.7
       - name: chr-F
         type: chrf
         value: 0.62913
  - task:
      name: Translation cat-ron
      type: translation
      args: cat-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.5
       - name: chr-F
         type: chrf
         value: 0.56885
  - task:
      name: Translation cat-spa
      type: translation
      args: cat-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: cat spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.6
       - name: chr-F
         type: chrf
         value: 0.53372
  - task:
      name: Translation fra-ast
      type: translation
      args: fra-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.7
       - name: chr-F
         type: chrf
         value: 0.52696
  - task:
      name: Translation fra-cat
      type: translation
      args: fra-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 34.6
       - name: chr-F
         type: chrf
         value: 0.60492
  - task:
      name: Translation fra-glg
      type: translation
      args: fra-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.3
       - name: chr-F
         type: chrf
         value: 0.57485
  - task:
      name: Translation fra-ita
      type: translation
      args: fra-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.3
       - name: chr-F
         type: chrf
         value: 0.56493
  - task:
      name: Translation fra-oci
      type: translation
      args: fra-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.2
       - name: chr-F
         type: chrf
         value: 0.57449
  - task:
      name: Translation fra-por
      type: translation
      args: fra-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.9
       - name: chr-F
         type: chrf
         value: 0.62211
  - task:
      name: Translation fra-ron
      type: translation
      args: fra-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.4
       - name: chr-F
         type: chrf
         value: 0.56998
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: fra spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.2
       - name: chr-F
         type: chrf
         value: 0.52880
  - task:
      name: Translation glg-ast
      type: translation
      args: glg-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.4
       - name: chr-F
         type: chrf
         value: 0.55090
  - task:
      name: Translation glg-cat
      type: translation
      args: glg-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.6
       - name: chr-F
         type: chrf
         value: 0.60550
  - task:
      name: Translation glg-fra
      type: translation
      args: glg-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.0
       - name: chr-F
         type: chrf
         value: 0.62026
  - task:
      name: Translation glg-ita
      type: translation
      args: glg-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.55834
  - task:
      name: Translation glg-oci
      type: translation
      args: glg-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.9
       - name: chr-F
         type: chrf
         value: 0.52520
  - task:
      name: Translation glg-por
      type: translation
      args: glg-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.7
       - name: chr-F
         type: chrf
         value: 0.60027
  - task:
      name: Translation glg-ron
      type: translation
      args: glg-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.8
       - name: chr-F
         type: chrf
         value: 0.55621
  - task:
      name: Translation glg-spa
      type: translation
      args: glg-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: glg spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.4
       - name: chr-F
         type: chrf
         value: 0.53219
  - task:
      name: Translation ita-ast
      type: translation
      args: ita-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 17.1
       - name: chr-F
         type: chrf
         value: 0.50741
  - task:
      name: Translation ita-cat
      type: translation
      args: ita-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.9
       - name: chr-F
         type: chrf
         value: 0.57061
  - task:
      name: Translation ita-fra
      type: translation
      args: ita-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.0
       - name: chr-F
         type: chrf
         value: 0.60199
  - task:
      name: Translation ita-glg
      type: translation
      args: ita-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.9
       - name: chr-F
         type: chrf
         value: 0.55312
  - task:
      name: Translation ita-oci
      type: translation
      args: ita-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 18.1
       - name: chr-F
         type: chrf
         value: 0.48447
  - task:
      name: Translation ita-por
      type: translation
      args: ita-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.0
       - name: chr-F
         type: chrf
         value: 0.58162
  - task:
      name: Translation ita-ron
      type: translation
      args: ita-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.2
       - name: chr-F
         type: chrf
         value: 0.53703
  - task:
      name: Translation ita-spa
      type: translation
      args: ita-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ita spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.1
       - name: chr-F
         type: chrf
         value: 0.52238
  - task:
      name: Translation oci-ast
      type: translation
      args: oci-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.2
       - name: chr-F
         type: chrf
         value: 0.53010
  - task:
      name: Translation oci-cat
      type: translation
      args: oci-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.2
       - name: chr-F
         type: chrf
         value: 0.59946
  - task:
      name: Translation oci-fra
      type: translation
      args: oci-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 39.0
       - name: chr-F
         type: chrf
         value: 0.64290
  - task:
      name: Translation oci-glg
      type: translation
      args: oci-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.0
       - name: chr-F
         type: chrf
         value: 0.56737
  - task:
      name: Translation oci-ita
      type: translation
      args: oci-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.2
       - name: chr-F
         type: chrf
         value: 0.54220
  - task:
      name: Translation oci-por
      type: translation
      args: oci-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 35.7
       - name: chr-F
         type: chrf
         value: 0.62127
  - task:
      name: Translation oci-ron
      type: translation
      args: oci-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 28.0
       - name: chr-F
         type: chrf
         value: 0.55906
  - task:
      name: Translation oci-spa
      type: translation
      args: oci-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: oci spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.8
       - name: chr-F
         type: chrf
         value: 0.52110
  - task:
      name: Translation por-ast
      type: translation
      args: por-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.5
       - name: chr-F
         type: chrf
         value: 0.54539
  - task:
      name: Translation por-cat
      type: translation
      args: por-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.4
       - name: chr-F
         type: chrf
         value: 0.61809
  - task:
      name: Translation por-fra
      type: translation
      args: por-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 39.7
       - name: chr-F
         type: chrf
         value: 0.64343
  - task:
      name: Translation por-glg
      type: translation
      args: por-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 30.4
       - name: chr-F
         type: chrf
         value: 0.57965
  - task:
      name: Translation por-ita
      type: translation
      args: por-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 26.3
       - name: chr-F
         type: chrf
         value: 0.55841
  - task:
      name: Translation por-oci
      type: translation
      args: por-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.3
       - name: chr-F
         type: chrf
         value: 0.54829
  - task:
      name: Translation por-ron
      type: translation
      args: por-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.8
       - name: chr-F
         type: chrf
         value: 0.57283
  - task:
      name: Translation por-spa
      type: translation
      args: por-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: por spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.2
       - name: chr-F
         type: chrf
         value: 0.53513
  - task:
      name: Translation ron-ast
      type: translation
      args: ron-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 20.1
       - name: chr-F
         type: chrf
         value: 0.52265
  - task:
      name: Translation ron-cat
      type: translation
      args: ron-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 32.6
       - name: chr-F
         type: chrf
         value: 0.59689
  - task:
      name: Translation ron-fra
      type: translation
      args: ron-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 37.4
       - name: chr-F
         type: chrf
         value: 0.63060
  - task:
      name: Translation ron-glg
      type: translation
      args: ron-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 29.3
       - name: chr-F
         type: chrf
         value: 0.56677
  - task:
      name: Translation ron-ita
      type: translation
      args: ron-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.6
       - name: chr-F
         type: chrf
         value: 0.55485
  - task:
      name: Translation ron-oci
      type: translation
      args: ron-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.8
       - name: chr-F
         type: chrf
         value: 0.52433
  - task:
      name: Translation ron-por
      type: translation
      args: ron-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 36.1
       - name: chr-F
         type: chrf
         value: 0.61831
  - task:
      name: Translation ron-spa
      type: translation
      args: ron-spa
    dataset:
      name: flores101-devtest
      type: flores_101
      args: ron spa devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 24.1
       - name: chr-F
         type: chrf
         value: 0.52712
  - task:
      name: Translation spa-ast
      type: translation
      args: spa-ast
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa ast devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 15.7
       - name: chr-F
         type: chrf
         value: 0.49008
  - task:
      name: Translation spa-cat
      type: translation
      args: spa-cat
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa cat devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 23.2
       - name: chr-F
         type: chrf
         value: 0.53905
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa fra devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 27.4
       - name: chr-F
         type: chrf
         value: 0.57078
  - task:
      name: Translation spa-glg
      type: translation
      args: spa-glg
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa glg devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.0
       - name: chr-F
         type: chrf
         value: 0.52563
  - task:
      name: Translation spa-ita
      type: translation
      args: spa-ita
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa ita devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 22.3
       - name: chr-F
         type: chrf
         value: 0.52783
  - task:
      name: Translation spa-oci
      type: translation
      args: spa-oci
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa oci devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 16.3
       - name: chr-F
         type: chrf
         value: 0.48064
  - task:
      name: Translation spa-por
      type: translation
      args: spa-por
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa por devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 25.8
       - name: chr-F
         type: chrf
         value: 0.55736
  - task:
      name: Translation spa-ron
      type: translation
      args: spa-ron
    dataset:
      name: flores101-devtest
      type: flores_101
      args: spa ron devtest
    metrics:
       - name: BLEU
         type: bleu
         value: 21.4
       - name: chr-F
         type: chrf
         value: 0.51623
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: news-test2008
      type: news-test2008
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 33.9
       - name: chr-F
         type: chrf
         value: 0.58939
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: news-test2008
      type: news-test2008
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 32.4
       - name: chr-F
         type: chrf
         value: 0.58695
  - task:
      name: Translation cat-fra
      type: translation
      args: cat-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: cat-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 54.6
       - name: chr-F
         type: chrf
         value: 0.71201
  - task:
      name: Translation cat-ita
      type: translation
      args: cat-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: cat-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 58.4
       - name: chr-F
         type: chrf
         value: 0.74198
  - task:
      name: Translation cat-por
      type: translation
      args: cat-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: cat-por
    metrics:
       - name: BLEU
         type: bleu
         value: 57.4
       - name: chr-F
         type: chrf
         value: 0.74930
  - task:
      name: Translation cat-spa
      type: translation
      args: cat-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: cat-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 78.1
       - name: chr-F
         type: chrf
         value: 0.87844
  - task:
      name: Translation fra-cat
      type: translation
      args: fra-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 46.2
       - name: chr-F
         type: chrf
         value: 0.66525
  - task:
      name: Translation fra-ita
      type: translation
      args: fra-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 53.8
       - name: chr-F
         type: chrf
         value: 0.72742
  - task:
      name: Translation fra-por
      type: translation
      args: fra-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-por
    metrics:
       - name: BLEU
         type: bleu
         value: 48.6
       - name: chr-F
         type: chrf
         value: 0.68413
  - task:
      name: Translation fra-ron
      type: translation
      args: fra-ron
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 44.0
       - name: chr-F
         type: chrf
         value: 0.65009
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 54.8
       - name: chr-F
         type: chrf
         value: 0.72080
  - task:
      name: Translation glg-por
      type: translation
      args: glg-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: glg-por
    metrics:
       - name: BLEU
         type: bleu
         value: 61.1
       - name: chr-F
         type: chrf
         value: 0.76720
  - task:
      name: Translation glg-spa
      type: translation
      args: glg-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: glg-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 71.7
       - name: chr-F
         type: chrf
         value: 0.82362
  - task:
      name: Translation ita-cat
      type: translation
      args: ita-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 56.4
       - name: chr-F
         type: chrf
         value: 0.72529
  - task:
      name: Translation ita-fra
      type: translation
      args: ita-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 65.2
       - name: chr-F
         type: chrf
         value: 0.77932
  - task:
      name: Translation ita-por
      type: translation
      args: ita-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-por
    metrics:
       - name: BLEU
         type: bleu
         value: 54.0
       - name: chr-F
         type: chrf
         value: 0.72798
  - task:
      name: Translation ita-ron
      type: translation
      args: ita-ron
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 51.1
       - name: chr-F
         type: chrf
         value: 0.70814
  - task:
      name: Translation ita-spa
      type: translation
      args: ita-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ita-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 62.9
       - name: chr-F
         type: chrf
         value: 0.77455
  - task:
      name: Translation lad-spa
      type: translation
      args: lad-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: lad-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 34.7
       - name: chr-F
         type: chrf
         value: 0.52243
  - task:
      name: Translation lad_Latn-spa
      type: translation
      args: lad_Latn-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: lad_Latn-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 42.6
       - name: chr-F
         type: chrf
         value: 0.59363
  - task:
      name: Translation oci-fra
      type: translation
      args: oci-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: oci-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 29.6
       - name: chr-F
         type: chrf
         value: 0.49660
  - task:
      name: Translation pms-ita
      type: translation
      args: pms-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: pms-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 20.0
       - name: chr-F
         type: chrf
         value: 0.40221
  - task:
      name: Translation por-cat
      type: translation
      args: por-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 52.2
       - name: chr-F
         type: chrf
         value: 0.71146
  - task:
      name: Translation por-fra
      type: translation
      args: por-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 60.9
       - name: chr-F
         type: chrf
         value: 0.75565
  - task:
      name: Translation por-glg
      type: translation
      args: por-glg
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-glg
    metrics:
       - name: BLEU
         type: bleu
         value: 59.0
       - name: chr-F
         type: chrf
         value: 0.75348
  - task:
      name: Translation por-ita
      type: translation
      args: por-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 58.8
       - name: chr-F
         type: chrf
         value: 0.76883
  - task:
      name: Translation por-ron
      type: translation
      args: por-ron
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 46.6
       - name: chr-F
         type: chrf
         value: 0.67838
  - task:
      name: Translation por-spa
      type: translation
      args: por-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: por-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 64.8
       - name: chr-F
         type: chrf
         value: 0.79336
  - task:
      name: Translation ron-fra
      type: translation
      args: ron-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ron-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 55.0
       - name: chr-F
         type: chrf
         value: 0.70307
  - task:
      name: Translation ron-ita
      type: translation
      args: ron-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ron-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 53.7
       - name: chr-F
         type: chrf
         value: 0.73862
  - task:
      name: Translation ron-por
      type: translation
      args: ron-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ron-por
    metrics:
       - name: BLEU
         type: bleu
         value: 50.7
       - name: chr-F
         type: chrf
         value: 0.70889
  - task:
      name: Translation ron-spa
      type: translation
      args: ron-spa
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: ron-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 57.2
       - name: chr-F
         type: chrf
         value: 0.73529
  - task:
      name: Translation spa-cat
      type: translation
      args: spa-cat
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 67.9
       - name: chr-F
         type: chrf
         value: 0.82758
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 57.3
       - name: chr-F
         type: chrf
         value: 0.73113
  - task:
      name: Translation spa-glg
      type: translation
      args: spa-glg
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-glg
    metrics:
       - name: BLEU
         type: bleu
         value: 63.0
       - name: chr-F
         type: chrf
         value: 0.77332
  - task:
      name: Translation spa-ita
      type: translation
      args: spa-ita
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 60.3
       - name: chr-F
         type: chrf
         value: 0.77046
  - task:
      name: Translation spa-por
      type: translation
      args: spa-por
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-por
    metrics:
       - name: BLEU
         type: bleu
         value: 59.1
       - name: chr-F
         type: chrf
         value: 0.75854
  - task:
      name: Translation spa-ron
      type: translation
      args: spa-ron
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: spa-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 45.5
       - name: chr-F
         type: chrf
         value: 0.66679
  - task:
      name: Translation fra-ita
      type: translation
      args: fra-ita
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: fra-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 31.2
       - name: chr-F
         type: chrf
         value: 0.59764
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 32.5
       - name: chr-F
         type: chrf
         value: 0.58829
  - task:
      name: Translation ita-fra
      type: translation
      args: ita-fra
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: ita-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 31.6
       - name: chr-F
         type: chrf
         value: 0.59084
  - task:
      name: Translation ita-spa
      type: translation
      args: ita-spa
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: ita-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 33.5
       - name: chr-F
         type: chrf
         value: 0.59669
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 32.3
       - name: chr-F
         type: chrf
         value: 0.59096
  - task:
      name: Translation spa-ita
      type: translation
      args: spa-ita
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: spa-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 33.2
       - name: chr-F
         type: chrf
         value: 0.60783
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 37.8
       - name: chr-F
         type: chrf
         value: 0.62250
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 36.2
       - name: chr-F
         type: chrf
         value: 0.61953
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 39.8
       - name: chr-F
         type: chrf
         value: 0.62953
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 34.9
       - name: chr-F
         type: chrf
         value: 0.61130
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 39.0
       - name: chr-F
         type: chrf
         value: 0.62397
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 34.3
       - name: chr-F
         type: chrf
         value: 0.60927
  - task:
      name: Translation fra-spa
      type: translation
      args: fra-spa
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: fra-spa
    metrics:
       - name: BLEU
         type: bleu
         value: 34.9
       - name: chr-F
         type: chrf
         value: 0.59312
  - task:
      name: Translation spa-fra
      type: translation
      args: spa-fra
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: spa-fra
    metrics:
       - name: BLEU
         type: bleu
         value: 33.6
       - name: chr-F
         type: chrf
         value: 0.59468
  - task:
      name: Translation cat-ita
      type: translation
      args: cat-ita
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: cat-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 47.8
       - name: chr-F
         type: chrf
         value: 0.69968
  - task:
      name: Translation cat-oci
      type: translation
      args: cat-oci
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: cat-oci
    metrics:
       - name: BLEU
         type: bleu
         value: 51.6
       - name: chr-F
         type: chrf
         value: 0.73808
  - task:
      name: Translation cat-ron
      type: translation
      args: cat-ron
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: cat-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 29.0
       - name: chr-F
         type: chrf
         value: 0.51178
  - task:
      name: Translation ita-cat
      type: translation
      args: ita-cat
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ita-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 48.9
       - name: chr-F
         type: chrf
         value: 0.70538
  - task:
      name: Translation ita-oci
      type: translation
      args: ita-oci
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ita-oci
    metrics:
       - name: BLEU
         type: bleu
         value: 32.0
       - name: chr-F
         type: chrf
         value: 0.59025
  - task:
      name: Translation ita-ron
      type: translation
      args: ita-ron
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ita-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 28.9
       - name: chr-F
         type: chrf
         value: 0.51261
  - task:
      name: Translation oci-cat
      type: translation
      args: oci-cat
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: oci-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 66.1
       - name: chr-F
         type: chrf
         value: 0.80908
  - task:
      name: Translation oci-ita
      type: translation
      args: oci-ita
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: oci-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 39.6
       - name: chr-F
         type: chrf
         value: 0.63584
  - task:
      name: Translation oci-ron
      type: translation
      args: oci-ron
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: oci-ron
    metrics:
       - name: BLEU
         type: bleu
         value: 24.6
       - name: chr-F
         type: chrf
         value: 0.47384
  - task:
      name: Translation ron-cat
      type: translation
      args: ron-cat
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ron-cat
    metrics:
       - name: BLEU
         type: bleu
         value: 31.1
       - name: chr-F
         type: chrf
         value: 0.52994
  - task:
      name: Translation ron-ita
      type: translation
      args: ron-ita
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ron-ita
    metrics:
       - name: BLEU
         type: bleu
         value: 29.6
       - name: chr-F
         type: chrf
         value: 0.52714
  - task:
      name: Translation ron-oci
      type: translation
      args: ron-oci
    dataset:
      name: wmt21-ml-wp
      type: wmt21-ml-wp
      args: ron-oci
    metrics:
       - name: BLEU
         type: bleu
         value: 21.3
       - name: chr-F
         type: chrf
         value: 0.45932
---
# opus-mt-tc-big-itc-itc

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

Neural machine translation model for translating from Italic languages (itc) to Italic languages (itc).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).
**Model Description:**
- **Developed by:** Language Technology Research Group at the University of Helsinki
- **Model Type:** Translation (transformer-big)
- **Release**: 2022-08-10
- **License:** CC-BY-4.0
- **Language(s):**  
  - Source Language(s): ast cat cbk fra fro glg hat ita lad lad_Latn lat lat_Latn lij lld oci pms por ron spa
  - Target Language(s): ast cat fra gcf glg hat ita lad lad_Latn lat lat_Latn oci por ron spa
  - Language Pair(s): ast-cat ast-fra ast-glg ast-ita ast-oci ast-por ast-ron ast-spa cat-ast cat-fra cat-glg cat-ita cat-oci cat-por cat-ron cat-spa fra-ast fra-cat fra-glg fra-ita fra-oci fra-por fra-ron fra-spa glg-ast glg-cat glg-fra glg-ita glg-oci glg-por glg-ron glg-spa ita-ast ita-cat ita-fra ita-glg ita-oci ita-por ita-ron ita-spa lad-spa lad_Latn-spa oci-ast oci-cat oci-fra oci-glg oci-ita oci-por oci-ron oci-spa pms-ita por-ast por-cat por-fra por-glg por-ita por-oci por-ron por-spa ron-ast ron-cat ron-fra ron-glg ron-ita ron-oci ron-por ron-spa spa-cat spa-fra spa-glg spa-ita spa-por spa-ron
  - Valid Target Language Labels: >>acf<< >>aoa<< >>arg<< >>ast<< >>cat<< >>cbk<< >>cbk_Latn<< >>ccd<< >>cks<< >>cos<< >>cri<< >>crs<< >>dlm<< >>drc<< >>egl<< >>ext<< >>fab<< >>fax<< >>fra<< >>frc<< >>frm<< >>frm_Latn<< >>fro<< >>fro_Latn<< >>frp<< >>fur<< >>fur_Latn<< >>gcf<< >>gcf_Latn<< >>gcr<< >>glg<< >>hat<< >>idb<< >>ist<< >>ita<< >>itk<< >>kea<< >>kmv<< >>lad<< >>lad_Latn<< >>lat<< >>lat_Grek<< >>lat_Latn<< >>lij<< >>lld<< >>lld_Latn<< >>lmo<< >>lou<< >>mcm<< >>mfe<< >>mol<< >>mwl<< >>mxi<< >>mzs<< >>nap<< >>nrf<< >>oci<< >>osc<< >>osp<< >>osp_Latn<< >>pap<< >>pcd<< >>pln<< >>pms<< >>pob<< >>por<< >>pov<< >>pre<< >>pro<< >>qbb<< >>qhr<< >>rcf<< >>rgn<< >>roh<< >>ron<< >>ruo<< >>rup<< >>ruq<< >>scf<< >>scn<< >>sdc<< >>sdn<< >>spa<< >>spq<< >>spx<< >>src<< >>srd<< >>sro<< >>tmg<< >>tvy<< >>vec<< >>vkp<< >>wln<< >>xfa<< >>xum<<
- **Original Model**: [opusTCv20210807_transformer-big_2022-08-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-itc/opusTCv20210807_transformer-big_2022-08-10.zip)
- **Resources for more information:**
  - [OPUS-MT-train GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)
  - More information about released models for this language pair: [OPUS-MT itc-itc README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-itc/README.md)
  - [More information about MarianNMT models in the transformers library](https://huggingface.co/docs/transformers/model_doc/marian)
  - [Tatoeba Translation Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge/

This is a multilingual translation model with multiple target languages. A sentence initial language token is required in the form of `>>id<<` (id = valid target language ID), e.g. `>>ast<<`

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
    ">>fra<< Charras anglés?",
    ">>fra<< Vull veure't."
]

model_name = "pytorch-models/opus-mt-tc-big-itc-itc"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Conversations anglaises ?
#     Je veux te voir.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-itc-itc")
print(pipe(">>fra<< Charras anglés?"))

# expected output: Conversations anglaises ?
```

## Training

- **Data**: opusTCv20210807 ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
- **Pre-processing**: SentencePiece (spm32k,spm32k)
- **Model Type:**  transformer-big
- **Original MarianNMT Model**: [opusTCv20210807_transformer-big_2022-08-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-itc/opusTCv20210807_transformer-big_2022-08-10.zip)
- **Training Scripts**: [GitHub Repo](https://github.com/Helsinki-NLP/OPUS-MT-train)

## Evaluation

* test set translations: [opusTCv20210807_transformer-big_2022-08-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-itc/opusTCv20210807_transformer-big_2022-08-10.test.txt)
* test set scores: [opusTCv20210807_transformer-big_2022-08-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-itc/opusTCv20210807_transformer-big_2022-08-10.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| cat-fra | tatoeba-test-v2021-08-07 | 0.71201 | 54.6 | 700 | 5664 |
| cat-ita | tatoeba-test-v2021-08-07 | 0.74198 | 58.4 | 298 | 2028 |
| cat-por | tatoeba-test-v2021-08-07 | 0.74930 | 57.4 | 747 | 6119 |
| cat-spa | tatoeba-test-v2021-08-07 | 0.87844 | 78.1 | 1534 | 12094 |
| fra-cat | tatoeba-test-v2021-08-07 | 0.66525 | 46.2 | 700 | 5342 |
| fra-ita | tatoeba-test-v2021-08-07 | 0.72742 | 53.8 | 10091 | 62060 |
| fra-por | tatoeba-test-v2021-08-07 | 0.68413 | 48.6 | 10518 | 77650 |
| fra-ron | tatoeba-test-v2021-08-07 | 0.65009 | 44.0 | 1925 | 12252 |
| fra-spa | tatoeba-test-v2021-08-07 | 0.72080 | 54.8 | 10294 | 78406 |
| glg-por | tatoeba-test-v2021-08-07 | 0.76720 | 61.1 | 433 | 3105 |
| glg-spa | tatoeba-test-v2021-08-07 | 0.82362 | 71.7 | 2121 | 17443 |
| ita-cat | tatoeba-test-v2021-08-07 | 0.72529 | 56.4 | 298 | 2109 |
| ita-fra | tatoeba-test-v2021-08-07 | 0.77932 | 65.2 | 10091 | 66377 |
| ita-por | tatoeba-test-v2021-08-07 | 0.72798 | 54.0 | 3066 | 25668 |
| ita-ron | tatoeba-test-v2021-08-07 | 0.70814 | 51.1 | 1005 | 6209 |
| ita-spa | tatoeba-test-v2021-08-07 | 0.77455 | 62.9 | 5000 | 34937 |
| lad_Latn-spa | tatoeba-test-v2021-08-07 | 0.59363 | 42.6 | 239 | 1239 |
| lad-spa | tatoeba-test-v2021-08-07 | 0.52243 | 34.7 | 276 | 1448 |
| oci-fra | tatoeba-test-v2021-08-07 | 0.49660 | 29.6 | 806 | 6302 |
| pms-ita | tatoeba-test-v2021-08-07 | 0.40221 | 20.0 | 232 | 1721 |
| por-cat | tatoeba-test-v2021-08-07 | 0.71146 | 52.2 | 747 | 6149 |
| por-fra | tatoeba-test-v2021-08-07 | 0.75565 | 60.9 | 10518 | 80459 |
| por-glg | tatoeba-test-v2021-08-07 | 0.75348 | 59.0 | 433 | 3016 |
| por-ita | tatoeba-test-v2021-08-07 | 0.76883 | 58.8 | 3066 | 24897 |
| por-ron | tatoeba-test-v2021-08-07 | 0.67838 | 46.6 | 681 | 4521 |
| por-spa | tatoeba-test-v2021-08-07 | 0.79336 | 64.8 | 10947 | 87335 |
| ron-fra | tatoeba-test-v2021-08-07 | 0.70307 | 55.0 | 1925 | 13347 |
| ron-ita | tatoeba-test-v2021-08-07 | 0.73862 | 53.7 | 1005 | 6352 |
| ron-por | tatoeba-test-v2021-08-07 | 0.70889 | 50.7 | 681 | 4593 |
| ron-spa | tatoeba-test-v2021-08-07 | 0.73529 | 57.2 | 1959 | 12679 |
| spa-cat | tatoeba-test-v2021-08-07 | 0.82758 | 67.9 | 1534 | 12343 |
| spa-fra | tatoeba-test-v2021-08-07 | 0.73113 | 57.3 | 10294 | 83501 |
| spa-glg | tatoeba-test-v2021-08-07 | 0.77332 | 63.0 | 2121 | 16581 |
| spa-ita | tatoeba-test-v2021-08-07 | 0.77046 | 60.3 | 5000 | 34515 |
| spa-lad_Latn | tatoeba-test-v2021-08-07 | 0.40084 | 14.7 | 239 | 1254 |
| spa-por | tatoeba-test-v2021-08-07 | 0.75854 | 59.1 | 10947 | 87610 |
| spa-ron | tatoeba-test-v2021-08-07 | 0.66679 | 45.5 | 1959 | 12503 |
| ast-cat | flores101-devtest | 0.57870 | 31.8 | 1012 | 27304 |
| ast-fra | flores101-devtest | 0.56761 | 31.1 | 1012 | 28343 |
| ast-glg | flores101-devtest | 0.55161 | 27.9 | 1012 | 26582 |
| ast-ita | flores101-devtest | 0.51764 | 22.1 | 1012 | 27306 |
| ast-oci | flores101-devtest | 0.49545 | 20.6 | 1012 | 27305 |
| ast-por | flores101-devtest | 0.57347 | 31.5 | 1012 | 26519 |
| ast-ron | flores101-devtest | 0.52317 | 24.8 | 1012 | 26799 |
| ast-spa | flores101-devtest | 0.49741 | 21.2 | 1012 | 29199 |
| cat-ast | flores101-devtest | 0.56754 | 24.7 | 1012 | 24572 |
| cat-fra | flores101-devtest | 0.63368 | 38.4 | 1012 | 28343 |
| cat-glg | flores101-devtest | 0.59596 | 32.2 | 1012 | 26582 |
| cat-ita | flores101-devtest | 0.55886 | 26.3 | 1012 | 27306 |
| cat-oci | flores101-devtest | 0.54285 | 24.6 | 1012 | 27305 |
| cat-por | flores101-devtest | 0.62913 | 37.7 | 1012 | 26519 |
| cat-ron | flores101-devtest | 0.56885 | 29.5 | 1012 | 26799 |
| cat-spa | flores101-devtest | 0.53372 | 24.6 | 1012 | 29199 |
| fra-ast | flores101-devtest | 0.52696 | 20.7 | 1012 | 24572 |
| fra-cat | flores101-devtest | 0.60492 | 34.6 | 1012 | 27304 |
| fra-glg | flores101-devtest | 0.57485 | 30.3 | 1012 | 26582 |
| fra-ita | flores101-devtest | 0.56493 | 27.3 | 1012 | 27306 |
| fra-oci | flores101-devtest | 0.57449 | 28.2 | 1012 | 27305 |
| fra-por | flores101-devtest | 0.62211 | 36.9 | 1012 | 26519 |
| fra-ron | flores101-devtest | 0.56998 | 29.4 | 1012 | 26799 |
| fra-spa | flores101-devtest | 0.52880 | 24.2 | 1012 | 29199 |
| glg-ast | flores101-devtest | 0.55090 | 22.4 | 1012 | 24572 |
| glg-cat | flores101-devtest | 0.60550 | 32.6 | 1012 | 27304 |
| glg-fra | flores101-devtest | 0.62026 | 36.0 | 1012 | 28343 |
| glg-ita | flores101-devtest | 0.55834 | 25.9 | 1012 | 27306 |
| glg-oci | flores101-devtest | 0.52520 | 21.9 | 1012 | 27305 |
| glg-por | flores101-devtest | 0.60027 | 32.7 | 1012 | 26519 |
| glg-ron | flores101-devtest | 0.55621 | 27.8 | 1012 | 26799 |
| glg-spa | flores101-devtest | 0.53219 | 24.4 | 1012 | 29199 |
| ita-ast | flores101-devtest | 0.50741 | 17.1 | 1012 | 24572 |
| ita-cat | flores101-devtest | 0.57061 | 27.9 | 1012 | 27304 |
| ita-fra | flores101-devtest | 0.60199 | 32.0 | 1012 | 28343 |
| ita-glg | flores101-devtest | 0.55312 | 25.9 | 1012 | 26582 |
| ita-oci | flores101-devtest | 0.48447 | 18.1 | 1012 | 27305 |
| ita-por | flores101-devtest | 0.58162 | 29.0 | 1012 | 26519 |
| ita-ron | flores101-devtest | 0.53703 | 24.2 | 1012 | 26799 |
| ita-spa | flores101-devtest | 0.52238 | 23.1 | 1012 | 29199 |
| oci-ast | flores101-devtest | 0.53010 | 20.2 | 1012 | 24572 |
| oci-cat | flores101-devtest | 0.59946 | 32.2 | 1012 | 27304 |
| oci-fra | flores101-devtest | 0.64290 | 39.0 | 1012 | 28343 |
| oci-glg | flores101-devtest | 0.56737 | 28.0 | 1012 | 26582 |
| oci-ita | flores101-devtest | 0.54220 | 24.2 | 1012 | 27306 |
| oci-por | flores101-devtest | 0.62127 | 35.7 | 1012 | 26519 |
| oci-ron | flores101-devtest | 0.55906 | 28.0 | 1012 | 26799 |
| oci-spa | flores101-devtest | 0.52110 | 22.8 | 1012 | 29199 |
| por-ast | flores101-devtest | 0.54539 | 22.5 | 1012 | 24572 |
| por-cat | flores101-devtest | 0.61809 | 36.4 | 1012 | 27304 |
| por-fra | flores101-devtest | 0.64343 | 39.7 | 1012 | 28343 |
| por-glg | flores101-devtest | 0.57965 | 30.4 | 1012 | 26582 |
| por-ita | flores101-devtest | 0.55841 | 26.3 | 1012 | 27306 |
| por-oci | flores101-devtest | 0.54829 | 25.3 | 1012 | 27305 |
| por-ron | flores101-devtest | 0.57283 | 29.8 | 1012 | 26799 |
| por-spa | flores101-devtest | 0.53513 | 25.2 | 1012 | 29199 |
| ron-ast | flores101-devtest | 0.52265 | 20.1 | 1012 | 24572 |
| ron-cat | flores101-devtest | 0.59689 | 32.6 | 1012 | 27304 |
| ron-fra | flores101-devtest | 0.63060 | 37.4 | 1012 | 28343 |
| ron-glg | flores101-devtest | 0.56677 | 29.3 | 1012 | 26582 |
| ron-ita | flores101-devtest | 0.55485 | 25.6 | 1012 | 27306 |
| ron-oci | flores101-devtest | 0.52433 | 21.8 | 1012 | 27305 |
| ron-por | flores101-devtest | 0.61831 | 36.1 | 1012 | 26519 |
| ron-spa | flores101-devtest | 0.52712 | 24.1 | 1012 | 29199 |
| spa-ast | flores101-devtest | 0.49008 | 15.7 | 1012 | 24572 |
| spa-cat | flores101-devtest | 0.53905 | 23.2 | 1012 | 27304 |
| spa-fra | flores101-devtest | 0.57078 | 27.4 | 1012 | 28343 |
| spa-glg | flores101-devtest | 0.52563 | 22.0 | 1012 | 26582 |
| spa-ita | flores101-devtest | 0.52783 | 22.3 | 1012 | 27306 |
| spa-oci | flores101-devtest | 0.48064 | 16.3 | 1012 | 27305 |
| spa-por | flores101-devtest | 0.55736 | 25.8 | 1012 | 26519 |
| spa-ron | flores101-devtest | 0.51623 | 21.4 | 1012 | 26799 |
| fra-ita | newssyscomb2009 | 0.60995 | 32.1 | 502 | 11551 |
| fra-spa | newssyscomb2009 | 0.60224 | 34.2 | 502 | 12503 |
| ita-fra | newssyscomb2009 | 0.61237 | 33.7 | 502 | 12331 |
| ita-spa | newssyscomb2009 | 0.60706 | 35.4 | 502 | 12503 |
| spa-fra | newssyscomb2009 | 0.61290 | 34.6 | 502 | 12331 |
| spa-ita | newssyscomb2009 | 0.61632 | 33.3 | 502 | 11551 |
| fra-spa | news-test2008 | 0.58939 | 33.9 | 2051 | 52586 |
| spa-fra | news-test2008 | 0.58695 | 32.4 | 2051 | 52685 |
| fra-ita | newstest2009 | 0.59764 | 31.2 | 2525 | 63466 |
| fra-spa | newstest2009 | 0.58829 | 32.5 | 2525 | 68111 |
| ita-fra | newstest2009 | 0.59084 | 31.6 | 2525 | 69263 |
| ita-spa | newstest2009 | 0.59669 | 33.5 | 2525 | 68111 |
| spa-fra | newstest2009 | 0.59096 | 32.3 | 2525 | 69263 |
| spa-ita | newstest2009 | 0.60783 | 33.2 | 2525 | 63466 |
| fra-spa | newstest2010 | 0.62250 | 37.8 | 2489 | 65480 |
| spa-fra | newstest2010 | 0.61953 | 36.2 | 2489 | 66022 |
| fra-spa | newstest2011 | 0.62953 | 39.8 | 3003 | 79476 |
| spa-fra | newstest2011 | 0.61130 | 34.9 | 3003 | 80626 |
| fra-spa | newstest2012 | 0.62397 | 39.0 | 3003 | 79006 |
| spa-fra | newstest2012 | 0.60927 | 34.3 | 3003 | 78011 |
| fra-spa | newstest2013 | 0.59312 | 34.9 | 3000 | 70528 |
| spa-fra | newstest2013 | 0.59468 | 33.6 | 3000 | 70037 |
| cat-ita | wmt21-ml-wp | 0.69968 | 47.8 | 1743 | 42735 |
| cat-oci | wmt21-ml-wp | 0.73808 | 51.6 | 1743 | 43736 |
| cat-ron | wmt21-ml-wp | 0.51178 | 29.0 | 1743 | 42895 |
| ita-cat | wmt21-ml-wp | 0.70538 | 48.9 | 1743 | 43833 |
| ita-oci | wmt21-ml-wp | 0.59025 | 32.0 | 1743 | 43736 |
| ita-ron | wmt21-ml-wp | 0.51261 | 28.9 | 1743 | 42895 |
| oci-cat | wmt21-ml-wp | 0.80908 | 66.1 | 1743 | 43833 |
| oci-ita | wmt21-ml-wp | 0.63584 | 39.6 | 1743 | 42735 |
| oci-ron | wmt21-ml-wp | 0.47384 | 24.6 | 1743 | 42895 |
| ron-cat | wmt21-ml-wp | 0.52994 | 31.1 | 1743 | 43833 |
| ron-ita | wmt21-ml-wp | 0.52714 | 29.6 | 1743 | 42735 |
| ron-oci | wmt21-ml-wp | 0.45932 | 21.3 | 1743 | 43736 |

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
* port time: Fri Aug 12 23:57:49 EEST 2022
* port machine: LM0-400-22516.local
