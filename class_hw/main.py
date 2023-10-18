"""Example for CountVectorizer."""
from CountVectorizer import CountVectorizer


if __name__ == '__main__':
    corpuses = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpuses)
    print('Feature names:', ', '.join(vectorizer.get_feature_names()) + '.')
    print('-' * 12)
    print('Count matrix:')
    for vec in count_matrix:
        print('\t' + ' '.join([str(n) for n in vec]))
