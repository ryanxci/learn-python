def checkio(first, second):
    first_set, second_set = set(first.split(',')), set(second.split(','))
    # 求交集
    result = first_set.intersection(second_set)
    return ','.join(sorted(result))
    # result = ''
    # l = first.split(',')
    # l.sort()
    # for w in l:
    #     if w in second.split(','):
    #         result = result + w + ','
    # return result.rstrip(',')


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

