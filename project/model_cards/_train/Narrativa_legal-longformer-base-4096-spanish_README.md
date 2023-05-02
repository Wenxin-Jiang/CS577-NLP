---
language:
- es
license: mit
widget:
- text: "Aprobada las Cortes Generales en sesiones plenarias del Congreso de los Diputados y del Senado celebradas el  de octubre de , la Constitución fue ratificada en referéndum el  de diciembre, siendo sancionada y promulgada por el rey Juan Carlos I el  de diciembre y publicada en el Boletín Oficial del Estado el  de diciembre del mismo año.

La promulgación de la Constitución implicó la culminación de la llamada transición a la democracia, que tuvo lugar como consecuencia de la muerte, el  de noviembre de , del anterior jefe de Estado, el dictador Francisco Franco, precipitando una serie de acontecimientos políticos e históricos que transformaron el anterior régimen dictatorial en un «Estado social y democrático de derecho que propugna como valores superiores del ordenamiento jurídico la libertad, la justicia, la igualdad y el pluralismo político», tal y como proclama el artículo primero de la Constitución.​ En él también se afianza el principio de «soberanía nacional», que «reside en el pueblo español»,​ y se establece «la Monarquía parlamentaria» como forma de gobierno.​ Deroga, además, en la Disposición Derogatoria, las Leyes Fundamentales del Reino aprobadas en  y modificadas en múltiples ocasiones, la última de ellas en  precisamente para abrir paso a la <mask>.

«La Constitución se fundamenta en la indisoluble unidad de la Nación española, patria común e indivisible de todos los españoles y reconoce el derecho a la autonomía de las nacionalidades y regiones que la integran» (artículo ). Establece una organización territorial basada «en municipios, en provincias y en las Comunidades Autónomas que se constituyan»,​ rigiendo «la solidaridad entre todas ellas».​​ Tras el proceso de formación del Estado de las Autonomías, las comunidades autónomas gozan de una autonomía de naturaleza política que configura a España como un Estado autonómico.n. ​ Las entidades locales, como los municipios y las provincias, gozan de una autonomía de naturaleza administrativa, y sus instituciones actúan en conformidad con criterios de oportunidad dentro del marco legal fijado por el Estado y las comunidades autónomas.​

El rey es el jefe de Estado, símbolo de su unidad y permanencia, arbitra y modera el funcionamiento regular de las instituciones, asume la más alta representación del Estado español en las relaciones internacionales, especialmente con las naciones de su comunidad histórica, y ejerce las funciones que le atribuyen expresamente la Constitución y las leyes.​ Sus actos tienen una naturaleza reglada, cuya validez depende del refrendo de la autoridad competente que, según el caso, es el presidente del Gobierno, el presidente del Congreso de los Diputados, o un ministro."
- text: "CONSEJO GENERAL DEL PODER JUDICIAL 18485. Acuerdo de 3 de noviembre de 2022, de la Comisión Permanente del Consejo General del Poder Judicial, por el que se convoca concurso para la provisión de puestos de trabajo en la Gerencia del Consejo. En la Gerencia del Consejo General del Poder Judicial se encuentran vacantes dos puestos de subalterno dotados presupuestariamente, con las características que se relacionan en el anexo I de este acuerdo y cuya provisión se considera necesaria en orden a la correcta asunción de las funciones encomendadas a ese órgano técnico. Por ello la Comisión Permanente del Consejo General del Poder Judicial, en su reunión del día de la fecha, ha acordado convocar un concurso de méritos para la cobertura de los citados puestos, de conformidad con lo dispuesto en los artículos 625 y concordantes de la Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial. El concurso de méritos se regirá por las siguientes Normas Primera. Requisitos de participación. 1. Podrán tomar parte en el presente concurso los funcionarios/as pertenecientes a las agrupaciones profesionales a que se refiere la disposición transitoria tercera del Real Decreto Legislativo 5/2015, de 30 de octubre, por el que se aprueba el texto refundido de la Ley del Estatuto Básico del Empleado Público (anterior grupo E del artículo 25 de la Ley 30/1984, de 2 de agosto) o a los cuerpos o escalas de Auxilio Judicial de la Administración de Justicia, de conformidad con el artículo 624 de la Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial, siempre que reúnan las condiciones generales exigidas al puesto de trabajo y los requisitos determinados en esta convocatoria en la fecha en que termine el plazo de presentación de solicitudes. 2. Los funcionarios/as con destino definitivo podrán participar siempre que hayan transcurrido, al menos, dos años desde la toma de posesión del último destino definitivo. No será necesario cumplir este plazo para los funcionarios/as que hayan sido removidos del puesto de trabajo obtenido por el procedimiento de concurso o, también, si ha sido suprimido su puesto de trabajo. Los funcionarios/as con destino definitivo en el Consejo, podrán participar si ha transcurrido, al menos, un año desde su toma de posesión en el último destino definitivo, salvo en el caso de aquellos/as que participen desde un puesto de trabajo con nivel inferior al convocado. 3. Los funcionarios/as en situación administrativa de <mask> en otras administraciones públicas o de excedencia voluntaria por interés particular o por agrupación familiar solo podrán participar en el concurso si en la fecha de finalización del plazo de presentación de solicitudes han transcurrido más de dos años en las indicadas situaciones. En el caso de la primera situación mencionada deberá haber transcurrido asimismo un plazo de dos años desde que obtuvieron su último destino definitivo. 4. Los funcionarios/as en situación de servicios especiales o en excedencia por cuidado de familiares solo podrán participar si en la fecha en que termina el plazo de presentación de solicitudes han transcurrido dos años desde la toma de posesión del último destino definitivo."
- text: "La Constitución española de 1978 es la <mask> suprema del ordenamiento jurídico español."
tags:
- Long documents
- longformer
- robertalex
- spanish
- legal

---

# Legal ⚖️ longformer-base-4096-spanish

`legal-longformer-base-4096` is a BERT-like model started from the RoBERTa checkpoint (**[RoBERTalex](https://huggingface.co/PlanTL-GOB-ES/RoBERTalex)** in this case) and pre-trained for *MLM* on long documents from the [Spanish Legal Domain Corpora](https://zenodo.org/record/5495529/#.Y205lpHMKV5). It supports sequences of length up to **4,096**!

**Longformer** uses a combination of a sliding window (*local*) attention and *global* attention. Global attention is user-configured based on the task to allow the model to learn task-specific representations.


This model was made following the research done by [Iz Beltagy and Matthew E. Peters and Arman Cohan](https://arxiv.org/abs/2004.05150).

## Model (base checkpoint)
[RoBERTalex](https://huggingface.co/PlanTL-GOB-ES/RoBERTalex?)
There are few models trained for the Spanish language. Some of the models have been trained with a low resource, unclean corpora. The ones derived from the Spanish National Plan for Language Technologies are proficient in solving several tasks and have been trained using large-scale clean corpora. However, the Spanish Legal domain language could be thought of as an independent language on its own. We, therefore, created a Spanish Legal model from scratch trained exclusively on legal corpora.

## Dataset
[Spanish Legal Domain Corpora](https://zenodo.org/record/5495529)
A collection of corpora of Spanish legal domain.

More legal domain resources: https://github.com/PlanTL-GOB-ES/lm-legal-es

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{narrativa2022legal-longformer-base-4096-spanish,
  title={Legal Spanish LongFormer by Narrativa},
  author={Romero, Manuel},
  publisher={Hugging Face},
  journal={Hugging Face Hub},
  howpublished={\url{https://huggingface.co/Narrativa/legal-longformer-base-4096-spanish}},
  year={2022}
}
```

## Disclaimer
The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.


> About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI