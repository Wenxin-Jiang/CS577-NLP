---
license: afl-3.0
widget:
- text: "The case of a 72-year-old male with @DISEASE$ with poor insulin control (fasting hyperglycemia greater than 180 mg/dl) who had a long-standing polyuric syndrome is here presented. Hypernatremia and plasma osmolality elevated together with a low urinary osmolality led to the suspicion of diabetes insipidus, which was subsequently confirmed by the dehydration test and the administration of @GENE$ sc."
  example_title: "Example 1"
- text: "Hypernatremia and plasma osmolality elevated together with a low urinary osmolality led to the suspicion of diabetes insipidus, which was subsequently confirmed by the dehydration test and the administration of @GENE$ sc. With 61% increase in the calculated urinary osmolarity one hour post desmopressin s.c., @DISEASE$ was diagnosed."
  example_title: "Example 2"
---

The following is a fine-tuning of the BioBert models on the GAD dataset.

The model works by masking the gene string with "@GENE$" and the disease string with "@DISEASE$".

The output is a text classification that can either be:
- "LABEL0" if there is no relation
- "LABEL1" if there is a relation.