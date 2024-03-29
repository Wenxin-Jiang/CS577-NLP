# BERT-mini model finetuned with M-FAC

This model is finetuned on SST-2 dataset with state-of-the-art second-order optimizer M-FAC.
Check NeurIPS 2021 paper for more details on M-FAC: [https://arxiv.org/pdf/2107.03356.pdf](https://arxiv.org/pdf/2107.03356.pdf).

## Finetuning setup

For fair comparison against default Adam baseline, we finetune the model in the same framework as described here [https://github.com/huggingface/transformers/tree/master/examples/pytorch/text-classification](https://github.com/huggingface/transformers/tree/master/examples/pytorch/text-classification) and just swap Adam optimizer with M-FAC.
Hyperparameters used by M-FAC optimizer:

```bash
learning rate = 1e-4
number of gradients = 1024
dampening = 1e-6
```

## Results

We share the best model out of 5 runs with the following score on SST-2 validation set:

```bash
accuracy = 84.74
```

Mean and standard deviation for 5 runs on SST-2 validation set:

| | Accuracy |
|:----:|:-----------:|
| Adam | 85.46 ± 0.58 |
| M-FAC | 84.20 ± 0.58 |

Results can be reproduced by adding M-FAC optimizer code in [https://github.com/huggingface/transformers/blob/master/examples/pytorch/text-classification/run_glue.py](https://github.com/huggingface/transformers/blob/master/examples/pytorch/text-classification/run_glue.py) and running the following bash script:

```bash
CUDA_VISIBLE_DEVICES=0 python run_glue.py \
  --seed 1234 \
  --model_name_or_path prajjwal1/bert-mini \
  --task_name sst2 \
  --do_train \
  --do_eval \
  --max_seq_length 128 \
  --per_device_train_batch_size 32 \
  --learning_rate 1e-4 \
  --num_train_epochs 3 \
  --output_dir out_dir/ \
  --optim MFAC \
  --optim_args '{"lr": 1e-4, "num_grads": 1024, "damp": 1e-6}'
```

We believe these results could be improved with modest tuning of hyperparameters: `per_device_train_batch_size`, `learning_rate`, `num_train_epochs`, `num_grads` and `damp`. For the sake of fair comparison  and a robust default setup we use the same hyperparameters across all models (`bert-tiny`, `bert-mini`) and all datasets (SQuAD version 2 and GLUE).

Our code for M-FAC can be found here: [https://github.com/IST-DASLab/M-FAC](https://github.com/IST-DASLab/M-FAC).
A step-by-step tutorial on how to integrate and use M-FAC with any repository can be found here: [https://github.com/IST-DASLab/M-FAC/tree/master/tutorials](https://github.com/IST-DASLab/M-FAC/tree/master/tutorials).

## BibTeX entry and citation info

```bibtex
@article{frantar2021m,
  title={M-FAC: Efficient Matrix-Free Approximations of Second-Order Information},
  author={Frantar, Elias and Kurtic, Eldar and Alistarh, Dan},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  year={2021}
}

```
