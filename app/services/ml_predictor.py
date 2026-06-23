
import joblib
import os

# ✅ Load model & vectorizer
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, 'ml', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'ml', 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_category(description):
    text = [description]
    text_vector = vectorizer.transform(text)
    prediction = model.predict(text_vector)
    return prediction[0]
