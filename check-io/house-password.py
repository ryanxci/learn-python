# -*- coding: utf-8 -*-
import re


def checkio(data):
    return re.match('^(?=.*[0-9].*)(?=.*[A-Z].*)(?=.*[a-z].*).{10,}$', data) is not None


if __name__ == '__main__':
    # These "asserts"Sample Text using only for self-checking and not necessary for auto-testing
    # a = checkio('bAse730onE4')
    # re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    # print(a)
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
