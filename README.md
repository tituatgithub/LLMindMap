# IISER Bhopal – DSE Knowledge Graph  

**Automated extraction of structured academic knowledge from the Department of Data Science & Engineering, IISER Bhopal using LLMs**

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Groq](https://img.shields.io/badge/Groq-Llama%203.1%208B-green)
![License](https://img.shields.io/badge/license-MIT-blue)
[![Contributors](https://img.shields.io/github/contributors/your-username/IISERB-DSE-Knowledge-Graph)](https://github.com/your-username/IISERB-DSE-Knowledge-Graph/graphs/contributors)

A fully automated pipeline that turns unstructured department web pages into a clean, query-ready **Knowledge Graph** containing:

- Faculty members  
- PhD scholars  
- Post-doctoral researchers  
- BS-MS students (3rd–5th year)  
- Research groups  
- Department & institute hierarchy  

**206 nodes · 249 relationships** (as of Nov 2025)

---

### Why this project?

- Demonstrates real-world **LLM-powered knowledge graph construction** from messy HTML/text  
- Zero-shot entity + relation extraction using **Groq + Llama 3.1 8B**  
- Reproducible, modular, and ready for extension to other departments/institutes  

---
├── data/raw/                  ← Original scraped text files
├── notebooks/                 ← Original Jupyter notebook
├── src/build_kg.py            ← Main clean & runnable script
├── knowledge_graphs/
│   ├── dse_kg.json            ← Final knowledge graph (JSON)
│   ├── nodes.csv              ← All entities
│   └── edges.csv              ← All relationships
├── requirements.txt
└── README.md


### Repository Structure
Output will be saved in knowledge_graphs/

Sample Nodes & Relations
Nodes include:

Faculty, Student (BS/MS/PhD/PostDoc), ResearchGroup, Department, Institute

Relations:

belongsTo → Department
guidedBy → Faculty advisor
memberOf → Research group
heads → HoD / Group head
partOf → Institute
Contributors
https://github.com/tituatgithub.png?size=100
@tituatgithubhttps://avatars.githubusercontent.com/u/129749737?v=4
@Rudra-prasad-tarai
