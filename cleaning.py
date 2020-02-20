import gensim
from gensim.utils import deaccent
import re

def normalize(nlp, doc, remove_stops=True, min_word_length=3, max_word_length=15, ngrams=False):
    """ Note: removing stop words isn't always a good idea. This might be appropriate for
    some types of document classification but for sentiment analysis removing stop words
    can change the meaning of a sentence and affect sentiment.
    """
    words = []
    for token in nlp(doc.lower()):
        if (remove_stops and token.is_stop) or token.is_punct or not token.is_alpha:
            continue
        word = token.lemma_
        # recheck stop words after lemmatization
        if remove_stops and (word in nlp.Defaults.stop_words):
            continue
        if min_word_length is not None and len(word) < min_word_length:
            continue
        if max_word_length is not None and len(word) > max_word_length:
            continue
        word = deaccent(word)
        if re.search('[^a-z]', word):
            continue
        words.append(word)
    if ngrams and words:
        # group common co-occurrances of words into n-grams: New York -> new_york
        # higher threshold results in fewer phrases
        phrases = gensim.models.phrases.Phrases([words], min_count=5, threshold=10)
        bigram = gensim.models.phrases.Phraser(phrases)
        words = bigram[words]
    return ' '.join(words)
