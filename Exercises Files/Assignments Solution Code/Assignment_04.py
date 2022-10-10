
from string import ascii_lowercase

class CaesarCipher:
    def __init__(self,key):
        self.key = key
        input_alphabet = ascii_lowercase
        encrypted_alphabet = input_alphabet[-key:]+input_alphabet[:-key]
        self.mapping = dict(zip(input_alphabet,encrypted_alphabet))
        self.reverse_mapping = dict(zip(encrypted_alphabet,input_alphabet))
        
    def print_mapping(self):
        for key,value in self.mapping.items():
            print(key,'->',value)
    
    def __call__(self,text):
        encrypted_text = ''
        for letter in text:
            encrypted_text +=self.mapping.get(letter, '')
        return encrypted_text
    
    def decrypt(self,text):
        plain_text = ''
        for letter in text:
            plain_text +=self.reverse_mapping.get(letter, '')
        return plain_text

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    cipher.print_mapping()
    print(cipher("hello world"))
    print(cipher.decrypt(cipher("hello world")))