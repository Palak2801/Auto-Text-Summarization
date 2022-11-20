import spacy

# 'en_core_web_sm' is an English word library that includes vocabulary and syntax
# can be used en_core_web_lg
nlp = spacy.load('en_core_web_sm')

# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# Import Heapq for Finding the Top N Sentences
from heapq import nlargest

# Summarizer function
def text_summarizer(raw_docx,k):
    raw_text = raw_docx
    docx = nlp(raw_text)

    # list of stop words there are in total 40 stop words in python
    stopwords = list(STOP_WORDS)

    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords and word.text not in punctuation and word.text != '\n':
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    keywords = nlargest(6, word_frequencies , key=word_frequencies.get)
    print(keywords)
    
    # Calculate maximum frequency
    maximum_frequncy = max(word_frequencies.values())

    # Perform Normalization to get frequency in range 0-1
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        
    # List of sentences in raw_text
    sentence_list = [ sentence for sentence in docx.sents ]

    # Sentence Scores need to be check
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Sentence arrange according to ranking
    summarized_sentences = nlargest(6, sentence_scores, key=sentence_scores.get)
    keywords = nlargest(k, word_frequencies , key=word_frequencies.get)
    # print(keywords)

    # Extracting main summary and converting it to string format
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary
