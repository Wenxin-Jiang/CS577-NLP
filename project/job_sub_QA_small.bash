#!/bin/bash
module load anaconda/2020.11-py38
conda activate PTM
module load cuda/11.7.0
module load gcc/6.3.0

cd $SLURM_SUBMIT_DIR

python train_QA.py