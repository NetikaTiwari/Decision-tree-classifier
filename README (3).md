
# Bank Marketing Predictor – Decision Tree Classifier

This project builds a **Decision Tree Classifier** to predict whether a customer will subscribe to a term deposit based on their demographic and behavioral attributes. It uses the **Bank Marketing dataset** from the UCI Machine Learning Repository.

---

## 📁 Project Structure

```
📁 project_folder/
├── decision tree classifier.ipynb   # Jupyter notebook for training
├── streamlit_app.py                 # Streamlit web app
└── README.md                        # Project documentation
```

> Note: The `decision_tree_model.pkl` file is auto-generated when you run the notebook.

---

## 🎯 Objective

To analyze customer data and predict their likelihood of subscribing to a term deposit using a decision tree model.

---

## 🧰 Technologies Used

- Python
- Jupyter Notebook
- scikit-learn
- pandas, numpy
- Streamlit (for the interactive app)

---

## 🚀 How to Run the App

1. Open terminal in the folder where your files are located.
2. Run the notebook first to generate the model:
   ```python
   joblib.dump(model, 'decision_tree_model.pkl')
   ```
3. Then start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
4. The app will open in your browser at:
   ```
   http://localhost:8501
   ```

---

## 📦 GitHub Upload Tips

- ✅ Include: `streamlit_app.py`, `decision tree classifier.ipynb`, `README.md`
- ❌ Exclude: `.ipynb_checkpoints/` and any unnecessary cache files
- Optional: Skip uploading `decision_tree_model.pkl` if your notebook saves it

---

## 🙋‍♀️ Author

**Netika Tiwari**  
Intern at Prodigy Infotech  
[LinkedIn](https://www.linkedin.com/in/netika-tiwari-21f2005/)

---

## 📌 Credits

- Dataset: [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
