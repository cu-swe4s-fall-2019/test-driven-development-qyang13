import sys


def read_stdin_col(col_num):
    '''
    Takes column number and return an array of numbers from the
    specific column of the specific input file. The file name is
    specified through stdin
    ---
    Input: col_num
    A 0-indexed column numbers
    ---
    Output: nums
    A numerical array containing numbers from that spefied column
    '''
    nums = []
    if sys.stdin is None:
        raise ValueError("Input data should be passed through STDIN")
        return None

    for l in sys.stdin:
        file_split = l.rstrip().split("\t")
        # Check if index is out of bound
        if col_num >= len(file_split) or col_num < 0:
            raise IndexError("Invalid column index number")
            return None
        try:
            nums.append(int(file_split[col_num]))
        except ValueError:
            print("Input value is not numerical")
            continue

    return nums
