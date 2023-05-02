---
license: cc0-1.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-voxrex-npsc-nst
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-voxrex-npsc-nst

This model is a fine-tuned version of [KBLab/wav2vec2-large-voxrex](https://huggingface.co/KBLab/wav2vec2-large-voxrex) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0475
- Wer: 0.0514

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Wer    |
|:-------------:|:-----:|:------:|:---------------:|:------:|
| 3.3888        | 0.05  | 500    | 3.2558          | 1.0    |
| 2.7683        | 0.11  | 1000   | 2.4163          | 1.0000 |
| 0.6279        | 0.16  | 1500   | 0.3610          | 0.3608 |
| 0.5093        | 0.21  | 2000   | 0.2610          | 0.2776 |
| 0.4024        | 0.26  | 2500   | 0.2219          | 0.2303 |
| 0.3705        | 0.32  | 3000   | 0.1940          | 0.2043 |
| 0.3588        | 0.37  | 3500   | 0.1806          | 0.1822 |
| 0.3312        | 0.42  | 4000   | 0.1611          | 0.1736 |
| 0.3062        | 0.47  | 4500   | 0.1571          | 0.1619 |
| 0.2838        | 0.53  | 5000   | 0.1482          | 0.1552 |
| 0.2896        | 0.58  | 5500   | 0.1406          | 0.1482 |
| 0.2704        | 0.63  | 6000   | 0.1311          | 0.1467 |
| 0.263         | 0.69  | 6500   | 0.1258          | 0.1406 |
| 0.2574        | 0.74  | 7000   | 0.1252          | 0.1343 |
| 0.252         | 0.79  | 7500   | 0.1162          | 0.1279 |
| 0.2355        | 0.84  | 8000   | 0.1161          | 0.1275 |
| 0.2381        | 0.9   | 8500   | 0.1095          | 0.1247 |
| 0.2354        | 0.95  | 9000   | 0.1106          | 0.1250 |
| 0.234         | 1.0   | 9500   | 0.1044          | 0.1186 |
| 0.2094        | 1.05  | 10000  | 0.1052          | 0.1157 |
| 0.2088        | 1.11  | 10500  | 0.1026          | 0.1158 |
| 0.2123        | 1.16  | 11000  | 0.0998          | 0.1120 |
| 0.3087        | 1.21  | 11500  | 0.0971          | 0.1108 |
| 0.1995        | 1.26  | 12000  | 0.0973          | 0.1085 |
| 0.1989        | 1.32  | 12500  | 0.0928          | 0.1063 |
| 0.1993        | 1.37  | 13000  | 0.0920          | 0.1064 |
| 0.1996        | 1.42  | 13500  | 0.0904          | 0.1050 |
| 0.1917        | 1.48  | 14000  | 0.0895          | 0.1051 |
| 0.1857        | 1.53  | 14500  | 0.0889          | 0.1038 |
| 0.1871        | 1.58  | 15000  | 0.0867          | 0.1054 |
| 0.2047        | 1.63  | 15500  | 0.0866          | 0.1017 |
| 0.1845        | 1.69  | 16000  | 0.0865          | 0.1007 |
| 0.178         | 1.74  | 16500  | 0.0835          | 0.0999 |
| 0.1741        | 1.79  | 17000  | 0.0838          | 0.0985 |
| 0.1737        | 1.84  | 17500  | 0.0833          | 0.0966 |
| 0.1713        | 1.9   | 18000  | 0.0799          | 0.0963 |
| 0.1703        | 1.95  | 18500  | 0.0802          | 0.0950 |
| 0.1735        | 2.0   | 19000  | 0.0785          | 0.0926 |
| 0.1619        | 2.06  | 19500  | 0.0785          | 0.0930 |
| 0.1707        | 2.11  | 20000  | 0.0787          | 0.0928 |
| 0.17          | 2.16  | 20500  | 0.0765          | 0.0902 |
| 0.1604        | 2.21  | 21000  | 0.0772          | 0.0918 |
| 0.1576        | 2.27  | 21500  | 0.0745          | 0.0912 |
| 0.1529        | 2.32  | 22000  | 0.0741          | 0.0906 |
| 0.1435        | 2.37  | 22500  | 0.0751          | 0.0888 |
| 0.1526        | 2.42  | 23000  | 0.0734          | 0.0892 |
| 0.1471        | 2.48  | 23500  | 0.0746          | 0.0886 |
| 0.1553        | 2.53  | 24000  | 0.0727          | 0.0872 |
| 0.1641        | 2.58  | 24500  | 0.0720          | 0.0862 |
| 0.1495        | 2.64  | 25000  | 0.0707          | 0.0868 |
| 0.1498        | 2.69  | 25500  | 0.0719          | 0.0864 |
| 0.1438        | 2.74  | 26000  | 0.0703          | 0.0853 |
| 0.1532        | 2.79  | 26500  | 0.0710          | 0.0854 |
| 0.1435        | 2.85  | 27000  | 0.0690          | 0.0847 |
| 0.1486        | 2.9   | 27500  | 0.0683          | 0.0882 |
| 0.1359        | 2.95  | 28000  | 0.0673          | 0.0839 |
| 0.1309        | 3.0   | 28500  | 0.0687          | 0.0843 |
| 0.1312        | 3.06  | 29000  | 0.0696          | 0.0865 |
| 0.1387        | 3.11  | 29500  | 0.0667          | 0.0857 |
| 0.1327        | 3.16  | 30000  | 0.0667          | 0.0845 |
| 0.1251        | 3.21  | 30500  | 0.0662          | 0.0820 |
| 0.1415        | 3.27  | 31000  | 0.0652          | 0.0831 |
| 0.1221        | 3.32  | 31500  | 0.0660          | 0.0822 |
| 0.1337        | 3.37  | 32000  | 0.0658          | 0.0799 |
| 0.1342        | 3.43  | 32500  | 0.0650          | 0.0808 |
| 0.1391        | 3.48  | 33000  | 0.0658          | 0.0791 |
| 0.1351        | 3.53  | 33500  | 0.0654          | 0.0794 |
| 0.1309        | 3.58  | 34000  | 0.0650          | 0.0781 |
| 0.1317        | 3.64  | 34500  | 0.0629          | 0.0783 |
| 0.1326        | 3.69  | 35000  | 0.0637          | 0.0795 |
| 0.1296        | 3.74  | 35500  | 0.0624          | 0.0773 |
| 0.1156        | 3.79  | 36000  | 0.0613          | 0.0759 |
| 0.1242        | 3.85  | 36500  | 0.0627          | 0.0761 |
| 0.1251        | 3.9   | 37000  | 0.0638          | 0.0758 |
| 0.1335        | 3.95  | 37500  | 0.0620          | 0.0756 |
| 0.1374        | 4.01  | 38000  | 0.0628          | 0.0756 |
| 0.1227        | 4.06  | 38500  | 0.0637          | 0.0770 |
| 0.1144        | 4.11  | 39000  | 0.0637          | 0.0775 |
| 0.1222        | 4.16  | 39500  | 0.0630          | 0.0738 |
| 0.1207        | 4.22  | 40000  | 0.0607          | 0.0720 |
| 0.1181        | 4.27  | 40500  | 0.0608          | 0.0724 |
| 0.1259        | 4.32  | 41000  | 0.0608          | 0.0734 |
| 0.1137        | 4.37  | 41500  | 0.0623          | 0.0718 |
| 0.1275        | 4.43  | 42000  | 0.0620          | 0.0721 |
| 0.1218        | 4.48  | 42500  | 0.0599          | 0.0703 |
| 0.1212        | 4.53  | 43000  | 0.0612          | 0.0708 |
| 0.1144        | 4.59  | 43500  | 0.0589          | 0.0702 |
| 0.1199        | 4.64  | 44000  | 0.0589          | 0.0695 |
| 0.1113        | 4.69  | 44500  | 0.0601          | 0.0698 |
| 0.1108        | 4.74  | 45000  | 0.0584          | 0.0695 |
| 0.1196        | 4.8   | 45500  | 0.0596          | 0.0694 |
| 0.1216        | 4.85  | 46000  | 0.0578          | 0.0703 |
| 0.1188        | 4.9   | 46500  | 0.0596          | 0.0684 |
| 0.1122        | 4.95  | 47000  | 0.0584          | 0.0671 |
| 0.1115        | 5.01  | 47500  | 0.0594          | 0.0682 |
| 0.1777        | 5.06  | 48000  | 0.0597          | 0.0682 |
| 0.108         | 5.11  | 48500  | 0.0573          | 0.0691 |
| 0.1132        | 5.16  | 49000  | 0.0583          | 0.0666 |
| 0.1091        | 5.22  | 49500  | 0.0582          | 0.0672 |
| 0.1056        | 5.27  | 50000  | 0.0578          | 0.0674 |
| 0.1027        | 5.32  | 50500  | 0.0574          | 0.0671 |
| 0.1112        | 5.38  | 51000  | 0.0569          | 0.0659 |
| 0.1096        | 5.43  | 51500  | 0.0582          | 0.0662 |
| 0.1098        | 5.48  | 52000  | 0.0576          | 0.0667 |
| 0.1088        | 5.53  | 52500  | 0.0560          | 0.0679 |
| 0.1076        | 5.59  | 53000  | 0.0579          | 0.0664 |
| 0.1037        | 5.64  | 53500  | 0.0556          | 0.0661 |
| 0.1039        | 5.69  | 54000  | 0.0572          | 0.0675 |
| 0.108         | 5.74  | 54500  | 0.0562          | 0.0662 |
| 0.1069        | 5.8   | 55000  | 0.0576          | 0.0663 |
| 0.1066        | 5.85  | 55500  | 0.0564          | 0.0651 |
| 0.0939        | 5.9   | 56000  | 0.0566          | 0.0644 |
| 0.1118        | 5.96  | 56500  | 0.0570          | 0.0650 |
| 0.1111        | 6.01  | 57000  | 0.0563          | 0.0668 |
| 0.1014        | 6.06  | 57500  | 0.0557          | 0.0660 |
| 0.0971        | 6.11  | 58000  | 0.0567          | 0.0667 |
| 0.0932        | 6.17  | 58500  | 0.0559          | 0.0664 |
| 0.1002        | 6.22  | 59000  | 0.0551          | 0.0640 |
| 0.1028        | 6.27  | 59500  | 0.0560          | 0.0629 |
| 0.0992        | 6.32  | 60000  | 0.0547          | 0.0641 |
| 0.0975        | 6.38  | 60500  | 0.0556          | 0.0630 |
| 0.0957        | 6.43  | 61000  | 0.0555          | 0.0632 |
| 0.0931        | 6.48  | 61500  | 0.0546          | 0.0641 |
| 0.0999        | 6.54  | 62000  | 0.0556          | 0.0633 |
| 0.0998        | 6.59  | 62500  | 0.0539          | 0.0628 |
| 0.0991        | 6.64  | 63000  | 0.0559          | 0.0630 |
| 0.1027        | 6.69  | 63500  | 0.0549          | 0.0628 |
| 0.097         | 6.75  | 64000  | 0.0547          | 0.0628 |
| 0.0933        | 6.8   | 64500  | 0.0544          | 0.0633 |
| 0.0919        | 6.85  | 65000  | 0.0535          | 0.0640 |
| 0.0973        | 6.9   | 65500  | 0.0543          | 0.0619 |
| 0.0979        | 6.96  | 66000  | 0.0525          | 0.0620 |
| 0.1076        | 7.01  | 66500  | 0.0529          | 0.0615 |
| 0.0888        | 7.06  | 67000  | 0.0546          | 0.0617 |
| 0.0926        | 7.11  | 67500  | 0.0530          | 0.0636 |
| 0.0902        | 7.17  | 68000  | 0.0540          | 0.0631 |
| 0.1004        | 7.22  | 68500  | 0.0529          | 0.0624 |
| 0.0963        | 7.27  | 69000  | 0.0534          | 0.0631 |
| 0.0946        | 7.33  | 69500  | 0.0534          | 0.0601 |
| 0.0897        | 7.38  | 70000  | 0.0525          | 0.0607 |
| 0.0925        | 7.43  | 70500  | 0.0535          | 0.0599 |
| 0.0883        | 7.48  | 71000  | 0.0518          | 0.0605 |
| 0.0942        | 7.54  | 71500  | 0.0522          | 0.0587 |
| 0.0863        | 7.59  | 72000  | 0.0533          | 0.0593 |
| 0.0894        | 7.64  | 72500  | 0.0529          | 0.0587 |
| 0.0908        | 7.69  | 73000  | 0.0519          | 0.0596 |
| 0.0878        | 7.75  | 73500  | 0.0521          | 0.0585 |
| 0.0949        | 7.8   | 74000  | 0.0524          | 0.0588 |
| 0.0962        | 7.85  | 74500  | 0.0521          | 0.0581 |
| 0.0918        | 7.91  | 75000  | 0.0513          | 0.0579 |
| 0.0933        | 7.96  | 75500  | 0.0522          | 0.0582 |
| 0.0839        | 8.01  | 76000  | 0.0536          | 0.0579 |
| 0.0868        | 8.06  | 76500  | 0.0526          | 0.0577 |
| 0.086         | 8.12  | 77000  | 0.0525          | 0.0590 |
| 0.0801        | 8.17  | 77500  | 0.0533          | 0.0586 |
| 0.0845        | 8.22  | 78000  | 0.0516          | 0.0578 |
| 0.0895        | 8.27  | 78500  | 0.0530          | 0.0583 |
| 0.0841        | 8.33  | 79000  | 0.0515          | 0.0584 |
| 0.0921        | 8.38  | 79500  | 0.0518          | 0.0573 |
| 0.0897        | 8.43  | 80000  | 0.0514          | 0.0583 |
| 0.0889        | 8.49  | 80500  | 0.0508          | 0.0582 |
| 0.1783        | 8.54  | 81000  | 0.0507          | 0.0574 |
| 0.0854        | 8.59  | 81500  | 0.0505          | 0.0580 |
| 0.0855        | 8.64  | 82000  | 0.0513          | 0.0577 |
| 0.0843        | 8.7   | 82500  | 0.0508          | 0.0580 |
| 0.0858        | 8.75  | 83000  | 0.0501          | 0.0578 |
| 0.0814        | 8.8   | 83500  | 0.0509          | 0.0580 |
| 0.0823        | 8.85  | 84000  | 0.0509          | 0.0575 |
| 0.0857        | 8.91  | 84500  | 0.0499          | 0.0599 |
| 0.0787        | 8.96  | 85000  | 0.0505          | 0.0598 |
| 0.0805        | 9.01  | 85500  | 0.0510          | 0.0606 |
| 0.0798        | 9.07  | 86000  | 0.0515          | 0.0603 |
| 0.0812        | 9.12  | 86500  | 0.0507          | 0.0586 |
| 0.0781        | 9.17  | 87000  | 0.0511          | 0.0612 |
| 0.0814        | 9.22  | 87500  | 0.0508          | 0.0589 |
| 0.0821        | 9.28  | 88000  | 0.0507          | 0.0588 |
| 0.0808        | 9.33  | 88500  | 0.0498          | 0.0571 |
| 0.0793        | 9.38  | 89000  | 0.0502          | 0.0574 |
| 0.0791        | 9.43  | 89500  | 0.0498          | 0.0568 |
| 0.0779        | 9.49  | 90000  | 0.0507          | 0.0570 |
| 0.0777        | 9.54  | 90500  | 0.0508          | 0.0573 |
| 0.0816        | 9.59  | 91000  | 0.0493          | 0.0573 |
| 0.0835        | 9.64  | 91500  | 0.0496          | 0.0563 |
| 0.0827        | 9.7   | 92000  | 0.0493          | 0.0559 |
| 0.0904        | 9.75  | 92500  | 0.0492          | 0.0564 |
| 0.0753        | 9.8   | 93000  | 0.0503          | 0.0557 |
| 0.0748        | 9.86  | 93500  | 0.0493          | 0.0554 |
| 0.0759        | 9.91  | 94000  | 0.0499          | 0.0557 |
| 0.0825        | 9.96  | 94500  | 0.0498          | 0.0566 |
| 0.0787        | 10.01 | 95000  | 0.0499          | 0.0561 |
| 0.0804        | 10.07 | 95500  | 0.0499          | 0.0562 |
| 0.0784        | 10.12 | 96000  | 0.0500          | 0.0555 |
| 0.0747        | 10.17 | 96500  | 0.0497          | 0.0548 |
| 0.0748        | 10.22 | 97000  | 0.0492          | 0.0565 |
| 0.0732        | 10.28 | 97500  | 0.0493          | 0.0547 |
| 0.0766        | 10.33 | 98000  | 0.0490          | 0.0552 |
| 0.0762        | 10.38 | 98500  | 0.0504          | 0.0551 |
| 0.0744        | 10.44 | 99000  | 0.0496          | 0.0553 |
| 0.0702        | 10.49 | 99500  | 0.0496          | 0.0548 |
| 0.0802        | 10.54 | 100000 | 0.0499          | 0.0545 |
| 0.1605        | 10.59 | 100500 | 0.0477          | 0.0543 |
| 0.0768        | 10.65 | 101000 | 0.0487          | 0.0552 |
| 0.0833        | 10.7  | 101500 | 0.0495          | 0.0550 |
| 0.0782        | 10.75 | 102000 | 0.0479          | 0.0553 |
| 0.0813        | 10.8  | 102500 | 0.0490          | 0.0542 |
| 0.0712        | 10.86 | 103000 | 0.0485          | 0.0541 |
| 0.0703        | 10.91 | 103500 | 0.0486          | 0.0544 |
| 0.0765        | 10.96 | 104000 | 0.0480          | 0.0538 |
| 0.0796        | 11.02 | 104500 | 0.0486          | 0.0535 |
| 0.0778        | 11.07 | 105000 | 0.0492          | 0.0535 |
| 0.0735        | 11.12 | 105500 | 0.0494          | 0.0533 |
| 0.068         | 11.17 | 106000 | 0.0485          | 0.0528 |
| 0.0687        | 11.23 | 106500 | 0.0498          | 0.0534 |
| 0.0641        | 11.28 | 107000 | 0.0493          | 0.0534 |
| 0.0712        | 11.33 | 107500 | 0.0485          | 0.0526 |
| 0.0827        | 11.38 | 108000 | 0.0484          | 0.0530 |
| 0.0715        | 11.44 | 108500 | 0.0480          | 0.0533 |
| 0.0733        | 11.49 | 109000 | 0.0482          | 0.0532 |
| 0.0754        | 11.54 | 109500 | 0.0481          | 0.0537 |
| 0.0719        | 11.59 | 110000 | 0.0475          | 0.0533 |
| 0.0707        | 11.65 | 110500 | 0.0479          | 0.0536 |
| 0.0687        | 11.7  | 111000 | 0.0483          | 0.0535 |
| 0.0713        | 11.75 | 111500 | 0.0485          | 0.0535 |
| 0.0674        | 11.81 | 112000 | 0.0482          | 0.0537 |
| 0.0704        | 11.86 | 112500 | 0.0487          | 0.0537 |
| 0.0691        | 11.91 | 113000 | 0.0484          | 0.0541 |
| 0.0708        | 11.96 | 113500 | 0.0485          | 0.0548 |
| 0.0683        | 12.02 | 114000 | 0.0487          | 0.0541 |
| 0.0691        | 12.07 | 114500 | 0.0492          | 0.0540 |
| 0.0679        | 12.12 | 115000 | 0.0486          | 0.0540 |
| 0.073         | 12.17 | 115500 | 0.0479          | 0.0545 |
| 0.0647        | 12.23 | 116000 | 0.0484          | 0.0534 |
| 0.0663        | 12.28 | 116500 | 0.0484          | 0.0532 |
| 0.0687        | 12.33 | 117000 | 0.0483          | 0.0532 |
| 0.0696        | 12.39 | 117500 | 0.0482          | 0.0541 |
| 0.068         | 12.44 | 118000 | 0.0487          | 0.0531 |
| 0.0681        | 12.49 | 118500 | 0.0483          | 0.0530 |
| 0.0774        | 12.54 | 119000 | 0.0481          | 0.0533 |
| 0.0656        | 12.6  | 119500 | 0.0484          | 0.0529 |
| 0.0628        | 12.65 | 120000 | 0.0479          | 0.0533 |
| 0.0657        | 12.7  | 120500 | 0.0490          | 0.0538 |
| 0.0668        | 12.75 | 121000 | 0.0485          | 0.0533 |
| 0.0656        | 12.81 | 121500 | 0.0484          | 0.0531 |
| 0.0745        | 12.86 | 122000 | 0.0474          | 0.0526 |
| 0.0654        | 12.91 | 122500 | 0.0485          | 0.0528 |
| 0.0764        | 12.97 | 123000 | 0.0482          | 0.0529 |
| 0.0673        | 13.02 | 123500 | 0.0491          | 0.0526 |
| 0.0649        | 13.07 | 124000 | 0.0489          | 0.0527 |
| 0.0655        | 13.12 | 124500 | 0.0485          | 0.0520 |
| 0.0688        | 13.18 | 125000 | 0.0476          | 0.0524 |
| 0.0683        | 13.23 | 125500 | 0.0475          | 0.0523 |
| 0.0632        | 13.28 | 126000 | 0.0480          | 0.0528 |
| 0.063         | 13.33 | 126500 | 0.0483          | 0.0528 |
| 0.1418        | 13.39 | 127000 | 0.0464          | 0.0531 |
| 0.0693        | 13.44 | 127500 | 0.0473          | 0.0525 |
| 0.0696        | 13.49 | 128000 | 0.0477          | 0.0519 |
| 0.0644        | 13.54 | 128500 | 0.0477          | 0.0520 |
| 0.0625        | 13.6  | 129000 | 0.0480          | 0.0518 |
| 0.0682        | 13.65 | 129500 | 0.0471          | 0.0517 |
| 0.0698        | 13.7  | 130000 | 0.0480          | 0.0521 |
| 0.0643        | 13.76 | 130500 | 0.0482          | 0.0522 |
| 0.065         | 13.81 | 131000 | 0.0478          | 0.0521 |
| 0.0648        | 13.86 | 131500 | 0.0482          | 0.0519 |
| 0.0689        | 13.91 | 132000 | 0.0476          | 0.0520 |
| 0.0721        | 13.97 | 132500 | 0.0473          | 0.0523 |
| 0.0652        | 14.02 | 133000 | 0.0474          | 0.0519 |
| 0.0651        | 14.07 | 133500 | 0.0479          | 0.0519 |
| 0.0638        | 14.12 | 134000 | 0.0478          | 0.0520 |
| 0.0626        | 14.18 | 134500 | 0.0482          | 0.0519 |
| 0.0656        | 14.23 | 135000 | 0.0479          | 0.0521 |
| 0.0633        | 14.28 | 135500 | 0.0478          | 0.0519 |
| 0.0665        | 14.34 | 136000 | 0.0480          | 0.0519 |
| 0.0638        | 14.39 | 136500 | 0.0478          | 0.0517 |
| 0.0691        | 14.44 | 137000 | 0.0474          | 0.0515 |
| 0.0642        | 14.49 | 137500 | 0.0476          | 0.0514 |
| 0.0696        | 14.55 | 138000 | 0.0475          | 0.0515 |
| 0.0601        | 14.6  | 138500 | 0.0478          | 0.0515 |
| 0.0616        | 14.65 | 139000 | 0.0476          | 0.0515 |
| 0.0648        | 14.7  | 139500 | 0.0477          | 0.0516 |
| 0.0682        | 14.76 | 140000 | 0.0477          | 0.0515 |
| 0.0641        | 14.81 | 140500 | 0.0474          | 0.0515 |
| 0.0579        | 14.86 | 141000 | 0.0475          | 0.0514 |
| 0.0613        | 14.92 | 141500 | 0.0475          | 0.0514 |
| 0.0624        | 14.97 | 142000 | 0.0475          | 0.0514 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1