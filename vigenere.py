from helper import rot_char, alp_pos, is_alpha
def encrypt(ptext, ktext):
    k_length = len(ktext)
    if k_length ==0:
        return ptext
    k_item = 0
    ctext =""
    for char in ptext:
        if is_alpha(char):
            ctext += str(rot_char(char, alp_pos(ktext[k_item % k_length])))
            k_item += 1
        else:
            ctext += char
    return ctext

def main():
    ptext = input("Type a message:")
    ktext = input(int("Encryption key:"))
    ctext = encrypt(ptext, ktext)
    print(ctext)

if __name__ == '__main__':
    main()
