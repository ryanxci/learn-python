# -*- coding: utf-8 -*-
import time
from collections import Counter


def checkio(data: list) -> list:
    # for c in data[:]:
    #     if data.count(c) == 1:
    #         data.remove(c)
    # return data
    # return [i for i in data if data.count(i) > 1]
    counter = Counter(data)
    return [item for item in data if counter[item] > 1]


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    start_time = time.time()
    print("start_time:" + time.time().__str__())
    checkio(list(range(100000)) + [0])
    end_time = time.time()
    print("end_time:" + time.time().__str__())
    print("time:" + (end_time - start_time).__str__())
    print("It is all good. Let's check it now")
    # print(list(checkio([1, 2, 3, 4, 5])))
