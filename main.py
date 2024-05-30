alphabet = ['a', 'b','c' ,'d' ,'e' ,'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt , 'decode' to decrypt\n")
text = input("Enter your text\n").lower()
shift = int(input("Enter No of shifts\n"))
def decrypt(cipher_text , shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
        print(f"The decoded text is {plain_text}")

        decrypt(cipher_text = text , shift_amount = shift)


def encrypt(plain_text, shift_amount):
    ciphertext = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        ciphertext += new_letter
    print(f"The encoded text is {ciphertext}")

encrypt(plain_text=text , shift_amount=shift)