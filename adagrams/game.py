from random import randint

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
    letters_list = list(LETTER_POOL.keys())
    draw_letters_list = []
    
    while len(draw_letters_list) < 10:
        letter_index = randint(0, len(letters_list) -1)
        letter = letters_list[letter_index]
        if LETTER_POOL[letter] > 0:
            draw_letters_list.append(letter)
            LETTER_POOL[letter] -= 1
    
    for letter in draw_letters_list:
        LETTER_POOL[letter] += 1
    
    return draw_letters_list
    
#Comment added just to practice push it to GitHub
def uses_available_letters(word, letter_bank):
    available_letters = letter_bank[:]
    word = word.upper()
    for letter in word: 
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass