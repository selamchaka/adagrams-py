import secrets

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

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    letter_freq = {}
    random_letters=[]
    selected_letters =[]
    while len(random_letters) < 26:
        r = secrets.choice(list(LETTER_POOL.keys()))
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
    word_str = ""
    temp_word = ""
    letter_bank_dic = {}
    word_dic ={}
    
    for letter in word:
        if str.upper(letter) in letter_bank:
            temp_word += letter
            word_str += str.upper(letter)
    for letter in letter_bank:
        if letter in letter_bank_dic:
            letter_bank_dic[str.upper(letter)] += 1
        else:
            letter_bank_dic[str.upper(letter)] = 1
    for letter in word_str:
        if letter in word_dic:
            word_dic[str.upper(letter)] += 1 
        else:
            word_dic[str.upper(letter)] = 1
    if word_dic[letter] > letter_bank_dic[letter]:
        return False
    elif temp_word != word:
        return False
    elif temp_word == word:
        return True   

def score_word(word):
    if word == "":
        return 0
    score_word = 0
    upper_word = str.upper(word)
    
    for letter in upper_word:
        for key, value in SCORE_CHART.items():
            if letter == key:
                score_word += value
                
    if len(word) in range(7, 11):
        score_word += 8
        
    return score_word 


def get_highest_word_score(word_list):
    highest_word = []
    highest_value = 0
    tie_word = []
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_value:
            highest_word = word
            highest_value = word_score
            tie_word = [highest_word]
        elif word_score == highest_value: # tie case
            tie_word.append(word)

    if len(tie_word) > 1 :
        if len(tie_word[0]) > len(tie_word[1]) and len(tie_word[0])==10 :
            return (tie_word[0], highest_value)
        elif len(tie_word[0]) < len(tie_word[1]) and len(tie_word[1])!=10 :
            return (tie_word[0], highest_value)
        elif len(tie_word[0]) == len(tie_word[1]):
            return(tie_word[0], highest_value)
        else:
            return(tie_word[1], highest_value)
    
    return (highest_word, highest_value)

            
    
    


