# def checkio(time_string):
#     f_time = ":".join([h.zfill(2) for h in time_string.split(":")])
#     width = [2, 4, 0, 3, 4, 0, 3, 4]
#     string = ""
#     for i, c in enumerate(f_time):
#         if c == ":":
#             string += c
#             string += " "
#             continue
#         s = str(bin(int(c))).replace("0b", "").zfill(width[i])
#         string += s
#         string += " "
#     # replace this for solution
#     return string.replace("0", ".").replace("1", "-").strip(" ")

# best solutions
"""
Convert a time to a pseudo-Morse code.
This 'binary-Morse' encoding represents the binary digits of a number as . and -
for 0 and 1 respectively.
"""

TO_MORSE = str.maketrans('01', '.-')


def to_morse(number, bits):
    """Return number in binary-Morse as a string with the given number of bits."""
    return "{0:0{1}b}".format(number, bits).translate(TO_MORSE)


def to_code(field):
    """Return a space-delimited string of binary-Morse digits."""
    tens, ones = divmod(int(field), 10)
    return "{} {}".format(to_morse(tens, 3), to_morse(ones, 4))


def checkio(data):
    """Return a string representing the time in a Morse code-like form."""
    return ' : '.join(map(to_code, data.split(':')))[1:]  # Strip leading .


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

