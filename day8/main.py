alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def encrypt(original_text, shift_amount):
    encrypted_wrd = ""
    length_alphabets = len(alphabets)
    for letter in original_text:
        new_index = alphabets.index(letter) + shift_amount
        encrypted_wrd += alphabets[new_index % length_alphabets]

    print(encrypted_wrd)


def decrypt(original_text, shift_amount):
    decrypted_wrd = ""
    length_alphabets = len(alphabets)
    for letter in original_text:
        new_index = alphabets.index(letter) - shift_amount
        decrypted_wrd += alphabets[new_index % length_alphabets]

    print(decrypted_wrd)


def caeser(direction, original_text, shift_amount):
    if direction == "encode":
        encrypt(original_text, shift_amount)
    elif direction == "decode":
        decrypt(original_text, shift_amount)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction, text, shift)

    