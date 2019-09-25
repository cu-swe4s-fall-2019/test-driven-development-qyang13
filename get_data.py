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
    try:
        f = open(sys.stdin)
    except  FileNotFoundError:
        raise FileNotFoundError("The input file does not exist")
        return None

    nums = []

    for l in f:
        file_split = l.rstrip().split("\t")
        try:
            nums.append(int(file_split[col_num]))
        except IndexError:
            f.close()
            raise IndexError("Index out of bound")

    f.close()
    return nums
