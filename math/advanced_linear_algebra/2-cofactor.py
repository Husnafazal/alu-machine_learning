    ...

    def cofactor(matrix):
        """
        Calculate the cofactor matrix of a matrix.

        Args:
        - matrix: List of lists. The input matrix.

        Returns:
        - List of lists. The cofactor matrix.
        """
        if (not isinstance(matrix, list) or
                not all(isinstance(row, list) for row in matrix)):
            raise TypeError("matrix must be a list of lists")

    ...
