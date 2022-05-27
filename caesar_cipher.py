# Encrypt plain text based on the input shift
def encrypt(plain_text, shift):
    cipher = ""
    
    for char in plain_text:
        code = ord(char)
        
        if char.isalpha():
            code = code + shift
            
            if char.islower():
                if code > 122:
                    code = (code - 122) + 96
            elif char.isupper():
                if code > 90:
                    code = (code - 90) + 64
            
        cipher += chr(code)
    return cipher

plain_text = input("Enter plain text: ")
shift = ""

while True:
    shift = input("Enter shift [1-25]: ")
    
    try:
        shift = int(shift)
        
        if shift >= 1 and shift <= 25:
            break
    except ValueError:
        continue

print(encrypt(plain_text, shift))