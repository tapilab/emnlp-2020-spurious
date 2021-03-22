# define the data structure and read data from file


import requests, tarfile
from io import BytesIO
import pandas as pd
import pickle
import numpy as np
import random

class Dataset:
    def __init__(self, X, y, vec, df, moniker):
        """
        X: feature matrix;
        y: labels;
        vec: CountVectorizer
        df: dataframe
        feats: features from CountVectorizer
        moniker: reference name to the dataset
        """
        print('new dataset with %d records' % len(df))
        display(df.head(1))
        self.X = X
        self.y = y
        self.vec = vec
        self.df = df
        self.feats = np.array(vec.get_feature_names())
        self.moniker = moniker # name of the dataset
        

class SentenceEdit:
    def __init__(self, context, sentence_idx, remove_wd, label):
        """
        Remove a word from a sentence;
        E.g., 
            remove_wd: delicious 
            sentence: Love this book full of delicious foods
            context: Love this book full of  foods (at most 5 (window size) left and right words)
        """
        self.remove_wd = remove_wd
        self.context = context
        self.sentence_idx = sentence_idx
        
        self.label = label
        self.cluster_id = -1
      
    def __repr__(self):
        return '%s / %s / %s' % (self.remove_wd, str(self.label), self.context)
    
def get_IMDB():
    """
    Get IMDB movie reviews from the link;
    Sentences labeled as pos and neg
    
    """
    data_url = 'http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz'

    web_response = requests.get(data_url, stream=True)
    gz_file = web_response.content # Content in bytes from requests.get, see comments below why this is used.
    zipfile = tarfile.open(fileobj=BytesIO(gz_file))
    neg_file = zipfile.extractfile('rt-polaritydata/rt-polarity.neg')
    pos_file = zipfile.extractfile('rt-polaritydata/rt-polarity.pos')
    df = pd.DataFrame([{'label': -1, 'text': t.decode("cp437").strip() } for t in neg_file] +
                      [{'label': 1, 'text': t.decode("cp437").strip()} for t in pos_file])

    return df


def get_kindle():
    """
    Kindle book reviews with sentiment labels;
    Pre-processed by:
        Split comments into sentences;
        Filter by keywords;
        Limit sentence length [5,50];
    """
#     df = pickle.load(open("/data/zwang/2020_S/EMNLP/V_5_doubleCheck_sentiment/kindle_sentiment_5_50.pickle",'rb'))
#     df = pickle.load(open("/data/zwang/2020_S/EMNLP/V_6_shortSents/kindle_short_sents.pickle",'rb'))
    df = pickle.load(open("/data/zwang/2020_S/Attention/matches/kindle/kindle_unique_sents.pkl",'rb'))
#     df = df.sample(frac=1)
    df.reset_index(drop=True,inplace=True)
        
    return df

# def get_toxic_comment(limit_length=False):
#     """
#     Toxic comment from wikipedia talk page;
#     target (toxic score) > 0.7 as 1
#     target (toxic score) < 0.5 as -1
#     """
#     data_url = 'https://www.dropbox.com/s/hy80mvdsf3jgzw5/toxic.csv?dl=1'
#     web_response = requests.get(data_url, stream=True)
#     df = pd.read_csv(io.StringIO(web_response.text))[['id','target','text','label']]
    
#     if(limit_length):
#         df['text_len'] = df['text'].apply(lambda x: len(x.split()))
#         df_select = df[(df['text_len']<65)]
#         pos_idx = random.sample(list(df_select[df_select['label']==1]['id'].values),5000)
#         neg_idx = random.sample(list(df_select[df_select['label']==-1]['id'].values),5000)

#         df = df_select[df_select['id'].isin(list(pos_idx)+list(neg_idx))]
#         df.reset_index(drop=True,inplace=True)
        
#     return df

def get_toxic_comment():
#     df = pickle.load(open("/data/zwang/2020_S/Toxic/Concat_last4_emb/V_6_shortSents/toxic_short_sents.pickle",'rb'))
    df = pickle.load(open("/data/zwang/2020_S/EMNLP/V_6_shortSents/toxic_short_sents.pickle",'rb'))
    df = df.sample(frac=1)
    df.reset_index(drop=True,inplace=True)
    
    return toxic_df


def get_toxic_tw():
    """
    Toxic tweets from paper: Characterizing Variation in Toxic Language by Social Context
    """
    random.seed(42)
    df = pd.read_csv(open("/data/zwang/2020_S/Toxic/Data/TW/toxic_tweets.csv"))
    df['label'] = df['hostile'].apply(lambda x: 1 if x==1 else -1)
    
    return df[['id','text','label']]




    
    
