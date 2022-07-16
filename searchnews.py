import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from tellerofuntruth import y_pred
from tellerofuntruth import score

def normalise(text):
    # Remove Unicode
    normalised_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Remove Mentions
    normalised_text = re.sub(r'@\w+', '', normalised_text)
    # Lowercase the document
    normalised_text = normalised_text.lower()
    # Remove punctuations
    normalised_text = re.sub(r'[^\w\s]','', normalised_text)
    # Lowercase the number
    normalised_text = re.sub(r'[0-9]', '', normalised_text)
    # Remove the doubled space
    normalised_text = re.sub(r'\s{2,}', ' ', normalised_text)
    return normalised_text

def search(q, df):
  print("What would you like to search for?: ", q)
  print()
  print("These are the most relevant results: ")
  # Convert the query become a vector
  q = [q]
  q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
  sim = {}
  # Calculate the similarity
  for i in range(10):
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
  
  # Sort the values 
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  return sim_sorted
  # Print the articles and their similarity values



col_list = ["title", "text", "label"]
df=pd.read_csv('/Users/eric/Desktop/cseHackathon/news.csv', usecols=col_list)

dataText = []
dataTextORIGINAL = []
dataTitle = []

# append article information into dataText list
i = 0
for articles in df['title']:
    dataText.append(normalise(df['text'][i]))
    dataTextORIGINAL.append(df['text'][i])
    dataTitle.append(df['title'][i])
    i+=1


# Instantiate a TfidfVectorizer object
vectorizer = TfidfVectorizer()
# It fits the dataText and transform it as a vector
X = vectorizer.fit_transform(dataText)
# Convert the X as transposed matrix
X = X.T.toarray()
# Create a dataTextFrame and set the vocabulary as the index
df = pd.DataFrame(X, index=vectorizer.get_feature_names_out())

while 1:
    prompt = input("search for: ")
    dataText_sorted = search(prompt, df)
    for i, j in dataText_sorted:
        if j != 0.0:
            print(dataTitle[i])
            print(f"this news is {y_pred[i]}, with a {round(score*100,2)}% accuracy")
            print(dataTextORIGINAL[i][:300] + '...')
            print()
            print()

# Todo:
# [X] "borrowed" fake news detection source code from https://dataText-flair.training/blogs/advanced-python-project-detecting-fake-news/
# [ ] search engine implementation 
# [ ] front end connected to backend 

# print(df['text'])