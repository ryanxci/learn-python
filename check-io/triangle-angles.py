import math
from typing import List


def checkio(a: int, b: int, c: int) -> List[int]:
    # l = sorted([a, b, c])
    # if l[0] + l[1] <= l[2]:
    #     return [0, 0, 0]
    # da = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
    # db = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))
    #
    # return sorted([da, db, 180-(da + db)])

    # best solutions
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    find_angle = lambda s1, s2, so: int(round(
        math.degrees(math.acos((s1 ** 2 + s2 ** 2 - so ** 2) / (2 * s1 * s2))), 0))
    return sorted([find_angle(a, b, c), find_angle(a, c, b), find_angle(b, c, a)])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))
    print(checkio(3, 4, 5))
    print(checkio(2, 2, 5))
    print(checkio(5, 4, 3))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    # print(math.degrees(math.acos(1 / 2)))
