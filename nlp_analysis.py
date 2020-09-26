from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.lm import MLE
import heapq
import csv
import pandas as pd
import gzip

file = 'Business Intelligence Analyst.txt.gz'  # file to be analyzed

# open scraped job data
with gzip.open(file, 'rb') as f:
    file_content = f.read()


# Bag of Words Inputs
n_bow = 20 # how many desired results you want in your bag of words model
bow_stp_wrds = ['business', 'experience', 'information', 'system', 'level', 'work', 'team', 'process', 'function',
                   'skill', 'ability', 'requirement', 'type', 'year', 'technology', 'full', 'timejob', 'support',
                   'technical', '’', 'knowledge', 'problem', ';', 'working', 'degree', 'related', ':', 'including',
                   'new', 'associateemployment', 'quality', 'understanding', 'issue', 'need', 'software', 'develop',
                   'strong', 'application', 'internal', 'required', 'written', 'ensure', 'identify', 'maintain',
                   'provide', 'technologyindustries', 'multiple', 'environment', 'levelemployment', 'change',
                   'developmentsalesindustries', 'across', 'service', 'high', 'within', 'using', 'seniority', 'plan',
                   'financial', 'time', 'assist', 'document', 'computer', 'industry', 'understand', 'training',
                   'recommendation', 'task', 'able', 'servicescomputer', 'skill', 'requirement', 'year', 'system',
                   'solution', 'user', 'process', 'issue', 'need', 'tool', 'problem',  'use', 'may', 'detail',
                   'operation', 'etc', 'preferred', 'must', 'create', 'case', 'meet', 'company', 'end', "'s",
                   'relationship', 'functional', 'practice', 'key', 'well', 'opportunity', 'external', 'partner',
                   'insight', 'effectively', 'technique', 'procedure', 'performance', 'office', 'role', 'self',
                   'health', 'expert', 'based', 'relevant', 'build', 'field', 'skill', 'requirement', 'professional',
                   'result', 'various', '5', 'meeting', 'year', 'system', 'solution', 'process', 'issue', 'need',
                   'tool', 'problem',  'review', 'recommendation', 'user', 'improvement', 'operation', 'technique',
                   'practice', 'organization', 'standard', 'member', '2', 'help', 'oriented', 'equivalent', 'source',
                   'application', 'manager', 'make', 'insight', 'relationship', 'result', 'include', 'request',
                   'opportunity', 'best',  'basic', 'duty', 'delivery', 'case', 'needed', 'conduct', 'excellent',
                   'initiative']

# N Grams Inputs
n_grams = 3

def bow_model(data, stp_wrds, n):  # need to re-examine how the dataframe is being tokenized. (basically rebuild)
    # steps: https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e
    # tokenize sentences using nltk.sent_tokenizer
    # tokenize words
    bow_string = [j for i in data for j in i]
    bow_string = "".join(bow_string)
    bow_string = bow_string.lower()
    puncts = '.?!,&-()â€™/+'
    for sym in puncts:
        bow_string = bow_string.replace(sym,' ')

    # remove stop words
    stop_words = set(stopwords.words('english'))      # remove general stop words
    stop_word_w_input = stop_words.union(stp_wrds)                        # remove input stop words
    job_titles = []                                   # remove job titles as stop words

    for col in data.columns:
        tokenized_titles = word_tokenize(col)
        for tkn in tokenized_titles:
            job_titles.append(tkn)

    final_stop_words = stop_words.union(job_titles)

    # tokenize data
    word_tokens = word_tokenize(bow_string)

    # lemmatize data
    lemmatizer = WordNetLemmatizer()
    clean_word_tokens = []

    for token in word_tokens:
        if token not in final_stop_words:
            clean_word_tokens.append(lemmatizer.lemmatize(token))

    # get word frequency (bag of words)
    word2count = {}
    for word in clean_word_tokens:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

    def sort_key(x):
        return -x[1], x[0]

    top_n_results = heapq.nsmallest(n, word2count.items(), key=sort_key)
    print(top_n_results)

# bow_model(df, bow_stp_wrds, n_bow)

# n-grams model





