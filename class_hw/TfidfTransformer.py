"""Tf-idf transformer class."""
import numpy as np
from typing import Union


class TfidfTransformer():
    """Convert a count matrix to tf-idf matrix."""

    def __init__(self) -> None:
        """Init tf-idf and count matrices as None."""
        self.count_matrix: Union[None, list[list[int]]] = None
        self.tfidf_matrix: Union[None, list[list[float]]] = None

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Calculate term-frequency matrix based on count matrix.

        Args:
            count_matrix (list[list[int]]): count matrix.

        Returns:
            list[list[int]]: term-frequency matrix.
        """
        tf_matrix = [[item/sum(doc) for item in doc] for doc in count_matrix]
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """
        Calculate idf-vector based on count matrix.

        Args:
            count_matrix (list[list[int]]): count matrix

        Returns:
            list[list[int]]: idf vector.
        """
        n = len(count_matrix)
        idf_vector = []
        for i in range(len(count_matrix[0])):
            doc_count = 0
            for j in range(n):
                if count_matrix[j][i] > 0:
                    doc_count += 1
            idf_vector.append(np.log((n + 1) / (doc_count + 1)) + 1)
        return idf_vector

    def fit_transform(self,
                      count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Calculate tf-idf matrix based on count matrix.

        Args:
            count_matrix (list[list[int]]): count matrix.

        Returns:
            list[list[int]]: tf-idf matrix.
        """
        self.count_matrix = count_matrix
        idf_vec = self.idf_transform(self.count_matrix)
        tf_matrix = self.tf_transform(self.count_matrix)
        self.tfidf_matrix = []
        for vec in tf_matrix:
            self.tfidf_matrix.append([vec[i] * idf_vec[i]
                                      for i in range(len(vec))])
        return self.tfidf_matrix
