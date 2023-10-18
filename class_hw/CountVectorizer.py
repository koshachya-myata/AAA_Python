"""CountVectorizer class."""
from typing import Union


class CountVectorizer():
    """Convert a collection of text documents to a matrix of token counts."""

    def __init__(self) -> None:
        """Initialize vocabulary as None."""
        self.vocabulary: Union[dict[str, int], None] = None

    @staticmethod
    def _get_vocabulary_from_words(corpuses_words: list[str]) -> dict[str,
                                                                      int]:
        """
        Construct a vocabulary dictionary from corpuses_words.

        Vocabulary is a mapping of terms to feature indices.
        Indices go in order like in unqiue corpuses_words.

        Args:
            corpuses_words (list[str]): list with words.

        Returns:
            dict[str, int]: vocabulary dictionary.
        """
        vocabulary = dict()
        ind = 0
        for word in corpuses_words:
            if word not in vocabulary:
                vocabulary[word] = ind
                ind += 1
        return vocabulary

    def fit_transform(self, raw_documents: list[str]) -> list[list[int]]:
        """
        Learn the vocabulary dictionary and return document-term count matrix.

        Args:
            raw_documents (list[str]): list of documents.

        Returns:
            list[list[int]]: count matrix.
        """
        corpuses = [doc.lower()for doc in raw_documents]
        self.vocabulary = CountVectorizer.\
            _get_vocabulary_from_words(' '.join(corpuses).split())
        count_matrix = []
        for corpus in corpuses:
            vec = [0] * len(self.vocabulary)
            for word in corpus.split():
                vec[self.vocabulary[word]] += 1
            count_matrix.append(vec)
        return count_matrix

    def get_feature_names(self) -> list[str]:
        """
        Return list of feature names in order like words in raw_documents.

        Returns:
            list[str]: list of feature names.
        """
        if self.vocabulary is None:
            return []
        return list(self.vocabulary)
