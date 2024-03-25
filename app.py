import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
model = pickle.load(open(r"C:\Users\djamb\OneDrive - Université Centrale\ML PROJECTS\email-classification\model\model.pkl",'rb'))
tfidf = pickle.load(open(r"C:\Users\djamb\OneDrive - Université Centrale\ML PROJECTS\email-classification\model\vectorizer.pkl",'rb'))
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button('Predict'):
    if not input_sms.strip():  
        st.error("Please enter a message") 
    else:
        # Prétraitement
        transformed_sms = transform_text(input_sms)
        # Vectorisation
        vector_input = tfidf.transform([transformed_sms])
        # Prédiction
        result = model.predict(vector_input)[0]
        # Affichage du résultat
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")