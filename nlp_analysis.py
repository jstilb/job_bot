from nltk import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.util import ngrams
import collections
import heapq
import gzip
import csv

# inputs
file = 'Business Intelligence Analyst.txt.gz'  # file to be analyzed (should be in project folder)
n = 20   # how many desired results you want in your bag of words model
g = 5    # desired number of grams for n-grams model
l = 200  # limit for n-grams results
save_file_as = "BI_Analyst_Results.txt"
save_location = '/Users/jmsitunes/Desktop/projects/job_bot/' # where you plan to save results
stop_words_input = ['a', 'u', 'at', 'year', 'le', 'etc', 'requirement', 'accredited', 'college', 'university',
                    'organization', 'employer', 'law', 'disability', 'accommodation', 'protected', 'race', 'color',
                    'work', 'opportunity', 'status', 'world', 'position', 'service', 'action', 'sexual', 'gender',
                    'veteran', 'sex', 'orientation', 'age', 'national', 'origin', 'seniority', 'employment', 'applicant',
                    'level', 'developmentsales', 'servicescomputer', 'associate', 'function', 'job', 'softwarefinancial',
                    'religion']
# 'a', 'u', 'at', 'year', 'le', 'etc', 'required', 'requirement', 'experience', 'skill', 'solution',
#                     'business', 'organization', 'employer', 'application', 'environment', 'system', 'law', 'preferred',
#                     'work', 'opportunity', 'status', 'world', 'role', 'position', 'service', 'action'



# open scraped job data
with gzip.open(file, 'rb') as f:
    data = f.read().decode('utf-8')

# sentence and work tokenization & normalization
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))  # remove general stop words
final_stop_words = stop_words.union(stop_words_input)  # remove input stop words

tokens = [word_tokenize(sen) for sen in sent_tokenize(data)]

def normalize(tkns):
    global normalized_tokens
    normalized_tokens = []
    for phrase in tkns:
        new_phrase = []
        for word in phrase:
            new_word = (lemmatizer.lemmatize(word.lower().strip()))  # lowers case, strips, and lemmatizes
            if new_word not in final_stop_words and word.isalnum():  # removes punctuation and stopwords
                new_phrase.append(new_word)
            else:
                continue
        normalized_tokens.append(new_phrase)


# part of speech tagging
tags = []


def tag(phrases):
    for phrase in phrases:
        tags.append(pos_tag(phrase))


# get word frequency (bag of words)
bow = {}


def get_bow_count(phrases):
    for phrase in phrases:
        for word in phrase:
            if word not in bow.keys():
                bow[word] = 1
        else:
            bow[word] += 1


def sort_key(x):
    return -x[1], x[0]


def bag_of_words(x):
    normalize(tokens)
    get_bow_count(normalized_tokens)
    top_n_results = heapq.nsmallest(x, bow.items(), key=sort_key)
    print(top_n_results)

def extract_ngrams(data, grms, limit):
    normalize(data)
    extracted_ngrams = []
    for phrase in normalized_tokens:
        n_grams = ngrams(phrase, grms)
        extracted_ngrams = extracted_ngrams + [' '.join(grams) for grams in n_grams]
    global results
    results = collections.Counter(extracted_ngrams).most_common()[:limit]
    print(results)

# def save_results(location, save_file, limit):
#     extract_ngrams(tokens, g, l)
#     with csv.open(location + save_file, 'wb') as f:
#         f.write(results[:limit])
#
# save_results(save_location, save_file_as, l)
# extract_ngrams(tokens, g, l)