import joblib
from preprocess import clean_text
model = joblib.load("models/spam_model.joblib")
vectorizer = joblib.load("models/vectorizer.joblib")
def predict_message(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    label = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0][1]
    return {"label": label, "spam_probability_percentage": round(float(proba)*100, 2)}