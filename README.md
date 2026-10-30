# Arabic Search Intent Classifier & Heuristic Taxonomy

> Stop misclassifying Arabic queries. Classify Egyptian and Gulf search intents accurately with a zero-dependency Python heuristic engine.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a lightweight, dependency-free Python CLI (`arabic_intent_classifier.py`) that ingests a CSV of Arabic keywords and classifies each query into Informational, Commercial Investigation, Transactional, or Navigational using a dialect-aware heuristic lexicon covering Egyptian, Saudi, and Gulf phrasing. Includes test suite with 100 sample queries.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `data/intent_lexicon_ar.json`
- `examples/classified_output.csv`
- `examples/input_keywords.csv`
- `LICENSE`
- `README.md`
- `src/classifier.py`
- `tests/test_classifier.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/classifier.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "seo",
  "repository": "arabic-search-intent-classifier",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Colloquial Arabic Intent Ambiguity:** Informational and commercial intent often overlap in Arabic social queries (e.g., 'كام سعره' vs 'أفضل نوع').
- **Transliterated Brand Queries:** Queries containing Arabizi or English brand names require phonological normalization prior to intent scoring.
- **Local Commercial Heuristics:** Keywords containing 'في الرياض' or 'كاش' signal immediate transactional and local purchase intent.

---

## 📚 Primary Documentation & Verifiable References

- [Google Search Central: Search Intent & Evaluator Guidelines](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) - Quality evaluation principles for transactional and informational intent.
- [NYU Abu Dhabi CAMeL Lab: Arabic NLP Resources](https://camel.abudhabi.nyu.edu/) - Computational linguistics datasets and dialectal morphology tools.
- [W3C Internationalization Language Enablement](https://www.w3.org/International/) - Standards for multilingual web information classification.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
