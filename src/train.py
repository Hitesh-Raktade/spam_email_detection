import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_text
# Load dataset
df = pd.read_csv("data/spam.csv", encoding='latin-1')
# Use only needed columns
df = df[["v1", "v2"]]
df.columns = ["label", "text"]
# Preprocess
df["text"] = df["text"].apply(clean_text)
# Split
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)
# Vectorizer + Model
vectorizer = TfidfVectorizer(stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)
# Evaluate
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))
# Save
joblib.dump(model, "models/spam_model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")