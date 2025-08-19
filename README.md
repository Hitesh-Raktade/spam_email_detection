# 📧 Spam Email Detection

A beginner-friendly **Spam Email Detection** project using **NLP, TF-IDF, and Logistic Regression**.  
This project classifies email or SMS messages as **spam** or **ham**. You can test it via a **web interface** built with **Flask**.

---

## 🔍 Features
- Clean and preprocess text (removes URLs, emails, numbers)  
- Transform text using **TF-IDF**  
- Train a **Logistic Regression** model for spam detection  
- Predict messages via **Flask web app**  
- Beginner-friendly structure for learning and further development  

---

## 📂 Folder Structure
spam_email_detection/
├─ data/ # Dataset (optional, don't upload large files)
├─ models/ # Saved model and vectorizer
├─ src/
│ ├─ app.py # Flask backend
│ ├─ train.py # Training script
│ ├─ predict.py # Prediction functions
│ └─ preprocess.py # Text cleaning
├─ templates/ # Frontend HTML files
│ └─ index.html


---

📈 How to Run
Make sure your trained model (spam_model.joblib) and vectorizer (vectorizer.joblib) are inside the models/ folder.
Start the Flask app:
python src/app.py
Open your browser:
http://127.0.0.1:5000/
Paste a message in the text box and click Analyze Email → see the prediction.

---

📊 Dataset
Used Kaggle SMS Spam Collection Dataset
Link: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Contains two columns: v1 (label) and v2 (text)
