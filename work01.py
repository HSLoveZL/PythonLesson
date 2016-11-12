#!/usr/bin/python2.7

def change_char(chars):
    return "%s" % (chars[:1].upper() + chars[1:].lower())

print map(change_char, ['adam', 'LISA', 'barT'])

