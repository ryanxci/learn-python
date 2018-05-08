# -*- coding: utf-8 -*-
import string


def checkio(text):
    d = {'a': 0}
    text = text.lower()
    # for c in text:
    #     if not c.isalpha():
    #         continue
    #     n = text.count(c)
    #     values = d.values()
    #     if max(values) < n:
    #         d.clear()
    #         d[c] = n
    #     elif max(values) == n:
    #         if list(d.keys())[0] > c:
    #             d.clear()
    #             d[c] = n
    print(max(string.ascii_lowercase, key=text.count))
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    # assert checkio("One") == "e", "All letter only once."
    # assert checkio("Oops!") == "o", "Don't forget about lower case."
    # assert checkio("AAaooo!!!!") == "a", "Only letters."
    # assert checkio("abe") == "a", "The First."
    # print("Start the long test")
    # assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    # print("The local tests are done.")
    checkio("AAaooo!!!!")
    # checkio("a" * 9000 + "b" * 1000)
    # checkio("a" * 9000 + "b" * 1000)
