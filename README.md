# 🚢 Titanic Survival Prediction: Expert Guide

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)

A complete, end-to-end Machine Learning pipeline that predicts passenger survival on the Titanic. This repository goes beyond basic code by including **expert-level notes** on the methodology, intuition, and detailed line-by-line explanations of the code.

## 🚀 Overview
The Titanic dataset is the legendary "Hello World" of Machine Learning. However, this repository tackles it from the perspective of an expert ML Engineer.

Inside the `Titanic_Guide.ipynb` notebook, you will find:
1. **Exploratory Data Analysis (EDA)** using Seaborn to find hidden correlations.
2. **Data Cleaning & Imputation** (Handling missing Ages and Embarkation ports).
3. **Feature Engineering** (Combining Siblings and Parents into a `FamilySize` feature, and extracting an `IsAlone` flag).
4. **Categorical Encoding** (One-Hot Encoding with `drop_first=True` to avoid the dummy variable trap).
5. **Model Training & Evaluation** (Comparing Logistic Regression against a Random Forest Classifier using precision/recall and confusion matrices).

---

## 🧠 Expert Notes & Intuition

### Why Random Forest instead of Deep Learning?
Neural Networks are incredibly powerful for images and text, but they are terrible for small, tabular datasets. The Titanic dataset only has ~891 rows. A Neural Network would heavily overfit (memorize the data instead of learning patterns). Random Forests naturally capture complex, non-linear interactions (e.g., "being a female *in 3rd class*") perfectly without requiring massive amounts of data or strict feature scaling.

### The Expert Workflow
An expert doesn't just guess an algorithm; they follow a strict methodology:
1. **Domain Intuition**: We first ask logical questions. *Did women and children get on lifeboats first?* Yes. *Did rich people survive more?* Yes. This tells us `Sex`, `Age`, and `Pclass` are our most critical signals.
2. **Feature Engineering (The Secret Sauce)**: Algorithms struggle to connect abstract dots. Instead of leaving `SibSp` (siblings) and `Parch` (parents) separate, combining them into `FamilySize` helps the model immediately understand the concept of "large families struggled to find lifeboats together."
3. **Data Leakage**: We are careful to split our data (`train_test_split`) *before* running standard scalers to ensure we don't accidentally leak information from the test set into the training set.
4. **Explainability**: We use `feature_importances_` to dissect exactly *why* the model made its decisions, proving to stakeholders that the model isn't just a black box.

## 🛠️ Local Setup
To run the notebook locally:
```bash
git clone https://github.com/Sxmxxrth/ml-titanic-survival.git
cd ml-titanic-survival
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
jupyter notebook
```



## 📁 Production Directory Structure

```text
📁 ml-titanic-survival/
├── 📄 README.md
├── 📄 Titanic_Guide.ipynb
├── 📁 config/
│   └── 📄 settings.yaml
├── 📄 requirements.txt
├── 📁 src/
│   ├── 📄 __init__.py
│   └── 📄 config.py
└── 📁 tests/
    ├── 📄 __init__.py
    └── 📄 test_smoke.py
```

## 🧪 Running Automated Tests

To run the automated production test suite, execute:

```bash
pytest tests/  # or python -m unittest discover -s tests
```
## 📝 License
MIT License
