def compute_eigenvectors(matrix):
    # This is a placeholder function. In practice, you'd need to implement
    # a method to compute eigenvalues and eigenvectors, such as the QR algorithm.
    # This step is highly non-trivial and requires a significant amount of code.
    pass

def svd_simple(A):
    # Step 1: Compute A^T A and AA^T
    AT_A = [[sum(a*b for a, b in zip(A_row, A_col)) for A_col in zip(*A)] for A_row in A]
    A_AT = [[sum(a*b for a, b in zip(AT_row, AT_col)) for AT_col in zip(*AT)] for AT_row in AT]

    # Placeholder steps for eigenvalue and eigenvector calculation
    # In practice, these require complex algorithms to compute
    eigenvalues_AT_A, eigenvectors_AT_A = compute_eigenvectors(AT_A)
    eigenvalues_A_AT, eigenvectors_A_AT = compute_eigenvectors(A_AT)

    # Step 2: The singular values are the square roots of the eigenvalues
    singular_values = [sqrt(val) for val in eigenvalues_AT_A]

    # Steps 3 and 4: Sort singular values and construct Sigma
    # Again, simplifying for educational purposes
    Sigma = sorted(singular_values, reverse=True)

    # Steps to construct U and V are omitted for brevity
    U = eigenvectors_A_AT
    V = eigenvectors_AT_A

    return U, Sigma, V
