from typing import List


def checkio(game: List[str]) -> str:
    columns = game[0][0] + game[1][0] + game[2][0], game[0][1] + game[1][1] + game[2][1], game[0][2] + game[1][2] + game[2][2]
    diagonal = game[0][0] + game[1][1] + game[2][2], game[0][2] + game[1][1] + game[2][0]

    for line in game:
        if line != "..." and len(set(line)) == 1:
            return line[0]

    for line in columns:
        if  line != "..." and len(set(line)) == 1:
            return line[0]

    for line in diagonal:
        if line != "..." and len(set(line)) == 1:
            return line[0]

    return 'D'


if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
