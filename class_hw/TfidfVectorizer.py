"""Tf-idf Vectorizer class."""
from CountVectorizer import CountVectorizer
from TfidfTransformer import TfidfTransformer
from typing import Union
from typing_extensions import override  # For Python < 3.12
# from typing import override  # For Python > 3.12


class TfidfVectorizer(CountVectorizer):
    """Convert a collection of text documents to a tf-idf matrix."""

    def __init__(self) -> None:
        """Init TfidfTransformer; init tfidf and count matrices as None."""
        super().__init__()
        self.transformer = TfidfTransformer()
        self.count_matrix: Union[None, list[list[int]]] = None
        self.tfidf_matrix: Union[None, list[list[float]]] = None

    @override
    def fit_transform(self,    # type: ignore  # bcs for tf-idf we return float
                      corpus: list[str]) -> list[list[float]]:
        """
        Calculate tf-idf matrix based on corpus.

        Args:
            corpus (list[str]): list of documents (in str).

        Returns:
            list[list[int]]: tf-idf matrix.
        """
        self.count_matrix = super().fit_transform(corpus)
        self.tfidf_matrix = self.transformer.fit_transform(self.count_matrix)
        return self.tfidf_matrix
