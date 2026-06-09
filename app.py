import streamlit as st
import pickle

# Load model
model = pickle.load(open("emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
emotion_map = pickle.load(open("emotion_mapping.pkl", "rb"))

# UI setup
st.set_page_config(page_title="Emotion Detection AI", page_icon="😊")

st.title("😊 Emotion Detection AI")
st.write("Enter your text and detect emotion instantly using ML")

text = st.text_area("Enter your text here:")

if st.button("Predict Emotion 🚀"):
    if text.strip():
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]

        st.success(f"Predicted Emotion: **{emotion_map[pred]}**")
    else:
        st.warning("Please enter some text!")