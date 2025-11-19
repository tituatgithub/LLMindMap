# IISER Bhopal – DSE Knowledge Graph

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Groq](https://img.shields.io/badge/Groq-Llama%203.1%208B-green)
![License](https://img.shields.io/badge/license-MIT-blue)

**Automated extraction of structured academic knowledge from the Department of Data Science & Engineering, IISER Bhopal using Large Language Models**

A fully automated pipeline that transforms unstructured department web pages into a clean, query-ready **Knowledge Graph** containing comprehensive information about faculty, students, researchers, and institutional structure.

## 📊 Current Statistics

- **206 nodes** across multiple entity types
- **249 relationships** connecting academic entities
- Last updated: November 2025

## 🎯 Project Overview

This project demonstrates real-world **LLM-powered knowledge graph construction** from unstructured web data. It leverages **Groq's Llama 3.1 8B** model to perform zero-shot entity and relation extraction from HTML and text content.

### Key Features

- 🤖 **Automated extraction** from department web pages
- 🧠 **Zero-shot learning** using Groq + Llama 3.1 8B
- 📈 **Structured output** ready for graph databases
- 🔄 **Modular design** easily extensible to other departments
- 🎓 **Comprehensive coverage** of academic hierarchy

## 📦 What's Inside the Knowledge Graph?

### Entity Types

- **Faculty members** - Professors and teaching staff
- **PhD scholars** - Doctoral candidates
- **Post-doctoral researchers** - PostDoc fellows
- **BS-MS students** - 3rd, 4th, and 5th year students
- **Research groups** - Organized research clusters
- **Department** - DSE organizational unit
- **Institute** - IISER Bhopal institution

### Relationship Types

| Relation | Description |
|----------|-------------|
| `belongsTo` | Entity → Department affiliation |
| `guidedBy` | Student → Faculty advisor |
| `memberOf` | Individual → Research group |
| `heads` | Faculty → Department/Group leadership |
| `partOf` | Department → Institute hierarchy |

## 🚀 Getting Started

### Prerequisites

```bash
python 3.9+
```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/iiser-dse-knowledge-graph.git
cd iiser-dse-knowledge-graph

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the extraction pipeline
python extract_knowledge_graph.py

# Output will be saved in knowledge_graphs/
```

## 📂 Repository Structure

```
iiser-dse-knowledge-graph/
├── extract_knowledge_graph.py    # Main extraction pipeline
├── requirements.txt               # Python dependencies
├── knowledge_graphs/              # Output directory
│   ├── nodes.json                # Extracted entities
│   └── relationships.json        # Extracted relations
├── src/
│   ├── scraper.py                # Web scraping module
│   ├── llm_extractor.py          # LLM-based extraction
│   └── graph_builder.py          # Graph construction
└── README.md
```

## 🔧 Technical Details

- **LLM Provider**: Groq Cloud
- **Model**: Llama 3.1 8B Instruct
- **Extraction Method**: Zero-shot prompting with structured output
- **Data Format**: JSON (nodes and edges)
- **Graph Database Compatible**: Neo4j, ArangoDB, NetworkX

## 🎓 Use Cases

- Academic network analysis
- Student-advisor relationship mapping
- Research collaboration discovery
- Department structure visualization
- Alumni tracking systems

## 🤝 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/tituatgithub">
        <img src="https://github.com/tituatgithub.png?size=100" width="100px;" alt=""/>
        <br />
        <sub><b>@tituatgithub</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Rudra-prasad-tarai">
        <img src="https://avatars.githubusercontent.com/u/129749737?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>@Rudra-prasad-tarai</b></sub>
      </a>
    </td>
  </tr>
</table>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- IISER Bhopal Department of Data Science & Engineering
- Groq for providing fast LLM inference
- Meta AI for Llama 3.1 model

## 📮 Contact

For questions or collaboration opportunities, please open an issue or reach out to the contributors.

---

**Made with ❤️ for academic knowledge organization**
