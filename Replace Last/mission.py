def replace_last(line: list) -> list:
    new_line = []
    if len(line) != 0:
        new_line.insert(0,line[-1])
        for i in line[0:len(line)-1]:
            new_line.append(i)
        return new_line
    else:
        return line


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
