LowCost-Phenotyping-AI-Lettuce-Thermal-Impact v1.0
Prototype of a low-cost phenotyping platform for analyzing thermal impact on lettuce**

---

Overview
This repository hosts the prototype of a **low-cost phenotyping system** designed to evaluate the **thermal impact and physiological disorders in lettuce (*Lactuca sativa L.*)** under tropical greenhouse conditions.  
The system applies **Artificial Intelligence (AI) and prompt-chaining logic** to interpret agronomic images and identify visual symptoms associated with **heat stress, tipburn, chlorosis, and dehydration**.

The platform was developed as part of Embrapa Hortaliças’ research on **digital phenotyping and climate resilience in horticulture**, contributing to the **Agenda ABC+** and the **United Nations Sustainable Development Goals (SDGs 2, 12, and 13)**.

---

Main Features
- Automated visual analysis of lettuce seedlings under thermal stress;
- AI-based interpretation of physiological disorders through chained prompts;
- Integration with open-source environments (Python);
- Standardized report generation for field or greenhouse experiments;
- Ready for adaptation to other vegetable crops or stress types.

---

Technical Information
Programming language:** Python 3.10+  
Main scripts:
- `# main_analise.py` — Main execution routine for thermal stress evaluation  
- `prompt_engine.py` — Prompt-chaining engine for agronomic reasoning  
- `import hashlib.py` — Hash generation and internal validation utilities  
- `Visual analysis prompt_heat stress evaluation.pynb` — Example notebook for guided use

Dependencies:  
`openai`, `pandas`, `numpy`, `matplotlib`,`os`, `json`, `hashlib`, VSB

---

Workflow
1. Capture experimental images from the low-cost phenotyping setup;  
2. Load images and metadata into the platform;  
3. Execute the main script for prompt-based interpretation;  
4. Review automatically generated diagnostics and comparative summaries.

---

Validation and TRL
The software has been validated internally using greenhouse experiments on lettuce cultivars sensitive to thermal stress.  
**Technology Readiness Level (TRL): 7** — validated in a relevant experimental environment.

---

Institutional Context
Developed by **Embrapa Hortaliças (Brazilian Agricultural Research Corporation)**  
as part of the research line *Climate-Resilient Horticulture and Digital Agriculture*.  
The system is part of the ongoing project on **low-cost AI phenotyping platforms** coordinated by  
**Carlos Eduardo Pacheco Lima, Ph.D. (Embrapa Hortaliças / CNPq DT Fellow / IPCC Reviewer)**.

---

Intellectual Property
This software is a **computer program under institutional analysis by Embrapa Hortaliças**, for registration with the **INPI (Brazilian Patent and Trademark Office)**.  
Temporary license provided under **BSD-3 Clause**, for research and educational use only.

> © 2025 Embrapa Hortaliças.  
> Redistribution and use in source and binary forms, with or without modification, are permitted under the BSD-3 license.

---

Citation
If you use this software in academic work, please cite as Zenodo platform:
Authors
Carlos Eduardo Pacheco Lima
PhD in Soils and Plant Nutrition
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
Productivity Fellow in Technological Development and Innovative Extension –
CNPq/Level C
E-mail: carlos.pacheco-lima@embrapa.br

Ítalo Moraes Rocha Guedes
PhD in Soils and Plant Nutrition
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
E-mail: italo.guedes@embrapa.br

Mariana Rodrigues Fontenelle
PhD in Agricultural Microbiology
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
E-mail: mariana.fontenelle@embrapa.br

Fábio Akiyoshi Suinaga
PhD in Genetics and Breeding
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
Productivity Fellow in Technological Development and Innovative Extension –
CNPq/Level 2
E-mail: fabio.suinaga@embrapa.br

Juscimar da Silva
PhD in Soils and Plant Nutrition
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
E-mail: juscimar.silva@embrapa.br

Marcos Brandão Braga
PhD in Irrigation and Drainage
Institution: Embrapa Vegetables
Address: Brasília, Federal District, Brazil
E-mail: marcos.braga@embrapa.br

- [License BSD-3 Clause](./LICENSE)

---

Keywords
*AI Phenotyping • Lettuce • Heat Stress • Low-Cost Sensors • Climate Resilience • Embrapa Hortaliças*

