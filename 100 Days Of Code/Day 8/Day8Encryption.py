from art import *
Art = text2art('ENCRYPTION')
print(Art)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input('Type ''encode'' to encrypt, type ''decode'' to decrypt:\n').lower()
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))


# def encrypt(original, shift_amount):
#     cipher = ''
#     for letter in original:
#         shifted = alphabet.index(letter) + shift_amount
#         shifted %= len(alphabet)
#         cipher += alphabet[shifted]
#     print(f'Here is the encoded result: {cipher}')

# encrypt(original=text, shift_amount=shift)


# def dencrypt(original, shift_amount):
#     output = ''
#     for letter in original:
#         shifted = alphabet.index(letter) - shift_amount
#         shifted %= len(alphabet)
#         cipher += alphabet[shifted]
#     print(f'Here is the decoded result: {cipher}')

# dencrypt(original=text, shift_amount=shift)


def caesar(original_text, shift_amount, encode_decode):
    output = ''

    if encode_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output += letter 
        else:
            shifted = alphabet.index(letter) + shift_amount
            shifted %= len(alphabet)
            output += alphabet[shifted]

    print(f'Here is the decoded result: {output}')

caesar(text, shift, direction)

should_continue = True

while should_continue:

    direction = input('Type ''encode'' to encrypt, type ''decode'' to decrypt:\n').lower()
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caesar(text, shift, direction)

    restart = input('Do you want to stop? Y or N.\n').lower()
    if restart == 'y':
        should_continue = False
        print('Goodbye.')