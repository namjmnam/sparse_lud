def initialize_lu_sparse(n):
    """Initialize L and U as empty lists of tuples for a sparse matrix of size n."""
    L = [(i, i, 1.0) for i in range(n)]  # Diagonal elements of L are 1
    U = []  # U starts empty
    return L, U

def add_to_sparse(matrix, i, j, value):
    """Add a value to a sparse matrix represented as a list of tuples."""
    for index, (row, col, val) in enumerate(matrix):
        if row == i and col == j:
            matrix[index] = (row, col, val + value)
            return
    matrix.append((i, j, value))

def get_from_sparse(matrix, i, j):
    """Retrieve a value from a sparse matrix represented as a list of tuples."""
    for row, col, value in matrix:
        if row == i and col == j:
            return value
    return 0.0  # Return 0 if the element is not explicitly stored

def lu_decomposition_sparse(A, n):
    """Perform LU decomposition on a sparse matrix A represented as a list of tuples."""
    L, U = initialize_lu_sparse(n)

    for k in range(n):
        # Update U: Directly add A's values for the upper triangular part
        for (i, j, value) in A:
            if i <= k and j == k:  # Assuming A is not necessarily upper triangular
                add_to_sparse(U, i, j, value)

        # Compute multipliers and update L and U for the lower triangular part
        for i in range(k+1, n):
            # Compute the multiplier for the current row i, column k
            a_ik = get_from_sparse(A, i, k)
            u_kk = get_from_sparse(U, k, k)
            if u_kk != 0:  # Avoid division by zero
                l_ik = a_ik / u_kk
                add_to_sparse(L, i, k, l_ik)
                
                # Update U based on the multiplier
                for j in range(k+1, n):
                    a_ij = get_from_sparse(A, i, j)
                    u_kj = get_from_sparse(U, k, j)
                    # Subtract the contribution of the current row of L from row i of A before adding to U
                    adjusted_value = a_ij - l_ik * u_kj
                    if adjusted_value != 0:
                        add_to_sparse(U, i, j, adjusted_value)

    return L, U

def sparse_forward_substitution(L, b):
    n = len(b)  # Assuming b is a dense vector for simplicity
    y = [0] * n
    for i in range(n):
        # For each row i, find the elements in L
        sum_y = 0
        for (row, col, value) in L:
            if row == i:
                if col < i:
                    sum_y += value * y[col]
                elif col == i:
                    y[i] = (b[i] - sum_y) / value
                    break
    return y

def sparse_backward_substitution(U, y):
    n = len(y)
    x = [0] * n
    for i in reversed(range(n)):
        sum_x = 0
        for (row, col, value) in reversed(U):
            if row == i:
                if col > i:
                    sum_x += value * x[col]
                elif col == i:
                    x[i] = (y[i] - sum_x) / value
                    break
    return x

# Example usage
n = 5  # Assuming a 4x4 matrix
A_sparse = [(0, 1, 2.0), (2, 3, 4.0), (3, 4, 5.0), (1, 0, 3.0), (2, 1, 2.0), (3, 2, 4.0)]  # Example sparse matrix representation
b = [1, 2, 3, 4, 5]
L, U = lu_decomposition_sparse(A_sparse, n)
print("L:", L)
print("U:", U)

y = sparse_forward_substitution(L, b)
x = sparse_backward_substitution(U, y)
print("x:", x)