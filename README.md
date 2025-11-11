# 🍈 Durian Knowledge Base

An open-source, manually-curated dataset containing detailed information on the most common diseases and pests affecting the Durian tree (Durio zibethinus) in Vietnam.

This project is part of the [PlantDoctor Project](https://github.com/TuMinhIT/PlantDoctor.git) (Please update this link to your actual project repo) and aims to provide high-quality, structured data for AI-powered plant disease diagnostics and chatbot libraries.

**Note:** The data content within `dataset.json` (such as names, symptoms, and treatments) is provided in **Vietnamese (vi)**.

## 📊 Statistics (As of 2025-11-11)

* **10 Diseases** (Fungi, Algae)
* **6 Pests** (Insects, Mites, Nematodes)
* **45+** Pesticides (Active ingredients & trade names)
* **30+** Annotated images
* **100%** of data is aggregated and verified from official Vietnamese agricultural sources (provincial Departments of Agriculture, research institutes, etc.).

## 📁 Data Structure

All data is contained in `dataset.json`. To understand the meaning of each field (e.g., `severity_level`, `active_ingredient`), please review the **[Data Dictionary](docs/data_dictionary.md)**.

## 🚀 Example Usage

To see how to load and query this data using Python, please see the **[example_usage.py](examples/example_usage.py)** file.

## 📜 License

This dataset is licensed under the **[Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE.md)**. You are free to use, share, and adapt it for any purpose (including commercial), as long as you provide proper attribution.

## 🤝 Citation

If you use this dataset in your research or project, please use the **[CITATION.cff](CITATION.cff)** file or cite as follows:

> Trinh Minh Thang. (2025). Durian Knowledge Base [Data set]. Version 0.16.1. Retrieved from https://github.com/mthegn1212/Durian_knowledge_base