#!/usr/bin/python2.7

def change_char(chars):
    return "%s" % chars.capitalize()

print map(change_char, ['adam', 'LISA', 'barT'])

