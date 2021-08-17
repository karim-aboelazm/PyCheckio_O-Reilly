import re
def unix_match(filename: str, pattern: str) -> bool:
    list = [('.', '\.'), ('?', '.'), ('[.]', '.'), ('[[]', '\['), ('[]]', '\]')]
    x = pattern
    for a, b in list:
        x = x.replace(a, b)
    if '[!]' not in pattern:
        x = x.replace('[!', '[^')
    else:
        x = x.replace('[!]', '\[!\]')
    if '[*]' not in pattern:
        x = x.replace('*', '.+')

    try:
        return re.match(x, filename) != None
    except:
        return pattern == filename


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
