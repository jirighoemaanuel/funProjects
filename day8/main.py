alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrpt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_wrd = ""
    for letter in original_text:
        new_index = alphabets.index(letter) + shift_amount
        encrypted_wrd += alphabets[new_index]

    return encrypted_wrd


print(encrypt(text, shift))
