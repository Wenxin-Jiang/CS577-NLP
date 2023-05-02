---
tags:
- summarization
- news
language: es
datasets:
- mlsum
widget:
- text: 'Al filo de las 22.00 horas del jueves, la Asamblea de Madrid vive un momento sorprendente: Vox decide no apoyar una propuesta del PP en favor del blindaje fiscal de la Comunidad. Se ha roto la unidad de los tres partidos de derechas. Es un hecho excepcional. Desde que arrancó la legislatura, PP, Cs y Vox han votado en bloque casi el 75% de las veces en el pleno de la Cámara. Juntos decidieron la composición de la Mesa de la Asamblea. Juntos invistieron presidenta a Isabel Díaz Ayuso. Y juntos han votado la mayoría de proposiciones no de ley, incluida la que ha marcado el esprint final de la campaña para las elecciones generales: acaban de instar al Gobierno de España a "la ilegalización inmediata" de los partidos separatistas "que atenten contra la unidad de la Nación". Los críticos de Cs no comparten el apoyo al texto de Vox contra el secesionisimo Ese balance retrata una necesidad antes que una complicidad, según fuentes del PP con predicamento en la dirección regional y nacional. Tras casi 15 años gobernando con mayoría absoluta, la formación conservadora vivió como una tortura la pasada legislatura, en la que dependió de Cs para sacar adelante sus iniciativas. El problema se agudizó tras las elecciones autonómicas de mayo. El PP ha tenido que formar con Cs el primer gobierno de coalición de la historia de la región, y ni siquiera con eso le basta para ganar las votaciones de la Cámara. Los dos socios gubernamentales necesitan a Vox, la menos predecible de las tres formaciones. "Tenemos que trabajar juntos defendiendo la unidad del país, por eso no quisimos dejar a Vox solo", dijo ayer Díaz Ayuso para justificar el apoyo de PP y Cs a la proposición de la extrema derecha sobre Cataluña. "Después nosotros llevábamos otra proposición para defender el blindaje fiscal de Madrid, y ahí Vox nos dejó atrás. No permitió que esto saliera. Es un grave error por su parte", prosiguió, recalcando el enfado del PP. "Demuestra que está más en cuestiones electoralistas", subrayó. "Los que pensamos, con nuestras inmensas diferencias, que tenemos cosas en común que nos unen como partidos que queremos Comunidades libres, con bajos impuestos, en las que se viva con seguridad y en paz, tenemos que estar unidos", argumentó. "Y por lo menos nosotros de nuestra línea no nos separamos". Al contrario de lo que está ocurriendo el Ayuntamiento de Madrid, donde el PP y Cs ya han defendido posiciones de voto distintas, pese a compartir el Gobierno, en la Asamblea los partidos de Díaz Ayuso e Ignacio Aguado están actuando con la máxima lealtad en las votaciones del pleno. Otra cosa son las comisiones. Y el caso Avalmadrid. Es en ese terreno donde Cs y Vox están buscando el margen de maniobra necesario para separarse del PP en plena campaña electoral, abandonando a su suerte a su socio para distinguirse ante los electores. —"Usted me ha dejado tirada", le espetó la presidenta de la Comunidad de Madrid a Rocío Monasterio tras saber que Vox permitiría que la izquierda tuviera mayoría en la comisión parlamentaria que investigará los avales concedidos por la empresa semipública entre 2007 y 2018, lo que podría incluir el de 400.000 euros aprobado en 2011, y nunca devuelto al completo, para una empresa participada por el padre de Isabel Díaz Ayuso. "Monasterio no es de fiar. Dice una cosa y hace la contraria", dice una fuente popular sobre las negociaciones mantenidas para repartirse los puestos de las diferentes comisiones, que Vox no cumplió tras buscar un segundo pacto con otras formaciones (que no llegó a buen puerto). Ilegalización de Vox Los tres partidos de derechas también se han enfrentado por la ubicación de Vox en el pleno. Las largas negociaciones para la investidura de Díaz Ayuso dejaron heridas abiertas. Y los diputados de Cs no desaprovechan la oportunidad de lanzar dardos contra los de Vox, pero luego coinciden con ellos en la mayoría de votaciones. Ocurrió, por ejemplo, el jueves, cuando se debatía la polémica proposición para instar al Gobierno nacional a ilegalizar a los partidos separatistas que atenten contra la unidad de España. —"Mostrar nuestra sorpresa ante la presentación por parte de Vox de esta propuesta", lanzó Araceli Gómez, diputada de la formación de Aguado. "Sorprende que planteen ustedes este asunto cuando está también sobre la mesa el debate de su propia ilegalización por atentar contra el ordenamiento jurídico o contra valores constitucionales como la igualdad o la no discriminación". Luego de esa descalificación, y ante la incredulidad de los diputados de los partidos de izquierdas, Cs unió sus votos a los de Vox y a los del PP. La decisión ha provocado polémica interna, como demuestra que Albert Rivera no la apoyara ayer explícitamente. Tampoco ha sido bien acogida por el sector crítico de la formación. Pero ha demostrado una cosa: en Madrid hay tres partidos que casi siempre votan como uno.'
---

# Spanish RoBERTa2RoBERTa (roberta-base-bne) fine-tuned on MLSUM ES for summarization

## Model
[BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) (RoBERTa Checkpoint)

## Dataset
**MLSUM** is the first large-scale MultiLingual SUMmarization dataset. Obtained from online newspapers, it contains 1.5M+ article/summary pairs in five different languages -- namely, French, German, **Spanish**, Russian, Turkish. Together with English newspapers from the popular CNN/Daily mail dataset, the collected data form a large scale multilingual dataset which can enable new research directions for the text summarization community. We report cross-lingual comparative analyses based on state-of-the-art systems. These highlight existing biases which motivate the use of a multi-lingual dataset.

[MLSUM es](https://huggingface.co/datasets/viewer/?dataset=mlsum)

## Results

|Set|Metric| Value|
|----|------|------|
| Test  |Rouge2 - mid -precision | 11.42|
| Test | Rouge2 - mid - recall | 10.58 |
| Test | Rouge2 - mid - fmeasure | 10.69|
| Test | Rouge1 - fmeasure | 28.83 |
| Test | RougeL - fmeasure  | 23.15 |

Raw metrics using HF/metrics `rouge`:

```python
rouge = datasets.load_metric("rouge")
rouge.compute(predictions=results["pred_summary"], references=results["summary"])

{'rouge1': AggregateScore(low=Score(precision=0.30393366820245, recall=0.27905239591639935, fmeasure=0.283148902808752), mid=Score(precision=0.3068521142101569, recall=0.2817252494122592, fmeasure=0.28560373425206464), high=Score(precision=0.30972608774202665, recall=0.28458152325781716, fmeasure=0.2883786700591887)),
 'rougeL': AggregateScore(low=Score(precision=0.24184668819794716, recall=0.22401171380621518, fmeasure=0.22624104698839514), mid=Score(precision=0.24470388406868163, recall=0.22665793214539162, fmeasure=0.2289118878817394), high=Score(precision=0.2476594458951327, recall=0.22932683203591905, fmeasure=0.23153001570662513))}
 
rouge.compute(predictions=results["pred_summary"], references=results["summary"], rouge_types=["rouge2"])["rouge2"].mid

Score(precision=0.11423200347113865, recall=0.10588038944902506, fmeasure=0.1069921217219595)
```

## Usage

 ```python
 import torch
 from transformers import RobertaTokenizerFast, EncoderDecoderModel
 device = 'cuda' if torch.cuda.is_available() else 'cpu'
 ckpt = 'Narrativa/bsc_roberta2roberta_shared-spanish-finetuned-mlsum-summarization'
 tokenizer = RobertaTokenizerFast.from_pretrained(ckpt)
model = EncoderDecoderModel.from_pretrained(ckpt).to(device)

def generate_summary(text):

    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)
    
text = "Your text here..."
generate_summary(text)
```

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI

