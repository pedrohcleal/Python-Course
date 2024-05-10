import string
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        strcode = ""
        while len(strcode) < len(self.text):
            strcode = strcode + self.text
        strcode = strcode[0:len(self.text)+1]
        dictalpha = {key: value for key, value in zip(self.alphabet,range(0,26))}
        dictkeys = {}
        for let in self.key:
            dictkeys[let] = dictalpha.get(let)
            
        pass
    
    def decode(self, text):
        pass

    
# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';

# creates a cipher helper with each letter substituted
# by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);

# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'
