import re
import numpy as np
import pandas as pd
from nltk.corpus import stopwords


def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt 

def addt_var_for_model(df, num_features):
    """select nesessary features""" 
    # From new data
    contract_feat = df[num_features]
    # Return
    return contract_feat

def combine_feature_dfs(df_words, df_feats):
    """Make into an array from sparse array"""
    test_array = df_words.toarray()
    test_stack = np.hstack((test_array, df_feats))
    return test_stack

nltk.download('stopwords')
stopwords = set(stopwords.words('english'))

def remove_stopwords(text):
    new_text = []
    for word in text.split():
        if word not in stopwords:
            new_text.append(word)
    return ' '.join(new_text)