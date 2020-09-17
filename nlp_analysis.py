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

file = 'Data Analyst.csv' # file to be analyzed
n_bow = 20 # how many desired results you want in your bag of words model
n_grams = 3

# open scraped job data
with open(file, newline='') as csvfile:
    data = csv.reader(csvfile)
    data_lists = list(data)

# remove job titles for bag of words model
for ls in data_lists:
    if len(ls) > 0:
        del ls[0]
    else:
        del ls


# normalize data
bow_string = [j for i in data_lists for j in i]
bow_string = "".join(bow_string)
bow_string = bow_string.lower()
puncts = '.?!,&-()â€™/+'

for sym in puncts:
    bow_string = bow_string.replace(sym,' ')

#tokenizing & lemmatizing data
stop_words = set(stopwords.words('english'))
stop_words.update(['business', 'experience', 'information', 'system', 'level', 'work', 'team', 'process', 'function',
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
                   'initiative'])
word_tokens = word_tokenize(bow_string)
tokenized_text = [list(map(str.lower, word_tokenize(sent)))
                  for sent in sent_tokenize(bow_string)]
lemmatizer = WordNetLemmatizer()
clean_word_tokens = []





#for token in word_tokens:
    #if token not in stop_words:
        #clean_word_tokens.append(lemmatizer.lemmatize(token))


# get word frequency (bag of words)
word2count = {}
# for word in clean_tokens:
    # if word not in word2count.keys():
        # word2count[word] = 1
    # else:
        # word2count[word] += 1

def sort_key(x):
    return -x[1], x[0]

# top_n_results = heapq.nsmallest(n, word2count.items(), key=sort_key)

# print(top_n_results)


# n-grams model
padded_sent = list(pad_sequence(tokenized_text[0], pad_left=True, left_pad_symbol="<s>",
                                pad_right=True, right_pad_symbol="</s>", n=n_grams))
# left off https://www.kaggle.com/alvations/n-gram-language-model-with-nltk
print(three_grams)



# train_data, padded_sents = padded_everygram_pipeline(n_grams, tokenized_text)
# model = MLE(n)
# model.fit(train_data, padded_sents)
# print(model.vocab.lookup(tokenized_text[0]))
