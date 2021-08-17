def checkio(data):
    def get_difference(n):
        mask = bin(n)[2:].zfill(len(data))
        return abs(sum(item if flag == '1' else -item for item, flag in zip(data, mask)))
    return min(map(get_difference, range(2**len(data)+1)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
