def verify_anagrams(first_word, second_word):
    # if len(first_word.replace(" ","")) != len(second_word.replace(" ","")):
    #     return False
    # for c in set(str(first_word).lower().replace(" ","")):
    #     if str(first_word).lower().count(c) != str(second_word).lower().count(c):
    #         return False
    # return True
    # best solutions
    return sorted(a.lower().replace(' ', '')) == sorted(b.lower().replace(' ', ''))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

