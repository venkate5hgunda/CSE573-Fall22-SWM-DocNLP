import nltk

nltk.download('all')

import os
import string
from nltk.stem import WordNetLemmatizer

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

print(ENGLISH_STOP_WORDS)

sw_nltk = stopwords.words('english')
print(sw_nltk)

wordnet_lemmatizer = WordNetLemmatizer()

def preprocess_textfile(filepath):
    # text reading
    tokens = []
    with open(filepath, 'r', encoding='utf8', errors='ignore') as f:
        text = f.read()
        # removal of stopwords
        # words = [word for word in text.split() if word.lower() not in sw_nltk]
        words = [word for word in text.split() if word.lower() not in ENGLISH_STOP_WORDS]
        new_text = " ".join(words)
        print("Old length: ", len(text))
        print("New length: ", len(new_text))
        # Removal of punctutaions
        tr_table = str.maketrans("", "", string.punctuation)
        s1 = new_text.translate(tr_table)
        # Tokenize the text
        tokenization = nltk.word_tokenize(s1)
        # lemmatize each token
        for w in tokenization:
            tokens.append(wordnet_lemmatizer.lemmatize(w))
    print(len(tokens))
    return tokens


rootdir = '/Users/keerthanagolusula/Downloads/20news-bydate/20news-bydate-train'
cleanedpath = '/Users/keerthanagolusula/Downloads/20news-bydate/cleanedData'

for dir in os.listdir(rootdir):
    dirpath = os.path.join(rootdir, dir)
    if os.path.isdir(dirpath):
        newdirpath = os.path.join(cleanedpath, dir)
        if not os.path.exists(newdirpath):
            os.makedirs(newdirpath)
        dirfile = open(newdirpath + "_file", 'w')
        tokendict = {}
        for file in os.listdir(dirpath):
            filepath = os.path.join(dirpath, file)
            print(filepath)
            tokens = preprocess_textfile(filepath)
            newfilepath = os.path.join(newdirpath, file + "_cleaned")
            newfile = open(newfilepath, "w")
            newfile.write('\n'.join(tokens))
            tokendict[file] = tokens
            newfile.close
        dirfile.write(str(tokendict))
        dirfile.close()


