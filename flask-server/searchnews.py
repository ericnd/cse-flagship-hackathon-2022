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

def tfidfSort(q, df, vec):
  # Convert the query become a vector
  q = normalise(q)
  q = [q]
  q_vec = vec.transform(q).toarray().reshape(df.shape[0],)
  sim = {}
  # Calculate the similarity
  for i in range(10):
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
  
  # Sort the values 
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  return sim_sorted
  # Print the articles and their similarity values

def getData():
    col_list = ["title", "text", "label"]
    df=pd.read_csv('/Users/eric/Desktop/cseHackathon/flask-server/data/news.csv', usecols=col_list)

    data = []
    i = 0
    for articles in df['title']:
        data.append(
            {
                'title': df['title'][i],
                'text': df['text'][i],
            })
        i+=1
    return data


def search(searchTerm):
    col_list = ["title", "text", "label"]
    df=pd.read_csv('/Users/eric/Desktop/cseHackathon/flask-server/data/news.csv', usecols=col_list)

    dataText = []
    # append article information into dataText list
    i = 0
    for articles in df['title']:
        dataText.append(normalise(df['text'][i]))
        i+=1

    # Instantiate a TfidfVectorizer object
    vectorizer = TfidfVectorizer()
    # It fits the dataText and transform it as a vector
    X = vectorizer.fit_transform(dataText)
    # Convert the X as transposed matrix
    X = X.T.toarray()
    # Create a dataTextFrame and set the vocabulary as the index
    df = pd.DataFrame(X, index=vectorizer.get_feature_names_out())

    resultList = []
    dataText_sorted = tfidfSort(searchTerm, df, vectorizer)
    for i, j in dataText_sorted:
        if j != 0.0:
            # print(f"this news is {y_pred[i]}, with a {round(score*100,2)}% accuracy")
            resultList.append(
                {
                    'articleId': i,
                    'validity': y_pred[i]
                }
            )


    return { 'accuracy': round(score*100,2),
             'articleIds': resultList 
           }

# Todo:
# [X] "borrowed" fake news detection source code from https://dataText-flair.training/blogs/advanced-python-project-detecting-fake-news/
# [X] search engine implementation source code from https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5
# [ ] front end connected to backend 

# print(df['text'])