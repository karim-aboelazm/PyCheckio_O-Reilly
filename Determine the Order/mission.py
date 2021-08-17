def checkio(data):
    letters = []
    for word in data:
        for c in word:
            if c not in letters:
                letters.append(c)
    letters = sorted(letters)
    rezult = ''
    for count in range(len(letters)):       # big for
        for l in letters:                   # smail for
            if ( l not in rezult
                and
                all(l not in word or l == word[0] for word in data)
                ):                          # if from comment above
                    rezult = rezult + l
                    for i in range(len(data)):  # delete finder letter form data
                        data[i] = data[i].replace(l, '')
                    break                   # break small for

    return rezult

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
