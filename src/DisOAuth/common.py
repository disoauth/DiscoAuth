from secrets import SystemRandom

UNICODE_ASCII_CHARACTER_SET = ('abcdefghijklmnopqrstuvwxyz'
                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                               '0123456789')


def generate_token(length=30, chars=UNICODE_ASCII_CHARACTER_SET):
    rand = SystemRandom()
    return ''.join(rand.choice(chars) for x in range(length))
