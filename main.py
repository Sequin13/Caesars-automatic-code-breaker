import requests
def ceasar_decrypt(text, shift):
    newTxt=""
    for i in range(len(text)):
        if text[i].isalpha():
            shifted=ord(text[i])-shift
            if shifted<ord('a'):
                shifted+=26
            newTxt+=chr(shifted)
        else:
            newTxt+=text[i]
    return newTxt

def list_of_eng_words():
    r = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
    return r.text.lower().split()

def is_eng_word(word):
    if word in list_of_eng_words():
        return True
    return False
def ceasar_break(text):
    l=[]
    for i in range(1,26):
        l.append(ceasar_decrypt(text, i).split())

    for words in l:
        c=0
        for word in words:
            if is_eng_word(word):
                c+=1
                if c==len(words):
                    return words
    return None

sepatator=" "
print(sepatator.join(ceasar_break("bqqmf po uif usff")))
print(sepatator.join(ceasar_break("kudnknaah rb wxc xw cqn cann")))
