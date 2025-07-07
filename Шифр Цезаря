import string

def caesar_cipher(text):
    def shift_letter(letter, shift):
        if 'a' <= letter <= 'z':
            return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        else:
            return letter  

    words = text.split()
    encrypted_words = []

    for word in words:
        clean_word = ''.join(char for char in word if char.isalnum())
        length = len(clean_word)
        encrypted_word = ''.join(shift_letter(letter, length) for letter in word)
        encrypted_words.append(encrypted_word)

    return ' '.join(encrypted_words)


input_text = input()
result = caesar_cipher(input_text)
print(result)  
