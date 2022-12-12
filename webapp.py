# importing libraries
import streamlit as st
from PIL import Image
from functions import *

st.set_page_config(
    page_title="UAS ML",
    page_icon="⭐",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/theofilusarifin/',
        'Report a bug': "https://www.linkedin.com/in/theofilusarifin/",
        'About': "# Cyberbullying Tweet Classification"
    }
)

# Page title
st.write('''
# UAS MACHINE LEARNING
## Cyberbullying Tweet Classification
***
''')

# Hero Image
image = Image.open('Web_Resource/img/hero.png')
st.image(image, use_column_width= True)

# Team section
st.info('''
**Team**
* 160420046 - Theofilus Arifin [[More Info]](https://www.linkedin.com/in/theofilusarifin/)
* 160420108 - Hans Wirjawan [[More Info]](https://www.linkedin.com/in/hans-wirjawan-977b15244/)
''')

# Description Section
st.write('''
    This website classify input tweet into 6 Categories using 3 Machine Learning Methods.
    ''')
col1, col2 = st.columns([2, 4])

# Categories
with col1:
    st.write('''
    Categories:
    * Age
    * Ethnicity
    * Gender
    * Religion
    * Other Cyberbullying
    * Not Cyberbullying

    ***
    ''')
# Machine Learning Method
with col2:
    st.write('''
    Machine Learning Methods:
    * Naive Bayes (NB) - Accuracy  73.89%
    * Random Forest (RF) - Accuracy 81.98%
    * Support Vector Machine (SVM) - Accuracy 82.90%

    ***
    ''')

# Text Box
st.header('Input Tweet ')
tweet_input = st.text_area("Write your tweet inside the textbox below", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
st.header("Inputted Tweet text ")
if tweet_input:
    tweet_input
else:
    st.write('''
    ***No Tweet Text Inputted!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
col1, col2, col3 = st.columns(3)

# Naive Bayes
with col1:
    st.write('''
    #### Naive Bayes
    ''')
    if tweet_input:
        prediction = nb_input_prediction(tweet_input)
        if prediction == "Age":
            st.image("Web_Resource/img/age.png",use_column_width= True)
        elif prediction == "Ethnicity":
            st.image("Web_Resource/img/ethnicity.png",use_column_width= True)
        elif prediction == "Gender":
            st.image("Web_Resource/img/gender.png",use_column_width= True)
        elif prediction == "Not Cyberbullying":
            st.image("Web_Resource/img/not.png",use_column_width= True)
        elif prediction == "Other Cyberbullying":
            st.image("Web_Resource/img/other.png",use_column_width= True)
        elif prediction == "Religion":
            st.image("Web_Resource/img/religion.png",use_column_width= True)
    else:
        st.write('''
        ***No Tweet Text Inputted!***
        ''')

# Random Forest
with col2:
    st.write('''
        #### Random Forest
    ''')
    if tweet_input:
        prediction = rf_input_prediction(tweet_input)
        if prediction == "Age":
            st.image("Web_Resource/img/age.png",use_column_width= True)
        elif prediction == "Ethnicity":
            st.image("Web_Resource/img/ethnicity.png",use_column_width= True)
        elif prediction == "Gender":
            st.image("Web_Resource/img/gender.png",use_column_width= True)
        elif prediction == "Not Cyberbullying":
            st.image("Web_Resource/img/not.png",use_column_width= True)
        elif prediction == "Other Cyberbullying":
            st.image("Web_Resource/img/other.png",use_column_width= True)
        elif prediction == "Religion":
            st.image("Web_Resource/img/religion.png",use_column_width= True)
    else:
        st.write('''
        ***No Tweet Text Inputted!***
        ''')

# SVM
with col3:
    st.write('''
        #### SVM
    ''')
    if tweet_input:
        prediction = svm_input_prediction(tweet_input)
        if prediction == "Age":
            st.image("Web_Resource/img/age.png",use_column_width= True)
        elif prediction == "Ethnicity":
            st.image("Web_Resource/img/ethnicity.png",use_column_width= True)
        elif prediction == "Gender":
            st.image("Web_Resource/img/gender.png",use_column_width= True)
        elif prediction == "Not Cyberbullying":
            st.image("Web_Resource/img/not.png",use_column_width= True)
        elif prediction == "Other Cyberbullying":
            st.image("Web_Resource/img/other.png",use_column_width= True)
        elif prediction == "Religion":
            st.image("Web_Resource/img/religion.png",use_column_width= True)
    else:
        st.write('''
        ***No Tweet Text Inputted!***
        ''')

st.write('''***''')

# About section
st.info('''
**About This Project**
* Source Code: [Github](https://github.com/Theofilusarifin/Project_ML.git)
* Dataset: [Kaggle](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')