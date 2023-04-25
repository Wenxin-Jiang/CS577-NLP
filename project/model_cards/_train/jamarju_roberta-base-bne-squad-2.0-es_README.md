---
language:
- es
datasets:
- squad_es
widget:
- text: "¿Quién era el duque en la batalla de Hastings?"
  context: "La dinastía normanda tuvo un gran impacto político, cultural y militar en la Europa medieval e incluso en el Cercano Oriente. Los normandos eran famosos por su espíritu marcial y, finalmente, por su piedad cristiana, convirtiéndose en exponentes de la ortodoxia católica en la que se asimilaron. Adoptaron la lengua galorromance de la tierra franca que establecieron, siendo su dialecto conocido como francés normando, normando o normando, una lengua literaria importante. El ducado de Normandía, que formaron por tratado con la corona francesa, fue un gran feudo de la Francia medieval, y bajo Ricardo I de Normandía se forjó en un principado cohesionado y formidable en la tenencia feudal. Los normandos se caracterizan tanto por su cultura, como por su singular arquitectura románica y sus tradiciones musicales, y por sus importantes logros e innovaciones militares. Aventureros normandos fundaron el Reino de Sicilia bajo Roger II después de conquistar el sur de Italia con los sarracenos y bizantinos, y una expedición en nombre de su duque, Guillermo el Conquistador, condujo a la conquista normanda de Inglaterra. La influencia cultural y militar normanda se extendió desde estos nuevos centros europeos a los estados cruzados del Cercano Oriente, donde su príncipe Bohemundo I fundó el Principado de Antioquía en el Levante mediterráneo, a Escocia y Gales en Gran Bretaña."
---

This is the [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) model ([source](https://github.com/PlanTL-SANIDAD/lm-spanish)) trained on the [squad_es v2.0.0](https://huggingface.co/datasets/squad_es) dataset ([source](https://github.com/ccasimiro88/TranslateAlignRetrieve)).

Current achievement: em=58.80, f1=67.40

Results:

```
{
    "epoch": 4.0,
    "eval_HasAns_exact": 48.51551956815115,
    "eval_HasAns_f1": 65.70745010262016,
    "eval_HasAns_total": 5928,
    "eval_NoAns_exact": 69.0893760539629,
    "eval_NoAns_f1": 69.0893760539629,
    "eval_NoAns_total": 5930,
    "eval_best_exact": 58.804182830156854,
    "eval_best_exact_thresh": 0.0,
    "eval_best_f1": 67.39869828034618,
    "eval_best_f1_thresh": 0.0,
    "eval_exact": 58.804182830156854,
    "eval_f1": 67.39869828034568,
    "eval_samples": 12211,
    "eval_total": 11858
}
```

Training script:

```
python -m torch.distributed.launch --nproc_per_node=3 ./run_qa.py \
    --model_name_or_path BSC-TeMU/roberta-base-bne \
    --dataset_name squad_es \
    --dataset_config_name v2.0.0 \
    --do_train \
    --do_eval \
    --learning_rate 3e-5 \
    --num_train_epochs 4 \
    --max_seq_length 384 \
    --doc_stride 128 \
    --output_dir ./models/roberta-base-bne-squad-2.0-es/ \
    --per_device_eval_batch_size=8   \
    --per_device_train_batch_size=8   \
    --version_2_with_negative \
    --ddp_find_unused_parameters=False \
    --overwrite_output_dir \
```
