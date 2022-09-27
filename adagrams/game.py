import random
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_freq = {}
    random_letters=[]
    selected_letters =[]
    while len(random_letters) < 26:
        r = random.choice(list(LETTER_POOL.keys()))
        random_letters.append(r)
    for letter in random_letters:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
        if letter_freq[letter] <= LETTER_POOL[letter]:
            selected_letters.append(letter)
    return (selected_letters[0:10])
    

def uses_available_letters(word, letter_bank):
    for letter in word:
        if letter in letter_bank:
            return True
        else:
            return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass