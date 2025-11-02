import Caesar_Cipher_logo
print(Caesar_Cipher_logo.logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after encryption {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption {plain_text}")


wanna_end = False
while not wanna_end:
    choice = input("Type encrypt for encryption and type decrypt for decryption: \n")
    text = input("Type Your message: \n").lower()
    shift = int(input("Enter shift key:\n"))
    if choice == "encrypt":
        encryption(plain_text=text, shift_key=shift)  # function call
    elif choice == "decrypt":
        decryption(cipher_text=text, shift_key=shift)  # function call
    play_again = input("Type yes if you want to go again otherwise no to exit.\n")
    if play_again == "no":
        print("Have a nice day, good bye")
        wanna_end = True
