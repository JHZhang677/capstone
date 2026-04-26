# Capstone Project Repository

## 1. Project Overview

This repository is used to manage all materials related to our capstone project, including datasets, code, documents, literature review, and meeting records.

The goal of this repository is to ensure a clear structure, standardized workflow, and efficient collaboration among team members.

---

## 2. Repository Structure

```text
capstone-project/
├── README.md
├── .gitignore
│
├── meeting_minutes/
│   ├── host/
│   └── supervisor/
│
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── README.md
│
├── docs/
│   ├── requirement_analysis/
│   ├── problem_statement/
│   └── project_plan/
│
├── literature_review/
│   ├── papers/
│   └── notes/
│
├── example_code/
├── final_code/
└── webpage/
```

---

## 3. Code Description Rules

All code files must include a header description at the beginning.

Each code file should clearly state:

* Purpose of the code
* Input data
* Output results
* How to run the code
* Required dependencies

### Example

```python
"""
File: wavelet_analysis.py
Purpose: Apply wavelet transform to time-series data
Input: data/processed_data/sample_data.csv
Output: figures/wavelet_result.png
Author: Jianhao Zhang
Last Updated: 2026-04-XX
"""
```

### Code Organization

* `example_code/`: experimental, testing, or learning code
* `final_code/`: final, stable, and project-ready code

---

## 4. File Naming Convention

To maintain consistency:

* Use lowercase letters
* Use underscores `_` instead of spaces
* Use clear and descriptive names

### Examples

```text
wavelet_analysis.py
meeting_minutes_2026_04_23.pdf
requirement_analysis_v1.md
```

Avoid:

```text
test.py
final_version2.py
new_file.py
```

---

## 5. Branch Creation Rules

All development must be done on branches.

Do NOT work directly on the `main` branch.

### Branch Naming Format

```text
feature/name-task
fix/name-issue
docs/name-description
```

### Examples

```text
feature/jianhao-wavelet-analysis
docs/jianhao-readme-update
fix/jianhao-data-error
```

---

## 6. Push & Merge Rules

Before pushing changes:

1. Pull the latest version from `main`
2. Work on your own branch
3. Ensure files are in the correct folders
4. Follow naming conventions
5. Do NOT upload temporary or system files
6. Write clear commit messages

### Standard Workflow

```bash
git checkout main
git pull origin main

git checkout -b feature/jianhao-task

git add .
git commit -m "Add wavelet analysis code"
git push origin feature/jianhao-task
```

### Commit Message Examples

```text
Add wavelet analysis code
Update README structure
Move meeting files into folders
Fix data processing issue
```

After pushing:

* Create a Pull Request (PR)
* Wait for review before merging into `main`

---

## 7. Dataset Rules

All datasets must be stored under:

```text
data/raw_data/        # original data
data/processed_data/  # cleaned data
```

### Rules

* Raw data must NOT be modified
* Processed data must be saved separately
* Large datasets should NOT be uploaded directly
* Include dataset descriptions in `data/README.md`
* Clearly document data source and processing steps
* Do NOT upload sensitive or private data

---

## 8. Data Documentation (data/README.md)

Each dataset should include:

* Data source
* File format
* Description of variables
* Processing steps

All transformations must be reproducible.

---

## 9. README Maintenance Rules

The README file must be kept up to date.

### Requirements

* Update README after any structural change
* Ensure consistency with actual repository structure
* Remove outdated information
* Keep formatting clean and readable

### Maintenance Rule

README should be reviewed:

* Before major submissions
* After structural updates

---

## 10. Collaboration Guidelines

To ensure smooth teamwork:

* Follow repository structure strictly
* Communicate before major changes
* Keep commits small and meaningful
* Avoid duplicate or unnecessary files
* Maintain clear documentation

---

## 11. Notes

* Do NOT upload unnecessary files (e.g., `.DS_Store`, cache files)
* Use `.gitignore` properly
* Keep the repository clean and organized

---

## 12. Maintainer

This repository structure and guideline are maintained by:

**Jianhao Zhang**

---

## 13. Summary

This guideline ensures:

* Clear file organization
* Standardized coding practice
* Efficient collaboration
* Reproducible research workflow

All team members should follow these rules throughout the project.

