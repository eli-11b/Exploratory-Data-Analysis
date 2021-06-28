import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Exploratory Data Analysis")
st.write('Eli Rivera, DCS, MBA')   
st.markdown('''
    ### Purpose:
      Exploratory data analysis is an approach to analyzing data sets with the goal of summarizing the characteristics. 
      During exploration, we try to find patterns, spot anomalies, and check assumptions. 
  ''')

#Choose delimiter
st.markdown("""#### Delimiter choice

Comma Separated Values (CSVs) or usually separated by a comma **(",")** but you can find them also separated by semi colons **(";")**, 
colons **(":")** or other punctuation or symbols. 


""")
delimiter_choice = [',',';',':']
choice = st.radio('Choose your delimiter',delimiter_choice)
if choice == ',':
  st.success('Okay you chose comma delimiter')
elif choice == ';':
  st.success('Okay you chose semi colon delimeter')
else:
  st.success('Okay you chose colon delimeter')

st.empty()
uploaded_file = st.file_uploader("Upload CSV")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, delimiter=choice)
  df = pd.DataFrame(df)

  #print the shape of the data
  st.markdown('''
  ### Data shape
    The data shape represents the (rows,columns) or (observations, characteristics) which represent the (first number, second number). 
    
    For machine learning the columns would be features **(x)** and one column, which we are trying to predict will be the label **(y)**. 

  ''')
  st.write(df.shape)

  #print column names
  st.markdown("### Column Names")
  st.write(df.columns)

  #print null values
  st.markdown('''
  ### Null Values in each column
  Null values can influence decision making. What will you do with them?

    1. Remove them? 
    2. Impute them?
    
  ''')
  st.write(df.isnull().sum())

  #duplicates
  st.markdown('''
  ### Duplicates
  Duplicates can impact decision making, what will you do with them?
  ''')
  st.write(df[df.duplicated()])

  st.empty()
  st.markdown("### Data head")
  st.markdown('''
    The head or first 5 rows of the data is often peeked at to get start to understand the type of data that is in the dataset. 
  ''')
  #print out head (top5)
  st.table(df.head(5))


  st.empty()
  st.markdown("### Data tail")
  st.markdown('''
    The tail or last 5 rows of the data is often peeked at to get start to understand the type of data that is in the dataset. 
  ''')
  #print out head (top5)
  st.table(df.tail(5))

st.markdown('''### Summary
During the exploratory data analysis phase you are looking at the data set with the goal of summarizing the characteristics. 
Performing exploratory data analysis can also help highlight the data cleansing steps that need to occur such as dropping duplicates, working with null values and more. Exploratory data analysis will give the data scientist the ability to plan out what to do with the data after initial exploration.

**Packages used:**
The language used for this project was python. The packages used were pandas, streamlit, and matplotlib. 

''')


st.markdown("### BIO")
st.markdown("#### Eli Rivera, DCS, MBA")
  #Exploratory Data Analysis
LOGO_IMAGE = '/Users/eli/documents/linkedin_image.jpg'
st.image(LOGO_IMAGE)
st.markdown('''
  Dr. Rivera's research interests include machine learning, data science, security, automation, and databases. He has Bachelor degrees in
  Criminal Justice, Homeland Security & Emergency Management, and Accounting. He has an MBA from Western Governors University and a Doctorate 
  in Computer Science, concentration in CyberSecurity and Information Assurance from Colorado Technical University. He also holds Microsoft Certified: Azure Data Scientist Associate, Microsoft Certified: Azure AI Engineer, Comptia: Project + and Tensorflow Developer certificates.
  His recent publication 'Countering Persistent Artificial Intelligence Attacks, A Qualitative Study' was published in ProQuest in 2021.
  
''')

