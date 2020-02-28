### Guillaume Couture Piché Word2Vec computation on reddit entrepreneur data ###

# 0. Load libraries and functions
import json
import string
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from pprint import pprint
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank 
ps = PorterStemmer() 
st = LancasterStemmer() 
stops = stopwords.words("english")    ## generate stop words
   
# 1. Data Import
# 1.1 Load Data 
entrepreneur_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\entrepreneur_top.json", 'r', encoding="utf8"))
etsy_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\etsy_top.json", 'r', encoding="utf8"))
eventproduction_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\eventproduction_top.json", 'r', encoding="utf8"))
freelance_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\freelance_top.json", 'r', encoding="utf8"))
itdept_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\itdept_top.json", 'r', encoding="utf8"))
smallbusiness_top  = json.load(open("C:\\Users\\EG63100\\OneDrive - Co-operators\\Documents\\Hackathon\\Slice 20200221\\smallbusiness_top.json", 'r', encoding="utf8"))

# 1.1 Gather data in one doc
docs = []
docs = docs + ([d['title'] + ' ' + d['text'] for d in entrepreneur_top])
docs = docs + ([d['title'] + ' ' + d['text'] for d in etsy_top])
docs = docs + ([d['title'] + ' ' + d['text'] for d in eventproduction_top])
docs = docs + ([d['title'] + ' ' + d['text'] for d in freelance_top])
docs = docs + ([d['title'] + ' ' + d['text'] for d in itdept_top])
docs = docs + ([d['title'] + ' ' + d['text'] for d in smallbusiness_top])




   
# 2. Clean the data

#  2.1 Tokenize all the documents
words = [word_tokenize(d) for d in docs]


#  2.2 Remove stop words and stem the words
words_clean = []

for sentence in words:
    sentence_clean = []
    for word in sentence:
        if len(word) > 1 and str.lower(word) not in stops and word not in string.punctuation:
            sentence_clean.append(ps.stem(str.lower(word)))
    words_clean.append(sentence_clean)

words_clean[5]

# 3. Word2Vec
# 3.1 Compute Word2Vec
w2v1 = Word2Vec(words_clean)

# 3.2 Results analysis
w2v1.wv['peopl'] #Vector for the word 'peopl'
  
w2v1.wv.most_similar('peopl') #Similar words to 'peopl'
w2v1.wv.most_similar('insur', topn = 10)


[w[0] for w in w2v1.wv.most_similar('insur', topn = 10)]  # 10 words that have the closest meaning to 'insur'
#['properti', 'accept', 'repair', 'agreement', 'damag', 'mortgag', 'packet', 'landlord', 'loan', 'deliveri'] 
# packet -> parcel 
# properti -> intellectual properti 


# 3.3 Results Extraction
insurwords = [ww[0] for ww in w2v1.wv.most_similar('insur', topn = 150)]
insurvec = [w2v1.wv[ww[0]] for ww in w2v1.wv.most_similar('insur', topn = 150)]
insurdist = [ww[1] for ww in w2v1.wv.most_similar('insur', topn = 150)]

# 4. TSNE
# 4.1 Compute TSNE 
tsne_model = TSNE(perplexity = 40, n_components = 2, init = 'pca', n_iter = 2500, random_state = 23)
new_values = tsne_model.fit_transform(insurvec)
	
# 5. Visualize results
x = []
y = []
for value in new_values:
    x.append(value[0])
    y.append(value[1])

cmap = sns.cubehelix_palette(as_cmap=True)

f, ax = plt.subplots()
ax.scatter(x, y, c = insurdist, s = 50, cmap = cmap)
for i in range(len(x)):
    ax.annotate(insurwords[i], xy = (x[i], y[i]), xytext = (5, 2), textcoords = 'offset points', ha = 'right', va = 'bottom')

f.colorbar(points)

plt.show()

# 5. Extract URL of some results
array_wow = []
ii = 0
for sentence in words_clean:
    if 'properti' in sentence:
        array_wow.append(ii)
    ii = ii + 1

array_wow


adjust_text(texts)
			
banjouille = [banjo['url'] for banjo in entrepreneur_top] + [banjo['url'] for banjo in etsy_top] + [banjo['url'] for banjo in eventproduction_top] + [banjo['url'] for banjo in freelance_top] + [banjo['url'] for banjo in itdept_top] + [banjo['url'] for banjo in smallbusiness_top]

banjouille[8]
