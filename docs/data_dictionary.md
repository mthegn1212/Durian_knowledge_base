# 📖 Durian Knowledge Base - Data Dictionary

This document explains the meaning of each key in the `dataset.json` file (as of v0.16.1).

---

## 1. Root Object

The JSON file is a single object with three main keys:

* `"metadata"`: (Object) General information about the dataset.
* `"diseases"`: (Array) A list of pathological diseases (caused by fungi, algae, etc.).
* `"pests"`: (Array) A list of harmful pests (insects, mites, nematodes).

---

## 2. Metadata Fields

Contains descriptive information about the dataset itself.

* `"name"`: The full name of the dataset.
* `"version"`: The current version (following SemVer MAJOR.MINOR.PATCH).
* `"description"`: A brief description of the dataset's purpose.
* `"creator"`: (Object) Information about the author.
    * `"name"`, `"affiliation"`, `"email"`, `"orcid"`
* `"created_date"`: The date the project was initiated.
* `"last_updated"`: The date the JSON file was last modified.
* `"license"`: The license code (e.g., "CC BY 4.0").
* `"geographical_coverage"`: The geographical region this data applies to (e.g., "Mekong Delta", "Tây Nguyên").
* `"number_of_diseases"`: Total count of items in the `diseases` array.
* `"number_of_pests"`: Total count of items in the `pests` array.
* `"data_source"`: A general description of the data sources.
* `"repository_url"`: The URL to this GitHub repository.

---

## 3. Disease and Pest Fields

Both `diseases` and `pests` are arrays of objects. Each object describes one specific problem.

### 3.1. General Information

* `"disease_id"` (or `"pest_id"`): A unique identifier (e.g., "SR001", "P001").
* `"disease_name"` (or `"pest_name"`): The most common name (e.g., "Stem Canker").
* `"scientific_name"`: The scientific name of the pathogen or pest (e.g., "Phytophthora sp.").
* `"common_names"`: (Array) Other common names.
* `"pathogen_type"` (or `"pest_type"`): The classification of the agent (e.g., "nấm" (fungus), "tảo" (algae), "Côn trùng chích hút" (Sucking insect)).
* `"severity_level"`: The assessed danger level.
    * `"rất_cao"` (Very High): Can kill the tree or cause total crop loss.
    * `"cao"` (High): Causes severe damage and significant yield reduction.
    * `"trung_bình"` (Medium): Causes harm but is less likely to be fatal to the tree.
* `"risk_season"`: (Array) Seasonal conditions when outbreaks are most likely (e.g., "mùa mưa" (rainy season), "mùa khô" (dry season)).

### 3.2. Symptoms (`symptoms`)

An object describing symptoms on different plant parts.

* `"leaves"`, `"stem"`, `"roots"`, `"fruits"`, `"flowers"`: (Array) An array of strings describing symptoms.
* `"early_stage"`: (String) Description of the earliest detectable signs.
* `"late_stage"`: (String) Description of the consequences of a severe infestation.

### 3.3. Conditions & Prevention

* `"favorable_conditions"`: (Array) Environmental or cultural conditions that favor the problem.
* `"prevention_methods"`: (Object) Proactive prevention measures.
    * `"cultural"`: (Array) Farming practices (pruning, fertilizing, sanitation...).
    * `"biological"`: (Array) Biological controls (natural enemies, beneficial fungi...).
    * `"chemical_prevention"`: (Array) Chemical prophylaxis (painting with lime, preventative spraying...).

### 3.4. Treatment Chemicals (`treatment_chemicals`)

An array of recommended pesticides/fungicides.

* `"chemical_id"`: A unique ID for the chemical entry (e.g., "SR001-CHEM01").
* `"name"`: A common trade name (e.g., "Ridomil Gold 68WG").
* `"active_ingredient"`: The chemical's active ingredient (e.g., "Metalaxyl + Mancozeb").
* `"type"`: The mechanism of action.
    * `"tiếp xúc"` (Contact): Kills on contact.
    * `"lưu dẫn"` (Systemic/Internal): Absorbed and translocated by the plant.
    * `"vị độc"` (Stomach Poison): Must be ingested by the pest.
    * `"xông hơi"` (Fumigant): Kills via gas/vapor.
* `"application_method"`: (String) How to apply it (e.g., "Phun lá" (Foliar spray), "Tưới gốc" (Soil drench)...).
* `"source"`: (String) The source that recommended this specific chemical.

### 3.5. Other Fields

* `"diagnosis_tips"`: (Array) Key "tricks" for accurate identification (e.g., "Dig up roots to check", "Wipe the leaf...").
* `"verified_sources"`: (Array) A list of official sources used to compile the data.
* `"images"`: (Array) A list of illustrative image objects.
    * `"image_id"`, `"description"`, `"filename"`.
* `"expert_notes"`: (String) A critical summary or "most important thing to know".
* `"data_quality"`: (Object) The creator's self-assessment of the data.
    * `"completeness"`: How complete is the data for this entry (0.0 - 1.0).
    * `"accuracy"`: How accurate is the data (0.0 - 1.0).
    * `"consistency"`: How consistent is the data across sources (0.0 - 1.0).
    * `"last_verified"`: The date this information was last fact-checked.