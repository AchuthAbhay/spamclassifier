import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps =PorterStemmer()


def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
         y.append(ps.stem(i))
    return " ".join(y)


tfidf= pickle.load(open('vectorizer.pkl','rb'))
model= pickle.load(open('model.pkl','rb'))

st.title("email/sms soam classifier")

input_sms=st.text_input("enter the message")
if st.button('predict'):

 transformed_sms=transform_text(input_sms)

 vector_input =tfidf.transform([transformed_sms])

 result=model.predict(vector_input)[0]

 if result ==1:
     st.header("spam")
 else:
     st.header("not Spam")    