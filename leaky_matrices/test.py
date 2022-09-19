from random import choices

def array_to_str(array):
    return "".join(str(value) for value in array)

def print_matrix(matrix):
    print("[")
    for row in matrix:
        print(f"  {row}")
    print("]")

def matrix(number, rows = 8, columns = 8):
    assert isinstance(number, str)
    matrix = list(list(int(digit) for digit in number[row*rows:row*rows+columns]) for row in range(rows))
    print_matrix(matrix)
    return matrix

def get_secret_key(*args):
    matrix = [[],[],[],[],[],[],[],[]]
    first = "00000000"
    for row in range(8):
        second = args[row]
        for column in range(8):
            if first[column] != second[column]:
                matrix[column].append(1)
            else:
                matrix[column].append(0)
        first = args[row]
    print_matrix(matrix)
    return matrix

if __name__ == "__main__":
    # key = get_secret_key("10000000", "10000000", "11111100", "11111100", "11011111", "10000101", "01110011", "00011100")
    key = get_secret_key("01000011", "11000001", "00111100", "11010001", "11010010", "11011010", "00111000", "01111101")
    # key = [[0, 0, 1, 1, 1, 0, 0, 0],
    #        [0, 1, 1, 1, 1, 1, 1, 1],
    #        [0, 0, 1, 0, 1, 1, 0, 0],
    #        [1, 0, 0, 1, 0, 0, 1, 0],
    #        [1, 1, 0, 1, 0, 1, 0, 1],
    #        [1, 1, 1, 1, 1, 1, 1, 0],
    #        [0, 0, 1, 1, 1, 1, 0, 0],
    #        [1, 1, 0, 0, 1, 0, 0, 0]]
    
    for n in range(8):
        challenge = str(input("8-digit binary: "))
        assert len(challenge) == 8
        assert challenge.count("0") + challenge.count("1") == 8
        
        challenge = tuple(int(value) for value in challenge)
        multiplied = tuple(sum(row[n]*challenge[n] for n in range(8)) for row in key)
        binary = tuple(value & 1 for value in multiplied)

        print(f"{array_to_str(challenge)} --> {array_to_str(multiplied)} --> {array_to_str(binary)}")

"""
Row n has an even number of 1s if response_n is 0, else 1

00000000 --> 10000000 --> 11000000 --> 11100000 --> ... --> 11111111
8 checks, turn a digit to 1 every check.
A change in the result produced means a 1 in that location within the secret key.

Analysing the key (line 34):

Input    --> Process  --> Final
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
10000000 --> 00011101 --> 00011101 --> Column 1: Rows 4, 5, 6 and 8
11000000 --> 01012202 --> 01010000 --> Column 2: Rows 2, 5, 6 and 8
11100000 --> 12112312 --> 10110110 --> Column 3: Rows 1, 2, 3, 6 and 7
11110000 --> 23123422 --> 01101000 --> Column 4: Rows 1, 2, 4, 5, 6 and 7
11111000 --> 34223533 --> 10001111 --> Column 5: Rows 1, 2, 3, 6, 7 and 8
11111100 --> 35324643 --> 11100001 --> Column 6: Rows 2, 3, 5, 6 and 7
11111110 --> 36334743 --> 10110101 --> Column 7: Rows 2, 4 and 6
11111111 --> 37335743 --> 11111101 --> Column 8: Rows 2 and 5

Key:
00111000
01111111
00101100
10010010
11010101
11111110
00111100
11001000


Analysing the secret key (line 33)
10000000 --> Column 1: Rows 1
10000000 --> Column 2: Rows 
11111100 --> Column 3: Rows 2, 3, 4, 5 and 6
11111100 --> Column 4: Rows 
11011111 --> Column 5: Rows 3, 7 and 8
10000101 --> Column 6: Rows 2, 4, 5 and 7
01110011 --> Column 7: Rows 1, 2, 3, 4, 6 and 7
00011100 --> Column 8: Rows 2, 3, 5, 6, 7 and 8

Secret Key:
key = [[1, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 1, 1, 1],
       [0, 0, 1, 0, 1, 0, 1, 1],
       [0, 0, 1, 0, 0, 1, 1, 0],
       [0, 0, 1, 0, 0, 1, 0, 1],
       [0, 0, 1, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 1]]

"""

