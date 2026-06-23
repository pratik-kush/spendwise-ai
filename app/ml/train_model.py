
import sys
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib

# ✅ Fix Python path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, BASE_DIR)

# ✅ Correct data path
data_path = os.path.join(BASE_DIR, "data", "transactions.csv")

df = pd.read_csv(data_path)

# ✅ Import your rule-based classifier
from app.services.category_predictor import classify_transaction

df['category'] = df['description'].apply(classify_transaction)

# ✅ Prepare data
X = df['description']
y = df['category']

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)

# ✅ Train model
model = LogisticRegression()

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y, test_size=0.2, random_state=42
)

# ✅ Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# ✅ Predict
y_pred = model.predict(X_test)

# ✅ Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")


# ✅ Save model
model_path = os.path.join(BASE_DIR, "app", "ml", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "app", "ml", "vectorizer.pkl")

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)


# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y, test_size=0.2, random_state=42
)

# ✅ Train again
model.fit(X_train, y_train)

# ✅ Predict
y_pred = model.predict(X_test)

# ✅ Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("✅ Accuracy calculated:", accuracy)

# ✅ Save accuracy to file
accuracy_path = os.path.join(BASE_DIR, "app", "ml", "accuracy.txt")

print("Saving accuracy at:", accuracy_path)

with open(accuracy_path, "w") as f:
    f.write(str(accuracy))

print("✅ accuracy.txt saved successfully")


# ✅ Save accuracy to file
accuracy_path = os.path.join(BASE_DIR, "app", "ml", "accuracy.txt")

with open(accuracy_path, "w") as f:
    f.write(str(accuracy))


print("✅ Model trained and saved successfully")


