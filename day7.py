from pyfiglet import Figlet

f = Figlet(font='slant')  # try fonts like 'block', 'bubble', 'banner'
print(f.renderText('CIPHER'))
encode_or_decode = input("encode or decode: ")
alphabets = [chr(i) for i in range(97, 123)]
message = input("Write a message: ").lower()
shift = int(input("enter shift: "))


def encoder(orginal_text, shift_amt, encode_or_decode):
    message = orginal_text.lower()
    shift = shift_amt
    cipher_text = ""

    for letter in message:
        if letter in alphabets:
            newindex = (alphabets.index(letter) + shift) % 26
            cipher_text += alphabets[newindex]

        else:
            cipher_text += letter

    print(cipher_text)
    return cipher_text

ciphered_text = encoder(message, shift)

def decoder(ciphered_text, shift_amt):
    cipher_text = ciphered_text
    shift = shift_amt
    original_text = ""
    for letter in cipher_text:

        if letter in alphabets:
            newindex2 = (alphabets.index(letter) - shift) % 26 # here negative indexing works

            original_text += alphabets[newindex2]

        else:
            original_text += letter

    return original_text

original = decoder(ciphered_text= ciphered_text, shift_amt=shift)
print(original)
