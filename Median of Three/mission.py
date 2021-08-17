from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    out = els[0:2]
    for i in range(2, len(els)):
        out.append(sorted(els[i-2:i+1])[1])
    return out

if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
