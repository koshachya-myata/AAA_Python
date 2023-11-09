"""Example for TfidfVectorizer."""
from TfidfVectorizer import TfidfVectorizer


if __name__ == '__main__':
    corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    for vec in tfidf_matrix:
        print(' '.join([str(round(n, 3)) for n in vec]))
