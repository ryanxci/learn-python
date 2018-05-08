def checkio(game_result: list) -> str:
    rows = game_result
    print(rows)
    # print([(r[i], r[2 - i]) for i, r in enumerate(rows)])
    # print(list(zip(*rows)))
    # 找出列
    cols = map(''.join, zip(*rows))
    l = list(cols)
    # print(l)
    # 找出斜边
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + l + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
    # if not len(game_result) == 3:
    #     return 'wrong game result!'
    #
    # if not all(len(row) == 3 for row in game_result):
    #     return 'wrong game result!'
    #
    # for row in game_result:
    #     s = set(row)
    #     if len(s) == 1:
    #         if s.copy().pop() == '.':
    #             continue
    #         return s.pop()
    #
    # size = len(game_result)
    # for i in range(size):
    #     s = set(row[i] for row in game_result)
    #     if len(s) == 1:
    #         if s.copy().pop() == '.':
    #             continue
    #         return s.pop()
    #     # for j in range(size):
    #     # print(game_result[i][j])
    #     # if len(set(game_result[i][j], game_result[i][j + 1], game_result[i][j + 2]))
    # s = {game_result[0][0], game_result[1][1], game_result[2][2]}
    # if len(s) == 1:
    #     if s.copy().pop() == '.':
    #         return 'D'
    #     return s.pop()
    #
    # s = {game_result[0][2], game_result[1][1], game_result[2][0]}
    # if len(s) == 1:
    #     if s.copy().pop() == '.':
    #         return 'D'
    #     return s.pop()
    #
    # return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    # print(list(map(''.join, zip(*[('O', '.'), ('O', 'O'), ('X', 'X')]))))

    # print(checkio([
    #     "X.X",
    #     "OX.",
    #     "XOO"]))
