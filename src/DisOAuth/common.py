from secrets import SystemRandom

_UNICODE_ASCII_CHARACTER_SET = ('abcdefghijklmnopqrstuvwxyz'
                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                               '0123456789')


def generate_token(length=30, chars=_UNICODE_ASCII_CHARACTER_SET):
    _rand = SystemRandom()
    return ''.join(_rand.choice(chars) for x in range(length))
