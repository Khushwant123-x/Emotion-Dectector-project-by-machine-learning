# 😊 Emotion Detector using Machine Learning

A Machine Learning-based Emotion Detection application that predicts human emotions from text input. This project uses Natural Language Processing (NLP) techniques along with a trained classification model to identify emotions such as happiness, sadness, anger, fear, surprise, and more.

---

## 🚀 Features

* Detect emotions from user-entered text
* NLP preprocessing pipeline
* Machine Learning-based classification
* Fast and lightweight prediction
* User-friendly interface
* Easy deployment using Streamlit

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* NLTK
* Streamlit
* Pickle

---

## 📂 Project Structure

```bash
Emotion-Detector/
│
├── app.py                 # Streamlit application
├── emotion_model.pkl      # Trained ML model
├── vectorizer.pkl         # TF-IDF Vectorizer
├── requirements.txt       # Project dependencies
├── dataset.csv            # Dataset (optional)
├── notebooks/           # Training notebooks
|-- emotion_mapping.pkl # Mapping emotion
└── README.md

```

---

## 📊 Dataset

The model is trained on an emotion-labeled text dataset containing multiple emotion categories such as:

* Joy 😊
* Sadness 😢
* Anger 😠
* Fear 😨
* Love ❤️
* Surprise 😲

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Emotion-Detector.git

cd Emotion-Detector
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, open:

```bash
http://localhost:8501
```

---

## 🧠 Machine Learning Pipeline

1. Text Cleaning
2. Tokenization
3. TF-IDF Vectorization
4. Model Training
5. Emotion Prediction

---

## 📈 Model Performance

We evaluated multiple machine learning models for emotion classification:

| Model                   | Accuracy |
| ----------------------- | -------- |
| Logistic Regression     | **88%+** |
| Multinomial Naive Bayes | **76%+** |

---

## 💡 Example

### Input

```text
I am feeling very excited about my new job!
```

### Output

```text
Emotion: Joy 😊
```

---

## 🔮 Future Improvements

* Deep Learning (LSTM/BERT)
* Multi-language support
* Speech Emotion Recognition
* Real-time Emotion Analysis
* API Integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

### 🔍 Key Insight

* Logistic Regression performed significantly better due to better handling of TF-IDF feature space.
* Multinomial Naive Bayes is faster but less accurate for complex emotion patterns.


## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Khushwant Singh Rajat**

AI/ML Enthusiast | Generative AI Developer | Machine Learning Engineer

If you found this project useful, don't forget to ⭐ the repository!
