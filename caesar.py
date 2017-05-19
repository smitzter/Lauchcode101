from helper import rot_char

def encrypt(mess, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ntext = ''
    for char in mess:
        ntext += str(rot_char(char, rot))
    return ntext

def main():
    mess = input("Type a message:")
    rot = input(int("Rotate by:"))
    print(encrypt(mess, rot))
    return None

if __name__ == '__main__':
    main()
