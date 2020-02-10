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
    def encrypt(message):
    return cipher(message, 1)

def decrypt(message):
    return cipher(message, -1)

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
        print encrypt(message)
    elif command == 'decrypt':
        print decrypt(message)
    else:
        print command + ' -> command not found'

if __name__ == '__main__':
    main()

    
