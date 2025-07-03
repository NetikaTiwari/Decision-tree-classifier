
# Decision Tree Classifier – Bank Marketing Prediction

This project builds a **Decision Tree Classifier** to predict whether a customer will subscribe to a term deposit based on their demographic and behavioral data.

---

## 📌 Objective

To analyze the **Bank Marketing dataset** from the UCI Machine Learning Repository and build a predictive model using the Decision Tree algorithm.

---

## 📊 Dataset

- **Source**: [UCI Machine Learning Repository – Bank Marketing](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **File Used**: `bank-full.csv`
- **Attributes**:
  - Age, Job, Marital, Education, Default, Housing Loan, Personal Loan, etc.
  - Target variable: `y` (Yes = subscribed, No = not subscribed)

---

## 🛠️ Tools & Technologies

- Python
- Jupyter Notebook
- Pandas, NumPy
- scikit-learn
- Matplotlib / Seaborn
- Streamlit (for deployment)
- Joblib (for model persistence)

---

## 🧠 Model Used

- **Decision Tree Classifier** from `sklearn.tree`
- **Evaluation Metrics**:
  - Accuracy
  - Confusion Matrix
  - Classification Report

---

## 🚀 Streamlit Web App

A Streamlit web app was created to allow interactive predictions.

### Features:
- Takes user input (age, job, marital status, etc.)
- Predicts whether the customer will subscribe
- Simple UI deployed via `streamlit_app.py`

### To Run:
```bash
streamlit run streamlit_app.py
```

---

## 🧪 How to Use

1. Clone the repository or download files
2. Run `Decision Tree Classifier.ipynb` to train and save the model
3. Run `streamlit_app.py` to launch the app

---

## 📁 File Structure

```
│
├── Decision Tree Classifier.ipynb   # Model training and saving
├── decision_tree_model.pkl          # Saved ML model
├── streamlit_app.py                 # Streamlit web app
└── README.md                        # Project description
```

---

## 📸 Screenshots

*(Add screenshots of your Streamlit UI and tree visualization here)*

---

## 👩‍💻 Author

**Netika Tiwari**  
Intern at Prodigy Infotech  
[LinkedIn Profile](https://www.linkedin.com/in/netika-tiwari-21f2005/)

---

## 📌 Note

This project was completed as part of my internship at **Prodigy Infotech** to demonstrate model building and deployment using real-world marketing data.
