def alp_pos(letter):
    return (ord(letter) -1) %32
    #returns a number beteen 0-25
    #needs to distinguish beteen upper and loer

def pos_to_char(num, upper):
    nchar= 65 if upper else 97
    return chr(num + nchar)

def is_upper(char):
     return ord(char) < 97

def is_alpha(char):
    val = ord(char)
    return (val > 64 and val < 91) or (val > 96 and val < 123)

def rot_char(char, rot):
    if not is_alpha(char):
        return char
    return pos_to_char((alp_pos(char) + int(rot)) % 26, is_upper(char))

def main():
    #word = input("Type a message:")
    #shift = int(input("Roatate by?"))
    return None

if __name__ == '__main__':
    main()
