from model import *
from utils import *
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore', category=Warning)

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--fpath', default='~/Downloads/steam-reviews-dataset/steam_reviews.csv')
    parser.add_argument('--ntopic', default=10)
    args = parser.parse_args()

    data = pd.read_csv(args.fpath)
    data = data.fillna('')  # only the comments has NaN's
    rws = data.review
    sentences, token_lists, idx_in = preprocess(rws, samp_size=100)
    # Define the topic model object
    tm = Topic_Model(k = args.ntopic, method = 'LDA_BERT')
    # Fit the topic model by chosen method
    tm.fit(sentences, token_lists)
    # Evaluate using metrics
    print('Coherence:', get_coherence(tm, token_lists, 'c_v'))
    print('Silhouette Score:', get_silhouette(tm))
    # visualize and save img
    visualize(tm)
    for i in range(tm.k):
        get_wordcloud(tm, token_lists, i)