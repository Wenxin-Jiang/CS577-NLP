---
language: th
widget:
- text: "สวนกุหลาบเป็นโรงเรียนอะไร"
  context: "โรงเรียนสวนกุหลาบวิทยาลัย (Suankularb Wittayalai School) (อักษรย่อ : ส.ก. / S.K.) เป็นโรงเรียนชายล้วน ระดับชั้นมัธยมศึกษาขนาดใหญ่พิเศษ สังกัดสำนักงานเขตพื้นที่การศึกษามัธยมศึกษาเขต 1 สำนักงานคณะกรรมการการศึกษาขั้นพื้นฐาน (ชื่อเดิม: กรมสามัญศึกษา) กระทรวงศึกษาธิการ ก่อตั้งโดย พระบาทสมเด็จพระจุลจอมเกล้าเจ้าอยู่หัว ได้รับการสถาปนาขึ้นในวันที่ 8 มีนาคม พ.ศ. 2424 (ขณะนั้นนับวันที่ 1 เมษายน เป็นวันขึ้นปีใหม่ เมื่อนับอย่างสากลถือเป็น พ.ศ. 2425) โดยเป็นโรงเรียนรัฐบาลแห่งแรกของประเทศไทย"
---
# wangchanberta-base-wiki-20210520-spm-finetune-qa

Finetuning `airesearchth/wangchanberta-base-wiki-20210520-spmd` with the training set of `iapp_wiki_qa_squad`, `thaiqa_squad`, and `nsc_qa` (removed examples which have cosine similarity with validation and test examples over 0.8; contexts of the latter two are trimmed to be around 300 `newmm` words). Benchmarks shared on [wandb](https://wandb.ai/cstorm125/wangchanberta-qa) using validation and test sets of `iapp_wiki_qa_squad`.
Trained with [thai2transformers](https://github.com/vistec-AI/thai2transformers/blob/dev/scripts/downstream/train_question_answering_lm_finetuning.py).

Run with:
```
export MODEL_NAME=airesearchth/wangchanberta-base-wiki-20210520-news-spm
CUDA_LAUNCH_BLOCKING=1 python train_question_answering_lm_finetuning.py \\n  --model_name $MODEL_NAME \\n  --dataset_name chimera_qa \\n  --output_dir $MODEL_NAME-finetune-chimera_qa-model \\n  --log_dir $MODEL_NAME-finetune-chimera_qa-log \\n  --model_max_length 400 \\n  --pad_on_right \\n  --fp16
```