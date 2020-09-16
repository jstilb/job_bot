from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import heapq
import csv

file = 'Data Analyst.csv' # file to be analyzed
n = 20 # how many desired results you want in your bag of words model

# open scraped job data
with open(file, newline='') as csvfile:
    data = csv.reader(csvfile)
    data_lists = list(data)

# remove job titles for bag of words model
for list in data_lists:
    if len(list) > 0:
        del list[0]
    else:
        del list


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
tokens = word_tokenize(bow_string)
lemmatizer = WordNetLemmatizer()
clean_tokens = []


for token in tokens:
    if token not in stop_words:
        clean_tokens.append(lemmatizer.lemmatize(token))


# get word frequency (bag of words)
word2count = {}
for word in clean_tokens:
    if word not in word2count.keys():
        word2count[word] = 1
    else:
        word2count[word] += 1

def sort_key(x):
    return -x[1], x[0]

top_n_results = heapq.nsmallest(n, word2count.items(), key=sort_key)

print(top_n_results)