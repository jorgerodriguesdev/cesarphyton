import sys
LETRAS = 'abcdefghijklmnopqrstuvwxyz'
CRYPT = 13
def cipher(message, dir):
    m = ''
    for c in message:
            if c in LETRAS:
            c_index = LETRAS.index(c)
            m += LETRAS[(c_index + (dir * CRYPT)) % len(LETRAS)]
        else:
            m += c
    return m
    
    
