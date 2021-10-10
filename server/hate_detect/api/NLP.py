from numpy import DataSource
from numpy import array
import numpy
from hate_detect.api.convert import csv_to_dataset
from sklearn.model_selection import train_test_split
#efficient version
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import SGDClassifier

import nltk
# nltk.download()
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer("english", ignore_stopwords=True)
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: ([stemmer.stem(w) for w in analyzer(doc)])
class LemmatizedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmatizedCountVectorizer, self).build_analyzer()
        return lambda doc: ([lemmatizer.lemmatize(w) for w in analyzer(doc)])

def train_model(connection):
    """This code is for initializing from a CSV file"""
    #data = csv_to_dataset("Sheet_1.csv","response_text","class")
    #X_train, X_test, y_train, y_test = train_test_split(data["data"], data["target"], test_size=0.33, random_state=42)
    lemmatizer = WordNetLemmatizer()
    data = numpy.array(connection.cursor().execute("select text,isHate from data order by date desc limit 5000").fetchall())
    print(data)
    X_train, X_test, y_train, y_test = train_test_split(data[:,0], data[:,1], test_size=0.33, random_state=42)
    # lemmatizer = WordNetLemmatizer()
    # stemmer = SnowballStemmer("english", ignore_stopwords=True)
    stemmed_count_vect = StemmedCountVectorizer(stop_words='english',ngram_range=(1,2))
    lemmatized_count_vect = LemmatizedCountVectorizer(ngram_range=(1,2))
    text_clf_svm = Pipeline([('vect',lemmatized_count_vect), # could also be stemmed, lemmatized is marginally better
                    ('tfidf',TfidfTransformer(use_idf=True)),
                    ('clf_svm',SGDClassifier(loss="hinge",alpha=0.0001,random_state=42)),
                   # ('clf_svm',MultinomialNB()) #can also pass MultiNomialNB
                    ])
    text_clf_svm = text_clf_svm.fit(X_train,y_train)
    calibrator = CalibratedClassifierCV(text_clf_svm, cv='prefit')
    model=calibrator.fit(X_train, y_train)
    return model

def predict(model,texts): 
    predictions = model.predict_proba(texts)
    print(predictions)
    #format
    #[(4chan text,predictions),...]
    return {"table":list(zip(list(texts),[i[1] for i in predictions]))}