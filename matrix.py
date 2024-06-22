#=================================================
# Shizza Fatima Shafqat 
# June 2024
# matrix.py
# This program is a Matrix Class incorporating the add, subtract, and multiply 
# methods which will work on matrices of any size. The code prompts the user for
# the size and elements of the matrices and the operation the user wants to perform. 
#================================================= 

class Matrix:
    def __init__(self, matrix_data):
        # Initializing matrix with provided data
        self.data = matrix_data
        self.rows = len(matrix_data)  # Number of rows in the matrix
        self.cols = len(matrix_data[0])  # Number of columns in each row of the matrix

    def __add__(self, other):
        # Adding two matrices after checking if they have the same dimensions
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result_data.append(row)
        return Matrix(result_data)

    def __sub__(self, other):
        # Subtracting two matrices after checking if they have the same dimensions
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result_data = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result_data.append(row)
        return Matrix(result_data)
    
    def __mul__(self, other):
        # Multiplying two matrices after checking if the column count of the first equals the row count of the second
        if self.cols != other.rows:
            raise ValueError("The number of columns of the first matrix must be equal to the number of rows of the second.")
        result_data = []
        for i in range(self.rows):
            result_row = []
            for j in range(other.cols):
                result_element = 0
                for k in range(self.cols):
                    result_element += self.data[i][k] * other.data[k][j]
                result_row.append(result_element)
            result_data.append(result_row)
        return Matrix(result_data)

def print_matrix(matrix):
    # Printing matrix rows neatly formatted
    for row in matrix.data:
        print(' '.join(map(str, row)))
        
def input_matrix():
    # Collecting matrix dimensions and elements from the user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix_data = []
    print("Enter the matrix data row by row (space-separated values):")
    for _ in range(rows):
        row_data = list(map(int, input().split()))
        if len(row_data) != cols:
            raise ValueError("The number of columns does not match the input size.")
        matrix_data.append(row_data)
    return Matrix(matrix_data)

def main():
    print("--------Input data for Matrix 1--------")
    matrix1 = input_matrix()

    print("--------Input data for Matrix 2--------")
    matrix2 = input_matrix()

    operation = input("Choose the operation (add, subtract, multiply): ").strip().lower()  # Sanitizing user input
    try:
        if operation == 'add':
            result = matrix1 + matrix2
        elif operation == 'subtract':
            result = matrix1 - matrix2
        elif operation == 'multiply':
            result = matrix1 * matrix2
        else:
            raise ValueError("Unsupported operation")  # Handling unexpected operation input

        print("The result of the operation is:")
        print_matrix(result)  # Printing the result in a formatted manner
    except ValueError as e:
        print(e)  # Printing error messages

if __name__ == "__main__":
    main()
